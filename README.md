# Presentation
The objective of this repository is to share with an [MIT license](https://spdx.org/licenses/MIT.html) the visualization tools used with public data and developed by the Wholesale Markets Surveillance Directorate ([DSMG](https://www.cre.fr/en/CRE/organization)) of the Regulatory Commission of Energy ([CRE](https://www.cre.fr/en)). It can be used by final users such as developers and energy analysts.

To obtain the proposed interactive visualizations, the user should :
* install the package, 
* download the input data,
* run one of the scripts with ipython and her own choice of parameters.

All suggestions are welcome at [opensource\[at\]cre.fr](mailto:opensource@cre.fr).

# Installation
It can be installed with :
```
cd ~/Downloads
git clone https://github.com/cre-dev/pub-data-visualization.git
cd pub-data-visualization
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -e .
```
The installation can then be tested with one of the following :
```
python3 scripts/weather/main_curve.py
```
or 
```
python3 scripts/load/main_forecasting_error.py
```
The scripts should terminate without any error.
They will create 3 folders in the home directory :
```
~/
├── _energy_plots/       # for the plots
├── _energy_public_data/ # for the raw data
├── _energy_tmp_data/    # for the transformed data
```

However, ipython should then be preferred for interactive plots.

# Download the input data
The data used for the visualizations proposed in this repository come from different public data sources.
only the data from eCO2mix and Météo-France are downloaded automatically.
Data from RTE and ENTSO-E should be downloaded manually.

## eCO2mix
Data about the supply and demand equilibrium and provided by Réseau de Transport d’Electricité ([RTE](https://www.rte-france.com/eco2mix/telecharger-les-indicateurs)) through [eCO2mix](https://www.rte-france.com/eco2mix/telecharger-les-indicateurs) allow to illustrate the production and the consumption on the French electricity network.
They **can be downloaded automatically**.
No account is necessary.

## ENTSO-E
The European Network of Transmission System Operators for Electricity ([ENTSO-E](https://www.entsoe.eu/)) publishes fundamental data on its [transparency platform](https://transparency.entsoe.eu/).
The source files used for the visualizations in this repository currently **have to be downloaded manually** with the [SFTP share](<https://transparency.entsoe.eu/content/static_content/Static content/knowledge base/SFTP-Transparency_Docs.html>).
An account is necessary.

## Météo-France
As the French national meteorological service, [Météo-France](http://meteofrance.com/) provides [observation data](https://donneespubliques.meteofrance.fr/?fond=produit&id_produit=90&id_rubrique=32) extracted from the Global Telecommunication System ([GTS](https://public.wmo.int/en/programmes/global-telecommunication-system)) of the World Meteorological Organization ([WMO](https://public.wmo.int/en)).
The data **can be downloaded automatically**.
No account is necessary.

## RTE
RTE publishes fundamental data about the French electricity transmission system.
The files currently **have to be downloaded manually** on the platform [RTE services portal](https://services-rte.com/en/download-data-published-by-rte.html).
An account is necessary.

## Local organization of the data
The data have to be stored as follows :

```
~/_energy_public_data/
├── 11_ENTSOE/
│  ├── ActualGenerationOutputPerGenerationUnit_16.1.A/
│  │  ├── 2021_01_ActualGenerationOutputPerGenerationUnit_16.1.A.csv
│  │  ├── …	 
│  ├── ActualTotalLoad_6.1.A/
│  │  ├── 2021_01_ActualTotalLoad_6.1.A.csv
│  │  ├── …	 
│  ├── DayAheadPrices_12.1.D/	 
│  │  ├── 2021_01_DayAheadPrices_12.1.D.csv
│  │  ├── …	 
│  ├── Outages/	 	 
│  │  ├── UnavailabilityOfGenerationUnits_15.1.A_B/	 
│  │  │  ├── 2021_01_UnavailabilityOfGenerationUnits_15.1.A_B.csv
│  │  │  ├── …	 
│  │  ├── UnavailabilityOfProductionUnits_15.1.C_D/	 
│  │  │  ├── 2021_01_UnavailabilityOfProductionUnits_15.1.C_D.csv
│  │  │  ├── …	 
├──20_MeteoFrance/	 	 
│  ├── synop/	 	 
│  │  ├── postesSynop.csv
│  │  ├── synop.201001.csv
│  │  ├── …	 
├──24_RTE/	 	 	 
│  ├── Centrales_production_reference/
│  │  ├── Centrales_production_reference.xls
│  ├── DonneesIndisponibilitesProduction/
│  │  ├── DonneesIndisponibilitesProduction_2010.xls
│  │  ├── …	 
│  ├── eCO2mix_RTE/	 
│  │  ├── eCO2mix_RTE_Annuel-Definitif_2012.xls
│  │  ├── …	 
│  ├── ProductionGroupe/	 
│  │  ├── ProductionGroupe_2012/
│  │  │  ├── ProductionGroupe_2012-semestre1.xls
│  │  │  ├── …
│  │  ├── …
```


# How-to : ready-to-run examples
In this repository, we propose a set of modules that read, format, transform and plot the input data from different public sources.
We also provide ready-to-run visualization scripts as illustrated below.
The parameters therein can be modified by the user.

## Indices

### Day-ahead fixing prices
![Auction prices](examples/indices/prices.png)
This figure, that represents the fixing prices of the day-ahead auctions, is obtained by running `scripts/indices/main_price.py`.
The data, provided by ENTSO-E, currently have to be downloaded manually.

## Load

### Load curve
![Load curve](examples/load/power.png)
This figure, obtained by running `scripts/load/main_power.py`, is a mere representation of the load curve.
Data from eCO2mix and ENTSO-E can serve as inputs.

### Day-ahead forecasting error
![Day-ahead forecasting error](examples/load/forecasting_error.png)
This figure represents the national load forecasting error and is obtained by running `scripts/load/main_forecasting_error.py`.
The data are provided by eCO2mix.


## Outages

### Animated view of the unavailability
![Animated view of the unavailability](examples/outages/animated_availability.png)
This figure is obtained by running `scripts/outages/main_animated_availability.py`.
The data have to be downloaded manually from ENTSO-E or RTE platforms.

### Evolution of the mean unavailability
![Evolution of the mean unavailability](examples/outages/evolution_mean_availability.png)
This figure is obtained by running `scripts/outages/main_evolution_mean_availability.py`.
The data have to be downloaded manually from ENTSO-E or RTE platforms.

### Expected availability program of a given unit
![Expected availability program of a given unit](examples/outages/expected_program.png)
This figure is obtained by running `scripts/outages/main_expected_program.py`.
The data have to be downloaded manually from ENTSO-E or RTE platforms.

### Availability programs
![Availability programs](examples/outages/incremental_programs.png)
This figure is obtained by running `scripts/outages/main_incremental_programs.py`.
The data have to be downloaded manually from ENTSO-E or RTE platforms.

### Regression delays
![Regression delays](examples/outages/regression_delays.png)
This figure is obtained by running `scripts/outages/main_regression_delays.py`.
The data have to be downloaded manually from ENTSO-E or RTE platforms.
It displays a linear fit between the initially announced and the finally observed length of the outages.
The coefficient being obtained with the minimization of a squared error, outliers have a significant effect.


## Production data

### Unit production
![Unit production](examples/production/power.png)
This figure is obtained by running `scripts/production/main_power.py`.
It can be used with data provided by eCO2mix, ENTSO-E or RTE.


## Weather data

### National mean weather
![Weather curve](examples/weather/curve.png)
This figure is obtained by running `scripts/weather/main_curve.py`.
The data, provided by Météo-France, are downloaded automatically.

### Distribution of the temperature
![Distribution temperature](examples/weather/distribution_temperature.png)
This figure is obtained by running `scripts/weather/main_distribution.py`.
The data, provided by Météo-France, are downloaded automatically.


## Multiplots

### Spot report
![Spot report](examples/multiplots/spot_report.png)
This figure is obtained by running `scripts/multiplots/main_spot_report.py`.
As it mixes data from different sources, the data from ENTSO-E and RTE have to be downloaded manually.

### Announced availability and observed production of a given unit
![Transparent production](examples/multiplots/transparent_production.png)
This figure is obtained by running `scripts/multiplots/main_transparent_production.py`.
The data from RTE have to be downloaded manually.

### 2D-distribution of price and load
![Price and Load](examples/multiplots/scatter_price_load.png)
This figure is obtained by running `scripts/multiplots/main_scatter_price_load.py`.
The data from ENTSO-E and RTE have to be downloaded manually.

### 2D-distribution of price and production
![Price and Production](examples/multiplots/scatter_price_production.png)
This figure is obtained by running `scripts/multiplots/main_scatter_price_production.py`.
The data from ENTSO-E and RTE have to be downloaded manually.

### 2D-distribution of price and weather
![Price and weather](examples/multiplots/scatter_price_weather.png)
This figure is obtained by running `scripts/multiplots/main_scatter_price_weather.py`.
The data from ENTSO-E have to be downloaded manually.




# Description of the code

## Documentation
An html documentation generated with Sphinx can be found in ./doc/pub_data_visualization.html.

## Parameters of the scripts

| Variable name                  | Type                            | Possible values                                                 | Purpose                                       |
| ---                            | ---                             | ---                                                             | ---                                           |
| close                          | bool                            | True; False	                                             | Close the figure after saving                 |
| contract_delivery_begin_year   | int                             | 2018; …                                                         | -                                             |
| contract_delivery_period_index | int	                           | depends on the selected contract_product                        | -                                             |
| contract_frequency             | string	                   | "M"; "Q"; …	                                             | -                                             |
| contract_profile               | string	                   | "BASE"; "PEAK" …                                                | -                                             |
| data_source_auctions           | string	                   | "ENTSOE"                                                        | -                                             |
| data_source_load               | string	                   | "eCO2mix"; "ENTSOE"                                             | -                                             |
| data_source_outages            | string                          | "ENTSOE"; "RTE"                                                 | -                                             |
| data_source_production         | string                          | "eCO2mix"; "ENTSOE"; "RTE"                                      | -                                             |
| data_source_weather            | string                          | "MétéoFrance"                                                   | -                                             |
| delivery_begin_dt_max          | None or localized pd.Timestamp  | -                                                               | -                                             |
| delivery_end_dt_min            | None or localized pd.Timestamp  | -                                                               | -                                             |
| diff_init                      | bool                            | True; False                                                     | Plot the differences between pairs of dates   |
| figsize                        | (int,int)                       | (8,6)                                                           | Figure size                                   |
| folder_out                     | path                            | global_var.path_plots                                           | Plots output                                  |
| load_nature                    | string                          | "load forecast D-1 (GW)";"load forecast D-0 (GW)"; "load (GW)"  | -                                             |
| map_code                       | string or list of strings       | "FR"; … or ["FR", "GB", "BE"…]                                  | -                                             |
| map_code_auctions              | string or list of strings       | "FR"; … or ["FR", "GB", "BE"…]                                  | -                                             |
| producer_outages               | None or string                  | any producer that publishes                                     | -                                             |
| production_dt_max              | None or localized pd.Timestamp  | -                                                               | -                                             |
| production_dt_min              | None or localized pd.Timestamp  | -                                                               | -                                             |
| production_nature              | string                          | "production (GW)"                                               | -                                             |
| production_source              | None or string                  | "biomass"; "solar"; …                                           | -                                             |
| publication_dt_max             | None or localized pd.Timestamp  | -                                                               | -                                             |
| publication_dt_min             | None or localized pd.Timestamp  | -                                                               | -                                             |
| smoother                       | string or pd.Timedelta          | "basic";                                                        | For aesthetic purposes                        |
| unit_name                      | None or string                  | any production unit                                             | -                                             |
| viewpoint_dt_extrapolate       | list of localized pd.Timestamp  | -                                                               | Position plotted as seen from these dates     |
| weather_nature                 | string                          | "observation"                                                   | -                                             |
| weather_quantity               | string                          | "nebulosity (%)"; '"temperature (°C)"; "wind_speed (m/s)"       | -                                             |



