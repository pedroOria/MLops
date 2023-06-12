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
- Para realizar el proyecto se necesito crear un repositorio local para mas adelante enlazarlo a nuestro repositorio de github, luego en la misma carpeta del proyecto levantaremos un entorno virtual asi podremos trabajar en el de forma mas profesional, ademas nos servira para mas adelante hacer el desployment. Muy importante crear tu .gitignore y tu archivo requirements.txt estos seran indispensables para el desployment del proyecto.

### Paso 2:
Realizar el ETL del archivo `movies_dataset.csv` y el archivo `credits.csv`.
- Tienes que desanidar las columnas para acceder al dato que deseas en este caso desanide todas las columnas, pero despues de acabar mi proyecto me doy cuenta que para hacer las consultas y hacer el sistema de recomendaciones, solo bastaba con desanidar, la columna de cast y la de crew. Despues seguiria transformar los datos para trabajar mas adelante con ellos.

### Paso 3:
Realizar las funciones que serian las consultas para la api.
- Para hacer las funciones creamos el archivo `movies_eda.csv` que contiene todas las transformaciones y se usara para extraer los datos deseados, en las primeras 2 consultas tendremos que hacer un mapeo para asi extraer los meses y dias de la columna `release_date`, en la tercera y cuarta consulta es mas accesible, solo tendremos que hacer un filtro de la columna title, para que se refleje en las demas columnas, en las dos ultimas usaremos los archivos `direcotr.csv` y `actores.csv` de igual manera solo hacemos un filtro del name y obtendremos los datos deseados en las demas columnas.

### Paso 4:
Realizar el desployment en Render.
- Para desplegar el proyecto es necesario haber creado tus archivos .gitignore y requirements.txt, ya que con estos archivos render, podra levantar tu proyecto y generarte un link para que lo puedas compartir y mas personas puedan ver tu proyecto ya no de forma local sino desde sus ordenadores. Este procedimiento es muy sencillo creas tu cuenta en "render.com" luego seleccionas la opcion de crear un web service y pegas el link de tu repositorio de github, completas los parametros para desplegar tu proyecto y le das en crear.

## Bibliografía

- https://www.youtube.com/watch?v=GWFC2_9_iVk&t=1460s
- https://nodd3r.com/blog/guia-de-como-hacer-un-proyecto-de-ciencia-de-datos-para-que-destaque-de-forma-eficiente
- https://www.youtube.com/watch?v=J0y2tjBz2Ao&t=10s
- https://www.youtube.com/watch?v=BvvH3ohis6E
- https://platzi.com/clases/4261-python-pip/55131-requirementstxt/ (si tienes platzi me guie de cursos como pip y entornos virtuales)


