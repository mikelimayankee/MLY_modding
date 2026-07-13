# Agent sweep notes: research gaps, muography status, data availability (2026-07-13)

(Condensed from research-agent output; quotes via search extraction — verify before
formal citation. Full details in agent transcript.)

## Muography

- VERIFIED GAP: no muography study/deployment/proposal for any Hawaiian volcano;
  no US volcano deployment at all. Absent from all Tanaka-school target lists.
- State of the art: Sakurajima (Oláh 2023 GRL, 2024 JGR — branched conduit,
  eruption-frequency link, ML forecasting from muographs); Vesuvius MURAVES (three
  1 m² scintillator trackers, ~1.5 km from summit, autonomous/low-power); Etna
  (detected cavity months before 2017 crater collapse); Stromboli (first muograph
  2019: 30–40% summit density deficit); La Soufrière (dynamic hydrothermal
  radiography); Puy de Dôme (joint muon+gravity Bayesian inversion).
- Reviews: Nature Reviews Methods Primers "Muography" (2023); Proc R Soc A
  477:20210320 (2021); Tanaka AGU monograph ch. 1 (2022); J Appl Phys 138:060701
  (2025, joint muography+deformation).
- Logistics: ~1 m² detector, 0.5–1 km rock, ~100 days for 5% density at 3°×3°;
  ~10 mrad angular resolution ≈ 10 m at 1 km; modular arrays cut exposure to weeks.
- Physical caveat: near-horizontal sightlines, top few hundred m only — shield
  geometry unfavorable; post-2018 caldera scarps/vent cones change the calculus.
  No published statement on Kīlauea's muographability exists either way.
- Tools for feasibility work: MUYSC simulation toolbox (GJI 237:540, 2024);
  Colombian site-selection template (arXiv:1705.09884); density priors from
  Gao et al. 2025 eikonal imaging (arXiv:2507.23692).

## Stated open questions, 2024–26 eruption

- Gas piston → fountaining link: HVO "does not yet have a full understanding of
  why the gas pistons are often a precursor... or why they might behave
  differently from episode to episode" (Volcano Watch Jul 2025).
- Vent dominance: since ep. 44 only the north vent fountains; "HVO scientists are
  still unsure what this means." Eps. 47–48 had south-vent-only precursory
  overflows yet north-vent fountaining.
- Forecasts "aren't perfect. Changes in the reinflation rate, brief deformation
  reversals, or even heavy rain can shift the timing."
- "We don't know when or how this eruption will end" (FAQ). No published
  explanation of abrupt episode terminations.
- Reservoir geometry: HMM vs SC distinct or one irregular body — unresolved
  (Wang et al. 2021 JGR); "architecture of subcaldera magma reservoirs... poorly
  understood" (Anderson et al. 2020).
- Gas-piston physics: foam vs slug vs dynamic-pressure-balance still live
  (Patrick 2016 EPSL; Poland 2018 GRL gravity → low-density foams).
- NO peer-reviewed paper on the 2024–26 eruption exists yet (Jul 2026) — only
  EGU abstracts (EGU26-9963 Reiss et al. dv/v+tremor+geodesy; EGU26-14959 Roman
  et al. pre/post-fountaining seismics; EGU26-810 SWRZ fault reactivation),
  Volcano Watch, and USGS notices.

## Public data

- Seismic: HV network fully open (FDSN/IRIS/EarthScope). 2024 ERZ 116-node
  campaign: archive status unconfirmed.
- GNSS: EarthScope/GAGE open (registration).
- Tilt: no public real-time API; batch data releases (2024 full year:
  ESC/IKI/JKA/KAE/POC/SDH/UWD/UWE; Jan–Jun 2025 DOI 10.5066/P1ZGFGBI); H2-2025+
  release pending.
- DEMs: 2019 airborne lidar (567 km², 30–100 pts/m²); rapid-response DEM series
  2020–present (ScienceBase 6407d404, updated ≥Sep 2025); 2023 NOAA/USGS Big
  Island lidar.
- Webcams live + VolcView/AshCam historical GUI; per-episode timelapses; no bulk
  API.
- Episode statistics: no machine-readable official catalog (gap); HANS public
  JSON APIs exist for notices (volcanoes.usgs.gov/hans-public/api/volcano/).
- SO2: USGS traverse data release 2023–25; TROPOMI open; no published TROPOMI
  study of the 2024–26 episodes (gap).

## Independent-researcher precedent

- Raspberry Shake: 78+ peer-reviewed publications on citizen data.
- Hawaiʻi Tracker → HVERI nonprofit; top-scored info source in perception research.
- Hawaiian-language newspaper archives → USGS SIR 2019-5010, JVGR 2020 (corrected
  1832/1868/1877 records), oral-tradition JVGR paper.
- HVO citizen tool "Is Tephra Falling?" (Feb 2026); HVO volunteer program (≥3 mo,
  open to non-students, individual research projects); CSAV coop research program.
- NPS RPRS permit required for any in-park instrument deployment; open to members
  of the public; no institutional-affiliation requirement found. No written
  USGS/HVO policy on unaffiliated collaboration found — inquire directly.

## Verified modeling gaps (attackable with public data)

1. No relaxation-oscillator / renewal-statistics model of the 2024–26 cycles
   (analogs: Puʻuʻōʻō JVGR 1994; Fagradalsfjall Nat Comms 2023, Bull Volc 2022).
2. No automated gas-piston/drainback catalog (HVO counts manually; ML precedent:
   VOISS-Net; arXiv:2404.19351 deep-learning collapse forecasting at Kīlauea).
3. No fountain-height vs tilt-drop scaling analysis; drainback volumes "poorly
   quantified" (lava-level algorithms ignore drops).
4. dv/v for 2024–26: conference-stage only (Reiss group) — differentiate, don't
   compete head-on. Published baseline: Wu et al. 2025 AGU Adv (pre-2018);
   Sci Adv 2017; EPS 2020; USGS 2018 CWI data release.
5. Muon feasibility/forward modeling: fully open (see above).
6. No TROPOMI per-episode SO2 mass balance.
7. High-res structural baseline for any density imaging: Gao et al. 2025
   (arXiv:2507.23692) eikonal tomography with per-pixel uncertainty.
