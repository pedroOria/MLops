from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = FastAPI()

@app.get('/')
async def read_root():
    return {'Bienvenidos a mi API'}

# funcion que retorna la cantidad de peliculas por mes
@app.get('/cantidad_filmaciones_mes/{mes}')
async def cantidad_filmaciones_mes(mes:str):
    a = pd.read_csv('pelis_mes.csv') 
    # Convertir el nombre del mes a minúsculas
    mes = mes.lower()
    
    # Crear un diccionario de mapeo para los nombres de los meses
    meses_dict = {
        'enero': 1,
        'febrero': 2,
        'marzo': 3,
        'abril': 4,
        'mayo': 5,
        'junio': 6,
        'julio': 7,
        'agosto': 8,
        'septiembre': 9,
        'octubre': 10,
        'noviembre': 11,
        'diciembre': 12
    }
    
    # Convertir la columna "release_date" a objetos de fecha y hora
    a['release_date'] = pd.to_datetime(a['release_date'], errors='coerce')
    
    # Obtener el número de mes correspondiente al nombre proporcionado
    mes_numero = meses_dict.get(mes)
    
    if mes_numero is None:
        raise ValueError('Nombre de mes inválido')
    
    # Filtrar las películas por mes
    peliculas_filtradas = a[a['release_date'].dt.month == mes_numero]
    
    # Obtener la cantidad de películas filtradas
    respuesta = len(peliculas_filtradas)
    
    return {'mes':mes, 'cantidad':respuesta}

# Funcion que retorna la cantidad de peliculas por dia
@app.get('/cantidad_filmaciones_dia/{dia}')
async def cantidad_filmaciones_dia(dia:str):
    df = pd.read_csv('pelis_mes.csv')  
    # Convertir el día a minúsculas
    dia = dia.lower()
    
    # Diccionario de mapeo de días de la semana a números de día
    dias_dict = {
        'lunes': 0,
        'martes': 1,
        'miércoles': 2,
        'jueves': 3,
        'viernes': 4,
        'sábado': 5,
        'domingo': 6
    }
    
    # Convertir la columna "release_date" a objetos de fecha y hora
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    
    # Obtener el número de día correspondiente al nombre proporcionado
    dia_numero = dias_dict.get(dia)
    
    if dia_numero is None:
        raise ValueError('Nombre de día inválido')
    
    # Filtrar las películas por día de la semana
    peliculas_filtradas = df[df['release_date'].dt.dayofweek == dia_numero]
    
    # Obtener la cantidad de películas filtradas
    respuesta = len(peliculas_filtradas)
    
    return {'dia':dia, 'cantidad':respuesta}

# Funcion que retorna el año de estreno y el score
@app.get('/score_titulo/{titulo}')
async def score_titulo(titulo:str):
    df = pd.read_csv('score.csv')
    titulo =titulo.lower()
    df_title = df[df['title'].str.lower()== titulo]
    
    # obtener el año de estreno
    anio = df_title['release_year'].values[0]

    # obtener la valoracion de la pelicula
    score = df_title['popularity'].values[0]
    
    return {'titulo':titulo, 'anio':anio,'popularidad':score}

# funcion que retorna el año los votos y el promedio de votos
@app.get('/votos_titulo/{titulo}')
async def votos_titulo(titulo:str):
    df = pd.read_csv('votos.csv')
    titulo =titulo.lower()
    df_title = df[df['title'].str.lower()== titulo]
    
    # obtener el año de estreno
    anio = df_title['release_year'].values[0]

    # obtener la cantidad de votos
    num_votos = df_title['vote_count'].values[0]

    # obtener el promedio de votos
    mean_votos = df_title['vote_average'].values[0]

    return {'titulo':titulo,'anio':anio,'voto_total':num_votos,'voto_promedio':mean_votos}

# funcion que retorna informacion del actor
@app.get('/get_actor/{nombre_actor}')
async def get_actor(nombre_actor:str):
    df = pd.read_csv('actores.csv')
    nombre_actor = nombre_actor.lower()
    actor_df = df[df['cast'].str.lower()==nombre_actor]

    # obtener la cantidad de peliculas
    cantidad_peliculas = len(actor_df)

    # obtener la recaudacion total
    retorno = actor_df['return'].sum()

    # obtener el promedio de la recaudacion

    promedio = actor_df['return'].mean()

    return {'actor':nombre_actor,'cantidad_filmaciones':cantidad_peliculas,'retorno_total':retorno,'retorno_promedio':promedio}

# funcion que retorna la informacion del director
@app.get('/get_director/{nombre_director}')
async def get_director(nombre_director:str):
    df = pd.read_csv('director.csv')
    nombre_director = nombre_director.lower()
    director_df = df[df['crew'].str.lower()==nombre_director]

    # obtener el retorno del mismo
    retorno = director_df['return'].sum()

    # obtener el nombre de cada pelicula, con su fecha de lanzamiento y su retorno individual, costo y ganancia de la misma. 
    peliculas = []
    for _, row in director_df.iterrows():
        pelicula = {
            'titulo': row['title'],
            'anio': row['release_date'],
            'retorno_pelicula': row['return'],
            'budget_pelicula': row['budget'],
            'revenue_pelicula': row['revenue']
        }
        peliculas.append(pelicula)

    return {
        'director': nombre_director,
        'retorno_total_director': retorno,      
        'peliculas': peliculas
    }

# funcion de Machine Learnig para recomendarte peliculas
#@app.get('/recomendacion/{titulo}')
#async def get_recomendations(title:str):
    #i = pd.read_csv('recomendacion.csv')
    #tfidf = TfidfVectorizer(stop_words='english')
    #i['overview'] = i["overview"].fillna("")
    #tfidf_matrix = tfidf.fit_transform(i['overview'])
    #coseno_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    #indices = pd.Series(i.index, index=i['title']).drop_duplicates()
    #idx = indices[title]
    #simil = list(enumerate(coseno_sim[idx]))
    #simil = sorted(simil, key=lambda x:x[1], reverse=True)
    #simil = simil[1:11]
    #movie_indices = [i[0] for i in simil]
    #lista = i['title'].iloc[movie_indices].to_list()[:5]
    #return {'lista recomendada': lista}