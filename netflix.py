import streamlit as st
import pandas as pd
import numpy as np
import codecs

st.title('Netflix app')
##Credencial
st.sidebar.image("logoUV.jpg")
st.sidebar.markdown("##")
##Nombre y matricula
st.header("Angel Moises Cruz Cruz")
st.markdown("S19004906")

URL='movies.csv'

@st.cache
def load_data(nrows):
    doc = codecs.open(URL,'r','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

def filter_data_by_film(film):
    filtered_data_film = data[data['name'].str.upper().str.contains(film)]
    return filtered_data_film

def filter_data_by_director(director):
    filtered_data_director = data[data['director'] == director]
    return filtered_data_director




data_load_state = st.text('Cargando...')
data = load_data(1000)
data_load_state.text("Done Angel Cruz! (using st.cache)")

if st.sidebar.checkbox('Mostrar todas las peliculas'):
    st.subheader('Todas las peliculas')
    st.write(data)


titlefilm = st.sidebar.text_input('Titulo de las pelicula :')
Buscar = st.sidebar.button('Buscar pelicula')

if (Buscar):
   data_film = filter_data_by_film(titlefilm.upper())
   count_row = data_film.shape[0]  
   st.write(f"Resultados encontrados: {count_row}")
   st.write(data_film)



selected_director = st.sidebar.selectbox("Seleccionar Director", data['director'].unique())
FilterbyDirector = st.sidebar.button('Filtrar director ')

if (FilterbyDirector):
   filterbydir = filter_data_by_director(selected_director)
   count_row = filterbydir.shape[0] 
   st.write(f"Resultados para filtro de directores: {count_row}")

   st.dataframe(filterbydir)