import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

titanic_link = 'titanic.csv'

titanic_data = pd.read_csv(titanic_link)

fig, ax = plt.subplots()

ax.hist(titanic_data['age'])

st.header("Histograma del Titanic")

st.pyplot(fig)

st.markdown("___")

fig2, ax2 = plt.subplots()

y_pos = titanic_data['class']
x_pos = titanic_data['fare']

ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuanto pagaron las clases del Titanic')

st.header("Grafica de Barras del Titanic")

st.pyplot(fig2)
