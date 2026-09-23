---
title: 'Forecast User Guide Section 5: Forecast Ensemble (ENS) Rationale and Construction'
authors: ECMWF
year: '2025'
url: https://confluence.ecmwf.int/spaces/FUG/pages/673550730/Section+5+Forecast+Ensemble+ENS+-+Rationale+and+Construction
final_url: https://confluence.ecmwf.int/spaces/FUG/pages/673550730/Section+5+Forecast+Ensemble+ENS+-+Rationale+and+Construction
retrieved: '2026-09-23'
sha256: e226ae8d9f4fc92c49f673c532905bf4306c07d1ba19430c597d2e0bd024979b
kind: html
parser: bc-web-readability
tier: http
engine: curl_cffi
escalated: false
found_by: exa
note: ''
chars: 13130
---

![](https://confluence.ecmwf.int/download/attachments/673550730/ThinkstockPhotos-955736436-new.jpg?version=1&modificationDate=1779559581343&api=v2)
*image © AzriSuratmin/iStock/Thinkstock*

* [Rationale of the Forecast Ensemble - ENS](#Section5ForecastEnsemble\(ENS\)RationaleandConstruction-RationaleoftheForecastEnsemble-ENS)
* [Uncertainties in NWP forecasting](#Section5ForecastEnsemble\(ENS\)RationaleandConstruction-UncertaintiesinNWPforecasting)
* [Structure and operation of the ENS](#Section5ForecastEnsemble\(ENS\)RationaleandConstruction-StructureandoperationoftheENS)
* [Qualitative use of the ENS](#Section5ForecastEnsemble\(ENS\)RationaleandConstruction-QualitativeuseoftheENS)
* [Quantitative use of the ENS ](#Section5ForecastEnsemble\(ENS\)RationaleandConstruction-QuantitativeuseoftheENS)
* [Characteristics of a good ensemble](#Section5ForecastEnsemble\(ENS\)RationaleandConstruction-Characteristicsofagoodensemble)
* [Additional Sources of Information](#Section5ForecastEnsemble\(ENS\)RationaleandConstruction-AdditionalSourcesofInformation)

### Uncertainties in NWP forecasting

No NWP model can produce consistently or precisely correct forecasts and there must be some uncertainty in the results of each forecast. The value of NWP forecasts that are produced would be greatly enhanced if the quality of those forecasts could be assessed beforehand. Consequently methods have been, and continue to be, developed to provide advance knowledge on the certainty (or uncertainty) of a particular forecast, and what possible alternative developments might occur. This is in parallel with improving the observational network, the data assimilation system, and the NWP models themselves.

The ECMWF forecast ensemble is based upon the idea that incorrect forecasts result from a combination of initial analysis errors and model deficiencies, the former dominating during the first five days or so.

Forecast models can produce incorrect results because of:

* initial condition uncertainties (also originating from errors in the first guess forecast):
* Lack of observations.
* Observation error.
* Errors in the data assimilation.
* model uncertainties:
* Limited resolution.
* Weaknesses in parameterisation of physical processes.
* boundary condition uncertainties:
* Insufficient detail of sub-grid scale orography.
* Insufficient knowledge of changing surface characteristics.
* Parameterised derivation of surface fluxes.

* the chaotic nature of the atmosphere:
* Small uncertainties grow to large errors (unstable flow)
* Small-scale errors will affect the large-scale (non-linear dynamics)
* Error-growth is flow dependant.

But even very good analysis systems and forecast models are prone to errors.

Analysis errors amplify most easily where the the atmosphere is most sensitive to small differences, in particular where strong baroclinic systems develop. These errors then move downstream and further amplify or change, and thereby affect the large-scale flow.

### Structure and operation of the ensemble

To estimate the effect of possible initial analysis errors and the consequent uncertainty of the forecasts, an ensemble is formed of many different “perturbed” initial states and one unperturbed analysis (the control member, CTRL).

Currently :

* [Ensemble Control Forecast](https://confluence.ecmwf.int/display/FUG/Section+2A.1.2.1+Medium+Range+Ensemble+forecasts#Section2A.1.2.1MediumRangeEnsembleforecasts-Ensemblecontrolforecast), or equally a forecast from any individual ensemble member, may be considered as a possible detailed solution during the first 15 days.

* [Medium range](https://confluence.ecmwf.int/display/FUG/Section+2A.1.2.2+Sub-seasonal+range+forecasts) ensemble consists of 50 members to investigate uncertainty and variability of detail in the forecast during the first 15 days.
* [Sub-seasonal range](https://confluence.ecmwf.int/display/FUG/Section+2A.1.2.2+Sub-seasonal+range+forecasts) 46 day ensemble consists of 100 members and the unperturbed control member to give probability of general conditions at longer ranges.
* [Seasonal range](https://confluence.ecmwf.int/display/FUG/Section+2A.1.2.3+Seasonal+forecasts) 7 month or 13 month ensemble of 50 members and the unperturbed control member to give probability of general conditions at longer ranges.

The different perturbations are derived at analysis time during the [generation of the ensemble](https://confluence.ecmwf.int/display/FUG/Section+5.1+Generation+of+the+Ensemble).

The ensemble forecast suite is then run using each of the perturbed and the unperturbed analyses as a starting point giving a range of forecast results which may diverge radically or remain broadly similar. To deal with uncertainty in the structure of the parameterisation schemes or with errors due to incomplete IFS modelling of unresolved scales, etc., perturbations are continually inserted into the ensemble members (but not the ensemble control) throughout execution of the forecasts. The perturbations are supplied by the Stochastically Perturbed Parameterisation Scheme (SPP).

[Singular Vectors](https://confluence.ecmwf.int/display/FUG/Section+5.1.2+Singular+Vectors+-+SV) (SVs) pick up localised areas of strong barotropic and baroclinic instability and these are also supplied as perturbations to the ensemble members.

Processing the ensemble of forecasts is computationally expensive. The [medium range](https://confluence.ecmwf.int/display/FUG/Section+2A.1.2.1+Medium+Range+Ensemble+forecasts) ensemble currently has 50 members and 9km resolution. The [sub-seasonal range](https://confluence.ecmwf.int/display/FUG/Section+2A.1.2.2+Sub-seasonal+range+forecasts) ensemble has 100 members so in order to save computation time the ensemble members are run with a lower resolution, currently 36km.

The [SI3](https://gmd.copernicus.org/articles/8/2991/2015/gmd-8-2991-2015.pdf) subprogram (within [NEMO](https://confluence.ecmwf.int/display/FUG/Section+2A.4+Dynamic+Ocean+Model+-+NEMO)) forecasts changes in the sea-surface temperature and sea-ice evolution. Note: In earlier versions of IFS up to and including Cy49r, ECMWF used LIM2 which is an earlier version of the Louvain-la-Neuve sea ice model currently available (Version 3.6).

### **Qualitative use of the ensemble**

If the perturbed forecasts more or less agree with the control member forecast, then the atmosphere can be considered to be in a predictable state. Any of the expected analysis errors appear not have a significant impact. In such cases it might be possible to issue a categorical forecast with reasonable, but not total, certainty.

If the perturbed forecasts deviate significantly from the control member forecast and from each other, then the atmosphere can be considered to be in a rather unpredictable state. In such cases it would not be possible to issue a categorical forecast with any certainty.

The way in which the perturbed forecasts differ from each other provides valuable indications of which weather patterns are likely to develop or, often equally importantly, not develop. Guidance on how to best to [deal with uncertainty](https://confluence.ecmwf.int/display/FUG/Section+7+ENS+Products+-+Dealing+with+Uncertainty) and on aids to [interpretation of various ensemble outputs](https://confluence.ecmwf.int/display/FUG/Section+8+ENS+Products+-+What+they+are+and+how+to+use+them) are given elsewhere within the this User Guide.

![](https://confluence.ecmwf.int/download/attachments/673550730/Fig2.5.X%20ENS%20Pic.png?version=1&modificationDate=1779559581314&api=v2)

**Fig5-1:** *An ensemble of forecasts produces a range of possible scenarios rather than a single predicted value. Addition or subtraction of small perturbations to the initial distribution of a parameter give several equally probable ensemble members each slightly different from the initial unperturbed analysis of the control member. The ensemble members evolve through the forecast period in slightly different ways and the distribution of the ensemble members gives an indication of the likelihood of occurrence of the different scenarios. In the schematic diagram, compared to initial conditions, a few ensemble members (small peak in ENS numbers) are grouped to give a similar forecast that is cooler, two forecasts predict relatively much warmer conditions, but the majority show a modest warming over initial conditions. Each solution is possible; the solution associated with the larger peak (larger number of ENS members) is more probable.*

### **Quantitative use of the ENS**

The ensemble mean (EM) forecast, or if required the ensemble median forecast (not necessarily the same as the EM) can be calculated from the ensemble. This tends to average out the less predictable atmospheric scales. The accuracy of the EM can be estimated theoretically by the spread of the ensemble so that, on average, the expected EM error is proportional to ensemble spread. More importantly, the ensemble provides information from which the probability of alternative developments is calculated, in particular those related to risk of extreme or high-impact weather.

The ensemble spread is a measure of the difference between the members and is represented by the standard deviation (Std) with respect to the EM. On average, small spread indicates high forecast accuracy of the ensemble mean, and indeed of the ensemble members in general; larger spread corresponds to lower forecast accuracy of the ensemble mean, and of most of the ensemble members. The ensemble spread is flow-dependent and in relative terms will vary for different parameters (e.g. in winter anticyclonic conditions over land spread might be relatively high for 2m temperature, but relatively low for mean sea level pressure). Spread usually increases with the forecast range, but there can be cases when the spread is larger at shorter forecast ranges than at longer ranges. This might happen when the first days are characterized by strong synoptic systems with complex structures but are followed by large-scale “fair weather” high pressure systems.

The spread around the ensemble mean as a measure of accuracy applies only to the ensemble mean forecast error. It does not apply to the median, nor control members, even if they happen to lie mid-range within the ensemble. The spread of the ensemble, relative to a particular ensemble member is, for example, about 41% larger than the spread around the ensemble mean. The spread with respect to the control members is initially the same as for the ensemble mean, but gradually increases, ultimately reaching the same 41% excess as any member (see Fig5-2).

![](https://confluence.ecmwf.int/download/attachments/673550730/Screenshot%202024-10-04%20at%2011.34.26.png?version=1&modificationDate=1779559581388&api=v2)

**Fig5-2:** *The plume diagram shows schematically the the spread of the ensemble for the whole forecast range (orange shaded area). The ensemble mean (red line) lies *more or less* in the middle of the ensemble spread. Any individual ensemble member (blue line) can lie anywhere within the spread. The [Ensemble Control Forecast](https://confluence.ecmwf.int/display/FUG/Section+2A.1.2.1+Medium+Range+Ensemble+forecasts#Section2A.1.2.1MediumRangeEnsembleforecasts-Ensemblecontrolforecast) solution (green line) does not constitute a part of the plume and can even on rare occasions be outside the plume (theoretically on average 4% of the time).*

### **Characteristics of a good ensemble**

Forecasts from a good ensemble should:

* display no mean errors (bias); otherwise the probabilities will be biased as well.
* exhibit sharpness (i.e. have relatively small spread where the uncertainty is small).
* have the ability to span the full climatological range; otherwise the probabilities will either over- or under-forecast the risks of anomalous or extreme weather events.

Systematic errors can be detected by [deterministic verification methods](https://confluence.ecmwf.int/display/FUG/Section+12.A+Statistical+Concepts+-+Deterministic+Data) (for mean errors) or through [probabilistic verification methods](https://confluence.ecmwf.int/display/FUG/Section+12.B+Statistical+Concepts+-+Probabilistic+Data) (for errors in the variability).

### Additional Sources of Information

(*Note: In older material there may be references to issues that have subsequently been addressed*)

* Watch a comprehensive lecture on [uncertainty and the use of an ensemble prediction system](https://confluence.ecmwf.int/display/OPTR/Our+training+resources?preview=/19661038/33817190/Sources%20of%20Uncertainty%20%28Dr.%20R.%20Buizza%29-20140507%201044-1.mp4) giving insight to forecast uncertainties, the use of an ensemble prediction system, and the ECMWF ENS system.
* Watch training videos on [sources of uncertainty and quantifying uncertainty](https://confluence.ecmwf.int/pages/viewpage.action?pageId=61127746).
* Read about [EDA and use of EDA and SV based perturbations in the EPS](https://www.ecmwf.int/sites/default/files/elibrary/2010/14602-newsletter-no123-spring-2010.pdf) (pages 17-28).

(FUG associated with Cy50r1)