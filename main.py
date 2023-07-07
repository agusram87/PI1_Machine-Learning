from fastapi import FastAPI
import pandas as pd
import datetime
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import iso639


# Crear una instancia de la aplicación
app = FastAPI()

# Cargamos el dataframe
df = pd.read_csv('proceso_etl_terminado.csv')

@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma:str):
    idioma_nombre = None
    try:
        codigo_iso639 = iso639.to_iso639_1(idioma.lower())
        idioma_nombre = iso639.to_name(codigo_iso639)
    except ValueError:
        return f"No se encontró información para el idioma {idioma}"

    cantidad_peliculas = len(df[df['original_language'] == codigo_iso639])
    return {'idioma':idioma, 'cantidad':cantidad_peliculas}
    
@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula:str):
    # Filtrar el dataframe por el título de la película
    pelicula_filtrada = df[df['title'] == pelicula]
    
    if len(pelicula_filtrada) > 0:
        # Convertir la duración y el año a tipo entero
        duracion = int(pelicula_filtrada['runtime'].values[0])
        anio = int(pelicula_filtrada['release_year'].values[0])
        
        # Devolver el resultado formateado
        return {'Pelicula': pelicula}, {'Duración': duracion}, {'Año': anio}
    else:
        return "No se encontró la película en el dataframe."



@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    # Filtra el DataFrame por la franquicia ingresada
    franquicia_filtrada = df[df['name_to_collection'] == franquicia]
    
    # Verifica si se encontró la franquicia
    if franquicia_filtrada.empty:
        return f"No se encontró información para la franquicia '{franquicia}'."
    
    # Calcula la cantidad de películas de la franquicia
    cantidad_peliculas = len(franquicia_filtrada)
    
    # Calcula la ganancia total y promedio de la franquicia
    ganancia_total = franquicia_filtrada['revenue'].sum()
    ganancia_promedio = franquicia_filtrada['revenue'].mean()    
    # Devuelve la información de la franquicia
    return {'franquicia':franquicia, 'cantidad':cantidad_peliculas, 'ganancia_total':ganancia_total, 'ganancia_promedio':ganancia_promedio}

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    cantidad_peliculas = df[df['pais_produccion'].apply(lambda x: pais in x)].shape[0]
    if cantidad_peliculas == 0:
        return f"No se encontraron películas producidas en el país {pais}."
    else:
        return {'pais':pais, 'cantidad':cantidad_peliculas}

@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora:str):
    productora_films = df[df['nombre_compania'].apply(lambda x: productora in x)]
    if productora_films.empty:
        return f"No se encontraron películas para la productora {productora}."
    else:
        total_revenue = productora_films['revenue'].sum()
        cantidad_peliculas = len(productora_films)
        return {'productora':productora, 'revenue_total': total_revenue,'cantidad':cantidad_peliculas}


@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:str):
    director_films = df[df['name_director'] == nombre_director]
    if director_films.empty:
        return f"No se encontraron películas para el director {nombre_director}."
    else:
        director_success = director_films['return'].mean()
        movie_list = []
        for _, row in director_films.iterrows():
            movie_info = {
                'title': row['title'],
                'release_date': row['release_date'],
                'return': row['return'],
                'budget': row['budget'],
                'revenue': row['revenue']
            }
            movie_list.append(movie_info)
    return {'director_success' : director_success, 'lista_peliculas': movie_list}

# ML
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo: str):
    # Obtener la fila correspondiente al título de la película ingresada
    pelicula = df[df['title'] == titulo]

    # Obtener las características de género de la película de interés
    generos_pelicula = pelicula['name_genres'].iloc[0].split(',')

    # Obtener la matriz de características de género de todas las películas
    generos = df['name_genres'].str.get_dummies(',')

    # Obtener la matriz de puntuaciones de todas las películas
    puntuaciones = df[['vote_average', 'vote_count']].values

    # Combinar las matrices de género y puntuaciones
    caracteristicas = pd.concat([generos, pd.DataFrame(puntuaciones, columns=['vote_average', 'vote_count'])], axis=1)

    # Calcular la similitud de coseno entre la película ingresada y todas las demás películas basada en características
    similitudes = cosine_similarity(caracteristicas.loc[pelicula.index], caracteristicas)

    # Obtener los índices de las películas más similares (excluyendo la película ingresada)
    indices_similares = similitudes.argsort()[0][::-1][1:]

    # Obtener los títulos de las 5 películas más similares
    peliculas_similares = df.iloc[indices_similares][:5]['title'].tolist()

    return {'lista recomendada': peliculas_similares}
