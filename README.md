<h1 align="center">Sistema de Consulta y Recomendación de Videojuegos</h1>
<hr>

<h2 align="center">Machine Learning Operations (MLOps)</h2>
<hr>
<h3 align="center">Proyecto Individual N°1 - Data Science Fulltime - Henry</h3>

## Descripción
<p align="justify">
  Este proyecto está enfocado en el desarrollo de una API desplegada en Render para la consulta y recomendación de videojuegos de la plataforma STEAM.

  La API permite la interacción con el usuario con el objetivo de obtener información específica de videojuegos y una recomendación de los mismos basada en similitudes con otros juegos. Todo esto en función de los inputs ingresados por el usuario.
</p>

## Rol a Desarrollar
<p align="justify"> 
  MLOps Engineer para el diseño e implementación de una API de consulta y recomendación de videojuegos desplegada a través de una plataforma.
  
  Data Scientist para la exploración y preparación de los datos, así como también para el desarrollo de los inputs que consume la API y un modelo de recomendación.
</p>

## Librerías y Requerimientos
<p align="justify">

  - **Python**: Utilizado en todo el proyecto.
  - **json/Gzip/ast**: Librerías de Python utilizadas para la ingesta de los datos.
  - **Numpy/Pandas**: Librerías de Python utilizadas para el desarrollo del proyecto en general.
  - **TextBlob**: Librería utilizada para el análisis de sentimientos.
  - **datetime**: Librería utilizada para la transformación de datos de fechas.
  - **Matplotlib**: Librería utilizada para la visualización de datos y sus relaciones.
  - **FastAPI**: Librería utilizada para crear la API.
  - **uvicorn**: Servidor para interactuar con la API.
  - **Render**: Plataforma utilizada para el despliegue de la aplicación.
  - **Base de datos inicial**: los datos utilizados en este proyecto se encuentran en el siguiente **([Link](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj))**. Son tres archivos en formato JSON, comprimidos con GZ los cuales se colocaron dentro de una carpeta llamada **Datos** 
  - **DataSet**: Carpeta llamada DataSets donde se guardarán los archivos consumidos por las funciones **([Link](https://github.com/PaulaPerosio/PI_Sistema_de_Recomendacion/tree/main/DataSets))**
  - **Requirements**: requerimientos para el funcionamiento de la API **([Link](https://github.com/PaulaPerosio/PI_Sistema_de_Recomendacion/tree/main/requirements.txt))**

</p>


## Organización Repositorio
<p align="justify">

  - **DataSets**: Aquí están los archivos generados en el proceso de ETL/EDA que sera consumidos por las funciones.
  - **main.py**: archivo principal de la API, donde se encuentran las funciones
  - **ETL-EDA.py**: Análisis exploratorio, transformación de datos, imputaciones y generación de archivos reducidos.
  - **requirements.txt**: requerimientos para el funcionamiento de la API

</p>


## Etapas del proyecto

### 1. Extracción, Transformación y Carga de datos ([ETL](https://github.com/PaulaPerosio/PI_Sistema_de_Recomendacion/blob/main/ETL.ipynb))

<p align="justify">
  
  Se realizó el proceso de extracción, transformación y carga de nuevos archivos dentro de la carpeta **([DataSets](https://github.com/PaulaPerosio/PI_Sistema_de_Recomendacion/tree/main/DataSets))**.
  Se trabajó cada uno de los archivos iniciales por separado. Los mismos estaban en formato JSON comprimidos y tenían columnas con datos anidados. Algunos de los pasos realizados fueron:
  - Abrir y leer los archivos
  - Desanidar los campos
  - Evaluar de manera exploratoria inicial el contenido de los archivos
  - Seleccionar las columnas según los requerimientos de las funciones a desarrollar posteriormente
  - Eliminar registros completamente nulos o duplicados
  - Analizar sentimientos con NLP utilizando la librería TextBlob a partir de las reseñas generadas por usuarios respecto a los juegos. '0' si es malo, '1' si es neutral y '2' si es positivo
  - Transformar y unificar los formatos en las columnas con fechas
  - Trabajar en cada columna de manera específica según lo necesario y convertirlas a un solo tipo de dato con previas transformaciones o eliminaciones de registros puntuales
  - Eliminar registros donde varios datos son nulos, generando que la información requerida para las funciones o el modelo sea insuficiente
  - Evaluar los requerimientos de cada función de manera independiente y realizar un ETL puntual para generar nuevos archivos JSON de mejor tamaño que serán consumidos por las funciones de la API
</p>


### 2. Creación de funciones ([Main](https://github.com/PaulaPerosio/PI_Sistema_de_Recomendacion/blob/main/main.py))

<p align="justify">
  Se desarrollaron 6 funciones para diferentes endpoints que se consumirán en la API y brindarán información específica de la base de datos de videojuegos utilizada; dichas funciones utilizan los archivos JSON generados anteriormente.

  También se trabajó en el manejo de errores dentro de cada función. Para ello, se tuvieron en cuenta las posibilidades donde los inputs sean ingresados en formatos no adecuados o los inputs ingresados no existan dentro de la base de datos. También se capturará cualquier otro posible error generado durante el uso de la API.

  Funciones desarrolladas:

  + def **userdata(*`user_id`: str*)**: Devuelve la cantidad de dinero gastado, el porcentaje de recomendación y la cantidad de juegos consumidos por el usuario ingresado.

  + def **countReviews(*`fecha_inicio_str`: str*, *`fecha_fin_str`: str*)**: Devuelve la cantidad de usuarios que realizaron reseñas y su porcentaje de recomendación entre las fechas ingresadas.

  + def **genre(*`genero`: str*)**: Devuelve el puesto en el que se encuentra el género ingresado en comparación con los demás géneros en función a la cantidad de horas que han sido jugadas.

  + def **userforgenre(*`genero`: str*)**: Devuelve un top 5 de usuarios y su URL en función a la cantidad de horas de juego en el género dado.

  + def **developer(*`desarrollador`: str*)**: Devuelve la cantidad de juegos y el porcentaje de contenido Free por año de la empresa desarrolladora ingresada.

  + def **sentiment_analysis(*`año_str`: int*)**: Devuelve la cantidad de reseñas de usuarios positivas, negativas y neutras según el año de lanzamiento.
</p>


### 3. Implementación de la API

<p align="justify">
  Creación de una API utilizando FastAPI y Uvicorn. La API brinda diferentes endpoints desarrollados que ofrecen información y recomendaciones a usuarios.

</p>


### 4. Análisis Exploratorio de Datos ( [EDA](https://github.com/PaulaPerosio/PI_Sistema_de_Recomendacion/blob/main/EDA.ipynb))

<p align="justify">
  Antes de abordar el entrenamiento de modelos de Machine Learning, se realizó un análisis exploratorio de datos (EDA). Este proceso involucró la investigación de relaciones entre variables, la identificación de outliers y patrones en los datos. Se ajustaron los datos para que nuestro modelo de Machine Learning pueda funcionar correctamente.
  
  Desarrollo de un análisis exploratorio de datos y visualización de los mismos. Algunas de las técnicas utilizadas incluyen:

- Tipo de dato de cada columna.
- Cantidad de filas y columnas en el conjunto de datos.
- Identificación de valores nulos en cada columna.
- Descripción estadística de los datos numéricos.
- Descripción estadística de los datos de texto.
- Matriz de correlación para identificar relaciones entre variables.
- Detección de outliers.
- Visualización de datos mediante histogramas, gráficos de dispersión y nube de palabras.

</p>


### 5. Desarrollo del Modelo de Machine Learning ( [Main](https://github.com/PaulaPerosio/PI_Sistema_de_Recomendacion/blob/main/main.py))

<p align="justify">
  Se desarrolló la función correspondiente al modelo de recomendación por similitud de relación ítem-ítem, es decir, el input es un juego y el output es una lista de juegos recomendados por similitud.

  + def **recomendacion_juego(*`item_id`: int*)** Devuelve una recomendación de 5 juegos similares al juego/item ingresado.

  Pasos dentro de la función:
  - Ingestar los datos.json cargados previamente; con géneros y años de lanzamiento en las columnas, e item/juego en las filas.
  - Determinar las características relevantes de cada juego del DataFrame y del juego ingresado (input).
  - Calcular el valor de similitud entre las características del input con las características de los demás juegos, utilizando el modelo de similitud del coseno.
  - Incorporar una nueva columna con los valores de similitud entre el input y cada juego del DataFrame.
  - Reordenar descendentemente el DataFrame respecto al valor de similitud.
  - Retornar una lista con los 5 juegos con mayor valor de similitud al juego ingresado.
  - Implementar código necesario para el manejo de errores dentro de la función.
  - Deploy del modelo de recomendación utilizando Render.
</p>


### 6. Despliegue ( [API](https://sistema-de-recomendacion-458k.onrender.com))

<p align="justify">
  Implementación de la API utilizando la plataforma Render. Esto permite la interacción de los usuarios con la API desarrollada, pudiendo así acceder y realizar consultas o pedidos de recomendación de videojuegos.

</p>


## **Enlaces**
+ Acceso a la API desarrollada [API](https://sistema-de-recomendacion-458k.onrender.com).

+ Presentación de la API y su funcionamiento [Video](......).


## **Contacto**

+ Paula Perosio [LinkedIn](https://www.linkedin.com/in/paula-perosio/)







