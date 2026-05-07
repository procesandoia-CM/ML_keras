import streamlit as st
from PIL import Image
import numpy as np
import os
import sys

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import apply_custom_theme, load_model_and_labels, preprocesar_imagen

st.set_page_config(
    page_title="Predicción - RPS Vision AI",
    page_icon="🔮",
    layout="wide"
)

def main():
    st.sidebar.title("🤖 RPS Vision AI")
    st.sidebar.markdown("---")
    
    # Selección de Tema
    st.sidebar.subheader("🎨 Apariencia")
    theme = st.sidebar.radio("Elige un tema:", ["Oscuro", "Claro"], key="theme_prediccion")
    apply_custom_theme(theme)
    
    st.sidebar.markdown("---")
    st.sidebar.info("Esta es la sección de inferencia de la app.")
    st.sidebar.markdown("[👈 Volver a la Landing Page](#)") # Aquí iría el enlace a GH pages en el futuro

    st.title("🔮 Predicción en Vivo")
    st.write("Sube una imagen o utiliza tu cámara web para ver al modelo en acción reconociendo Piedra, Papel o Tijera.")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "keras_model.h5")
    labels_path = os.path.join(base_dir, "labels.txt")
    
    model, labels = load_model_and_labels(model_path, labels_path)
    
    if model is None or labels is None:
        st.warning(f"Por favor, asegúrate de que los archivos `keras_model.h5` y `labels.txt` estén en el directorio principal.")
        return
        
    opcion = st.radio("¿Cómo deseas proporcionar la imagen?", ["Cargar un archivo", "Usar la cámara"])
    
    imagen_mostrada = None
    
    if opcion == "Cargar un archivo":
        uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            imagen_mostrada = Image.open(uploaded_file).convert("RGB")
    else:
        camera_image = st.camera_input("Toma una foto a tu mano")
        if camera_image is not None:
            imagen_mostrada = Image.open(camera_image).convert("RGB")
            
    if imagen_mostrada is not None:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.image(imagen_mostrada, caption='Imagen de entrada', use_container_width=True)
            
        with col2:
            with st.spinner("Analizando la imagen..."):
                # Preprocesar e Inferir
                data = preprocesar_imagen(imagen_mostrada)
                prediction = model.predict(data)
                index = np.argmax(prediction)
                class_name = labels[index]
                confidence_score = prediction[0][index]
                
                # Quitar el número del label si viene con formato "0 Piedra"
                if " " in class_name:
                    class_name = class_name.split(" ", 1)[1]
                
                st.subheader("Resultado de la Predicción:")
                st.markdown(f'<div class="card" style="text-align: center;">', unsafe_allow_html=True)
                st.markdown(f'<div class="metric-value">{class_name}</div>', unsafe_allow_html=True)
                st.progress(float(confidence_score))
                st.write(f"**Confianza:** {confidence_score * 100:.2f}%")
                st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
