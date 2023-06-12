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

### Paso 1:
Prepara el entorno de trabajo.
- Crea un repositorio local y enlázalo con tu repositorio de GitHub. Configura un entorno virtual en la carpeta del proyecto para trabajar de manera más profesional y facilitar el despliegue posterior. No olvides crear un archivo `.gitignore` y `requirements.txt`, ya que son indispensables para el despliegue del proyecto.

### Paso 2:
Realizar el ETL del archivo `movies_dataset.csv` y el archivo `credits.csv`.
- Desanida las columnas de los archivos para acceder a los datos deseados. En este caso, se desanidaron todas las columnas, pero al final del proyecto se descubrió que solo era necesario desanidar las columnas cast y crew. Realiza las transformaciones necesarias en los datos para facilitar su manejo posterior.

### Paso 3:
Realizar las funciones que serian las consultas para la api.
- Crea el archivo `movies_eda.csv`, que contiene todas las transformaciones y se utilizará para extraer los datos deseados. En las primeras dos consultas, se realiza un mapeo para extraer los meses y días de la columna release_date. En las consultas siguientes, se realiza un filtro en la columna title para obtener los datos correspondientes en las demás columnas. Para las últimas dos consultas, se utilizan los archivos `directores.csv` y `actores.csv`, donde también se realiza un filtro por nombre para obtener los datos deseados en las demás columnas.

### Paso 4:
Realizar el desployment en Render.
- Para desplegar el proyecto, asegúrate de haber creado los archivos `.gitignore` y `requirements.txt`. Render te permitirá levantar tu proyecto y generar un enlace para compartirlo con otras personas. Regístrate en "render.com", selecciona la opción de crear un servicio web y pega el enlace de tu repositorio de GitHub. Completa los parámetros necesarios y haz clic en crear para desplegar tu proyecto.

## Bibliografía

- https://www.youtube.com/watch?v=GWFC2_9_iVk&t=1460s
- https://nodd3r.com/blog/guia-de-como-hacer-un-proyecto-de-ciencia-de-datos-para-que-destaque-de-forma-eficiente
- https://www.youtube.com/watch?v=J0y2tjBz2Ao&t=10s
- https://www.youtube.com/watch?v=BvvH3ohis6E
- https://platzi.com/clases/4261-python-pip/55131-requirementstxt/ (si tienes platzi me guie de cursos como pip y entornos virtuales)


[<img src="https://avatars.githubusercontent.com/u/117546891?s=400&u=6a6327d1cbf13545fd79dbb73d8193b5b01e5548&v=4" width=115><br><sub>Pedro Oria</sub>](https://github.com/pedroOria)