---
title: "Research"
permalink: /research/
layout: single
author_profile: true
toc: true
toc_label: "Contents"
toc_icon: "book"
toc_sticky: true
---

## Exoplanets 🪐

Exoplanets are planets that orbit stars beyond our Solar System. When an exoplanet crosses in front of its host star, some starlight filters through its atmosphere, interacting with gas molecules and atoms before it reaches us on Earth. This light contains fingerprints of the gases in that atmosphere if we split it into its constituent colours (a spectrum). This is known as transmission spectroscopy. We can then deduce the composition of these atmospheres using computational models to compare the spectral features of known gases with the observed spectrum. This process is called an atmospheric retrieval.

### Hints of H₂S and SO₂ in the atmosphere of L 98-59 d

I was a part of an international team of scientists who used JWST to observe one transit of [L 98-59 d](https://exoplanetarchive.ipac.caltech.edu/overview/L98-59), a planet slightly larger and heavier than Earth, across the disc of its host star. We then obtained the transmission spectrum of the atmosphere of the exoplanet from these observations. This spectrum hinted at the possible presence of an atmosphere filled with sulphur dioxide and hydrogen sulphide.

<figure>
  <img src="/assets/images/research/L98-59_banner.jpg" alt="Illustration L 98-59 d">
  <figcaption>An illustration of what the planet L 98-59 d could look like</figcaption>
</figure>

This discovery was surprising, as it stands out in stark contrast to the atmospheres of rocky planets in our own solar system, where water vapour and carbon dioxide are much more prevalent. Earth's atmosphere, for example, is rich in nitrogen and oxygen, with trace amounts of water vapour. Meanwhile, Venus has a thick atmosphere dominated by carbon dioxide. Even Mars has a thin atmosphere dominated by carbon dioxide. Additional observations will be necessary to confirm the presence of these gases. 

<figure>
  <img src="/assets/images/research/money_plot.pdf" alt="Transmission spectrum of L 98-59 d">
  <figcaption>Transmission spectrum of L 98-59 d obtained using NIRSpec G395H on JWST, showing absorption features consistent with sulphur compounds.</figcaption>
</figure>

The potential presence of SO₂ and H₂S raises questions about their origin. One explosive possibility is volcanism driven by gravitational interactions similar to those that drive volcanic activity on Jupiter's moon Io. To find out more about this, read my article in [The Conversation](https://theconversation.com/a-distant-planet-seems-to-have-a-sulphur-rich-atmosphere-hinting-at-alien-volcanoes-243200).

### JWST ERS Transit: WASP-39 b

I was a member of the [JWST ERS Transit](https://ers-transit.github.io) collaboration. A part of the research conducted by this collaboration led to the first [confirmation of atmospheric CO₂ in the atmosphere of WASP-39 b using JWST](https://webbtelescope.org/contents/news-releases/2022/news-2022-042).

<figure>
  <img src="/assets/images/research/webb_w39_co2.jpg" alt="WASP-39 b CO2 detection">
  <figcaption>JWST spectrum of WASP-39 b showing spectral features of carbon dioxide in an exoplanet atmosphere. Image from <a href="https://webbtelescope.org/contents/media/images/2022/060/01GJ3Q66DTT4HPMDCVNC9GXH5Y?news=true">NASA, ESA, CSA, Joseph Olmsted (STScI)</a></figcaption>
</figure>

### Hot Spinning Planets

I have explored the effect of centrifugal forces on the transmission spectra of an exoplanet atmosphere. The centrifugal acceleration due to a planet's rotation opposes the gravitational pull on a planet's atmosphere and increases its scale height. Conventional forward models used for low resolution space-based retrievals generally do not include this effect. When this assumption is removed, I found that atmospheric retrievals produce significantly different results for close-in gas giant planets with low gravity, which are ideal targets for transmission spectroscopy.

<figure>
  <img src="/assets/images/research/puffy_planet.png" alt="Effect of centrifugal force on transmission spectroscopy">
  <figcaption>Centrifugal forces affect the shape of an exoplanet's atmosphere, impacting transmission spectroscopy measurements.</figcaption>
</figure>

### Exo-Venuses and Atmospheric Retrievals

I am interested in understanding the atmospheres of potential Venus-like exoplanets, otherwise known as Exo-Venuses. I mostly work with [NEMESISPY](https://jingxuan97.github.io/nemesispy/), a Python adaptation of the [NEMESIS](https://nemesiscode.github.io/) code for atmospheric retrieval of exoplanets.


## Research Tools

I use a variety of computational and statistical tools in my research:
- **Data Analysis & Modeling**: Python (NumPy, SciPy, Pandas) for exoplanet spectral analysis; Bayesian frameworks for parameter estimation
  
- **Scientific Programming**: Data pipelines for astronomical observations; spectral extraction algorithms; Git/GitHub for collaborative development

- **Statistical Methods**: Bayesian inference, nested sampling, for quantifying uncertainties in atmospheric parameters

- **Data Visualization**: Publication-quality plots with matplotlib/seaborn; representations of multi-dimensional parameter spaces


## Publications

### First-Author Papers

- [Atmospheric Retrievals Suggest the Presence of a Secondary Atmosphere and Possible Sulfur Species on L98-59 d from JWST NIRSpec G395H Transmission Spectroscopy](https://iopscience.iop.org/article/10.3847/2041-8213/ad73d0), Banerjee, A.; Barstow, J.K.; Gressier, A.; Espinoza, N.; Sing, D.K. et al. *ApJL*, 975, L11, 2024

- [Effect of centrifugal force on transmission spectroscopy of exoplanet atmospheres](https://doi.org/10.1093/mnrasl/slad058), Banerjee, A.; Barstow, J.K.; Haswell, C.A.; Lewis, S.R., *Monthly Notices of the Royal Astronomical Society: Letters*, 523, L64, 2023

### Co-Author Papers

- [Hints of a Sulfur-rich Atmosphere around the 1.6 R⊕ Super-Earth L98-59 d from JWST NIRSpec G395H Transmission Spectroscopy](https://iopscience.iop.org/article/10.3847/2041-8213/ad73d1), Gressier, A.; Espinoza, N.; Allen, N.H.; Sing, D.K.; Banerjee, A. et al. *ApJL*, 975, L10, 2024

- [Early Release Science of the exoplanet WASP-39b with JWST NIRSpec PRISM](https://doi.org/10.1038/s41586-022-05677-y), Rustamkulov, Z., et al., *Nature* 614, 659–663, 2023

- [Identification of carbon dioxide in an exoplanet atmosphere](https://doi.org/10.1038/s41586-022-05269-w), JWST Transiting Exoplanet Community Early Release Science Team, *Nature* 614, 649–652, 2023

- [Modelling the atmosphere of lava planet K2-141b: implications for low and high resolution spectroscopy](https://academic.oup.com/mnras/article/499/4/4605/5948140), Nguyen, T.G.; Cowan, N.B.; Banerjee, A.; Moores, J.E., *Monthly Notices of the Royal Astronomical Society*, 499, 4605, 2020

## Talks & Presentations

### 2025
- Talk at UK Exoplanet Meeting, Leeds
- **Invited Seminar at Exoclimatology Group, University of Exeter**

### 2024
- **Invited Talk at Max Planck Institute for Astronomy, Heidelberg**
- Talk at National Astronomy Meeting, Hull
- **Invited Talk at Oxoplanet Journal Club, Oxford**
- Talk at Nemesis Symposium 4, Oxford
- Poster at Exoplanets 5, Leiden
- Unconference Session lead at dot Astronomy 13, Madrid
- Poster at UK Exoplanet Meeting, Birmingham

### 2023
- Talk at OU Physics Research Day, Milton Keynes
- Talk at UK Exoplanet Meeting, London
- Talk at Open Dialogues across Physics and Astronomy, Milton Keynes

### 2022
- Poster at UK Exoplanet Meeting, Edinburgh

### 2019
- Exoplanets Very Close to Their Host Star, McGill Space Institute, Montreal