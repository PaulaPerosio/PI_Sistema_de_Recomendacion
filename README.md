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
  - **Datetime**: Librería utilizada para la transformación de datos de fechas.
  - **Matplotlib**: Librería utilizada para la visualización de datos y sus relaciones.
  - **FastAPI**: Librería utilizada para crear la API.
  - **Uvicorn**: Servidor para interactuar con la API.
  - **Render**: Plataforma utilizada para el despliegue de la aplicación.
  - **Datos**: Crear una carpeta llamada **Datos** y colocar los archivos del siguiente enlace **([Link](https://drive.google.com/drive/folders/1L1JMFUtNDDaiLh7_IA5JwunKxdey80Q4?usp=sharing))**. Estos son los datos iniciales utilizados en este proyecto, los cuales estan en formato JSON, comprimidos con GZ.
  - **DataSet**: Crear una carpeta llamada **DataSets** donde se guardarán los archivos consumidos por las funciones **([Link](https://github.com/PaulaPerosio/PI_Sistema_de_Recomendacion/tree/main/DataSets))**
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

### 1. Analisis Exploratorio, Extracción, Transformación y Carga de datos ([ETL-EDA](https://github.com/PaulaPerosio/PI_Sistema_de_Recomendacion/blob/main/ETL-EDA.ipynb))

<p align="justify">

  De manera alternada e iterativa, se realizó el análisis exploratorio de datos (EDA) y el proceso de extracción, transformación (ETL).
  
  Como parte del proceso de EDA, se evaluó la presencia de nulos, duplicados, outliers, tipos y cantidad de datos, así como la descripción estadística de los mismos. También se trabajó con la visualización de datos y el análisis de sus relaciones mediante histogramas, gráficos de dispersión, entre otros.

  Como parte del proceso de ETL, se desanidaron datos, se eliminaron registros nulos, duplicados y outliers. Además, se realizaron transformaciones de datos específicas necesarias para el diseño de las funciones.

  El resultado de este proceso de EDA y ETL fue preparar los datos y generar nuevos archivos JSON de menor tamaño que serán consumidos por las funciones de la API **([DataSets](https://github.com/PaulaPerosio/PI_Sistema_de_Recomendacion/tree/main/DataSets))**.

</p>


### 2. Creación de funciones ([Main](https://github.com/PaulaPerosio/PI_Sistema_de_Recomendacion/blob/main/main.py))

<p align="justify">
  Se desarrollaron 6 funciones para diferentes endpoints que se consumirán en la API y brindarán información específica de la base de datos de videojuegos utilizada; dichas funciones utilizan los archivos JSON generados anteriormente. Se trabajó en el manejo de errores dentro de cada función y se considero la posibilidad de datos de entrada erroneos, que no existan en la base de datos o cualquier otro posible error generado durante el uso de la API.

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


### 4. Desarrollo del Modelo de Machine Learning ( [Main](https://github.com/PaulaPerosio/PI_Sistema_de_Recomendacion/blob/main/main.py))

<p align="justify">
  Se desarrolló la función correspondiente al modelo de recomendación por similitud de relación ítem-ítem, es decir, el input es un juego y el output es una lista de juegos recomendados por similitud. Se trabajó utilizando la función de similitud del coseno.

  + def **recomendacion_juego(*`item_id`: int*)** Devuelve una recomendación de 5 juegos similares al juego/item ingresado.

</p>


### 5. Despliegue ( [API](https://sistema-de-recomendacion-458k.onrender.com/docs))

<p align="justify">
  Implementación de la API utilizando la plataforma Render. Esto permite la interacción de los usuarios con la API desarrollada, pudiendo así acceder y realizar consultas o pedidos de recomendación de videojuegos.

</p>


## **Enlaces**
+ Acceso a la API desarrollada [Render](https://sistema-de-recomendacion-458k.onrender.com/docs).

+ Presentación de la API y su funcionamiento [Video](https://drive.google.com/file/d/11ytwIvUTu8rfUJiFiIrOKUZIHZ1-QnxO/view?usp=sharing).


## **Contacto**

+ Paula Perosio [LinkedIn](https://www.linkedin.com/in/paula-perosio/)







