# pages/1_inscripcion_proveedores.py
import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(
    page_title="Inscripción de Proveedores",
    page_icon="📝",
    layout="wide"
)

def guardar_proveedor(nombre, tipo, estilo, precio_promedio, ubicacion):
    conn = sqlite3.connect('proveedores.db')
    c = conn.cursor()
    try:
        c.execute('''
            INSERT INTO proveedores 
            (nombre, tipo, estilo, precio_promedio, puntuacion, ubicacion)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nombre, tipo, estilo, precio_promedio, 5.0, ubicacion))
        conn.commit()
        return True
    except Exception as e:
        st.error(f"Error al guardar: {str(e)}")
        return False
    finally:
        conn.close()

def main():
    st.title("Inscripción de Proveedores")
    
    with st.form("provider_form"):
        nombre = st.text_input("Nombre:")
        tipo = st.selectbox(
            "Tipo:",
            ["DJ", "Animación", "Catering", "Fotografía"]
        )
        estilo = st.text_input("Estilo:")
        precio_promedio = st.number_input("Precio Promedio (€):", min_value=0.0)
        ubicacion = st.text_input("Ubicación:")
        
        submitted = st.form_submit_button("Guardar Proveedor")
        
        if submitted:
            if guardar_proveedor(nombre, tipo, estilo, precio_promedio, ubicacion):
                st.success("¡Proveedor guardado exitosamente!")
                st.balloons()
    
    # Sección de carga masiva
    st.divider()
    st.subheader("Importación Masiva desde Excel")
    uploaded_file = st.file_uploader(
        "Selecciona un archivo Excel o CSV",
        type=['xlsx', 'xls', 'csv']
    )
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            if st.button("Importar Datos"):
                df['puntuacion'] = 5.0
                conn = sqlite3.connect('proveedores.db')
                df.to_sql('proveedores', conn, if_exists='append', index=False)
                conn.close()
                st.success(f"Se importaron {len(df)} proveedores exitosamente")
                st.balloons()
        
        except Exception as e:
            st.error(f"Error al procesar el archivo: {str(e)}")

if __name__ == "__main__":
    main()