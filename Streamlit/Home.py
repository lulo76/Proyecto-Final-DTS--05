import streamlit as st

st.title("Proyecto Olist")
st.markdown("***")

tab1, tab2, tab3 = st.tabs(["¿Que es Olist?", "Modelo de negocio", "Informacion"])

with tab1:
   st.header("¿Que es Olist?")
   st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/Olist-800x400.jpg?raw=true")
   st.write("""Olist es un acelerador de ventas y la herramienta esencial para a
        quellos que buscan vender más en internet. Cada comerciante, 
        en línea o físico encuentra en el ecosistema Olist, soluciones que 
        cumplen con todos los pasos presentes en una operación de venta en línea. 
        Para aquellos que compran, Olist es una garantía adicional de calidad de operación,
         seguridad y seriedad, ya que cuenta con miles de inquilinos rigurosamente seleccionados 
         y que operan dentro de altos estándares de requisitos operativos.""")
    


with tab2:
    st.header("Modelo de Negocio")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/olist.png?raw=true")
    st.write("""En este diagrama podemos ver el proceso interno del flujo de compra hasta la entrega del producto
                 al cliente""")
    st.markdown("***")
    st.subheader("Diagrama Entidad-Relacion")
    st.write("""Aqui podemos ver la representacion del Modelo de Negocios en la Base de Datos""")
    if st.checkbox("mostrar diagrama"): 
        st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/der_actual.png?raw=true")

with tab3:
   st.header("Informacion")
   st.write("""Con el correr del tiempo, es cada vez es más frecuente que una persona genere una compra de
    cualquier producto a través de internet. Esta decisión puede verse afectada por diferentes factores,
    pero uno de ellos, que puede ser determinante es la opción de entrega puerta a puerta, donde el comprador
    desde la comodidad de su casa o trabajo puede esperar y recibir su compra. Precisamente, este es uno de
    los servicios principales que desarrolla Olist. Es por esto, que se encuentra en constante evaluación de
    su propio servicio.     
    Por este motivo, para poder mantenerse a la vanguardia, Olist se asesora con nuestra empresa de consultoría
    para realizar un análisis exhaustivo de  sus servicios, con la intención de mejorar las prestaciones a sus 
    cliente.""")
   st.markdown("***")
   st.write("""En este proyecto Olist nos solicito que encontraramos soluciones innovadoras que permitan a sus usuarios vender 
   sus productos a un mayor número de clientes, haciendo foco en los grandes mercados de brasil, donde pudieran instalar
   nuevos hubs, para lograr mejoras en los tiempos de entregas. Sumado a esto nos informo que necesitaban
    saber cuales eran las categorias de productos mas vendidas y evaluar la satisfaccion de los clientes.""")
   st.markdown("***")
   st.write("""Por otro lado se nos ha brindado información, con el fin de detectar cuales son los puntos flacos en el 
     proceso de logística, para disminuir los tiempos de entrega, desde que el consumidor realiza una compra hasta que
     recibe el producto. Además de ello analizar posibles mejoras relacionadas y presentar posibles soluciones. """)