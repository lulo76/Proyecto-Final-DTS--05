import streamlit as st

st.header("Sugerencias del Equipo")
st.markdown("***")

st.write("""Con el analisis que hemos realizado podemos sugerir que en un primer momento las medidas que se tomen, esten 
        orientadas a la region de San Paulo que es donde radican la mayor cantidad de ventas, de nuestros clientes. En este
        sentido podemos recomendar que de existir la posibilidad de incorporar un nuevo hub(Centro de Distribucion), se ubique
        en esta zona o en lugares aledaños.""")
st.markdown("***")
st.write("""En cuanto al analisis de los tiempos de entrega, podemos sugerir cambios en 3 puntos principales, en un primer punto
    sugerimos dinamizar la aprobacion de las ordenes de compra, esto podria realizarse a mediano/largo plazo con la implementacion de
    una billetera virtual que permita que el pago del cliente ingrese de manera agil. En un segundo punto, sugerimos implementar un sistema
    de puntos o reviews de vendedores para aquellos vendedores que despachen su producto antes de los 2 dias o algun metodo similar para incentivar
    que los productos se despachen lo mas rapido posible. En tercer lugar recomendamos revisar la posibilidad de que en ciudades como San Paulo se 
    implemente para productos pequeños la paqueteria liviana y los moto-envios, o algun sistema similar tercerizado que permita optimizar los tiemmpos
    sobre todo con paquetes de pequeño porte. """)
st.markdown("***")
st.write("""En cuanto a las categorias de productos, sugerimos revisar las tendencias actuales de mercado, de modas o productos de actualidad
    ya que entre las categorias menos vendidas encontramos productos que ya estan en desuso como 'dvd-s""")
st.write("""En relacion a los productos que mas se han vendido, recomendamos complementar con el analisis de sentimiento que le brindamos, para 
    lanzar campañas de marketing en fechas u horarios optimos para aumentar sus ventas. Es decir, con los recursos que disponemos, podemos alcanzar
    un mayor indice de ventas de dichos productos, e impulsar otros""")

st.markdown("***")
st.subheader("En el siguiente videos podemos obtener mas informacion sobre el funcionamiento de Olist")

st.video("https://youtu.be/jXJYaVRL5SU")