# RPS Vision AI: Clasificador de Piedra, Papel o Tijera

Bienvenido a **RPS Vision AI**, una aplicación interactiva desarrollada en Python utilizando **Streamlit** y **TensorFlow**. Este proyecto demuestra cómo un modelo de Machine Learning puede ser integrado en una aplicación web funcional, abarcando el ciclo de vida completo de un modelo desde el entrenamiento hasta su despliegue.

## 📌 El Proyecto

El objetivo de este proyecto es clasificar imágenes tomadas por el usuario (mediante la cámara web o subiendo un archivo) en tres categorías:
- **Piedra**
- **Papel**
- **Tijera**

El modelo base es un clasificador de Deep Learning (Keras) que fue entrenado previamente, y esta aplicación sirve como interfaz para interactuar con él de manera intuitiva y visualmente atractiva.

---

## 🛠️ Requisitos e Instalación

Para ejecutar este proyecto localmente, asegúrate de tener Python instalado (se recomienda Python 3.8+).

1. **Clona o descarga este repositorio** (o navega al directorio donde se encuentran estos archivos).
2. **Crea un entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```
3. **Instala las dependencias necesarias:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Ejecución de la Aplicación

Una vez instaladas las dependencias, asegúrate de que los archivos del modelo (`keras_model.h5`) y las etiquetas (`labels.txt`) se encuentren en la misma carpeta que `app.py`.

Ejecuta el siguiente comando en la terminal:

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador predeterminado (usualmente en `http://localhost:8501`).

---

## 🏗️ Estructura del Proyecto

- `index.html` y `style.css`: La **Landing Page** estática. Diseñada con UI/UX moderno (Glassmorphism), lista para ser desplegada en **GitHub Pages**.
- `app.py`: La aplicación interactiva principal en Streamlit, lista para desplegarse en **Streamlit Cloud**.
- `utils.py`: Funciones de utilidad para preprocesamiento del modelo y temas visuales.
- `requirements.txt`: Lista de librerías requeridas.
- `.gitignore`: Archivos ignorados para el control de versiones.
- `keras_model.h5`: El modelo de Deep Learning entrenado.
- `labels.txt`: Etiquetas de clasificación (0 Piedra, 1 Papel, 2 Tijera).
- `README.md`: Este documento explicativo.

---

## 🚀 Guía de Despliegue (Deployment)

Este proyecto está diseñado con una **Arquitectura Distribuida**, separando el Frontend informativo del Backend interactivo:

### 1. Desplegar la Landing Page (GitHub Pages)
Sube todo este repositorio a GitHub. Luego, ve a la pestaña **Settings > Pages** de tu repositorio y selecciona la rama `main` (o `master`) como fuente. Tu `index.html` estará disponible globalmente con toda la teoría del proyecto.

### 2. Desplegar la App de Predicción (Streamlit Cloud)
Crea una cuenta en [share.streamlit.io](https://share.streamlit.io/) y conecta tu repositorio de GitHub. Selecciona el archivo `app.py` como punto de entrada. 

### 3. Conectar Ambos
Una vez que tengas el enlace en vivo de tu app de Streamlit, **edita el archivo `index.html`** y reemplaza el `#` en el atributo `href` del botón `🚀 Probar la Aplicación` con la URL real de tu Streamlit.


---

## 🧠 Ciclo de Vida del Machine Learning Aplicado

Este proyecto es el resultado de las siguientes fases típicas que maneja un **ML Specialist** o **Data Engineer**:

1. **Recolección de Datos:** Captura de imágenes representativas para Piedra, Papel y Tijera bajo diferentes condiciones.
2. **Entrenamiento (Training):** Uso de redes neuronales convolucionales (CNN) para aprender las características de cada gesto.
3. **Exportación:** Generación del archivo `.h5` (pesos del modelo) y el archivo de texto con las etiquetas.
4. **Despliegue (Deployment):** Creación de una aplicación amigable con Streamlit para realizar inferencia en tiempo real y aportar valor al usuario final.

---

*Desarrollado con ❤️ por un Especialista en Machine Learning.*
