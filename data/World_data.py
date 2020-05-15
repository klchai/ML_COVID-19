import os
import sys
import pandas as pd

# DIR_WORLD_DATA = os.path.join('./data',"world")

def load_italy():
    # Détection du répertoire
#     os.makedirs(DIR_WORLD_DATA, exist_ok=True)
#     fil1=os.path.join(DIR_WORLD_DATA,'time_series_covid19_confirmed_global.csv')
#     file2=os.path.join(DIR_WORLD_DATA,'time_series_covid19_deaths_global.csv')
#     file3=os.path.join(DIR_WORLD_DATA,'time_series_covid19_recovered_global.csv')
    # Lire les données
    df1 = pd.read_csv('./data/world/time_series_covid19_confirmed_global.csv',encoding='utf8',sep=',')
    df2 = pd.read_csv('./data/world/time_series_covid19_deaths_global.csv',encoding='utf8',sep=',')
    df3 = pd.read_csv('./data/world/time_series_covid19_recovered_global.csv',encoding='utf8',sep=',')
    
    confirmed = df1.loc[df1['Country/Region']=='Italy']
    death = df2.loc[df2['Country/Region']=='Italy']
    recovered = df3.loc[df3['Country/Region']=='Italy']
    
    for col_to_drop in ['Province/State', 'Country/Region', 'Lat', 'Long']:
        confirmed=confirmed.drop(col_to_drop,1)
        death=death.drop(col_to_drop,1)
        recovered=recovered.drop(col_to_drop,1)
    
    I = []
    R = []
    D = []
    
    for k,v in confirmed.iteritems():
        I.append(confirmed[k].sum())
    
    for k,v in recovered.iteritems():
        R.append(recovered[k].sum())
        
    for k,v in death.iteritems():
        D.append(death[k].sum())
        
    res = pd.DataFrame()
#     days = confirmed[1]
#     print(days)
#     res["time"]=list(range(114))
    res["infected"]=I
    res["recovered"]=R
    res["death"]=D
    
    null_data = [0,1,2,3,4,5,6,7,8]
    res = res.drop(null_data)
    res = res.reset_index(drop=True)
    
    return res
    