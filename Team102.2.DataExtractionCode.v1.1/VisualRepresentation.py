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
    df_demografia_habitatges = pd.read_excel(xls, 'Demografia-Habitatges', index_col=0, header=0)

    return df_poblacio, df_demografia, df_lloguer, df_edat_sexe, df_demografia_habitatges

st.title('Dades Tarragonès')
st.write("Dades dels municipis del Tarragonès, utilitza el menú lateral per generar gràfiques i comparar dades de diferents municipis.")
df_poblacio, df_demografia, df_lloguer, df_edat_sexe, df_demografia_habitatges = load_data()

# Side Bar
multiselect = st.sidebar.multiselect(
    "Filtrar per municipi, selecciona multiples municipis per comparar-los:",
    df_poblacio.index
)
st.sidebar.subheader('\nEscull les dades per visualitzar')

st.sidebar.write('LLoguer:')
preu_lloguer = st.sidebar.checkbox('Preu lloguer ultima decada')

st.sidebar.write('Població:')
poblacio = st.sidebar.checkbox("Població")
tasa_poblacio_activa = st.sidebar.checkbox("Tasa població Activa")
taxa_atur = st.sidebar.checkbox("Taxa d'atur")
renda_familiar = st.sidebar.checkbox('Renda familiar disponible per habitant')
minims_mercat = st.sidebar.checkbox('Mínims per accedir al mercat de lloguer')

st.subheader('Dades Població')
st.write(df_poblacio)

st.subheader('Dades Demogràfiques')
st.write(df_demografia)

st.subheader('Preu lloguer última dècada')
st.write(df_lloguer)

st.subheader('Dades Edat-Genere')
st.write(df_edat_sexe)

st.subheader('Dades Demografia-Habitatges')
st.write(df_demografia_habitatges)


#st.bar_chart(df_lloguer["renda"])

#if st.checkbox('Show Age Gender Data'):
#    st.subheader('Age Gender Data')
#    st.write(df_edat_sexe)
