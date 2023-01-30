import streamlit as st

st.title("Visualizaciones")
tab1, tab2, tab3 = st.tabs(["Tiempo de Entrega", "Satisfaccion del Cliente", "Ventas por Producto"])

with tab1:
    st.title("Disminuir tiempos de Entrega")
    st.subheader("KPI:")
    #st.markdown("***")
    st.subheader(""" Reducir los tiempos de entrega 5% semestral.""")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/imagen2.png?raw=true")
    st.write("""En el primer grafico de arriba a la izquierda(Velocimetro) podemos observar el promedio nacional
           de demora en todo el proceso, desde que el consumidor compra el producto hasta que es entregado. A su lado se
           encuentra el promedio nacional de tiempos de entrega estimados, ambas medidas estan en dias""")

    st.write("""El grafico titulado 'Diferencia Porcentual' en la parte superior muestra el porcentaje de diferencia
     entre el tiempo estimado y el tiempo real que existe para las entregas.""")
    
    st.write("""En el mapa podemos ver visualmente el promedio de entrega en dias por estado. Entendemos que brasil tiene una geografia 
            particular por lo que creemos necesario hacer esta distincion por zona.""")

    st.write("""Las 3 tarjetas debajo del grafico del 'promedio de tiempo real de entrega'  de la parte superior muestra,
    en orden descendente, muestran las 3 fases en que dividimos el proceso de entrega para su analisis. La primera tarjeta, muestra
    el tiempo promedio en que tarda en aprobarse una orden. La segunda muestra el tiempo que demora el vendedor en despachar el 
    producto, luego de aprobada la compra. Cabe destacar que esta parte del proceso no depende de Olist pero decidimos incluirla porque influye
    de sobremanera en el resultado del proceso final. 
    La tercer tarjeta muestra el tiempo de demora de Olist en entregar el producto, desde que lo recibe hasta entregarlo 
    al consumidor. Es decir, esta parte depende pura y exclusivamente de la empresa""")

    st.write("""El grafico de barras nos indican porcentualmente la cantidad de compras que se realizan por estado, el grafico
    restante muestra el promedio de tiempos de entrega por region.""")
with tab2:
    st.title("Satisfaccion del cliente en relacion a tiempos de entrega")
    st.subheader("KPI:")
    st.subheader("""Aumentar en 2% semestral por 3 años las reviews positivas""")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/imagen1.png?raw=true")
    st.write("""En el mapa ubicado en la parte superior izquierda podemos ver el promedio de scores de reseñas discriminado
        por region""")
    st.write("""En el grafico de velocimetro ubicado a su derecha podemos ver el promedio de score de reseñas nacional.""")
    st.write("""En la tabla que se encuentra en la parte superior derecha , encontramos el porcentaje  y la cantidad
    de reseñas que pertenece a cada score""")
    st.write("""En la parte inferior izquierda podemos encontrar la evolucion de los scores de reseñas a lo largo del tiempo""")
    st.write("""A su derecha podemos ver el total acumulado por cada puntaje del score de reseñas""")

with tab3:
    st.title("Distribucion de Ventas por Categoria de Productos")
    st.subheader("KPI:")
    st.subheader("Aumentar la cantidad de productos vendidos en un 15% anual")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/imagen3.png?raw=true")

    st.write("""En el grafico de la parte superior izquierda tenemos el acumulado de ventas separado por categoria de
    productos""")
    st.write("""En el grafico de barras horizontales observamos la cantidad de ventas totales segmentadas por año""")
    st.write("""En la tajeta tenemos el acumulado total de ventas para el periodo seleccionado""")
    st.write("""Por ultimo en la parte inferior encontramos la evolucion en el tiempo de la cantidad de ventas de la
    plataforma de Olist""")
    