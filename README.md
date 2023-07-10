<p align=center><img src=https://dce0qyjkutl4h.cloudfront.net/wp-content/webp-express/webp-images/uploads/2022/07/Data-Engineering.jpg.webp><p>

:sunglesses:# **Link de la aplicacion de consulta y recomendacion de peliculas:** **[API deploy](https://new1-dep.onrender.com/docs#/)** :sunglasses:

<h1 align=center> Proyecto Individual #1 Data Science - MLOps </h1>

<h2> Etapas del proceso de trabajo:</h2>

El proyecto consiste en ponernos en un roll de un Cientifico de Datos para una empresa que provee servicios de agregacion de plataformas de streaming. Tenemos que crear un modelo de ML que soluciona un problema de negocios: En este caso un sistema de recomendación.


<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

# - **Extracción, transformacion y carga - ETL**
En principio contamos con dos dataset en donde tenemos los datos crudos que tenemos que transformar para poder trabajar con las funciones que le vamos a hacer a nuestra API.
Los dataset tienen muchas columnas con valores anidados.
Nuestro trabajo va a ser desanidarlos con los datos necesarios que vamos a utilizar para trabajar y una vez que los datos esten guardados en forma correcta en sus respectivas columnas, vamos a proceder a concatenar los dos dataset para convertirlo en uno solo para que se nos sea mas cómodo y eficiente a la hora de trabjar.

En este proceso basicamente empezamos a cargar los datos, los transformamos y luego lo cargamos en un nuevo dataset o archivo CSV llamado 'proceso_etl_terminado.csv'.

Con este dataset ya podemos trabajar con las funciones para empezar a realizar consultas que nos piden. 
Son 6 Funciones:
* En la primera nos indican que tenemos que ingresar un idioma y la función debe devolver la cantidad de peliculas en dicho idioma
* En la segunda función nos pinden que ingresemos el nombre de una pelicula y que retornemos su duración en minutos y también que devuelva el año en que se estrenó.
* En la tercera funcion debemos ingresar la franquicia y debemos retornar la cantidad de pelicuas, ganancia total y promedio.
* En la cuarta función debemos ingresar un país y retornar la cantida de pelicuas que hay de ese país.
* En la quinta función, al ingresar el nombre de la productora, nos tiene que retornar el 'revenue' total y la cantidad de peliculas que realizó.
* En la sexta función nos piden que ingresemos el nombre del director y tenemos que devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.

## - **Analisis exploratorio de datos - EDA** 

EDA (Exploratory Data Analysis) o Análisis Exploratorio de Datos es una etapa fundamental en el proceso de análisis de datos en el campo de la ciencia de datos. Consiste en examinar y comprender los datos de manera sistemática y detallada, utilizando técnicas y métodos estadísticos, visuales y computacionales.

El objetivo principal del EDA para nuestro es descubrir patrones, identificar relaciones, detectar valores atípicos y comprender las características de los datos, con el fin de obtener información valiosa y respuestas a preguntas específicas. Durante el EDA en el archivo 'EDA.ipynb', se aplican diversas técnicas, como la visualización de datos, estadísticas descriptivas, análisis de correlación, distribución de datos, entre otros, para explorar, resumir y presentar los datos de manera efectiva.

Este analisis me permitió obtener una comprensión profunda de los datos, identificar posibles problemas o errores en los datos, formular hipótesis y generar ideas para futuros análisis. Me ayudó a tomar decisiones informadas sobre qué técnicas o modelo de Machine Lerning para aplicar al sistema de recomendación de nuestra API.

## **Modelo machine learning**

Machine Learning, o Aprendizaje Automático, es un campo de estudio en el ámbito de la inteligencia artificial que se centra en el desarrollo de algoritmos y modelos que permiten a las computadoras aprender y mejorar automáticamente a partir de datos sin ser programadas explícitamente.

En lugar de seguir instrucciones específicas, los algoritmos de Machine Learning utilizan patrones y estructuras en los datos para identificar relaciones, hacer predicciones y tomar decisiones. El objetivo es permitir que las máquinas aprendan de forma autónoma, a medida que se les proporcionan más datos y experiencia.

## Algoritmo utilizado: Similitud del coseno

La similitud del coseno es una medida utilizada en el procesamiento del lenguaje natural y en la recuperación de información para determinar la similitud entre dos vectores de características. Se calcula utilizando el coseno del ángulo entre los vectores en un espacio vectorial.

El resultado de la similitud del coseno es un valor entre -1 y 1. Un valor de 1 indica una similitud perfecta entre los vectores, mientras que un valor de -1 indica una similitud completamente opuesta. Un valor cercano a 0 indica poca similitud entre los vectores.

En resumen: La similitud del coseno, para este proyecto, nos permite calcular la similitud entre las características de las peliculas y encontrar las peliculas mas similares en términos de género y puntuación.

## Scikit-Learn
Se utilizo el modulo Scikit-learn y la clase TfidfVectorizer de sklearn para calcular la frecuencia de las palabras que aparecen en el campo tags y se ignoraron todas las palabras comunes del ingles(stopwords) ya que no aportar valor a mi modelamiento.

Para este modelo nos volcamos en las columnas 'name_genres', 'vote_average' y 'vote_count'
Basicamente porque estas columnas aportan información relevante y distintiva para el sistema de recomendación. El genero permite ofrecer recomendaciones basada en preferencias similares, mientras que las puntuaciones promedio y la cantidad de votos permiten evaluar la calidad y la popularidad  de las peliculas. Al combinar estas caracaterísticas, el sistema puede proporcionar recomendaciones mas ajustadas a los gustos y preferencias de los usuarios.

## **Desarrollo API**
## API
API es el acrónimo de "Application Programming Interface" (Interfaz de Programación de Aplicaciones). Se trata de un conjunto de reglas y protocolos que permite a diferentes aplicaciones y sistemas comunicarse e interactuar entre sí de manera estandarizada.

Una API define las funciones y métodos que una aplicación proporciona para que otros programas puedan utilizar sus servicios y acceder a sus datos de manera controlada. Funciona como una capa de abstracción que permite a los desarrolladores utilizar ciertas funcionalidades de una aplicación o servicio sin necesidad de conocer todos los detalles internos de su implementación.

<!-- ![API](/src/appmaster.avif) -->
<p align=center><img src=https://appmaster.io/cdn-cgi/image/width=768,quality=83,format=auto/api/_files/PqV7MuNwv89GrZvBd4LNNK/download/><p>


# Fast API
Toda el desarrollo de la API se encuentra en el [Repositorio de la API](https://github.com/agusram87/PI).

## Render
Una vez completada la implementación y las pruebas, la API fue desplegada en la plataforma Render, que ofrece una infraestructura escalable y confiable para alojar aplicaciones web. Esta combinación de tecnologías permitió crear una API robusta y de alto rendimiento, capaz de procesar solicitudes y brindar respuestas eficientes a los usuarios. El despliegue en Render garantizó una disponibilidad constante y una buena experiencia de uso.

 ![Render](/src/RENDER.png)




