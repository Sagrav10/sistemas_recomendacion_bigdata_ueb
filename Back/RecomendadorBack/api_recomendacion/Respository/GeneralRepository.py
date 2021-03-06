from  api_recomendacion.models import Calificaciones,UsuariosSr
import   api_recomendacion.Recomendador.calificacionUtilRepo as reco
import api_recomendacion.Recomendador.DatasetUtil as dataSet
import pandas as pd



def listarUsuario():
  usuarios = list(UsuariosSr.objects.values())
  codigo_usuarios=[]
  for i in usuarios:
    codigo_usuarios.append(i.get("cod_usuario"))
  return (codigo_usuarios)

def prueba():
  pass


def devolverJuegosDict(index_games):
  df=dataSet.getPandasDataFrame()
  if(len(index_games)<1):
    return ("Por el momento no te podemos recomendar videojuegos, pronto podras ver recomendaciones")
  df['Num'] = df.index.astype(str)
  devolver=df.iloc[index_games]
  if(len(devolver.index)>16):
    return df.iloc[index_games].sample(16).to_dict('r')
  return df.iloc[index_games].to_dict('r')

def devolverJuegosDictGusto(index_games,gustos):
  df=dataSet.getPandasDataFrame()
  df['puntuacion']=df.index.to_series().map(gustos)
  df['puntuacion'] = df['puntuacion'].fillna(0)
  if(len(index_games)<1):
    return ("Por el momento no te podemos recomendar videojuegos, pronto podras ver recomendaciones")
  df['Num'] = df.index.astype(str)
  devolver=df.iloc[index_games]
  if(len(devolver.index)>16):
    return df.iloc[index_games].sample(16).to_dict('r')
  return df.iloc[index_games].to_dict('r')




#TODO modificar estooooo!!
def devolverJuegosDictGustoNoGusto(index_games,gustos):
  pass

def indexPeliculas():
  id_peliculas = dataSet.getPandasDataFrame().index.values.tolist()
  return (id_peliculas)


def cantidad_usuarios():
  return len(list(UsuariosSr.objects.values()))

def generarMatrizColaborativa():
  usuarios_ids=listarUsuario()
  peliculas_ids=indexPeliculas()
  usuarioNone=["default"]*len(peliculas_ids)
  df=pd.DataFrame({"default":usuarioNone})
  for cod_usuario in usuarios_ids:
    df[cod_usuario] = df.index.to_series().map(reco.dictCalificaciones(cod_usuario))
  df = df.drop('default', axis=1)
  return df


