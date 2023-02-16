import streamlit as st
import pandas as pd

st.title( 'Streamlit - Buscar nombres')

DATA_URL = ('https://firebasestorage.googleapis.com/v0/b/testing-calculator-554e7.appspot.com/o/dataset%2Fdataset.csv?alt=media&token=09e7887b-5e68-47e8-abd9-10d8c86a0c9c')

@st.cache
def load_data_byname (name):
    data = pd.read_csv (DATA_URL)
    filtered_data_byname = data[data [ 'name' ].str.contains (name) ]

    return filtered_data_byname

myname = st.text_input ( 'Name :')

if (myname):
    filterbyname = load_data_byname (myname)
    count_row = filterbyname.shape[0] # Gives number of rows
    st.write(f"Total names : {count_row}")

    st.dataframe (filterbyname)