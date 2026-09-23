---
title: 'Forecast User Guide Section 8.1.1: Basic ensemble products'
authors: ECMWF
year: '2025'
url: https://confluence.ecmwf.int/spaces/FUG/pages/673551037/Section+8.1.1+Basic+ensemble+products
final_url: https://confluence.ecmwf.int/spaces/FUG/pages/673551037/Section+8.1.1+Basic+ensemble+products
retrieved: '2026-09-23'
sha256: 0f7fcb697de27e06d478764d89a1b8057129358397090b873dffa3c2d54cb17a
kind: html
parser: bc-web-readability
tier: http
engine: curl_cffi
escalated: false
found_by: exa
note: ''
chars: 14648
---

*Note: HRES and [Ensemble Control Forecast](https://confluence.ecmwf.int/display/FUG/Section+2A.1.2.1+Medium+Range+Ensemble+forecasts#Section2A.1.2.1MediumRangeEnsembleforecasts-Ensemblecontrolforecast) are scientifically, structurally and computationally identical. With effect from Cy49r1, Ensemble Control Forecast output is* *equivalent* *to HRES output where shown in the diagrams.*

**Basic ensemble products**

products display only the raw ensemble forecast data, without any particular modification or post-processing.

### Postage stamps

Postage Stamps” (or "Postage Stamps Maps or Charts") show the individual forecast charts of MSLP and 850hPa temperature of all the ensemble members, including the ensemble control. For ease of visual comparison these are shown all together. They cover a limited area of the globe, normally Europe and eastern North Atlantic. The charts are intended to be used for reference (e.g. to explain the spread in terms of the synoptic developments and, in particular, the reasons for extreme weather etc).

It might seem attractive to identify the member which verifies best in the early part of the forecast (say at T+12) and assume this member will continue to provide the best forecast during the rest of the medium range period. But this is not true; the performance of any member during the first 12hrs of the forecast has little relevance to its skill beyond T+48hrs in the same area.

### Clustering

In order to compress the amount of information being produced by the ensemble and highlight the most predictable parts, individual ensemble members that are "similar" according to some measure (or norm) can be grouped together. This process is known as [clustering](https://confluence.ecmwf.int/display/FUG/Section+8.1.3+Clustering).

![](https://confluence.ecmwf.int/download/attachments/673551037/Screenshot%202023-11-18%20at%2010.21.34.png?version=1&modificationDate=1779559613920&api=v2)

**Fig8.1.1-1:** *of postage stamps showing PMSL forecasts from ensemble control, and all 50 ensemble members, DT 12UTC 15 October 2023, VT T+144hr at 12UTC 21* *October 2023.* *Some large differences in the pressure pattern can be seen on individual ensemble members. Each member has been allocated to* [cluster](https://confluence.ecmwf.int/display/FUG/Section+8.1.3+Clustering)*, shown in a different colour heading above each frame for lead-times T+120 and above only. The representative member of each cluster is here shown by arrows. The clusters are shown in Fig8.1.1-2 and Fig8.1.1-3.*

![](https://confluence.ecmwf.int/download/attachments/673551037/Screenshot%202023-11-18%20at%2010.26.38.png?version=1&modificationDate=1779559613693&api=v2)

**Fig8.1.1-2:** [Clustering](https://confluence.ecmwf.int/display/FUG/Section+8.1.3+Clustering)*or the case shown in Fig8.1.1-1. The three clusters for T+144hr are in the left column. Clustering is based on 500hPa geopotential height pattern.*

![](https://confluence.ecmwf.int/download/attachments/673551037/Screenshot%202023-11-18%20at%2010.25.37.png?version=1&modificationDate=1779559613761&api=v2)

**Fig8.1.1-3:** [Clustering](https://confluence.ecmwf.int/display/FUG/Section+8.1.3+Clustering)*or the case shown in Fig8.1.1-1. The three clusters for T+144hr are in the left column. Clustering is based on 500hPa geopotential height pattern.*

### **Spaghetti diagrams**

Spaghetti diagrams are available on ecCharts. The charts display from each ensemble member for MSLP, or 500hPa geopotential height, or 850hPa temperature. The isoline values are selected by the user (e.g. 1015hPa, or 546dam, or 0°C). The isolines are drawn for each member. At short lead times the isolines are very tightly packed for forecasts because the spread of the ensembles is quite limited. As the forecast progress they become increasingly spread showing the flow-dependent increase in forecast uncertainty. Spaghetti diagrams are sensitive to gradients; in areas of weak gradient they can show a large spread of the isolines, even if the situation is highly predictable. Conversely, in areas of strong gradient they can display a small spread of the isolines, even if there are important forecast variations.

![](https://confluence.ecmwf.int/download/attachments/673551037/Fig6.1.3%20SpaghettiPlotT%2B30.png?version=1&modificationDate=1779559614608&api=v2)

**Fig8.1.1-4:** *Spaghetti Plot 500hPa geopotential height plotted at 560dam DT 12UTC 26 May 2017, VT T+30hr at 18UTC 27 May 2017.* *The ensemble members (grey) are quite tightly packed except at about 20°W where gradients are slack and there is some uncertainty in the trough*

![](https://confluence.ecmwf.int/download/attachments/673551037/Fig6.1.4%20SpaghettiPlotT%2B144.png?version=1&modificationDate=1779559614324&api=v2)

**Fig8.1.1-5:** *Spaghetti Plot 500hPa geopotential height plotted at 560dam DT 12Z 26 May 2017, VT T+144hr at 01 June 2017. The ensemble members (grey) have become more spread out, but retain the general pattern of an upper ridge over the northwest Atlantic and another over the North Sea but there are differences in position (or speed of movement eastwards) and amplitude. *The control ensemble member is shown in red.**

### **Ensemble mean**

The ensemble mean (EM) forecast is a simple average of the ensemble results. It is an effective product because averaging reduces or removes atmospheric features that differ amongst the members.

The ensemble mean tends to weaken gradients. It may show only a weak or spread-out feature but this does not imply:

* there is no noteworthy development in any, or all, of the members.
* that the more developmental outcomes are themselves less probable, since all are equally likely.

All ensemble members might forecast an intense low-pressure system with gale force winds, but in different positions. But in this case, the ensemble mean will only show a rather shallow spread out depression giving the impression of weak average winds. High-impact events, which in the ensemble mean appear weak or absent, can be easily overlooked, or at best regarded as less predictable.

It is essential to inspect the postage stamps and/or use probabilities in conjunction with ensemble mean charts and diagrams.

The ensemble mean is most suited to parameters like temperature and pressure, which usually have a rather symmetric . In the short range the ensemble mean is very similar to the ensemble control due to the symmetry (equal positive and negative) of the initial perturbations.

### **Ensemble median**

The ensemble median is defined as the value of the middle ensemble member where the members have been ranked by value.Ensemble median might be more suitable than the ensemble mean for wind speeds and precipitation as these have skewed distributions.

**![](https://confluence.ecmwf.int/download/attachments/673551037/Fig7.1.5%20Mean%26Membs%20Low%20NE%20Atl.png?version=1&modificationDate=1779559614234&api=v2)**

****Fig8.1.1-6:**** *Ensemble mean PMSL (red) and Spaghetti Plot (grey) from ensemble DT 00UTC 10 June 2017 T+120 hr VT 00UTC 15 June 2017. There is amongst ensemble members in the location and shape of the depressions. The ensemble mean depression is smooth by comparison and less deep (the inner isobar has a value of 995hPa). Because of averaging of the members, the pressure gradients and associated winds will generally be less strong in the ensemble mean . C*hart taken from ecCharts.**

****![](https://confluence.ecmwf.int/download/attachments/673551037/Fig7.1.6%20Low%20NE%20Atl%20Spread%2000Z150617.png?version=1&modificationDate=1779559614187&api=v2)****

****Fig8.1.1-7:**** *As Fig8.1.1-5 the spread of mean sea level pressure (PMSL) by ensemble members (coloured - orange: high spread, blue: low spread). Highest spread of PMSL is on the eastern side of the depression indicating greater uncertainty strength of a southerly wind. spread to the west where most members suggest a fairly low pressure and higher probability of a northerly flow. is near the centre of the depression indicated by the ensemble mean but wind direction is very uncertain upon individual ensemble members. *Chart taken from ecCharts*****.*****

### ****Probabilities****

The most consistent way to convey forecast uncertainty information is by the probability of the occurrence of an event. The event can be general or user-specific regarding probability of exceeding an event threshold. The event threshold to the point at which the user has to take some action to mitigate potential damage from a significant weather event. Probabilities can be:

* instantaneous (e.g. probability 10m wind speed exceeds 20m/s as a given time),
* calculated over a time interval (e.g. probability precipitation exceeds 50mm during a defined 12 hour period). This is possible because the values are themselves originally computed as values accumulated over some (shorter) time interval.

#### **Probability of precipitation**

Probability of precipitation (PoP) totals include all precipitation types (rain, snow, etc. but not hail) in mm of rainfall or rainfall equivalent falling in 6 hour or 12 hour periods using colour shading. As a rough guide 1 mm rainfall equivalent approximates to 1 cm of snowfall.

![](https://confluence.ecmwf.int/download/attachments/673551037/Screenshot%202023-11-27%20at%2013.14.03.png?version=1&modificationDate=1779559613642&api=v2)

**Fig8.1.1-8:** *Probability of precipitation chart showing probability of total precipitation (large scale precipitation plus convective precipitation) exceeding 1mm during the 6 hours preceding the validity time.*

#### Probability of extreme gusts

Probabilities for extreme wind gusts are computed as probabilities over 24 hours because it is considered more important to know that an extreme wind gust might occur than to know the precise time.

![](https://confluence.ecmwf.int/download/attachments/673551037/Fig7.1.7%20Low%20NE%20Atl%20WindProb%2000Z150617.png?version=1&modificationDate=1779559614147&api=v2)

********Fig8.1.1-9:******** *As Fig8.1.1-7 with the probability of wind ≥10m/s. There is a higher probability (dark blue) in the area west of Ireland where the pressure gradient is uncertain although the direction is fairly certain. *The ensemble mean (Fig8.1.1-6) would not suggest such strong winds.*There is very low probability (white) south of Greenland where the gradient is generally light but the direction is uncertain.* *Chart taken from ecCharts. Light blue >25%, Blue >50%, Dark blue >75% probability.*

#### **Probability of combined events**

Additionally, ecCharts can display the probability of a combination of events occurring together. For example:

* 2m temperature and total precipitation (to aid rain/snow forecasting).
* strong wind gusts and heavy snowfall (for assessment of drifting snow).
* 10m wind speed and total precipitation.
* 10m wind speed and significant wave height (to help forecast dangerous conditions at sea).

![](https://confluence.ecmwf.int/download/attachments/673551037/Fig7.1.8%20Low%20NE%20Atl%20WaveHt4m%2000Z150617.png?version=1&modificationDate=1779559614102&api=v2)

**Fig8.1.1-10:** *As Fig8.1.1-7 with the probability of significant wave height ≥4m. Chart taken from ecCharts. Yellow >25%, Orange >50% probability.*

![](https://confluence.ecmwf.int/download/attachments/673551037/Fig7.1.9%20Low%20NE%20Atl%20Wind%26WaveHt4m%2000Z150617.png?version=1&modificationDate=1779559614059&api=v2)

**Fig8.1.1-11:** *As Fig8.1.1-7 with the probability of significant wave height ≥4m AND wind ≥10m/s. Chart taken from ecCharts. Light blue >10%, Green >20%, Yellow >30% probability.*

Thresholds are under user control. The probability is computed as the ratio of the number of the ensemble members in which both event conditions are met to the total number of ensemble members. The current available charts are probabilities of:

![](https://confluence.ecmwf.int/download/attachments/673551037/Fig8.1.12%20ProbSnowAndWind.png?version=1&modificationDate=1779559613957&api=v2)

**Fig8.1.1-12:** *Chart taken from ecCharts showing ensemble probability of wind gust ≥10m/s and ≥2mm/12hr *(ecCharts colour bands for this scheme denote Light blue 5-35%, Blue 35-65%, Dark blue 65-95%, Purple >95%)*. There is a 31% probability of exceeding the thresholds at Munich (shown in the box).* *The location of Munich is shown by the pin.*

### **Forecast expressed in terms of intervals**

Forecast intervals (e.g. “temperatures between 2°C and 5°C”, or “precipitation between 5 and 8mm/24hr”) can be used as a hybrid between categorical and probabilistic forecasts. ecCharts provide a simple way of displaying probabilities above or below thresholds and by intercomparison can give a indication of probability of a parameter lying between the thresholds. For example for maximum temperatures at Vilnius, (see Fig8.1.1-13) there is a 20% probability of being ≥20°C, and from Fig8.1.1-14 there is a 25% probability of being ≤15°C. Therefore there is a 55% probability that the maximum temperature will lie between these two values. Combinations of parameters are possible (e.g. the probability of combined events of wind gust and total snowfall is available on ecCharts as an aid to forecasting drifting of snow).

![](https://confluence.ecmwf.int/download/attachments/673551037/Fig6.1.5%20ProbBalticTemp%3E20.png?version=1&modificationDate=1779559614298&api=v2)

**Fig8.1.1-13:** *Chart taken from ecCharts showing ensemble probability of maximum 2m temperature ≥20°C during a 12hr interval (ecCharts colour bands for this scheme denote 5%-20%-40%-60%-80%-95%-100%). There is a 20% probability of maximum temperatures ≥20°C at Vilnius (shown in the box). The location of Vilnius is shown by the pin.*

![](https://confluence.ecmwf.int/download/attachments/673551037/Fig6.1.6%20ProbBalticTemp%3C15.png?version=1&modificationDate=1779559614267&api=v2)

**Fig8.1.1-14:** *Chart taken from ecCharts showing ensemble probability of maximum 2m temperature ≤15°C during a 12hr interval (ecCharts colour bands for this scheme denote 5%-20%-40%-60%-80%-95%-100%). There is a 25% probability of maximum temperatures ≤15°C at Vilnius (shown in the box).* *The location of Vilnius is shown by the pin.*

### Additional Sources of Information

(*Note: In older material there may be references to issues that have subsequently been addressed*)

* Watch a detailed theoretical presentation regarding [Statistical Post-Processing of Ensemble Forecasts](https://confluence.ecmwf.int/display/OPTR/Our+training+resources?preview=/45754015/45942081/TK_StatisticalPostrocessing_2015.mp4) (30sec delay before start).

(FUG associated with Cy50r1)