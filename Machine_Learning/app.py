import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import ml_model

#st.title("PROYECTO GRUPAL DTS05")
st.markdown('### Analisis de sentimientos en reviews')
title = st.text_input('Escribe tu review en portugues', '', max_chars=200)
image_positivo = Image.open('positivo.PNG')
image_negativo = Image.open('negativo.PNG')
if title != '':
    pred = ml_model.predict(title)
    pred_mlp = pred['mlp']
    pred_cnn = pred['cnn']
    pred_lstm = pred['lstm']
    pred_global = (pred_mlp + pred_cnn + pred_lstm)/3

    col1, col2 = st.columns(2)
    with col1:
        if pred_global > 0.5:
            st.image(image_positivo, caption='')
        else:
            st.image(image_negativo, caption='')

    with col2:
        st.markdown('#')
        st.markdown('#')
        st.markdown('##### Positivo:   '+str(int(round(pred_global*100, 0)))+' %')
        st.markdown('##### Negativo:  '+str(int(round((1-pred_global)*100, 0)))+' %')

    if st.button('Mostrar detalles'):    
        fig, axs = plt.subplots(1,3, figsize=(10,2))
        axs[0].bar(['Positivo','Negativo'],np.array([pred_mlp, 1-pred_mlp]), color=['green','red'])
        axs[1].bar(['Positivo','Negativo'],np.array([pred_cnn, 1-pred_cnn]), color=['green','red'])
        axs[2].bar(['Positivo','Negativo'],np.array([pred_lstm, 1-pred_lstm]), color=['green','red'])
        axs[0].set_title('Modelo MLP')
        axs[1].set_title('Modelo CNN')
        axs[2].set_title('Modelo LSTM')
        st.pyplot(fig)
    else:
        st.markdown('')

    
