#!/usr/bin/env python3
"""Live episode-onset watcher for Kilauea summit seismic data.

Pulls recent HV-network waveforms via FDSN (IRIS/EarthScope), computes 1-minute
RSAM, and classifies the current regime against the four-mode ladder:

  1 BASELINE    quiet pause; RSAM near pause floor, low variance
  2 PISTON      cyclic bursts every ~5-15 min (gas pistons); banded RSAM,
                high burst-to-floor ratio, floor still near baseline
  3 PRECURSORY  sustained elevated RSAM between baseline and eruptive levels
                (dome fountains / overflows); floor ratcheting upward
  4 ERUPTIVE    sustained RSAM >> baseline and climbing/plateaued high;
                with steep deflationary tilt = episode in progress

Run from a machine with open internet (this repo's authoring container has
FDSN hosts blocked). Requires: pip install obspy pandas matplotlib

  python onset_watch.py                 # last 6 h, UWE+RIMD, plot + verdict
  python onset_watch.py --hours 12 --stations UWE,RIMD,OBL
  python onset_watch.py --loop 300      # re-check every 5 min forever

Thresholds are RELATIVE (multiples of a trailing quiet-floor estimate), so no
absolute calibration is needed; still, sanity-check the verdict against the
webcams — a helicopter or rockfall can spoof 10 minutes of anything.
"""

import argparse
import sys
import time

import numpy as np
import pandas as pd

BURST_GAP_MIN, BURST_GAP_MAX = 3.0, 20.0   # gas-piston cadence window (minutes)
PISTON_RATIO = 2.5                         # burst peak vs floor
PRECURSORY_FLOOR = 2.0                     # sustained floor vs baseline floor
ERUPTIVE_FLOOR = 6.0                       # sustained floor vs baseline floor


def fetch_rsam(stations, hours):
    from obspy import UTCDateTime
    from obspy.clients.fdsn import Client

    client = Client("IRIS")
    t1 = UTCDateTime()
    t0 = t1 - hours * 3600
    frames = []
    for sta in stations:
        try:
            st = client.get_waveforms("HV", sta, "*", "HHZ,EHZ", t0, t1)
        except Exception as e:
            print(f"  {sta}: no data ({e})", file=sys.stderr)
            continue
        st.merge(fill_value=0).detrend("demean")
        for tr in st:
            idx = pd.date_range(
                tr.stats.starttime.datetime,
                periods=tr.stats.npts,
                freq=pd.Timedelta(seconds=tr.stats.delta),
            )
            x = pd.Series(np.abs(tr.data), index=idx)
            frames.append(x.resample("1min").mean().rename(sta))
    if not frames:
        raise SystemExit("no data from any station — check network/station codes")
    return pd.concat(frames, axis=1)


def classify(rsam: pd.DataFrame) -> dict:
    """Median-combine stations, then classify the most recent 30 minutes."""
    s = rsam.median(axis=1).dropna()
    # quiet floor: 10th percentile of the full window (assumes window includes
    # some pre-escalation data; widen --hours if everything is already hot)
    floor = np.nanpercentile(s, 10)
    recent = s.iloc[-30:]
    r_floor = np.nanpercentile(recent, 25) / floor
    r_peak = recent.max() / max(np.nanpercentile(recent, 25), 1e-9)

    # burst cadence: peaks > PISTON_RATIO * local floor, spacing in piston band
    peaks = recent[recent > PISTON_RATIO * np.nanpercentile(recent, 25)]
    cadence = None
    if len(peaks) >= 3:
        gaps = np.diff(peaks.index.view("int64")) / 60e9  # minutes
        gaps = gaps[gaps > 1.0]
        if len(gaps) and BURST_GAP_MIN <= np.median(gaps) <= BURST_GAP_MAX:
            cadence = float(np.median(gaps))

    slope = np.polyfit(range(len(recent)), recent.to_numpy(), 1)[0] / floor

    if r_floor >= ERUPTIVE_FLOOR:
        mode, label = 4, "ERUPTIVE — sustained high tremor; if tilt is in steep deflation, the episode is running"
    elif r_floor >= PRECURSORY_FLOOR:
        mode, label = 3, "PRECURSORY — sustained elevated tremor (dome fountains/overflows); onset window is hours-scale"
    elif cadence:
        mode, label = 2, f"PISTON — cyclic bursts every ~{cadence:.0f} min (gas pistons); column is high, watch for escalation"
    else:
        mode, label = 1, "BASELINE — pause floor"

    return dict(
        mode=mode,
        label=label,
        floor_ratio=round(float(r_floor), 2),
        burst_ratio=round(float(r_peak), 2),
        burst_cadence_min=cadence and round(cadence, 1),
        floor_slope_per_min=round(float(slope), 4),
        last_sample=str(s.index[-1]),
    )


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--stations", default="UWE,RIMD")
    p.add_argument("--hours", type=float, default=6)
    p.add_argument("--loop", type=int, default=0, help="re-check every N seconds")
    p.add_argument("--plot", action="store_true")
    args = p.parse_args()
    stations = args.stations.split(",")

    while True:
        rsam = fetch_rsam(stations, args.hours)
        verdict = classify(rsam)
        print(f"\n=== {verdict['last_sample']} UTC ===")
        print(f"MODE {verdict['mode']}: {verdict['label']}")
        for k in ("floor_ratio", "burst_ratio", "burst_cadence_min", "floor_slope_per_min"):
            print(f"  {k}: {verdict[k]}")
        if args.plot:
            import matplotlib

            matplotlib.use("Agg")
            import matplotlib.pyplot as plt

            ax = rsam.plot(figsize=(12, 4), lw=0.8, title="HV 1-min RSAM")
            ax.figure.tight_layout()
            ax.figure.savefig("onset_watch.png", dpi=130)
            print("  plot -> onset_watch.png")
        if not args.loop:
            break
        time.sleep(args.loop)


if __name__ == "__main__":
    main()
