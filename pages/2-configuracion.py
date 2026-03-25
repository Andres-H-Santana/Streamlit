import streamlit as st

st.title("Selector de Color RGB 🎨")

st.write("Ajusta los valores para crear tu color:")

# Sliders RGB
r = st.slider("Rojo (R)", 0, 255, 100)
g = st.slider("Verde (G)", 0, 255, 100)
b = st.slider("Azul (B)", 0, 255, 100)

# Convertir a formato CSS
color = f"rgb({r}, {g}, {b})"

# Mostrar color
st.markdown(f"""
<div style="
    width: 100%;
    height: 200px;
    background-color: {color};
    border-radius: 10px;
    border: 2px solid black;
"></div>
""", unsafe_allow_html=True)

# Mostrar valores
st.write(f"Código RGB: {color}")