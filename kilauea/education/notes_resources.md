# Agent sweep notes: curriculum resources (verified 2026-07-13)

## Textbooks / canonical reviews

- Parfitt & Wilson, *Fundamentals of Physical Volcanology* (Wiley-Blackwell 2008 —
  only edition).
- Sigurdsson et al. (eds), *The Encyclopedia of Volcanoes*, 2nd ed. 2015 (current;
  no 3rd ed. exists). https://shop.elsevier.com/books/the-encyclopedia-of-volcanoes/sigurdsson/978-0-12-385938-9
- Segall, *Earthquake and Volcano Deformation* (Princeton 2010). https://press.princeton.edu/books/hardcover/9780691133027/earthquake-and-volcano-deformation
- Fagents, Gregg & Lopes (eds), *Modeling Volcanic Processes* (Cambridge 2013) —
  quantitative bridge text for geophysicists.
- Gonnermann & Manga: "The Fluid Mechanics Inside a Volcano" (Annu Rev Fluid Mech
  2007) https://gonnermann.rice.edu/publications/gonnermann-2007-the-fluid.pdf ;
  "Dynamics of magma ascent in the volcanic conduit" (2013)
  https://www.seismo.berkeley.edu/~manga/gonnermannmanga2012.pdf ;
  Gonnermann "Magma Fragmentation" (AREPS 2015).
- Cashman, Sparks & Blundy 2017 Science eaag3055 (open PDF via Bristol:
  https://research-information.bris.ac.uk/ws/files/107826509/Science_Final_complete.pdf);
  Cashman & Sparks 2013 GSA Bull "How volcanoes work: a 25 year perspective";
  Phil Trans R Soc A 377:20180298 (2019) reservoir-architecture review.
- Chouet & Matoza 2013 JVGR 252:108 (volcano-seismology review);
  Matoza & Roman 2022 Bull Volc 84:86 (100 years of volcano seismology);
  Thelen et al. 2022 "Trends in volcano seismology 2010–2020" (open IAVCEI PDF);
  Fee et al. 2022 volcano infrasound review.
- Oppenheimer, *Eruptions that Shook the World* (Cambridge 2011).

## Free USGS canon

- PP 1801 *Characteristics of Hawaiian Volcanoes* (2014) — all chapters free:
  https://pubs.usgs.gov/pp/1801/ (Ch.1 HVO lab; Ch.3 growth/degradation; Ch.5 magma
  supply/storage/transport; Ch.6 petrology; Ch.7 gas).
- PP 1350 *Volcanism in Hawaii* (1987, 62 chapters): https://pubs.usgs.gov/pp/1987/1350/
- PP 1806 Wright & Klein, *Two Hundred Years of Magma Transport and Storage at
  Kīlauea 1790–2008*: https://pubs.usgs.gov/pp/1806/
- PP 1867 series (2018 collapse/LERZ; PP1867A = 2008–2018 summit lava lake):
  https://pubs.usgs.gov/publication/pp1867A
- Neal et al. 2019 Science open PDF:
  https://volcanoes.usgs.gov/vsc/file_mngr/file-204/367.full.pdf
- GM 92 *Mauna Loa Revealed* — paywalled (Wiley/AGU).

## Courses / lectures

- edX (UIcelandX): "Monitoring Volcanoes and Magma Movements" — free to audit:
  https://www.edx.org/course/monitoring-volcanoes-and-magma-movements
- MIT OCW 12.001 volcano lectures (intro-level only).
- USGS Public Lecture Series videos; HVO Volcano Awareness Month (January) talks.
- UH Hilo CSAV International Training Program in Volcano Monitoring — VERIFIED
  running 2026: Jun 6–Aug 1 (8 wks), $9,000 incl. housing, cohort <12, open to
  unaffiliated/international applicants; UH Hilo + Cascades Volcano Observatory/MSH.
  Apply by Dec 1. https://hilo.hawaii.edu/csav/international/
- "MAGMA lecture series": NOT FOUND (likely confusion with Caltech magmasource).

## VICTOR cyberinfrastructure

- victor.ldeo.columbia.edu — JupyterHub cloud hub (NSF #2126268; Volcanica paper
  jvolcanica.org/ojs/index.php/volcanica/article/view/393). Pre-installed Tephra2,
  lava-flow codes, geochem calculators, pyVICTOR, teaching modules. Open-source/
  open-access; self-serve compute for unaffiliated users not explicitly confirmed —
  check portal.

## Open software (all verified real/maintained)

- ObsPy (github.com/obspy/obspy); MSNoise (msnoise.org) + SeisMIC (dv/v);
  covseisnet (github.com/leonard-seydoux/covseisnet); Infrapy
  (github.com/LANL-Seismoacoustics/infrapy).
- GBIS (comet.nerc.ac.uk/geodetic-bayesian-inversion-software-gbis/; Bagnardi &
  Hooper 2018) + VMOD (Python, 2023GC011341); MintPy (github.com/insarlab/MintPy)
  + ASF OpenSARlab MintPy recipe book.
- Thermobar (Volcanica paper 161); alphaMELTS 2 (github.com/magmasource/alphaMELTS;
  melts.ofm-research.org).
- VolcFlow; MOLASSES (gscommunitycodes.usf.edu); Q-LavHA (fard.research.vub.be/q-lavha);
  Tephra2 (github.com/geoscience-community-codes/tephra2); Plumeria (real/open,
  canonical URL via USGS).

## Open data

- FDSN network HV (fdsn.org/networks/detail/HV/) via service.iris.edu →
  service.earthscope.org; ObsPy FDSN client.
- EarthScope/GAGE (ex-UNAVCO) GNSS: unavco.org/data/gps-gnss (gage-data login).
- ASF Vertex/HyP3 Sentinel-1 on-demand InSAR (8,000 free credits/mo):
  hyp3-docs.asf.alaska.edu → MintPy.
- HVO monitoring pages (usgs.gov/volcanoes/kilauea/science/monitoring-data-kilauea);
  quake feeds via ANSS/ComCat; no formal documented HVO REST API.
- EarthChem/GEOROC 2.0 for Hawaiian lava chemistry (earthchem.org).
- USGS 3DEP lidar DEMs incl. 2023 Big Island lidar (apps.nationalmap.gov/3depdem/).
- HVO webcams + timelapse archives (usgs.gov/volcanoes/kilauea/webcams).
