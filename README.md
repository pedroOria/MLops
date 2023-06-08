# PROYECTO INDIVIDUAL DATA SCIENCE 11

En este repositorio encontrarás mi primer proyecto individual de machine learning ops de la carrera Data Science del bootcamp de SoyHenry. ¡Espero sea de tu agrado!

La finalidad de este proyecto es afianzar los conocimientos adquiridos durante el bootcamp, especialmente en la elaboración y ejecución de una API.

Una Application Programming Interface (API) es una interfaz que permite la comunicación entre dos aplicaciones, independientemente de la infraestructura subyacente. Son herramientas muy versátiles y fundamentales para la creación de, por ejemplo, pipelines, ya que permiten mover y brindar acceso simple a los datos que se deseen disponibilizar a través de diferentes endpoints o puntos de salida de la API.

Hoy en día contamos con FastAPI, un web framework moderno y de alto rendimiento para construir APIs con Python.

## Descripción del proyecto

El proyecto consiste en realizar la ingesta de datos desde diversas fuentes, aplicar las transformaciones pertinentes y luego disponibilizar los datos limpios para su consulta a través de una API construida en un entorno virtual.

Los datos fueron proporcionados en los archivos movies_dataset.csv y credits.csv. Se realizó un EDA (Exploratory Data Analysis) para cada dataset y se corrigieron los tipos de datos, valores nulos, valores duplicados, entre otros.

Posteriormente, se relacionaron los datasets que fueron transformados en la primera etapa mediante consultas a la API. Los datasets tratan sobre películas, sus directores, sus actores, recaudación, presupuesto, entre otros, de diferentes plataformas como Netflix, Disney, etc.

## Consultas disponibles

Estas son algunas de las consultas disponibles en la API:

- `cantidad_filmaciones_mes( Mes )`: Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset. Ejemplo de retorno: X cantidad de películas fueron estrenadas en el mes de X.

- `def cantidad_filmaciones_dia( Dia )`: Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset. Ejemplo de retorno: X cantidad de películas fueron estrenadas en los días X

- `def score_titulo( titulo_de_la_filmación )`: Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score. Ejemplo de retorno: La película X fue estrenada en el año X con un score/popularidad de X

## Estructura del proyecto

Para realizar este proyecto, primero se realizaron la ingesta y la normalización de los datos, lo cual se puede ver en el archivo `ETL.ipynb`. Luego, se relacionan en los datasets resultantes (`actores.csv`,`director.csv`,`pelis_mes.csv`,`recomendacion.csv`,`score.csv`,`votos.csv`) con el archivo `main.py` para realizar las consultas con FastAPI y adicionalmente el archivo `requirements.txt` donde guardo todas las librerias necesarias para levantar el proyecto. Por último, se hara el desployment de la API con Render.

## Bibliografía

- https://www.youtube.com/watch?v=GWFC2_9_iVk&t=1460s
- https://nodd3r.com/blog/guia-de-como-hacer-un-proyecto-de-ciencia-de-datos-para-que-destaque-de-forma-eficiente
- https://www.youtube.com/watch?v=J0y2tjBz2Ao&t=10s
- https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/
- https://www.youtube.com/watch?v=BvvH3ohis6E
- https://platzi.com/clases/4261-python-pip/55131-requirementstxt/ (si tienes platzi me guie de cursos como pip y entornos virtuales)


