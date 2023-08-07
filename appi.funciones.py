from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df_idioma = pd.read_csv("idioma_original.csv")
df_duracion = pd.read_csv('duracion.csv')
df_franquicia = pd.read_csv('franquicias.csv')
df_paises = pd.read_csv('paises.csv')
df_productoras = pd.read_csv('productoras.csv')
df_diectores = pd.read_csv('dir.csv')



# Entrenamiento del modelo de recomendación
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df_tranform['title'])
matriz_simil = cosine_similarity(tfidf_matrix)

app = FastAPI()

# http://127.0.0.1:8000/docs
 
@app.get("/peliculas_idioma/{Idioma}")
def pelicula_idioma(idioma):
    idioma = idioma
    cantidad = df_idioma['idioma_original'].value_counts()[idioma]
    return print(cantidad, ' peliculas fueron estrenadas en idioma', idioma)




@app.get("/peliculas_duracion/{Pelicula}")
def duracion_pelicula(pelicula):

    duracion = df_duracion.loc[df_duracion['titulo_original'] == pelicula]['duracion'].values[0]
    año = df_duracion.loc[df_duracion['titulo_original'] == pelicula]['año_realizacion'].values[0]
    return print(pelicula, '. Duracion:', duracion, '. Año', año)




@app.get("/franquicia/{Franquicia}")
def franquicia(franquicia):
    cantidad_titulos = df_franquicia.loc[df_franquicia['franquicia'] == franquicia]['titulo_original'].count()
    recaudacion_total = df_franquicia.loc[df_franquicia['franquicia'] == franquicia]['recaudacion'].sum()
    recaudacion = ('US${:,}'.format(round(recaudacion_total)))
    recaudacion_promedio = recaudacion_total / cantidad_titulos
    recaudacion_prom = ('US${:,}'.format(round(recaudacion_promedio)))
    return print('La franquicia', franquicia, 'posee', cantidad_titulos, 'peliculas', 'una ganancia total de', recaudacion, 'y una ganancia promedio de', recaudacion_prom)



@app.get("/peliculas_pais/{Pais}")
def pelicula_pais(pais):
    pais = pais
    cantidad = df_paises['pais'].value_counts()[pais]
    return print('Se producjeron ', cantidad, ' peliculas en', pais)



@app.get("/productoras_exitosas/{Productora}")
def productora_exitosa(compañia):
    funcion_productora = df_productoras.loc[df_productoras['compañia'].isin([compañia])]
    revenue = funcion_productora['recaudacion'].sum()
    revenue_res = ('{:,}'.format(round(revenue)))
    cantidad = funcion_productora['pelicula_id'].nunique()

    return print(
        'La productora',compañia,'ha tenido un revenue total de USD$'+revenue_res+','
        '\ny realizo un total de',cantidad,'peliculas.'
        )



@app.get("/get_director/{nombre_director}")
def get_director(director):
    director = director
    dir_subset = df_diectores.loc[df_diectores['director'].isin([director])]
    retorno = dir_subset['recaudacion'].sum()
    cantidad_peliculas = dir_subset['pelicula_id'].nunique()
    lista = dir_subset[['titulo_original', 'fecha_realizacion', 'recaudacion', 'presupuesto', 'ganancia']].values.tolist()



    return print('El director', director, 'ha generado una retorno total de', retorno, ', y ha dirigido', cantidad_peliculas, 'peliculas, cuyos nombres, fecha de lanzamiento, retorno, costo y ganancia son:' 
    '\n',  lista)


@app.get("/recomendacion/{director}")
def recomendacion_por_director(director):
    dir_subset = mvp_funcion_dir.loc[mvp_funcion_dir['director'].isin([director])]
    recomendacion = dir_subset.loc[dir_subset['director'] == director]['titulo_original'].tolist()
    return print('Director: ', director,
                 '\n', 'Pelis recomendadas:', recomendacion)