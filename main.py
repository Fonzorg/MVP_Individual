from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

mvp_funciones_movies = pd.read_csv('movies_ampliada.csv')


app = FastAPI()

# Entrenamiento del modelo de recomendación
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(mvp_funciones_movies['titulo_original'])
matriz_simil = cosine_similarity(tfidf_matrix)

# Funciones: 
 
@app.get("/peliculas_idioma/{Idioma}")
def pelicula_idioma(idioma):
    idioma = idioma
    cantidad = mvp_funciones_movies['idioma_original'].value_counts()[idioma]
    return print(cantidad, ' peliculas fueron estrenadas en idioma', idioma)


@app.get("/peliculas_duracion/{Pelicula}")
def duracion_pelicula(pelicula):

    duracion = mvp_funciones_movies.loc[mvp_funciones_movies['titulo_original'] == pelicula]['duracion'].values[0]
    año = mvp_funciones_movies.loc[mvp_funciones_movies['titulo_original'] == pelicula]['año_realizacion'].values[0]
    return print(pelicula, '. Duracion:', duracion, '. Año', año)


@app.get("/franquicia/{Franquicia}")
def franquicia(franquicia):
    cantidad_titulos = mvp_funciones_movies.loc[mvp_funciones_movies['franquicia'] == franquicia]['titulo_original'].count()
    recaudacion_total = mvp_funciones_movies.loc[mvp_funciones_movies['franquicia'] == franquicia]['recaudacion_y'].sum()
    recaudacion = ('US${:,}'.format(round(recaudacion_total)))
    recaudacion_promedio = recaudacion_total / cantidad_titulos
    recaudacion_prom = ('US${:,}'.format(round(recaudacion_promedio)))
    return print('La franquicia', franquicia, 'posee', cantidad_titulos, 'peliculas', 'una ganancia total de', recaudacion, 'y una ganancia promedio de', recaudacion_prom)

@app.get("/peliculas_pais/{Pais}")
def pelicula_pais(pais):
    pais = pais
    cantidad = mvp_funciones_movies['pais'].value_counts()[pais]
    return print('Se producjeron ', cantidad, ' peliculas en', pais)

@app.get("/productoras_exitosas/{Productora}")
def productora_exitosa(compañia):
    funcion_productora = mvp_funciones_movies.loc[mvp_funciones_movies['compañia'].isin([compañia])]
    revenue = funcion_productora['recaudacion_y'].sum()
    revenue_res = ('{:,}'.format(round(revenue)))
    cantidad = funcion_productora['pelicula_id'].nunique()

    return print(
        'La productora',compañia,'ha tenido un revenue total de USD$'+revenue_res+','
        '\ny realizo un total de',cantidad,'peliculas.')

@app.get("/get_director/{nombre_director}")
def get_director(director):
    director = director
    dir_subset = mvp_funciones_movies.loc[mvp_funciones_movies['crew_nombre'] == director]
    retorno = dir_subset['recaudacion_y'].sum()
    cantidad_peliculas = dir_subset['pelicula_id'].nunique()
    lista = dir_subset[['titulo_original', 'fecha_realizacion', 'recaudacion_y', 'presupuesto_y', 'ganancia']].values.tolist()

# Recomendacion:

@app.get("/recomendacion/{titulo}")
def recomendacion(titulo: str):
    indice_peli = mvp_funciones_movies[mvp_funciones_movies['titulo_original'] == titulo].index[0]
    sim_scores = list(enumerate(matriz_simil[indice_peli]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_pelis_simil = [mvp_funciones_movies.iloc[sim_score[0]]['titulo_original'] for sim_score in sim_scores[1:6]]
    return {
        'titulo': titulo,
        'recomendaciones': top_pelis_simil
    }