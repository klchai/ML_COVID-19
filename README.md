# ML_COVID-19
Projet Machine Learning sur coronavirus COVID-19

> Author: Kelun CHAI, Djaber SOLIMANI

## COVID_19 en France
Dans le fichier `ML_COVID-19.ipynb`, vous pouvez trouver:
1. L'exploration des données
  - Contenu des données
  - Les variables, la période de mesure
2. Visualisation des données
  - Nombre total de décès causés par COVID-19 en France
  - Répartition des décès par sexe (5 mai 2020)
  - Nombre de décès à Paris
  - Nombre cumulé de services hospitaliers ayant déclaré au moins un cas - sur la carte de France
  - Proportion de tests positifs dans la région parisienne
3. Les modèle SIR, SEIR et SEIRD

## Data
We suggest that using `World_data` for prediction.
### World_data
> Source: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
> File: `time_series_covid19_confirmed_global.csv`,`time_series_covid19_deaths_global.csv`,`time_series_covid19_recovered_global.csv`

World_data provides following functions:
1. clean(): data cleaning for 3 csv files from CSSE Jhons Hopkins and export an new CSV
2. load_france(): return DataFrame of France
3. load_UK(): return DataFrame of United Kingdom
4. load_italy(): return DataFrame of Italy
5. load_china(): return DataFrame of China
6. load_canada(): return DataFrame of Canada

## Models
### SIR Model
Path: `model/sir.ipynb`
1. Un model SIR encapsulé
2. Modèle SIR fitted sur les données réelles

### SEIR Model
Path: `model/seir.ipynb`
1. Un model SEIR encapsulé
2. Modèle SEIR fitted sur les données réelles

### SEIRD Model
Path: `model/seird.ipynb`
1. Un model SEIRD encapsulé
2. Modèle SEIRD fitted sur les données réelles
