# Presentation
A complete description of this project is given in ./documentation.pdf.
To obtain the proposed interactive visualizations, the user should :
* install the package, 
* download the input data,
* run one the scripts with ipython and her own choice of parameters.

All suggestions are welcome at <opensource@cre.fr>.

# 1. Installation
It can be installed with :
```
cd ~/Downloads
git clone https://github.com/cre-os/energy-data-visualization.git
cd energy-data-visualization
conda create --name visu python=3.8 pip
conda activate visu
pip install -e .
```
The installation can then be tested with one of the following :
```
python scripts/weather/main_curve.py
```
or 
```
python scripts/load/main_forecasting_error.py
```
The scripts should terminate without any error.
They will create 3 folders in ~/ : 
- one for the raw data,
- one for the transformed data,
- one for the plots.

However, ipython should then be preferred for interactive plots.

# 2. Download the input data
The data used for the visualizations proposed in this repository come from different public data sources.
only the data from eCO2mix and Météo-France are downloaded automatically.
Data from RTE and ENTSO-E should be downloaded manually.
They have to be stored as described in the documentation.

## eCO2mix
Data about the supply and demand equilibrium and provided by Réseau de Transport d’Electricité through [eCO2mix](https://www.rte-france.com/eco2mix/telecharger-les-indicateurs) allow to illustrate the production and the consumption on the French electricity network.
They **can be downloaded automatically**.
No account is necessary.

## ENTSO-E
The European Network of Transmission System Operators for Electricity publishes fundamental data on its [transparency platform](https://transparency.entso.eu/).
The source files used for the visualizations in this repository currently **have to be downloaded manually** with the [SFTP share](<https://transparency.entsoe.eu/content/static_content/Static content/knowledge base/SFTP-Transparency_Docs.html>).
An account is necessary.

## Météo-France
As the French national meteorological service, Météo-France provides [observation data](https://donneespubliques.meteofrance.fr/?fond=produit&id_produit=90&id_rubrique=32) extracted from the Global Telecommunication System of the World Meteorological Organization.
The data **can be downloaded automatically**.
No account is necessary.

## RTE
RTE publishes fundamental data about the French electricity transmission system.
The files currently **have to be downloaded manually** on the platform [RTE services portal](https://services-rte.com/en/download-data-published-by-rte.html).
An account is necessary.

# 3. How-to : examples
In this repository, we propose a set of modules that read, format, transform and plot the input data from different public sources.
We also provide ready-to-run visualization scripts as illustrated below.
The parameters therein can be modified by the user.
Additionally, other possible visualizations are described in the documentation.

## Distribution of the temperature
![Distribution temperature](examples/distribution_temperature.png)
This figure is obtained by running scripts/weather/main_distribution.py.
The data, coming from Météo-France, are downloaded automatically.

## Availability programs
![Availability programs](examples/incremental_programs.png)
This figure is obtained by running scripts/outages/main_incremental_programs.py.
The data have to be downloaded manually from ENTSO-E or RTE platforms.

## Spot report
![Spot report](examples/spot_report.png)
This figure is obtained by running scripts/multiplots/main_spot_report.py.
As it mixes data from different sources, the data from ENTSO-E and RTE have to be downloaded manually.



