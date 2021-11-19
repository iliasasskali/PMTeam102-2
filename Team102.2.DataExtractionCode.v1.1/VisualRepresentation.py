import streamlit as st
import pandas as pd

# python3 -m pipenv shell  
# python3 -m pip install streamlit   
# streamlit run VisualRepresentation.py                                                                 

@st.cache
def load_data():
    # Fetching data from excel file
    xls = pd.ExcelFile('DataSprint.xlsx')
    df_poblacio = pd.read_excel(xls, 'Poblacio', index_col=0)
    df_demografia = pd.read_excel(xls, 'Demografia', index_col=0)
    df_lloguer = pd.read_excel(xls, 'Lloguer-Decada',  index_col=1)
    df_edat_sexe = pd.read_excel(xls, 'Poblacio-Edat-Sexe', index_col=2)
    df_demografia_habitatges = pd.read_excel(xls, 'Demografia-Habitatges', index_col=0)

    return df_poblacio, df_demografia, df_lloguer, df_edat_sexe, df_demografia_habitatges

st.title('Tarragonès Data')
df_poblacio, df_demografia, df_lloguer, df_edat_sexe, df_demografia_habitatges = load_data()

multiselect = st.sidebar.multiselect(
    "Filter info by municipi or select multiple municipis to compare them:",
    df_poblacio.index
)

st.subheader('Poblation Data')
st.write(df_poblacio)

st.subheader('Demografic Data')
st.write(df_demografia)

st.subheader('Last Decade Rent Data')
st.write(df_lloguer)

st.subheader('Age Gender Data')
st.write(df_edat_sexe)

st.subheader('Age Gender Data')
st.write(df_demografia_habitatges)

st.bar_chart(df_lloguer["renda"])

if st.checkbox('Show Age Gender Data'):
    st.subheader('Age Gender Data')
    st.write(df_edat_sexe)

st.line_chart(df_demografia)