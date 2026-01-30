import streamlit as st
import numpy as np
from mechaSVG import Plot, Line, Scatter

st.set_page_config(page_title="Grafica IRC ", layout="centered")

st.title("📊 Gráficas de IRC")
st.markdown(
    """
    Esta aplicación permite generar **gráficas vectoriales (SVG)** de alta calidad usando **mechaSVG**, ideal para publicaciones científicas o presentaciones.
    """
)

st.sidebar.header("Parámetros de la gráfica")

# Selección de tipo de gráfica
tipo = st.sidebar.selectbox(
    "Tipo de gráfica",
    ["Línea", "Dispersión"]
)

# Número de puntos
n = st.sidebar.slider("Número de puntos", 10, 200, 50)

# Generación de datos
x = np.linspace(0, 10, n)
y = np.sin(x)

st.subheader("Vista previa de la gráfica")

# Crear gráfica con mechaSVG
plot = Plot(width=600, height=400)

if tipo == "Línea":
    plot.add(Line(x, y, stroke="blue", stroke_width=2))
else:
    plot.add(Scatter(x, y, fill="red", radius=3))

# Renderizar SVG
svg_code = plot.render()

st.components.v1.html(svg_code, height=450)

# Descarga
st.subheader("Descargar gráfica")

st.download_button(
    label="Descargar SVG",
    data=svg_code,
    file_name="grafica_mechaSVG.svg",
    mime="image/svg+xml"
)

st.markdown("---")
st.subheader("¿Cómo usar esta aplicación?")
st.markdown(
    """
    1. Selecciona el **tipo de gráfica** (línea o dispersión) desde la barra lateral.
    2. Ajusta el **número de puntos** que se usarán para generar los datos.
    3. Visualiza la gráfica SVG en tiempo real.
    4. Descarga el archivo SVG para usarlo en artículos, diapositivas o edición vectorial.

    **Ventaja clave**: al ser SVG, la imagen no pierde calidad al escalarse.
    """
)

st.info("Instala las dependencias con: pip install streamlit mechaSVG numpy")
