import streamlit as st

st.header("Comunicate con nosotros")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.subheader("Hector")    
    if st.checkbox("Contacta a Hector"):
            st.markdown("herrerae.hj87@gmail.com")
            st.subheader("Linkedin de Hector")
            st.markdown("https://www.linkedin.com/in/herrerraespinolahj/")
            

with col2:
    st.subheader("Karen")
    if st.checkbox("Contacta a Karen"):
            st.markdown("krnlau07@gmail.com")
            st.subheader("Linkedin de Karen")
            st.markdown("https://www.linkedin.com/in/karen-uzcategui-b236a3248/")


with col3:
    st.subheader("Joaquin")
    if st.checkbox("Contacta a Joaquin"):
            st.markdown("joaquintwosantos@gmail.com")
            st.subheader("Linkedin de Joaquin")
            st.markdown("https://www.linkedin.com/in/joaquin-d-187203244")


with col4:
    st.subheader("Lucas")
    if st.checkbox("Contacta a Lucas"):
            st.markdown("lucaswayar@outlook.com")
            st.subheader("Linkedin de Lucas")
            st.markdown("https://www.linkedin.com/in/lucaswayar/")


with col5:
    st.subheader("Armando")
    if st.checkbox("Contacta a Armando"):
            st.markdown("amadrigal.fismat@gmail.com")
            st.subheader("Linkedin de Armando")
            st.markdown("https://www.linkedin.com/in/armadrigal")