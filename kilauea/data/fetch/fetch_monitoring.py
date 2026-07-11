#!/usr/bin/env python3
"""Pull Kīlauea summit monitoring data: earthquakes, seismic RSAM, and tilt.

Run from a machine with open internet access (the analysis container that
authored this repo blocks earthquake.usgs.gov / volcanoes.usgs.gov / IRIS).

  pip install requests obspy pandas matplotlib
  python fetch_monitoring.py --start 2026-07-04 --end 2026-07-12

Outputs CSVs into ./out/ and a summary plot out/summit_picture.png.

Endpoint status:
  - USGS FDSN event API ..... verified, stable, documented
  - IRIS FDSN dataselect .... verified, stable, documented (HV network is public)
  - HVO tilt ................ best-effort; the public JSON API behind the HVO
    monitoring pages has changed paths before. Two candidates are tried; if both
    fail, open https://www.usgs.gov/volcanoes/kilauea/summit-tiltmeter-uwd in a
    browser, watch DevTools Network tab for the JSON request, and update
    TILT_ENDPOINTS below.
"""

import argparse
import io
import json
import pathlib
import sys

import pandas as pd
import requests

OUT = pathlib.Path(__file__).parent / "out"

SUMMIT = dict(latitude=19.406, longitude=-155.283)

# Seismic stations near the summit vents. RIMD/UWE/UWB sit on the caldera rim;
# these are the stations HVO's public tremor/RSAM displays are built from.
SEISMIC_STATIONS = ["UWE", "RIMD", "UWB", "OBL"]

TILT_ENDPOINTS = [
    # candidate 1: VSC tilt API (channel = station code, e.g. UWD, SDH)
    "https://volcanoes.usgs.gov/vsc/api/tiltapi?channel={sta}&starttime={start}&endtime={end}",
    # candidate 2: path-style variant
    "https://volcanoes.usgs.gov/vsc/api/tiltapi/{sta}/{start}/{end}",
]
TILT_STATIONS = ["UWD", "SDH"]  # UWD = Uēkahuna (summit reference), SDH = Sand Hill


def fetch_earthquakes(start: str, end: str) -> pd.DataFrame:
    """Summit-region earthquake catalog (8 km radius) from the USGS FDSN API."""
    r = requests.get(
        "https://earthquake.usgs.gov/fdsnws/event/1/query",
        params=dict(
            format="csv",
            starttime=start,
            endtime=end,
            maxradiuskm=8,
            orderby="time-asc",
            **SUMMIT,
        ),
        timeout=60,
    )
    r.raise_for_status()
    df = pd.read_csv(io.StringIO(r.text), parse_dates=["time"])
    df.to_csv(OUT / "earthquakes.csv", index=False)
    return df


def fetch_rsam(start: str, end: str) -> pd.DataFrame:
    """Compute 10-minute RSAM from raw HV waveforms via IRIS FDSN dataselect.

    RSAM (real-time seismic amplitude) is the standard tremor-level proxy:
    mean absolute amplitude of the (detrended) vertical channel per window.
    """
    from obspy import UTCDateTime
    from obspy.clients.fdsn import Client

    client = Client("IRIS")
    t0, t1 = UTCDateTime(start), UTCDateTime(end)
    frames = []
    for sta in SEISMIC_STATIONS:
        try:
            st = client.get_waveforms("HV", sta, "*", "HHZ,EHZ", t0, t1)
        except Exception as e:  # station gaps are routine; keep going
            print(f"  {sta}: no data ({e})", file=sys.stderr)
            continue
        st.merge(fill_value=0).detrend("demean")
        for tr in st:
            x = pd.Series(
                abs(tr.data),
                index=pd.date_range(
                    tr.stats.starttime.datetime,
                    periods=tr.stats.npts,
                    freq=pd.Timedelta(seconds=tr.stats.delta),
                ),
            )
            rsam = x.resample("10min").mean().rename(f"{sta}.{tr.stats.channel}")
            frames.append(rsam)
    df = pd.concat(frames, axis=1) if frames else pd.DataFrame()
    df.to_csv(OUT / "rsam_10min.csv")
    return df


def fetch_tilt(start: str, end: str) -> pd.DataFrame:
    frames = {}
    for sta in TILT_STATIONS:
        for tmpl in TILT_ENDPOINTS:
            url = tmpl.format(sta=sta, start=start, end=end)
            try:
                r = requests.get(url, timeout=60)
                r.raise_for_status()
                payload = r.json()
            except (requests.RequestException, json.JSONDecodeError) as e:
                print(f"  tilt {sta}: {url} failed ({e})", file=sys.stderr)
                continue
            frames[sta] = pd.json_normalize(payload)
            break
    if not frames:
        print(
            "  No tilt endpoint worked — see module docstring for how to find "
            "the current one.",
            file=sys.stderr,
        )
        return pd.DataFrame()
    df = pd.concat(frames, names=["station"])
    df.to_csv(OUT / "tilt.csv")
    return df


def plot(quakes: pd.DataFrame, rsam: pd.DataFrame) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7), sharex=True)
    if not rsam.empty:
        rsam.plot(ax=ax1, lw=0.8)
        ax1.set_ylabel("RSAM (counts)")
        ax1.set_title("Kīlauea summit — tremor proxy (10-min RSAM)")
    if not quakes.empty:
        ax2.scatter(quakes["time"], quakes["mag"], s=12, alpha=0.6)
        ax2.set_ylabel("magnitude")
        ax2.set_title("Summit-region earthquakes (8 km radius)")
    fig.tight_layout()
    fig.savefig(OUT / "summit_picture.png", dpi=150)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--start", required=True)
    p.add_argument("--end", required=True)
    args = p.parse_args()
    OUT.mkdir(exist_ok=True)

    print("earthquakes...")
    quakes = fetch_earthquakes(args.start, args.end)
    print(f"  {len(quakes)} events")
    print("RSAM from IRIS...")
    rsam = fetch_rsam(args.start, args.end)
    print("tilt...")
    fetch_tilt(args.start, args.end)
    print("plot...")
    plot(quakes, rsam)
    print(f"done -> {OUT}")


if __name__ == "__main__":
    main()
