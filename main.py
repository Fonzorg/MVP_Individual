from fastapi import FastAPI
import pandas as pd


app = FastAPI()

# FUNCIONES:

mvp_funciones_movies = pd.read_csv('dataset_normalizado.csv')
 
 
@app.get("/peliculas_idioma/{Idioma}")
def pelicula_idioma(idioma: str):
    idioma = idioma
    cantidad = mvp_funciones_movies['idioma_original'].value_counts()[idioma]
    
    return f"{cantidad} peliculas fueron estrenadas en idioma {idioma}"



@app.get("/peliculas_duracion/{Pelicula}")
def duracion_pelicula(pelicula: str):

    duracion = mvp_funciones_movies.loc[mvp_funciones_movies['titulo_original'] == pelicula]['duracion'].values[0]
    año = mvp_funciones_movies.loc[mvp_funciones_movies['titulo_original'] == pelicula]['año_realizacion'].values[0]
    
    return f"{pelicula}. Duracion: {duracion}. Año: {año}"


@app.get("/franquicia/{Franquicia}")
def franquicia(franquicia: str):
    cantidad_titulos = mvp_funciones_movies.loc[mvp_funciones_movies['franquicia'] == franquicia]['titulo_original'].count()
    recaudacion_total = mvp_funciones_movies.loc[mvp_funciones_movies['franquicia'] == franquicia]['recaudacion_y'].sum()
    recaudacion = ('US${:,}'.format(round(recaudacion_total)))
    recaudacion_promedio = recaudacion_total / cantidad_titulos
    recaudacion_prom = ('US${:,}'.format(round(recaudacion_promedio)))

    return f"La franquicia {franquicia}, posee {cantidad_titulos}, peliculas, una ganancia total de {recaudacion} y una ganancia promedio de {recaudacion_prom}"

@app.get("/peliculas_pais/{Pais}")
def pelicula_pais(pais: str):
    pais = pais
    cantidad = mvp_funciones_movies['pais'].value_counts()[pais]
    return print('Se producjeron ', cantidad, ' peliculas en', pais)

@app.get("/productoras_exitosas/{Productora}")
def productora_exitosa(compañia: str):
    funcion_productora = mvp_funciones_movies.loc[mvp_funciones_movies['compañia'].isin([compañia])]
    revenue = funcion_productora['recaudacion_y'].sum()
    revenue_res = ('{:,}'.format(round(revenue)))
    cantidad = funcion_productora['pelicula_id'].nunique()

    return f"La productora {compañia} ha tenido un revenue total de USD$ {revenue_res}\n y realizo un total de {cantidad} peliculas"

@app.get("/get_director/{nombre_director}")
def get_director(director: str):
    director = director
    dir_subset = mvp_funciones_movies.loc[mvp_funciones_movies['crew_nombre'] == director]
    retorno = dir_subset['recaudacion_y'].sum()
    cantidad_peliculas = dir_subset['pelicula_id'].nunique()
    lista = dir_subset[['titulo_original', 'fecha_realizacion', 'recaudacion_y', 'presupuesto_y', 'ganancia']].values.tolist()

    return f"El director {director} ha generado un retorno total de {retorno}, y ha dirigido {cantidad_peliculas} peliculas, cuyo nombre, fecha de lanzamiento, retorno, costo y ganancia son: {lista}"

# RECOMENDACIONES:

df_recomendaciones = pd.read_csv('dataset_recomendaciones.csv')

@app.get("/recomendacion/{titulo}")
def recomendaciones(titulo: str):
    recomendaciones = df_recomendaciones[df_recomendaciones['titulo_original'] == titulo]['recomendaciones'].iloc[0]

    return f"Titulo:{titulo} Recomendaciones: {recomendaciones}"

