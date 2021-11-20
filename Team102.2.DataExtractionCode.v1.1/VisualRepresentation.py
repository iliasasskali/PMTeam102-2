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

def plot_cities_data(cities, data):
    for d in data:
        if d in df_poblacio.columns:    #Comprobar en que hoja esta la info
            st.bar_chart(df_poblacio[d][cities])
        elif d in df_demografia.columns:
            st.bar_chart(df_demografia[d][cities])
        elif d in df_lloguer.columns:
            st.bar_chart(df_lloguer[d][cities])
        elif d in df_edat_sexe.columns:
            st.bar_chart(df_edat_sexe[d][cities])
        elif d in df_demografia_habitatges.columns:
            st.bar_chart(df_demografia_habitatges[d][cities])

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

st.sidebar.write('Demografia:')
densitat_poblacio = st.sidebar.checkbox("Densitat de població")
joves_emancipacio = st.sidebar.checkbox("Joves amb edat d'emancipar-se")
relacions_dependencia = st.sidebar.checkbox("Relacions de dependencia")
index_envelliment = st.sidebar.checkbox("Índex d'envelliment")
index_recanvi = st.sidebar.checkbox("Índex de recanvi poblacional")

st.sidebar.write('Poblacio segons Edat-Genere:')
h0_14 = st.sidebar.checkbox("Homes de 0 a 14 anys")
h15_64 = st.sidebar.checkbox("Homes de 15 a 64 anys")
h65_m = st.sidebar.checkbox("Homes de 65 anys i més")
d0_14 = st.sidebar.checkbox("Dones de 0 a 14 anys")
d15_64 = st.sidebar.checkbox("Dones de 15 a 64 anys")
d65_m = st.sidebar.checkbox("Dones de 65 anys i més")
t0_14 = st.sidebar.checkbox("Total de 0 a 14 anys")
t15_64 = st.sidebar.checkbox("Total de 15 a 64 anys")
t65_m = st.sidebar.checkbox("Total de 65 anys i més")

st.sidebar.write('Demografia i habitatges:')
pob_cat = st.sidebar.checkbox("Població per lloc de neixament - Catalunya")
pob_esp = st.sidebar.checkbox("Població per lloc de neixament - Resta d'Espanya")
pob_est = st.sidebar.checkbox("Població per lloc de neixament - Estranger")
pob_nac_esp = st.sidebar.checkbox("Població per nacionalitat - Espanyola")
pob_nac_est = st.sidebar.checkbox("Població per nacionalitat - Estrangera")
mob_est_no_uni = st.sidebar.checkbox("Movilitat obliga per estudis no universitaris (Curs 2019/20)")
mob_est_no_uni_perc = st.sidebar.checkbox("Movilitat obliga per estudis no universitaris (Curs 2019/20) - Alumnes residents que estudien al mateix municipi")
hab_fam_tot = st.sidebar.checkbox("Habitatges familiars totals")
hab_fam_prin = st.sidebar.checkbox("Habitatges familiars principals")
hab_fam_vuits = st.sidebar.checkbox("Habitatges familiars buits")
hab_fam_lloguer = st.sidebar.checkbox("Habitatges familiars de lloguer")
hab_fam_61_90 = st.sidebar.checkbox("Habitatges familiars de 61 a 90 m2")
hab_fam_91_120 = st.sidebar.checkbox("Habitatges familiars de 91 a 120 m2")
ist = st.sidebar.checkbox("Index socioeconomic territorial (IST)")
llars_1_persona = st.sidebar.checkbox("Llars per grandaria de la llar - 1 persona")
llars_2_persona = st.sidebar.checkbox("Llars per grandaria de la llar - 2 persones")
llars_3_persona = st.sidebar.checkbox("Llars per grandaria de la llar - 3 persones")
llars_4m_persona = st.sidebar.checkbox("Llars per grandaria de la llar - 4 persones i més")
llars_parella = st.sidebar.checkbox("Llars per tipus de nucli - Parella sense fills")
llars_parella_fills = st.sidebar.checkbox("Llars per tipus de nucli - Parella amb fills")
llars_pare_mare_fills = st.sidebar.checkbox("Llars per tipus de nucli - Pare o Mare amb fills")
hab_fam_prin_prop = st.sidebar.checkbox("Habitatges familiars principals de propietat")
habitants_habitatge = st.sidebar.checkbox("Habitants per habitatge")

if len(multiselect) > 0:
    plot_cities_data(multiselect, ['Població Activa', "Tasa població activa"])

else:
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
