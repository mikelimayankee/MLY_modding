# VOLC 500 — Term I: Foundations (~160 h, 19 weeks at ~8–10 h/wk)

Detailed plan of study. Convention: [$] = purchase required; everything else is
free/open. Each module ends with a 45-minute oral exam before the next begins.

---

## M1 · Physical Volcanology & Eruption Dynamics — 4 weeks (~60 h)

**Job:** the shared vocabulary and governing physics of eruptions — how magma
ascends, why eruptions take the styles they do, and how intensity/magnitude are
quantified. Sets up every later module.

**Texts**
- Parfitt & Wilson, *Fundamentals of Physical Volcanology* (Wiley-Blackwell,
  2008), ch. 1–7: magma generation and segregation → ascent and storage →
  eruption triggering → explosive vs effusive styles → Hawaiian and Strombolian
  mechanisms. [$] (~230 pp; the term's backbone)
- Cashman & Sparks (2013), "How volcanoes work: a 25-year perspective," *GSA
  Bulletin* 125:664 — the field's self-assessment; read week 1 for the map.
- *Encyclopedia of Volcanoes* 2e (2015): skim pt. II overview chapters as
  reference alongside P&W. [$]

**Problem sets**
1. Magmastatic vs lithostatic pressure; buoyancy-driven ascent rates; when and
   why basaltic dikes stall (density filter → your radial-vent knowledge).
2. Melt viscosity (VFT parameterizations) across basalt→rhyolite; consequences
   for fragmentation.
3. Eruption size bookkeeping: VEI, magnitude and intensity scales (Pyle);
   place episodes 1–51, 1959 Kīlauea Iki, and 2018 LERZ on one axis pair.

**Data lab** — *The episode ensemble as an eruption-physics dataset.*
Using `kilauea/data/episodes.csv`: compute per-episode mean and peak mass
eruption rates from volumes and durations; build the intensity–duration diagram;
overlay Puʻuʻōʻō episodes 4–47 and Kīlauea Iki 1959 from published tables. Where
do the "tall short" episodes (34, 35, 39, 43) plot vs the "long low" ones (3, 16,
17)? Deliverable: notebook + 1-page interpretation.

**Oral exam scope:** ascent physics, style controls, the fountaining threshold
qualitatively (quantitative version returns in M5).

---

## M2 · Magma Genesis, Petrology & Geochemistry — 8 weeks (~70 h)

**Job:** the gap module — deliberately double-length. Everything from mantle
melting to phase diagrams to isotope fingerprinting, built toward reading the
Hawaiian plume literature critically.

**Texts**
- *Encyclopedia of Volcanoes* 2e, pt. I (origin and transport of magma:
  mantle melting, melt migration, magma chambers). [$]
- USGS PP 1801 ch. 6, Helz et al., "Petrologic Insights into Basaltic
  Volcanism at Historically Active Hawaiian Volcanoes" — free:
  https://pubs.usgs.gov/pp/1801/ (the Hawaiʻi-specific spine of the module)
- Cashman, Sparks & Blundy (2017), "Vertically extensive and unstable magmatic
  systems," *Science* 355:eaag3055 — open PDF via the Bristol repository.
- Phil. Trans. R. Soc. A 377:20180298 (2019), magma reservoir architecture — open.
- Application reading: Lynn et al. (2017) *CMP* (Keanakākoʻi primitive magmas =
  low-supply signature); Wanless et al. (2006) *JVGR* (shield-stage alkalics —
  you know the story; now do the petrology).
- Optional desk reference: Winter, *Principles of Igneous and Metamorphic
  Petrology* 2e. [$]

**Problem sets** (weekly, six sets)
1. Batch vs fractional melting equations; adiabatic decompression melting of
   plume mantle; why supply ∝ plume flux.
2. Binary and ternary phase diagrams (Fo–Di–An); lever rule; reading a cotectic.
3. Fractional crystallization arithmetic: olivine control lines on MgO
   diagrams; why Kīlauea whole-rocks scatter along Fo-control.
4. Trace elements: partition coefficients, Rayleigh fractionation, why Nb/Y
   tracks degree of melting (the Pietruszka 2010-shift tracer).
5. Radiogenic isotopes: why Pb/Sr/Nd don't fractionate during melting; mixing
   hyperbolas; derive the three-component requirement from orthogonal trends.
6. High-pressure fractionation: cpx-dominated crystallization at 1 GPa and how
   it drives a tholeiite across the alkalic divide (the Wanless mechanism).

**Data labs** (three)
- **alphaMELTS 2** (github.com/magmasource/alphaMELTS; start with the web
  applet at melts.ofm-research.org): crystallize a Kīlauea parental melt at
  1 atm and at 1 GPa; show the 1 GPa liquid line of descent goes alkalic.
  Reproduce Wanless before believing Wanless.
- **GEOROC 2.0** (via earthchem.org): pull Kīlauea + Mauna Loa historical lava
  chemistry; replot the ²⁰⁶Pb/²⁰⁴Pb–⁸⁷Sr/⁸⁶Sr orthogonal trends and locate the
  "shared component" intersection yourself.
- **Thermobar** (open Python): thermobarometry on published Halemaʻumaʻu glass
  analyses (USGS Dec 2020–Sep 2024 geochem data release); where is the magma
  equilibrating?

**Oral exam scope:** the full chain — plume melting → storage → fractionation →
what a lava analysis can and cannot tell you. Expect the Os-isotope paper to
come up.

---

## M3 · Volcano Geodesy — 3 weeks (~45 h; accelerated, your home turf)

**Job:** volcano-specific source models and the Hawaiian deformation canon; you
supply the inverse-theory maturity, the module supplies the volcanology.

**Texts**
- Segall, *Earthquake and Volcano Deformation* (Princeton, 2010): the
  dislocation/crack foundations, then the magma-chamber and volcano-deformation
  chapters and viscoelastic/poroelastic effects. [$]
- USGS PP 1801 ch. 5, Poland, Miklius & Montgomery-Brown, "Magma Supply,
  Storage, and Transport at Shield-Stage Hawaiian Volcanoes" — free.
- Wang, Shirzaei et al. (2021), *JGR* 126:e2021JB021803 — post-2018 refill
  constrains the HMM vs SC reservoir system.
- Anderson et al. (2019), "Magma reservoir failure and the onset of caldera
  collapse at Kīlauea in 2018," *Science* — the <4% withdrawal result.

**Problem sets**
1. Derive the Mogi solution; tilt Green's functions; predict the sign and
   relative amplitude of UWD tilt for an HMM-centered pressure drop — explain
   the sawtooth you've been watching from first principles.
2. Depth–ΔV trade-off; what single-station tilt can and cannot resolve (the
   one-instrument caveat of this pause, formalized).
3. Sill vs sphere vs dike: discriminating source geometry from the pattern of
   tilt/GPS/InSAR.

**Data labs**
- **Tilt inversion:** public UWD releases (2024 full-year; Jan–Jun 2025, DOI
  10.5066/P1ZGFGBI): extract per-episode deflation amplitudes; invert for
  source depth/ΔV with a hand-rolled MCMC or GBIS
  (comet.nerc.ac.uk/gbis). Compare your ΔV series against erupted volumes —
  first contact with the mass-balance problem (capstone topic 4).
- **InSAR:** ASF Vertex → HyP3 on-demand interferograms (free credits) →
  MintPy time series (OpenSARlab recipe book) over the summit, 2021–2026;
  recover the refill signal and the episode sawtooth if coherence allows.

**Oral exam scope:** source models, resolution limits, the 2018 collapse
mechanics, and a defense of your inversion choices.

---

## M4 · Volcano Seismology — 4 weeks (~60 h)

**Job:** the signal taxonomy you've been using informally all month — VT, LP,
VLP, tremor, gas-piston bursts — with the source physics underneath, and the
processing stack to work with it.

**Texts**
- Chouet & Matoza (2013), "A multi-decadal view of seismic methods for
  detecting precursors of magma movement and eruption," *JVGR* 252:108 — the
  module's spine. [$ paywalled; USGS-authored — obtainable via the USGS
  publications warehouse or interlibrary loan]
- Matoza & Roman (2022), "One hundred years of advances in volcano seismology
  and acoustics," *Bull. Volcanology* 84:86 — open access.
- Thelen et al. (2022), "Trends in volcano seismology 2010–2020" — free PDF
  via IAVCEI.
- Chouet & Dawson (2015), *JGR* — gas-piston VLP source at Halemaʻumaʻu; the
  cigar-shaped bursts you watched on 2026-07-12.
- *Encyclopedia of Volcanoes* 2e, McNutt volcano-seismology chapter, as the
  gentle on-ramp. [$]

**Problem sets**
1. Fluid-filled crack resonance: why LP/VLP frequencies encode geometry and
   fluid properties; crack stiffness scaling.
2. Tremor source models (intermittent flow, eddy shedding, repeating LPs);
   what "tremor amplitude" physically integrates.
3. Design of RSAM/SSAM; detection statistics for burst events (builds directly
   toward the gas-piston catalog, capstone topic 3).

**Data labs** (require an unblocked machine: FDSN hosts are egress-denied in
the authoring container)
- **ObsPy + FDSN (IRIS/EarthScope), network HV:** pull continuous UWE + RIMD
  around the onsets of episodes 49, 50, and 51; compute 1-min RSAM
  (`kilauea/data/fetch/onset_watch.py` is the starting point); identify
  baseline / piston-band / precursory / eruptive regimes and time the coupled
  tilt–tremor–fountain transition.
- **Spectral lab:** spectrograms across one onset; find the frequency band of
  the piston bursts; compare with Chouet & Dawson's 4–5 Hz result.
- **Cadence lab:** automated burst detection on the 2026-07-09→11 piston
  sequence; measure the 5–15 min cadence HVO reported, from raw data.

**Oral exam scope:** signal taxonomy with source physics, what tremor is and
isn't, and a walkthrough of your episode-51 onset data.

---

## Term I synthesis paper (due before Term II)

2,500–3,500 words: **"Anatomy of an episode: the geophysical life cycle of a
2026 Kīlauea fountaining event."** Integrate M1 style physics, M3 deformation
budget, and M4 seismic phenomenology around one episode you observed directly.
M2 shows up as the composition of what erupted. This paper is deliberately the
embryo of capstone topics 2–4.
