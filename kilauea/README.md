# Kīlauea Summit Eruption — Episode 1–50 Precursor Analysis

Study of the episodic Halemaʻumaʻu lava-fountaining eruption (began 2024-12-23),
assembled 2026-07-11 to answer:

> "Today I saw a decrease in summit tilt accompanied by a seismic signal that was
> between the pre-eruption steady-state signal and the normal baseline. Why?"

## Contents

- `data/episodes.csv` — per-episode dataset (episodes 1–50): onset/end times,
  durations, fountain heights, pause lengths, precursory activity, tilt/tremor notes.
- `report/analysis.md` — narrative + data synthesis: the inflation–deflation cycle,
  gas-piston precursors, the July 2026 sequence, and the interpretation of the
  2026-07-11 observation.
- `data/sources.md` — source URLs for every claim.
- `report/outlook.md` — future scenarios, Holocene precedents, volume ledger.
- `education/` — DIY MSc-equivalent volcanology curriculum and five vetted
  independent-research topics (`curriculum.md`, `research_topics.md`).

## Data-access notes

This environment's egress policy blocks direct HTTPS to `earthquake.usgs.gov`,
`volcanoes.usgs.gov`, `www.usgs.gov`, `volcano.si.edu`, and IRIS web services, so raw
time-series (UWD/SDH tilt, RSAM/tremor, FDSN event catalog) could not be pulled
programmatically. The dataset below is reconstructed from HVO daily updates / HANS
notices, USGS episode chronology pages, and news archives surfaced via web search.
Scripts for pulling the raw series from an unrestricted machine are in `data/fetch/`.
