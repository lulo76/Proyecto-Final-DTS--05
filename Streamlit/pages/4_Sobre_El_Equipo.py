import streamlit as st

st.title("Equipo de Trabajo")

st.markdown("Este proyecto lo realizamos de la siguiente manera:")

st.subheader("Nuestro Repo")
st.markdown("https://github.com/lulo76/Proyecto-Final-DTS--05")


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Nuestro Team", "Diagrama de Gantt", "Workflow","Consultas de Ejemplo", "Metodologias"])

with tab1:
    st.subheader("Nuestro team")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/dev%20team%20olist.png?raw=true")

with tab2:
    st.subheader("Utilizamos el siguiente diagrama de Gant:")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/diagrama_ganttterminado.png?raw=true")

with tab3: 
    st.subheader("El Workflow de trabajo se estructuro de la siguiente manera")
    st.markdown("Etapa Local")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/Workflow_actual.png?raw=true")
    st.write("""En esta primer etapa buscamos manejar los archivos de forma local, realizando un analisis EDA y pasos 
            preliminares para entender que necesitamos para el proyecto""")
    st.markdown("Escalabilidad")
    st.write("""En este segundo momento intentamos escalar el flujo de datos para hacerlo en la nube mediante
            tecnologias como Amazon Web Services(AWS) que nos ahorran tiempo en los procesos. De esta manera confeccionariamos
            el Datawarehouse en la nube""")
    st.markdown("***")
    st.subheader("Utilizamos el gestor de proyecto trello")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/trello.png?raw=true")
    st.write("""Para coordinar las tareas del dia a dia utilizamos esta herramienta, asi cada integrante del equipo 
            puede reportar en que se encuentra trabajando y a su vez saber como esta el avance sus compañeros.""")
with tab4:
    st.title("Consultas de Ejemplo")
    st.subheader("En los siguientes videos podemos ver ejemplos de consultas a la base de datos creada en Amazon Web Services")
    st.markdown("En este video podemos ver las consultas realizadas desde una conexion con MYSQL Workbench")
    st.video("https://youtu.be/2dOqwHUKen4")
    st.markdown("En este video podemos ver consultas realizadas desde python directamente al DataWarehouse creado en AWS")
    st.video("https://www.youtube.com/watch?v=377Ax9C-Lcs")

with tab5: 
    st.subheader("Metodologia Agile-Scrum")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/metodologia.png?raw=true")
    st.write("""Metodología de trabajo.
        La metodología de gestión de proyecto utilizada se cree muy importante para llegar a los
        objetivos propuestos. Se utilizará metodología considerada ágil al ser colaborativa, rápida
        y efectiva, iterativa, respaldada por datos y fundamentalmente que se valore a las personas}
        por encima de los procesos ya que se deduce que es la mejor y más eficiente manera de trabajo.
        En particular se realizará la metodología Scrum, que se basa en “Sprints” para crear un ciclo 
        de proyecto, en este caso, sprints de una semana. Cada sprint culminará con la demostración del
        progreso del trabajo realizado hasta el momento, frente al Product Owner. La duración total del 
        proyecto será de 4 semanas. Siendo la última exclusivamente para presentación final y demostrar 
        puesta en producción. Se realizan reuniones diarias (guiadas por un Scrum Master) con el objetivo
        de conocer a todos los participantes del proyecto, dividiendo, organizando trabajo y tiempos por 
        cada integrante y así garantizar que las tareas se finalicen a tiempo y de manera correcta.""")