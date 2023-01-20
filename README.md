<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png>

# <h1 align=center> **PROYECTO FINAL GRUPAL** </h1>

# <h2 align=center>***Karen Uzcategui Briceño - Joaquin Dos Santos - Hector Herrera Espinola -</p> Armando Madrigal Lucatero - Lucas Wayar*** </h2>

# <h2 align=center>**Data Engineering - Machine Learning - Data Analyst**</h2>

<p align="center">
   
<img src="https://www.palermo.edu/Archivos_content/2021/negocios/julio/data/datascience-640.jpg"  height=300>

</p>

<hr>  

## **Introduccion.**

***Contexto.***

En 2021, la venta minorista de productos a través de e-commerce significó un saldo aproximado de 5.2 trillones de dólares en
todo el mundo y se infiere que dicha cifra aumentará un 56% en los próximos años, llegando a los 8.1 trillones en 2026.
Olist es una compañía brasileña prestadora de servicio e-commerce para PYMES que funciona como un marketplace, es decir,
funciona como “tienda de tiendas” donde diferentes vendedores pueden ofrecer sus productos a consumidores finales.

***¿Qué es E-commerce Olist?***

Olist es un acelerador de ventas y la herramienta esencial para aquellos que buscan vender más en internet. Cada comerciante,
en línea o físico encuentra en el ecosistema Olist, soluciones que cumplen con todos los pasos presentes en una operación de
venta en línea. Para aquellos que compran, Olist es una garantía adicional de calidad de operación, seguridad y seriedad, ya
que cuenta con miles de inquilinos rigurosamente seleccionados y que operan dentro de altos estándares de requisitos operativos.


## **Problemática.**

El equipo de Marketing y Ventas de Olist busca nuevas maneras de lograr un crecimiento y expansión en el uso de su plataforma.
En base a su análisis preliminar, han detectado que el tiempo de entrega de los productos tiene un gran impacto en todo el ciclo
compra-entrega, desde la utilización de la plataforma por parte de los vendedores hasta la recepción de la mercadería  parte de
los clientes. 
Es por este motivo que Olist nos han contratado  como un grupo de consultores con el fin de evaluar el  impacto del delivery time
real en todo el proceso.


## **Objetivos**

Para este trabajo, se determinarán los siguientes objet  ivos con el fin de evaluar puntos de mejora de cara a la problemática planteada.
Estos objetivos son:
 + Relación entre tiempo de entrega estimada versus tiempo de entrega real:
      Se realizará una evaluación sobre cuáles son los motivos fundamentales sobre la diferencia entre ambos con el fin de
      identificar potenciales puntos de mejora. Esto nos permitirá determinar qué porcentaje de variación existe entre ambos y se
      analizará la opción de abrir (o no) nuevos centros de distribución.
 + Determinación de costos logísticos:
    Se espera determinar cuales son los costos que están relacionados a la entrega de producto  entendiendo el impacto que los mismos
    tienen a nivel nacional.
 + Evaluar la satisfacción del cliente en referencia a tiempos de entrega:
    Se espera determinar el porcentaje de clientes actuales que están desconformes con el servicio prestado.
 + Pronóstico de evolución/crecimiento de Olist para Brasil:
    Se espera determinar la evolución a lo largo del tiempo con el fin de estimar una proyección en base a situación actual en contraste
    con las ideas de mejora que se plantearán (resultado del análisis).
 

## **Objetivos y KPI's asociados.**

La definición de KPIs está basada en los objetivos propuestos anteriormente. Con esto evaluaremos cuál es la situación de
Olist en el mercado para que, con nuestro conocimientos del sector detectar oportunidades de mejora que sirvan principalmente,
para mejorar las prestaciones de la empresa



 + Obj: Disminuir los tiempos de entrega.
   Reducir los tiempos de entrega 5% semestral.
   Tiempo entrega = (Demora real - Demora estimado) / Cantidad de envíos


 + Obj: Disminuir las valoraciones negativas de 1 y 2 estrellas
   Aumentar en una 2% semestral las reviews positivas
   Reviews positivas 1-2 estrellas = Total de reviews negativas (1 y 2) / Total de usuarios

 + Obj: Aumentar la cantidad de ventas por cliente.
   Aumentar la cantidad de productos vendidos en un 15% por año
   Ventas = Cantidad de productos / 365 días (Un año)

   Variaciones anuales (2017, 2018) y periodo total (2017 y 2018)


## **Alcance.**

El alcance del proyecto está en la obtención de conclusiones para compartirlas con los Stakeholders que permitan la toma de decisiones.
Este trabajo será de alcance Nacional, es decir solo a Brasil abarcando todo el proceso de publicación de productos hasta la recepción de los mismos.
Para lograr esto, se planificarán las  tareas por semana de trabajo y cada una de ellas corresponderá a una fase a la cual se le asignarán
objetivos “locales” para cumplirlos en tiempo y forma.
Esta planificación se divisieron en etapas las cuales detallamos a continuación:

***ETAPA 1: Data Engineering.***</p>En esta etapa como primer paso se procederá a realizar una Proceso ETL, donde extraeremos los datos necesarios, los transformaremos
y cargaremos en una base de datos conservando las relaciones entre las tablas. En un segundo momento procederemos a realizar un análisis
EDA, en el que nos enfocaremos en la normalización de los mismos, la limpieza de los datos, detectar posibles outliers, valores faltantes
y demás errores a modificar.
De esta manera buscaremos que los datos queden disponibles para los próximos pasos del proyecto, en formatos manipulables fácilmente y
que permitan un mejor análisis.


***ETAPA 2: Machine Learning.***</p>En esta etapa se desarrollará un sistema de análisis de sentimientos para analizar las reviews con el fin de identificar el grado
de satisfacción del cliente final. En segunda instancia se realizará un análisis predictivo de series de tiempo con el fin de
analizar y proyectar las ventas de la empresa. La implementación de estos sistemas estará basada en diferentes modelos, tanto de Machine Learning
clásico, así como de Deep Learning.
Los pasos a seguir en este proceso son los siguientes:
 + Feature Engineering.
 + Implementación de modelos y pipelines.
 + Evaluación de modelos.
 + Selección de modelos.
 + Despliegue de modelos a producción.



***ETAPA 3: Data Analyst.***</p>En esta etapa se desarrollara el análisis de los datos. Esto implica entender la situación, medir los KPI's establecidos y armar las
conclusiones preliminares resultado del análisis.
Se utilizarán herramientas de visualización con el fin de provocar un impacto visual con la información obtenida que permita comunicar
de una manera simple los resultados.
Para esta etapa se realizarán (no limitado a) las siguientes tareas:
  + Creación de las métricas.
  + Armado de visualizaciones y dashboards interactivos.
  + Medición de los KPIs establecidos.
  + Armado de storytelling.


***Etapa 4: Conclusiones.***</p>Se procederá a la presentación de conclusiones y sugerencias por parte del equipo externo.


## **Metodología de trabajo.**

La metodología de gestión de proyecto utilizada se cree muy importante para llegar a los objetivos propuestos. Se utilizará metodología
considerada ágil al ser colaborativa, rápida y efectiva, iterativa, respaldada por datos y fundamentalmente que se valore a las personas
por encima de los procesos ya que se deduce que es la mejor y más eficiente manera de trabajo.
En particular se realizará la metodología Scrum, que se basa en “Sprints” para crear un ciclo de proyecto, en este caso, sprints de una
semana. Cada sprint culminará con la demostración del progreso del trabajo realizado hasta el momento, frente al Product Owner. La duración
total del proyecto será de 4 semanas. Siendo la última exclusivamente para presentación final y demostrar puesta en producción.
Se realizan reuniones diarias (guiadas por un Scrum Master) con el objetivo de conocer a todos los participantes del proyecto, dividiendo,
organizando trabajo y tiempos por cada integrante y así garantizar que las tareas se finalicen a tiempo y de manera correcta.

***El cronograma tentativo previsto es:***

El siguiente diagrama de Gantt describe el ciclo completo del proyecto. Se espera que todos los miembros del equipo realicen un
seguimiento de ese progreso utilizando el diagrama. El proyecto esta sujeto a un ciclo de 19 días.

<p align=center><img src="https://raw.githubusercontent.com/lulo76/Proyecto-Final-DTS--05/main/Assets/Gantt.jpeg"  height=300>

## **Stack tecnológico.**

 + Python.
 + Machine Learning.
 + MySQL.
 + Power BI.
 + AirFlow.
 + Streamlit.
 + AWS.
 + Github.
 + Trello.

## **Entregables**

***Diseño detallado***

 + Tablero online en streamlit para disponibilizar la información y realización de consultas 
   API para detectar la satisfacción del cliente por medio de las reseñas.

***Desarrollo a futuro  del proyecto.***

 + Disponibilizar los datos  para consulta en un tablero en tiempo real que consuma los datos a través de una api de forma automatizada.
   Con esto buscamos que se brinde la información que el cliente necesite consultar en el momento

## **Equipo de trabajo.**

***Roles y responsabilidades.***

 + Lucas Doyel Morales Wayar - Data Scientist
 + Joaquin Dos Santos Rodriguez - Data Engineer
 + Armando Madrigal Lucatero - Machine Learning Engineer
 + Karen Francelia Uzcategui Briceño -Data Analyst
 + Hector Javier Herrera Espínola - Data Analyst

***+ Cabe destacar que el cumplimiento de los roles no está sujeta únicamente al tipo de perfil establecido, sino que cada integrante
podrá brindar soporte en diversas áreas y/o tareas durante todo el proceso.***
   
   
   
***Análisis preliminar de calidad de datos***


Para análisis preliminar de los datos en relación a la problemática decidimos utilizar como fuente principal los datasets provistos. Para un análisis más detallado en el anexo “Análisis preliminar” encontrarán información más precisa de los tipos de datos que utilizaremos como insumo principal, el estado en el que nos llegan y posibles modificaciones rápidas. Sin embargo no descartamos ampliar a futuro con información complementaria para enriquecer el análisis posterior y cubrir demandas del cliente. 

El Diagrama Entidad-Relación está disponible en este  [Diagrama Entidad-Relación](https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/Diagrama%20ER.jpg)
