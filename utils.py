import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

def apply_custom_theme(theme):
    if theme == "Oscuro":
        bg_color = "#0E1117"
        text_color = "#FAFAFA"
        card_bg = "#1E2127"
        accent = "#FF4B4B"
    else:
        bg_color = "#FFFFFF"
        text_color = "#31333F"
        card_bg = "#F0F2F6"
        accent = "#FF4B4B"
        
    st.markdown(f"""
        <style>
            .stApp {{
                background-color: {bg_color};
                color: {text_color};
            }}
            .card {{
                background-color: {card_bg};
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
            }}
            h1, h2, h3 {{
                color: {accent};
            }}
            .metric-value {{
                font-size: 2rem;
                font-weight: bold;
                color: {accent};
            }}
        </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_model_and_labels(model_path="keras_model.h5", labels_path="labels.txt"):
    try:
        model = tf.keras.models.load_model(model_path, compile=False)
        with open(labels_path, "r") as f:
            labels = [line.strip() for line in f.readlines()]
        return model, labels
    except Exception as e:
        st.error(f"Error cargando el modelo o las etiquetas: {e}")
        return None, None

def preprocesar_imagen(image):
    # Keras / Teachable Machine espera una imagen de 224x224
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    
    # Normalizar la imagen
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    
    # Crear el batch de 1 imagen
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    return data
