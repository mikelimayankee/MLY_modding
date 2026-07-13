# Five Research Topics for an Independent Geophysicist — Hawaiʻi Volcanism

**Vetted against the literature 2026-07-13** (gap-scan sources in `notes_gaps.md`).
Selection criteria: (1) genuine verified gap; (2) executable with public data and
no lab/institutional affiliation; (3) leverages a deep-geophysics + muon-detection
background; (4) publishable venue identified. Ranked by fit.

---

## 1. Muography feasibility study for Kīlauea — the first for any Hawaiian volcano

**The gap, verified:** No muography study, deployment, or published proposal exists
for Kīlauea, Mauna Loa, or any Hawaiian volcano. Tanaka-school target lists cover
Japan, Italy, Guadeloupe, Colombia — Hawaiʻi is absent. No US volcano deployment
exists at all.

**Why the gap exists (and why it's the paper, not the obstacle):** muography images
the top few hundred meters of edifice along near-horizontal sightlines — steep
stratocones are ideal; a broad low shield with a 1–2 km-deep reservoir is not. But
post-2018 Kīlauea is not the pre-2018 shield: there is now a 500+ m-deep caldera
with near-vertical scarps, a rebuilding vent-cone complex, a growing tephra
blanket, and 88+ m of new lava fill of unknown density structure. Whether any
site geometry yields usable muon flux through scientifically interesting rock —
the vent cones, the down-dropped block edge, the collapse-scarp stratigraphy, the
solidified-vs-molten fill — is an open, quantitative, answerable question.

**Method (all ingredients public):** MUYSC end-to-end muography simulator (GJI
2024) + USGS 2019 lidar and 2020–2026 rapid-response DEM series + density priors
from Gao et al. 2025 eikonal tomography (arXiv:2507.23692) + detector performance
specs from the MURAVES (Vesuvius) and Sakurajima papers. Compute
acceptance/exposure/resolution for candidate sites; propagate DEM and density
uncertainty; deliver a site-selection and sensitivity atlas (template: the
Colombian methodology paper, arXiv:1705.09884).

**Deliverable & venue:** "Muographic imaging potential of post-collapse Kīlauea:
a feasibility and site-selection study" — GJI, JVGR, or Volcanica. Zero deployment
required. Follow-on if positive: NPS research permit (RPRS — open to members of
the public) + HVO coordination for a pilot detector. This is your PhD proposal,
resurrected, aimed at an unclaimed target.

## 2. Failure-time statistics and a relaxation-oscillator model of the episode cycles

**The gap, verified:** No renewal-process/hazard-function statistical model and no
ODE-level oscillator model of the 2024–26 episodic cycles has been published.
HVO's forecasting is empirical tilt-threshold extrapolation, self-described as
imperfect. Analog models exist for Puʻuʻōʻō 1983–86 (dike thermal-balance, JVGR
1994) and Fagradalsfjall (Nat Comms 2023) — nobody has done the current sequence,
which is the best-instrumented episodic basaltic eruption in history.

**Method:** public UWD tilt data releases (2024, H1-2025, more coming) + the
episode catalog (start from `../data/episodes.csv`, harden it against USGS
notices). Fit hazard functions for onset conditional on re-inflation fraction;
quantify how deflationary interruptions (this week's live case!) reset the clock;
build the minimal ODE (recharge–threshold–discharge with gas-piston leakage) and
test against 50+ cycles. Bonus: out-of-sample forecast skill vs HVO's published
windows — you have the receipts, we catalogued every window this week.

**Venue:** Bulletin of Volcanology or GRL-class letter. Timeline: months.

## 3. Open episode catalog + automated gas-piston/drainback event detection

**The gap, verified:** No machine-readable public catalog of the 50+ episodes
exists (an unofficial site maintains one; provenance unverified). HVO counts
precursory overflow–drainback events manually (">180 events" before ep. 36).
No automated gas-piston catalog exists for 2024–26 (or for the 2008–2018 lake
era at scale).

**Method:** HV network continuous data (fully open via FDSN) + STA/LTA and
spectral classifiers (or a VOISS-Net-style CNN) for the burst events; validate
against HVO's manual counts and webcam timelapses; publish the catalog + code as
an infrastructure paper (Volcanica explicitly welcomes these) with a DOI'd
dataset. This becomes the substrate for topics 2 and 4 — and a community service
that makes an independent researcher's name known at HVO.

**Venue:** Volcanica (open access, no APC) or Seismica. Timeline: months, mostly
engineering you already know how to do.

## 4. Fountain-height / tilt-drop / volume scaling — the energy budget of an episode

**The gap, verified:** No published quantitative scaling analysis across the
episodes (height vs deflation magnitude vs erupted volume vs pause length), and
drainback volumes are explicitly poorly quantified (USGS lava-level algorithms
"ignore periods when the lava level drops"). The foam-collapse/critical-ascent
fountaining model makes testable predictions nobody has tested against the 50-
episode ensemble.

**Method:** per-episode fountain heights and volumes (USGS notices/chronologies —
already half-assembled in our dataset), UWD tilt drops (µrad → ΔV via M3-lab
source models), rapid-response DEM differencing for fill volumes (public
ScienceBase series). Ask: does height scale with reservoir overpressure proxy?
Is the ~60% erupted-to-fill efficiency (our `outlook.md` estimate) stable? What
does the missing mass (drainback + densification) do episode to episode?

**Venue:** JVGR or Bull Volc. Pairs naturally with topic 2 (one dataset, two papers).

## 5. Per-episode SO2 mass balance from TROPOMI

**The gap, verified:** No published satellite SO2 analysis of the 2024–26 episodes.
Precedent methodology exists (TROPOMI/PlumeTraj on Mauna Loa 2022, La Palma).
Episodes emit tens of kt/day vs 1–5 kt/day in pauses — a huge, cleanly episodic
signal nobody has integrated.

**Method:** Copernicus S5P L2 SO2 (open) + PlumeTraj-class trajectory analysis;
integrate per-episode SO2 mass; compare against erupted volume (petrologic method
in reverse) to partition syn-eruptive vs pause degassing — a direct test of the
gas-accumulation models for episodic fountaining, and a completely independent
check on the tilt-based mass balance of topic 4.

**Venue:** GRL, JGR-Atmospheres-adjacent, or Bull Volc. Ground-truth: USGS
2023–25 traverse data release.

---

## Practical notes for the unaffiliated researcher

- **Permits:** anything *deployed* in Hawaiʻi Volcanoes NP needs an NPS Scientific
  Research & Collecting Permit (RPRS, open to the public) + park approval; current
  vents are inside the park, so a muon pilot also means HVO coordination. Pure
  data/modeling work (topics 2–5, and topic 1's feasibility phase) needs nothing.
- **Paths to legitimacy:** HVO volunteer program (≥3 months, individual research
  projects, open to non-students); UH Hilo CSAV international course; presenting
  at AGU/IAVCEI as an independent (normal and accepted); Volcanica/Seismica as
  APC-free open venues friendly to unaffiliated authors.
- **Precedent that this works:** Hawaiian-language newspaper archive research
  became USGS SIR 2019-5010 and JVGR papers; Raspberry Shake citizen data appears
  in 78+ peer-reviewed publications; Hawaiʻi Tracker went from Facebook group to
  an HVERI nonprofit program. Independent contribution to Hawaiʻi volcanology is
  an established genre, not an aspiration.
- **Priority collision warning:** the Reiss (EGU26-9963) group is actively working
  dv/v + tremor on the 2024–26 sequence — avoid head-on competition there;
  topics 1–5 above are chosen to be orthogonal to their published trajectory.
