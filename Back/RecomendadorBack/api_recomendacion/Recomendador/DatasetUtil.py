import pandas as pd
import os
from recomendacion_videojuegos.settings import MEDIA_ROOT




def getPandasDataFrame():

  df = pd.read_csv("api_recomendacion/Recomendador/pruebaGeneral.csv",delimiter=";")
  print(os.getcwd())
  df = pd.read_csv("https://raw.githubusercontent.com/mcarob/csvPandasVideojuegos/main/pruebaGeneral.csv",delimiter=";")
  df = df.drop('Unnamed: 0', axis=1)
  return df

