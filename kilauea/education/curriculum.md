# DIY MSc-Equivalent Program in Volcanology

**Designed 2026-07-13 for a student with an MSc in earth science, deep geophysics
background (cosmic-ray muon detection for magma-body imaging), and 25+ years of
Kīlauea field observation.** Format: interactive — each module is run as a seminar
with Claude in this workspace: readings → problem set (generated and graded against
your reasoning, oral-exam style) → data lab on real Hawaiian data → discussion.
Estimated effort: ~600–700 hours ≈ 2 academic years part-time (10–12 h/wk), or
~1 year at half-time intensity. All resources verified available as of Jul 2026
(see `notes_resources.md`); free unless marked [$].

**Spine texts** (used across modules):
- Parfitt & Wilson, *Fundamentals of Physical Volcanology* (2008) [$]
- Sigurdsson et al. (eds), *Encyclopedia of Volcanoes*, 2nd ed. (2015) [$] — reference
- Fagents, Gregg & Lopes (eds), *Modeling Volcanic Processes* (2013) [$] — the
  quantitative bridge text; your calculus/continuum background makes this the core
- Segall, *Earthquake and Volcano Deformation* (2010) [$]
- USGS PP 1801 *Characteristics of Hawaiian Volcanoes* (2014) — free, the Hawaiʻi bible

---

## Term 1 — Foundations (4 modules, ~160 h)

### M1. Physical volcanology & eruption dynamics
- Read: Parfitt & Wilson ch. 1–7; Cashman & Sparks 2013 GSA Bull "How volcanoes
  work: a 25-year perspective."
- Problem sets: magmastatic pressure/ascent-rate calcs; fragmentation criteria;
  eruption-style regime diagrams.
- Lab: classify all 50+ episodes of the current eruption (our `data/episodes.csv`)
  on a Hawaiian-fountaining intensity/duration diagram; compare Puʻuʻōʻō 1983–86.

### M2. Magma genesis, petrology & geochemistry ← your biggest gap; go slow
- Read: Encyclopedia of Volcanoes pt. I; PP 1801 ch. 6 (petrologic insights);
  Cashman, Sparks & Blundy 2017 *Science* (transcrustal mush systems); Phil Trans
  R Soc A 377:20180298 (reservoir architecture).
- Problem sets: mantle melting (batch/fractional, adiabats); phase diagrams
  (Fo–Di–An); fractional crystallization arithmetic; tholeiite vs alkalic
  discrimination; isotope mixing math (build to the Pietruszka three-source model).
- Labs: (a) alphaMELTS 2 — crystallize a Kīlauea parental melt at 1 atm and 1 GPa,
  reproduce the Wanless radial-vent alkalic result yourself; (b) pull GEOROC
  Kīlauea/Mauna Loa glass data, replot the Pb–Sr orthogonal trends from egae121;
  (c) Thermobar thermobarometry on published 2020–24 Halemaʻumaʻu glasses.

### M3. Volcano geodesy ← your strength; move fast, focus on volcano-specific models
- Read: Segall ch. 7–9, 12 (magma chamber, dike, viscoelastic sources); PP 1801
  ch. 5 (magma supply/storage/transport); Wang et al. 2021 JGR (post-2018 refill
  constrains the reservoir system); Anderson et al. 2020 *Science* (collapse).
- Problem sets: Mogi/spheroid/sill forward models; tilt vs GPS sensitivity; why UWD
  sees what it sees (map its position vs the HMM and SC reservoirs).
- Labs: (a) invert the public 2024–25 UWD tilt releases for source depth/ΔV per
  episode (GBIS or hand-rolled MCMC — your call); (b) ASF HyP3 → MintPy Sentinel-1
  time series over the summit 2021–2026; recover the sawtooth.

### M4. Volcano seismology
- Read: Chouet & Matoza 2013 JVGR (the review); Matoza & Roman 2022; Thelen et al.
  2022 (open IAVCEI PDF); Chouet & Dawson 2015 (gas-piston VLPs — you watched
  these live this week).
- Problem sets: LP/VLP source mechanisms; tremor source models; RSAM/SSAM design.
- Labs: (a) ObsPy + IRIS FDSN: pull HV continuous data around three episode onsets,
  build RSAM, find the precursory intermediate band you observed on 2026-07-11;
  (b) locate gas-piston bursts by cross-station amplitude ratios; (c) spectrogram
  the onset tremor ramp of episode 51 (when it happens).

## Term 2 — Dynamics (4 modules, ~160 h)

### M5. Conduit physics & magma rheology
- Read: Gonnermann & Manga 2007 Annu Rev Fluid Mech; Gonnermann & Manga 2013 (in
  *Modeling Volcanic Processes*); Gonnermann 2015 (fragmentation).
- Problem sets: bubble nucleation/growth; permeability development; conduit flow
  regimes; the critical-ascent-speed fountaining threshold (the "champagne cork").

### M6. Degassing, volatiles & gas monitoring
- Read: PP 1801 ch. 7 (100 years of gas at HVO); Encyclopedia pt. IV gas chapters;
  Patrick et al. 2016 EPSL + Poland et al. 2018 GRL (gas pistoning: foam vs slug).
- Labs: (a) TROPOMI SO2 retrievals over the 2024–26 episodes (Copernicus open
  data); per-episode mass loading vs the USGS traverse data release 2023–25;
  (b) solubility modeling (SolEx/VolatileCalc-class tools) for Kīlauea melt.

### M7. Hawaiian & Strombolian eruption mechanisms
- Read: Head & Wilson fountaining theory (via Parfitt & Wilson ch. 6 + refs);
  Fagradalsfjall cyclic fountaining (Nat Comms 2023) and Geldingadalir tremor
  (Bull Volc 2022) as the comparative modern dataset; Volcano Watch mechanism
  pieces (in `../report/notes/mechanism_science.md`).
- Lab: dimensional analysis of fountain height vs mass flux; test against the 50
  episodes; where does episode 43's 540 m sit vs Kīlauea Iki's 580 m?

### M8. Explosive volcanism, tephra & hazards
- Read: Encyclopedia explosive chapters; Swanson Keanakākoʻi papers; Houghton et
  al. on the 2018 explosions and the "stomp-rocket" mechanism (Nature Geosci 2024).
- Labs: (a) Tephra2 (VICTOR or local): reproduce plausible 1790-class dispersal
  under trade-wind vs Kona-wind profiles; (b) Q-LavHA lava-flow inundation from a
  hypothetical caldera-overflow vent (ties to `../report/outlook.md` §4).

## Term 3 — Hawaiʻi Specialization (3 modules, ~140 h)

### M9. Hawaiian volcanism: the canon
- Read: PP 1801 ch. 1, 3, 4; PP 1350 selected chapters (Lockwood radiocarbon,
  Klein eruption patterns, Decker overview); PP 1806 (200 years of supply);
  PP 1867 series (2018); Neal et al. 2019 *Science* (open PDF).
- Seminar: reconstruct the full 1500 CE → present narrative from primary sources —
  you already know the story; now attach the evidence chain to every link.

### M10. Hotspot geochemistry & the plume
- Read: Loa/Kea literature; Pietruszka et al. 2024 egae121 + the Os follow-up;
  Wilding et al. 2022 (magmatic web); DePaolo & Stolper 1996 (plume-transit
  models); Lipman 1995 / Lipman & Moore 1996.
- Seminar: the diversion-hypothesis debate — write a 3,000-word review taking a
  position (you're halfway there from this week's discussions).

### M11. Monitoring & forecasting operations
- Read: PP 1801 ch. 2; HVO forecast-window methodology (Volcano Watch May 2026);
  alert-level/notification system docs; Wu et al. 2025 AGU Adv (dv/v before 2018);
  Gao et al. 2025 arXiv (eikonal imaging + uncertainty).
- MOOC: edX UIcelandX "Monitoring Volcanoes and Magma Movements" (audit, free).
- Lab: build your own episode-51+ forecast tool from public tilt (you informally
  ran this exercise live on 2026-07-11–13; now formalize it with uncertainty).

## Term 4 — Research Methods & Capstone (~150 h)

### M12. Research toolchain
- MSNoise/SeisMIC dv/v pipeline on HV data (one pause–episode cycle).
- covseisnet network covariance on the precursory band.
- MUYSC muography simulation toolbox — bridge module to your capstone (see
  `research_topics.md` topic 1).
- VICTOR hub orientation (check independent-account eligibility).

### Capstone
One of the five topics in `research_topics.md`, executed to submission-ready
draft (Volcanica, JVGR, Bull Volc, or GJI depending on topic). The episode
dataset in `../data/episodes.csv` and the fetch tooling in `../data/fetch/` are
your starting corpus.

### Optional intensives
- **UH Hilo CSAV International Training Program** — 8 weeks (Jun 6–Aug 1 2026
  session; next cohort apply by Dec 1), $9,000 incl. housing, cohort <12, open to
  unaffiliated applicants; UH Hilo + Cascades Volcano Observatory/Mount St.
  Helens. The single highest-value credential-adjacent experience available to an
  independent. https://hilo.hawaii.edu/csav/international/
- **HVO volunteer program** — ≥3-month placements, open to non-students,
  includes individual research projects. The insider path.
  https://www.usgs.gov/observatories/hvo/volunteer-hawaiian-volcano-observatory
- HVO Volcano Awareness Month talks (every January, in-person — you're local
  often enough).

## Assessment (how we keep it honest)
- Per module: problem set (graded), data-lab notebook (reviewed), 45-min oral
  exam with Claude (you defend, I probe — Socratic, no multiple choice).
- Per term: one 2,500–3,500-word synthesis paper.
- Capstone: full draft + mock peer review (I referee as three different reviewers).
