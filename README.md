# PROYECTO INDIVIDUAL DATA SCIENCE 11

En este repositorio encontrarás mi primer proyecto individual de machine learning ops de la carrera Data Science del bootcamp de SoyHenry. ¡Espero sea de tu agrado!

La finalidad de este proyecto es afianzar los conocimientos adquiridos durante el bootcamp, especialmente en la elaboración y ejecución de una API.

Una Application Programming Interface (API) es una interfaz que permite la comunicación entre dos aplicaciones, independientemente de la infraestructura subyacente. Son herramientas muy versátiles y fundamentales para la creación de, por ejemplo, pipelines, ya que permiten mover y brindar acceso simple a los datos que se deseen disponibilizar a través de diferentes endpoints o puntos de salida de la API.

Hoy en día contamos con FastAPI, un web framework moderno y de alto rendimiento para construir APIs con Python.

## Descripción del proyecto

El proyecto consiste en realizar la ingesta de datos desde diversas fuentes, aplicar las transformaciones pertinentes y luego disponibilizar los datos limpios para su consulta a través de una API construida en un entorno virtual dockerizado.

Los datos fueron proporcionados en archivos de diferentes extensiones, como CSV y JSON. Se realizó un EDA (Exploratory Data Analysis) para cada dataset y se corrigieron los tipos de datos, valores nulos, valores duplicados, entre otros.

Posteriormente, se relacionaron los datasets que fueron transformados en la primera etapa mediante consultas a la API. Los datasets tratan sobre películas, su franquicia, país de producción, recaudación, presupuesto, entre otros, de diferentes plataformas como Netflix, Disney, etc.

## Consultas disponibles

Estas son algunas de las consultas disponibles en la API:

- `franquicia(franquicia)`: Se ingresa el nombre de la franquicia y retorna la cantidad de películas, la ganancia total y el promedio. Ejemplo de respuesta: `{'franquicia': franquicia, 'cantidad': respuesta, 'ganancia_total': respuesta, 'ganancia_promedio': respuesta}`.

- `peliculas_pais(pais)`: Se ingresa el nombre del país y retorna la cantidad de películas producidas en ese país. Ejemplo de respuesta: `{'pais': pais, 'cantidad': respuesta}`.

- `productoras(productora)`: Se ingresa el nombre de la productora y retorna la ganancia total y la cantidad de películas producidas por esa productora. Ejemplo de respuesta: `{'productora': productora, 'ganancia_total': respuesta, 'cantidad': respuesta}`.

## Estructura del proyecto

Para realizar este proyecto, primero se realizaron la ingesta y la normalización de los datos, lo cual se puede ver en el archivo `transformation.ipynb`. Luego, se relaciona el dataset resultante (`df.csv`) con el archivo `main.py` para realizar las consultas con FastAPI. Por último, se hara el desployment de la API con Render.

## Bibliografía

- https://www.youtube.com/watch?v=GWFC2_9_iVk&t=1460s
- https://nodd3r.com/blog/guia-de-como-hacer-un-proyecto-de-ciencia-de-datos-para-que-destaque-de-forma-eficiente
- https://www.youtube.com/watch?v=J0y2tjBz2Ao&t=10s
- https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/
- https://www.youtube.com/watch?v=BvvH3ohis6E
- https://platzi.com/clases/4261-python-pip/55131-requirementstxt/ (si tienes platzi me guie de cursos como pip y entornos virtuales)
