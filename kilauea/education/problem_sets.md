# VOLC 500 — Problem Set Manifest (all terms)

**Purpose.** Machine-actionable specification of every problem set in the program,
written so a future instructor agent (e.g., Claude Opus) can instantiate, issue,
and grade any set without further design work. Each entry specifies intent,
required quantitative content, data dependencies, deliverables, and grading
guidance. The instructor expands each problem into fully-worked form (with
numbers) at issue time.

## Instructions to the executing instructor agent

1. **Student profile:** MSc earth science; strong geophysics (continuum
   mechanics, inverse theory, signal processing, Python); PhD-proposal-level
   muon-detection background; 25+ years of Kīlauea field observation; weakest in
   petrology/geochemistry. Do NOT scaffold linear algebra, statistics, or coding.
   DO scaffold phase-equilibria and geochemical reasoning from first principles.
2. **Instantiation:** where a problem says "current," refresh against live
   sources (HVO updates, `kilauea/data/episodes.csv`, tilt releases) before
   issuing — episode counts and tilt values in this manifest freeze at
   2026-07-14 (51st episode pending). Prefer real Kīlauea numbers over invented
   ones; when inventing, state so.
3. **Format per set:** issue as a single document — header (ID, due window,
   est. hours), reading checklist, problems, deliverable spec. Student returns
   written work + notebooks. Grade against the rubric notes; then conduct a
   short oral follow-up probing the weakest answer.
4. **Grading philosophy:** full credit requires correct physics *and* stated
   assumptions *and* order-of-magnitude sanity checks. Deduct for unpropagated
   uncertainty. Reward disagreement with the literature when defended.
5. **Solutions:** generate a worked solution key privately at issue time (do
   not deliver until after grading). If your key and the student disagree,
   re-derive before ruling.
6. **Constants/data the sets assume:** Kīlauea tholeiite melt ρ ≈ 2,600–2,750
   kg/m³, η ≈ 10–10² Pa·s at ~1,150 °C; host rock ρ ≈ 2,300–2,900 kg/m³;
   g = 9.81; HMM reservoir ~1–2 km depth, SC ~3–5 km; UWD at ~1.9 km from the
   vent region; episode-50 deflation 15.3 µrad; pause recharge ~2 µrad/day;
   supply ~0.11 km³/yr combined (PP 1806). Verify against sources when material.

---

# TERM I

## PS-M1.1 — Pressure, buoyancy, and why dikes stall
*Reading: Parfitt & Wilson ch. 1–3. Est. 6 h.*

Objectives: magmastatic reasoning; density filtering; ascent-rate scales.
Problems (expand each with numbers at issue):
1. Compute lithostatic vs magmastatic pressure profiles for a 5-km column
   through layered Hawaiian crust (vesicular basalt over dense cumulates);
   find the level of neutral buoyancy; relate to HMM reservoir depth.
2. Derive dike ascent velocity from the viscous-flow approximation
   (w²Δρg/3η); evaluate for a 1-m basaltic dike; compare with observed
   Kīlauea dike propagation rates (~0.1–1 m/s, e.g. 2018, June 2024).
3. Explain, with a pressure-balance sketch and calculation, why the 1859
   radial vent erupted at 3,380 m on Mauna Loa's flank instead of the summit.
4. Estimate overpressure needed to lift magma the final ~100 m to the
   Halemaʻumaʻu vent rims; compare against the µrad-scale tilt threshold as an
   order-of-magnitude consistency check (state every assumption).
Rubric notes: (2) must non-dimensionalize before plugging numbers; (4) is a
Fermi problem — grade the assumption chain, not the answer.

## PS-M1.2 — Viscosity, volatiles, fragmentation
*Reading: Parfitt & Wilson ch. 4–5. Est. 6 h.*

1. VFT/Giordano-style viscosity estimates for Kīlauea basalt vs a rhyolite at
   eruption temperatures; four-orders-of-magnitude table.
2. Henry's-law solubility: dissolved H₂O and CO₂ vs depth for Hawaiian magma;
   depth of CO₂ vs H₂O exsolution; why Kīlauea outgasses CO₂ at the summit
   even in repose.
3. Bubble growth regimes (viscous vs diffusive limits); compute Peclet-like
   numbers for basalt vs rhyolite; connect to fragmentation criteria.
4. Show quantitatively why Hawaiian basalt fountains rather than pliniates:
   compare bubble rise velocity to melt ascent velocity (the decoupling
   criterion), then state the condition that flips it (the foam-collapse /
   critical-ascent-speed runaway).
Rubric: (4) is the conceptual heart of the whole program; require both regimes
and the crossover expressed as a dimensionless ratio.

## PS-M1.3 — Eruption size bookkeeping
*Reading: Parfitt & Wilson ch. 6–7; Pyle chapter in Encyclopedia. Est. 5 h.*

1. Define and compute Pyle magnitude and intensity for: episode 50
   (5.3M m³ DRE-equivalent, 7 h), episode 3 (8.5 d), Kīlauea Iki 1959 ep. 15,
   2018 LERZ, ʻAilāʻau (~5.2 km³, ~60 yr). One log-log plot.
2. Where does VEI fail for Hawaiian activity? Propose and defend a two-axis
   alternative for episodic fountaining.
3. Mass eruption rate ↔ fountain height: apply the thermal-plume and ballistic
   scalings; test against episodes 43 (1,770 ft) and 46 (~650 ft) with
   published volumes/durations.
Data: `kilauea/data/episodes.csv`. Rubric: unit discipline (bulk vs DRE) is
half the grade on (1).

## PS-M2.1 — Mantle melting arithmetic
*Reading: Encyclopedia pt. I melting chapter; PP 1801 ch. 6 §mantle. Est. 8 h.*

1. Derive batch and fractional (Shaw) melting equations for incompatible
   elements from mass balance; plot C_L/C_0 vs F for D = 0.001, 0.1, 1.
2. Adiabatic decompression: compute melt fraction vs depth for plume mantle
   (potential temperature ~1,550 °C vs MORB ~1,350 °C); why hotspots melt deeper
   and more.
3. Why does Nb/Y track degree of melting? Work the D-values; then reproduce the
   logic of the Pietruszka 2010-shift argument and state what would falsify it.
4. Estimate Hawaiian plume volume flux from buoyancy-flux literature values;
   compare with the ~0.1–0.2 km³/yr magma supply; comment on melt-extraction
   efficiency.
Rubric: (3) must reach "lower F → higher Nb/Y" via arithmetic, not citation.

## PS-M2.2 — Phase diagrams I (binary/ternary)
*Reading: Winter chs. on phase equilibria or equivalent; MELTS applet warmup.
Est. 8 h.*

1. Di–An binary: liquidus/solidus reading, lever rule at three temperatures,
   equilibrium vs fractional crystallization paths.
2. Fo–Di–An ternary: cotectic descent from a picritic composition; predict the
   crystallization sequence olivine → olivine+cpx → +plag; compare with
   observed Kīlauea phenocryst assemblages (PP 1801 ch. 6).
3. Peritectic behavior (Fo–SiO₂): incongruent melting; why olivine + evolved
   liquid can coexist; relevance to olivine-control trends.
Rubric: hand-drawn (or hand-plotted) diagrams with labeled arrows required;
software allowed only to check.

## PS-M2.3 — Fractional crystallization & olivine control
*Reading: PP 1801 ch. 6. Est. 6 h.*

1. On an MgO–CaO/Al₂O₃ plot of GEOROC Kīlauea data (student pulls it),
   identify the olivine-control line; compute the Fo content of the
   controlling olivine from the array slope.
2. Rayleigh fractionation of Ni (D_Ni^ol ≈ 10–15): how fast does Ni crash?
   Use it to bound percent olivine removed between a parental (MgO ~16%) and
   erupted (MgO ~7%) Kīlauea melt.
3. Where does the "missing" olivine live? Reconcile with the cumulate-rich
   south caldera / rift stored volumes and the 2018 evidence.
Data: GEOROC/EarthChem export. Rubric: (1)-(2) numeric; (3) essay, cite PP 1801.

## PS-M2.4 — Trace elements as process fingerprints
*Est. 6 h.*

1. Spidergram construction from raw GEOROC data: normalize three Kīlauea lavas
   and one Mauna Loa lava to primitive mantle; annotate every anomaly you can
   defend.
2. Partial melting vs fractional crystallization: design the discrimination
   test (which ratios move, which don't) and apply it to episodic-eruption
   glasses vs 1959 Iki picrites.
3. The Keanakākoʻi problem: given Lynn et al.'s Fo89 olivines and primitive
   melts, compute what F and/or transit-time change is implied vs the modern
   evolved (Fo81) regime — the low-supply signature, quantified.
Rubric: (3) is the bridge to Swanson's supply cycle; require an explicit
supply-rate statement.

## PS-M2.5 — Radiogenic isotopes & mixing
*Reading: Pietruszka et al. 2024 (egae121) with supplement. Est. 8 h.*

1. Why melting/crystallization can't fractionate ⁸⁷Sr/⁸⁶Sr or ²⁰⁶Pb/²⁰⁴Pb;
   two-component mixing hyperbola derivation; when is it a straight line?
2. Digitize (or re-derive from published values) the Kīlauea and Mauna Loa
   Pb–Sr arrays; show algebraically why two orthogonal linear trends demand
   ≥3 endmembers; locate the shared-component intersection with uncertainty.
3. The Os objection: given ¹⁸⁷Os/¹⁸⁸Os constant at 0.1357 ± 0.0013 in Mauna Loa
   lavas, compute the maximum mass fraction of shared-source melt permitted
   under stated endmember assumptions. Then argue both sides in ≤500 words.
Rubric: (3) is pre-work for the M10 term paper; grade the bounding calculation
hardest.

## PS-M2.6 — High-pressure fractionation (the Wanless problem)
*Reading: Wanless et al. 2006 ×2. Est. 6 h. Pairs with alphaMELTS lab.*

1. Why does cpx replace olivine as the dominant liquidus phase near 1 GPa?
   (Gibbs / phase-boundary shift argument, qualitative but rigorous.)
2. Using the student's own alphaMELTS runs: tabulate liquid alkalinity index
   vs pressure of fractionation; find the minimum pressure that yields the
   Moʻikeha hawaiite (~5.5 wt% total alkalies) from a Mauna Loa tholeiite.
3. Defend or refute: "the radial-vent alkalics require a separate deep conduit
   that bypasses the summit reservoir." Use degassed-vs-undegassed cone
   morphology as independent evidence.
Rubric: (2) must cite run files; (3) graded as a mini peer-review.

## PS-M3.1 — The Mogi problem, owned
*Reading: Segall volcano-deformation chapters. Est. 6 h.*

1. Derive surface displacements for a point pressure source in an elastic
   half-space; obtain the tilt field by differentiation; show max tilt at
   r = d/2·√2 (verify the geometry factor yourself — do not trust this
   manifest).
2. With HMM at ~1.5 km depth and UWD at ~1.9 km horizontal distance: compute
   µrad per 10⁶ m³ of ΔV; then convert episode-50's 15.3 µrad to ΔV and
   compare against its erupted 5.3M m³ — interpret the ratio (drainback?
   compressibility? geometry?).
3. Sensitivity: how would the same episode read on SDH? Why does losing SDH
   matter (or not) for the threshold forecast?
Rubric: (2)'s discrepancy discussion is the point — magma compressibility must
appear.

## PS-M3.2 — Trade-offs and what one tiltmeter can't know
*Est. 5 h.*

1. Show the depth–ΔV trade-off for a single tilt observation analytically;
   then demonstrate numerically how adding one GPS vertical breaks it.
2. Bayesian setup (student's choice of sampler): invert synthetic UWD-only
   data for depth/ΔV with realistic noise; report posterior; discuss
   identifiability honestly.
3. The July 2026 deflationary interruptions: pose two source hypotheses
   (shallow leak vs deep supply throttle) and design the observation that
   discriminates them (what would each look like on UWD vs GNSS vs gravity?).
Rubric: (3) is graded as experimental design.

## PS-M3.3 — Geometry discrimination
*Reading: Segall crack/sill chapters; Anderson 2019; Wang 2021. Est. 5 h.*

1. Sphere vs sill vs dike: characteristic displacement/tilt patterns; build
   the discrimination table.
2. The 2018 collapse: from Anderson's <4% withdrawal / ~17 MPa result, back
   out reservoir volume and compressibility assumptions; verify the arithmetic.
3. Episode-30 dike (Aug 2025): given precursory rim seismicity and a new
   fissure, sketch the deformation field a summit tilt network should have
   seen; what did the single-station record permit HVO to conclude?
Rubric: (2) must reproduce Anderson's numbers within stated rounding.

## PS-M4.1 — Signal taxonomy with physics attached
*Reading: Chouet & Matoza 2013 §§1–4; McNutt chapter. Est. 6 h.*

1. VT vs LP vs VLP vs tremor: for each, the source model, characteristic band,
   and one Kīlauea 2024–26 example (student pulls waveforms).
2. Fluid-filled crack resonance: compute fundamental frequency for a crack of
   given dimensions/fluid; invert the observed 4–5 Hz piston-burst band for
   plausible geometries; state the crack-stiffness degeneracy.
3. Why is eruption tremor broadband and sustained? Compare three published
   tremor mechanisms and identify which the fountaining episodes favor
   (justify from RSAM behavior at onset/end abruptness).
Rubric: (2) degeneracy statement mandatory.

## PS-M4.2 — RSAM/SSAM engineering
*Est. 5 h. Builds directly on `data/fetch/onset_watch.py`.*

1. Design trade-offs in RSAM: window length, filtering, station choice —
   quantify each with real HV data around one onset.
2. Detection statistics for gas-piston bursts: build ROC curves for two
   detector designs against a hand-labeled hour of the 2026-07-09→11 sequence.
3. Define, quantitatively, the four regimes of the mode ladder
   (baseline/piston/precursory/eruptive) from data alone; compare with the
   thresholds hard-coded in `onset_watch.py`; propose improvements as a PR.
Rubric: (3) deliverable is an actual pull request; grade the diff.

## PS-M4.3 — The coupled transition
*Reading: Chouet & Dawson 2015. Est. 6 h.*

1. For episode 51's actual onset (or 50's if 51 hasn't fired): measure the
   tremor ramp time, the tilt inflection time, and first-fountain time from
   webcam frames; bound the physical delays between reservoir, conduit, and
   surface.
2. VLP inversion in concept: what station geometry would resolve the piston
   source's moment tensor? Design the minimal network.
3. Energy: integrate RSAM-proxy energy across one full episode; compare
   seismic energy to thermal/kinetic output (order of magnitude); why is
   seismic efficiency so low?
Rubric: (1) is the star — real timing measurements with uncertainties.

---

# TERM II

## PS-M5.1 — Conduit flow regimes (3 problems: derive the two-phase flow-regime
map for basaltic conduits; compute where in the conduit episode-era Kīlauea
sits; slug vs churn vs annular and their surface expressions). *Gonnermann &
Manga 2013 is the source; est. 6 h.*

## PS-M5.2 — Bubbles with numbers (nucleation supersaturation thresholds;
diffusive growth timescales; coalescence and permeability onset; compute foam
stability time for Halemaʻumaʻu magma and compare with observed piston periods
of 5–15 min — the quantitative gas-piston test). *Est. 7 h.*

## PS-M5.3 — The runaway (linear stability sketch of the fountaining
transition: perturb ascent rate, track gas-volume feedback; derive the critical
ascent speed concept; map onto the observed abrupt onsets and abrupt ends —
why is the system bistable?). *Est. 7 h. This is the theory core of capstone
topic 2.*

## PS-M6.1 — Volatile budgets (petrologic method end-to-end: from melt-inclusion
and matrix-glass H₂O/CO₂/S to per-episode SO₂ mass; predict episode-50's SO₂
release from its volume; compare with reported tens-of-kt/day rates). *Est. 6 h.*

## PS-M6.2 — Plume transport (SO₂ column → mass: what TROPOMI actually
measures; compute expected DU signal for a 30 kt/day episode under trade-wind
advection; design the per-episode integration scheme used in capstone topic 5).
*Est. 6 h.*

## PS-M6.3 — Foam vs slug, adjudicated (write the discriminating-predictions
table for the three gas-piston models — shallow foam, deep slug, dynamic
pressure balance — across seismic, gravity, SO₂, and visual observables; score
each against Patrick 2016, Poland 2018, and the 2026 observations; verdict with
uncertainty). *Est. 6 h; graded as a review memo.*

## PS-M7.1 — Fountain mechanics (Wilson ballistic + gas-thrust scalings;
compute predicted height vs mass flux curve; place all 51+ episodes; residual
analysis — what explains the scatter: vent geometry, gas fraction, drainback?).
*Est. 6 h; feeds capstone topic 4.*

## PS-M7.2 — Comparative episodicity (build the comparison table: Kīlauea Iki
1959 / Mauna Ulu 1969 / Puʻuʻōʻō 1983–86 / Fagradalsfjall 2021 / current —
periods, heights, supply rates, pause behavior; test the "supply rate sets
period" hypothesis quantitatively). *Est. 6 h.*

## PS-M8.1 — Keanakākoʻi physics (phreatomagmatic energetics: water-magma mass
ratios and explosivity; compute the water influx needed for a 1790-class event
given post-2018 water-table geometry — why refill is de-arming the system).
*Est. 5 h.*

## PS-M8.2 — Tephra transport (Tephra2 hands-on: reproduce the episode-38 ash
footprint qualitatively; then the 1790 scenario under two wind profiles;
sensitivity to column height and grain-size distribution). *Est. 6 h.*

## PS-M8.3 — Hazard quantification (fountaining hazards matrix: tephra,
Pele's hair, SO₂/vog, inclined fountains, void spaces; for each: exposure,
forecastability, and the episode-38/41 case studies; write the public-facing
one-pager and the technical appendix). *Est. 5 h.*

---

# TERM III

## PS-M9.1 — Evidence-chain audit (take the 1500 CE → present narrative and, for
ten load-bearing claims, attach the primary evidence and its uncertainty:
e.g., caldera date, ʻAilāʻau volume, 1790 fatalities, 1840 supply drop,
1924 mechanism; flag the three weakest links in the standard story).
*Est. 8 h; sources: PP 1350, PP 1801, PP 1806, Swanson papers.*

## PS-M9.2 — The supply ledger (reconcile PP 1806's 1790–2008 supply history
with post-2008 estimates and the current 0.18 km³/yr; build the 235-year
supply-rate time series with uncertainties; identify every regime change and
its proposed cause). *Est. 7 h; feeds the M10 paper and capstone topic 2.*

## PS-M10.1 — Plume geometry problems (Loa/Kea endmember geochemistry;
compute expected isotopic drift as the island migrates; where does the
"horizontal gradient vs bilateral asymmetry" debate become testable? Design
the sample set that settles it). *Est. 6 h.*

## PS-M10.2 — Position paper prep (structured argument map for the shared-source
hypothesis: every published claim, its evidence class, its strongest objection;
ends in the student's 3,000-word M10 term paper — the manifest entry for that
paper: thesis required, ≥15 primary sources, one original calculation).
*Est. 12 h including paper.*

## PS-M11.1 — Forecast verification (score HVO's episode windows 1–51+ as
probabilistic forecasts: reliability, sharpness, Brier-style scoring adapted to
windows; where does the tilt-target model fail and why — stalls, storms,
threshold drift). *Est. 7 h; the statistical spine of capstone topic 2.*

## PS-M11.2 — Build-your-own forecast (using public tilt + the episode catalog:
implement the threshold model with uncertainty; hindcast episodes 45–51;
compare skill against HVO's published windows; write the honest limitations
section). *Est. 8 h.*

---

# TERM IV

## PS-M12.1 — dv/v practicum (MSNoise/SeisMIC on one pause–episode cycle of HV
data; do coseismic-episode velocity drops exist? compare against Reiss et al.'s
EGU abstract claims; document processing choices completely). *Est. 8 h.*

## PS-M12.2 — Muography forward problem (MUYSC + 3DEP DEM: compute integrated
density along sightlines from three candidate detector sites toward the north
vent cone; exposure-time table for 1 m² detector; identify the single best
site and its resolvable target — the feasibility kernel of capstone topic 1).
*Est. 10 h.*

## CAP-GATES — Capstone gate reviews (three scheduled instructor reviews:
G1 proposal defense — scope, data, methods, venue; G2 midpoint — results
audit, pivot decision; G3 pre-submission — full manuscript, triple-referee
mock review with written reports in the style of the target journal).
*The executing agent runs all three; G3 referee reports are graded documents.*

---

## Administrative notes for the executing agent

- Issue one set at a time; do not release solution keys forward.
- Every set's oral follow-up: 15 min, three questions, at least one drawn from
  the student's weakest written answer and one connecting to live volcano state.
- Log completions by appending to `kilauea/education/progress.md` (create on
  first use: date, set ID, grade, oral notes, follow-ups owed).
- If the eruption has ended or transitioned by execution time, adapt "current
  episode" references to the most recent analogous activity and note the
  adaptation in the issued set.
- The student may negotiate scope; hold the line on M2 rigor and on
  uncertainty-propagation everywhere.
