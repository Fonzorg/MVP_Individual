<p align="center">
  <img src="https://github.com/Fonzorg/MVP_Individual/assets/108815192/c418e5f8-0524-4e7a-83ea-eebd78bc3de3" />
</p>

# MVP Proyecto Individual
## Machine Learning Operations (MLOps)
### _Alfonzo Rubianes Gravier_

## Objetivo Principal del Proyecto Individual N° 1.

El objetivo principal del presente proyecto es entregar un “Minimum Viable Product” (MVP), que proporcione una recomendacion a los usuarios.
Un MVP es un producto con suficientes características para satisfacer a los clientes iniciales y proporcionar retroalimentación para el desarrollo futuro. 

## Tareas desarrolladas.

Para lograr el objetivo principal, debemos desarrollar procesos de ETL, un Analisas Exploratorio de los Datos y desarrollar un modelo de machine learning.
Este proceso busca desarrollar, entrenar, desplegar y monitorear un modelo que aprende de los datos. En este caso, los pasos seguidos fueron los siguientes:

# Adquisición de datos: 
Consistio en obtener los datos que se usaron en el modelo.
En este caso particular, tales datos fueron extraidos de dos archivow .csv: 'movies' y 'credit' que luego se normalizaron y unieron en un solo dataset usado para el desarrollo de este proyecto: 'dataset_normalizado.csv'.

# Preprocesamiento: 
Incluyo procedimientos de ETL, como normalizar, combinar, eliminar y crear variables, todo ello en busca de mejorar su calidad y adecuarlas al modelo.
Siguiendo las consignas del proyecto, se realizaron las siguientes Transformaciones:
 _Se desanidaron los datos de las columnas 'belongs_to_collection', 'production_companies', 'production_compañies' y 'geners'._
 _Los valores nulos de los campos revenue, budget se rellenados por el número 0._
 _Los valores nulos del campo release date deben eliminarse._
 _Se creo la columna 'año_realizacion' donde extraerán el año de la fecha de estreno, y 'ganancia', con el cociente entre 'recaudacion' y 'presupuesto'. En este ultimo caso, cuando no habian datos, se rellenaba el registro con el valor 0._
 _Se eliminaron varias colimnas que no se utilizaron._
 _Y todo ello derivo en la creacion de un dataset normalizado para las funciones y otro para la recomendacion_
 
_El prosesamiento aludido se puede analisar en el archivo: 'mvp_transformaciones' en este repositorio._

# Análisis exploratorio (EDA): 
Implico visualizar y correlacionar los datos para entenderlos mejor y detectar posibles problemas o patrones. 
Vale decir que este paso suele hacerse tambien antes de preprosesamiento.
_Este analisis se halla en el archivo 'eda_movies' en este repositorio_

# Algoritmo machine learning: 
Se refiere a la elección del método o técnica que se aplicaro al problema. 
En este caso me decidi por similitud de coceno para la recoemndacion solicitada en la consigna. Este recomendara las cinco peliculas mas parecidas al titulo dado.
Luego he entrenado el modelo y validado el mismo logrando optimizarlo.

# Generar una api y desplegar la misma por Rendel: 
Implico poner el proyecto a disposicion para que pueda ser usado por otros. Para este proyecto, y siguiendo las consignas, se disponibilizaron las siguientes funciones:
def peliculas_idioma(idioma)
def peliculas_duracion(pelicula)
def franquicia(franquicia)
def peliculas_pais(pais)
def productoras_exitosas(productora)
def get_director(director)
def recomendaciones(titulo)

_Sus respectivas descripciones y codigos estan en el archivo 'main' en este repositorio_

## Rol a desarrollar
Desempeñando un rol de Data Scientist he seguido un proceso integral desde la obtencion de los datos hasta el despliegue de la api. 
Como comentario personal, hace dos semanas y media no hubiera creido hacer lo que hice. Sin embargo, habiendo descubierto en el proceso fortalezas que desconocia y debilidades sobre las que debo trabajar, veo lo hecho en retrospectiva y encuentro mucho que poder cambiar y mejorar. 
Pero como se dijo, y lo pude constatar, la velocidad es crucial!

_En el siguiente repositorio encontraran los datasets normalizados y archivos .py y ipynb sobre los que se sustenta la presente entrega; como asi tambien los archivos aludidos a lo largo de los puntos anteriores._
