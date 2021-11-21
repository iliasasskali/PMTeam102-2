from numpy import int64, isnan, nan
import streamlit as st
import pandas as pd
import json

from streamlit.config import _check_conflicts 

# cd Team102...
# python3 -m pipenv shell  
# python3 -m pip install openpyxl 
# python3 -m pip install streamlit   
# streamlit run VisualRepresentation.py                                                                 

col1, col2 = st.columns(2)
with col1:
    st.image('https://incasolsolars.cat/wp-content/uploads/2020/04/cropped-logo_incasol_transp_neg-1.png', width=256)
with col2:
    st.image('https://www.upf.edu/documents/7283915/220614254/UPFt_rgb.png/99b73f76-6b25-8b0d-f297-cdeb13c64962?t=1547110100870', width=256)

@st.cache
def load_data():
    # Fetching data from excel file
    xls = pd.ExcelFile('DataSprint.xlsx')
    df_poblacio = pd.read_excel(xls, 'Poblacio', index_col=0)
    df_demografia = pd.read_excel(xls, 'Demografia', index_col=0)
    df_lloguer = pd.read_excel(xls, 'Lloguer-Decada',  index_col=1)
    df_edat_sexe = pd.read_excel(xls, 'Poblacio-Edat-Sexe', index_col=2)
    df_demografia_habitatges = pd.read_excel(xls, 'Demografia-Habitatges', index_col=0, header=0)#.fillna(0).astype(int64)   #CAMBIO AQUI DE NAN A 0
    with open("checkbox_column.json", "r", encoding ="utf8") as json_file:
        checkbox_column = json.load(json_file)

    return df_poblacio, df_demografia, df_lloguer, df_edat_sexe, df_demografia_habitatges, checkbox_column

df_poblacio, df_demografia, df_lloguer, df_edat_sexe, df_demografia_habitatges, checkbox_column = load_data()

def plot_cities_data(cities, data):
    for d in data:
        if d in df_poblacio.columns:    # Comprobar en que hoja esta la info
            st.subheader(d)
            st.bar_chart(df_poblacio[d][cities])
        elif d in df_demografia.columns:
            st.subheader(d)
            st.bar_chart(df_demografia[d][cities])
        elif d in df_lloguer.columns:   # Va por año este
            st.subheader("Preu lloguer ultima decada:")
            df_temp_cities = []
            for city in cities:
                if city in df_lloguer.index:
                    data = {city:list(df_lloguer[d][city])}  
                    df_temp = pd.DataFrame(data, index = df_lloguer["any"][city])
                    df_temp_cities.append(df_temp.copy())
            final_df = pd.concat(df_temp_cities, axis=1)
            st.line_chart(final_df)
        elif d in df_edat_sexe.columns:
            st.subheader(d)
            st.bar_chart(df_edat_sexe[d][cities])
        elif d in df_demografia_habitatges.columns: #Comprobar celdas con nan
            if not isnan(df_demografia_habitatges[d][cities].values).all():
                st.subheader(d)
                st.bar_chart(df_demografia_habitatges[d][cities])

st.title('Dades Tarragonès')
st.write("Dades dels municipis del Tarragonès, utilitza el menú lateral per generar gràfiques i comparar dades de diferents municipis.")

# Side Bar
cities = st.sidebar.multiselect(
    "Filtrar per municipi, selecciona multiples municipis per comparar-los:",
    df_poblacio.index
)
st.sidebar.subheader('\nEscull les dades per visualitzar')

checklist = {}
st.sidebar.write('LLoguer:')
checklist["preu_lloguer"] = st.sidebar.checkbox('Preu lloguer ultima decada')

st.sidebar.write('Població:')
checklist["poblacio"] = st.sidebar.checkbox("Població")
checklist["poblacio_activa"] = st.sidebar.checkbox("Població Activa")
checklist["tasa_poblacio_activa"] = st.sidebar.checkbox("Tasa població Activa")
checklist["poblacio_desocupada"] = st.sidebar.checkbox("Població Desocupada")
checklist["taxa_atur"] = st.sidebar.checkbox("Taxa d'atur")
checklist["renda_familiar"] = st.sidebar.checkbox('Renda familiar disponible per habitant')
checklist["minims_mercat"] = st.sidebar.checkbox('Mínims per accedir al mercat de lloguer')

st.sidebar.write('Demografia:')
checklist["densitat_poblacio"] = st.sidebar.checkbox("Densitat de població")
checklist["joves_emancipacio"] = st.sidebar.checkbox("Joves amb edat d'emancipar-se")
checklist["relacions_dependencia"] = st.sidebar.checkbox("Relacions de dependencia")
checklist["index_envelliment"] = st.sidebar.checkbox("Índex d'envelliment")
checklist["index_recanvi"] = st.sidebar.checkbox("Índex de recanvi poblacional")

st.sidebar.write('Poblacio segons Edat-Genere:')
checklist["h0_14"] = st.sidebar.checkbox("Homes de 0 a 14 anys")
checklist["h15_64"] = st.sidebar.checkbox("Homes de 15 a 64 anys")
checklist["h65_m"] = st.sidebar.checkbox("Homes de 65 anys i més")
checklist["d0_14"] = st.sidebar.checkbox("Dones de 0 a 14 anys")
checklist["d15_64"] = st.sidebar.checkbox("Dones de 15 a 64 anys")
checklist["d65_m"] = st.sidebar.checkbox("Dones de 65 anys i més")
checklist["t0_14"] = st.sidebar.checkbox("Total de 0 a 14 anys")
checklist["t15_64"] = st.sidebar.checkbox("Total de 15 a 64 anys")
checklist["t65_m"] = st.sidebar.checkbox("Total de 65 anys i més")

st.sidebar.write('Demografia i habitatges:')
checklist["pob_cat"] = st.sidebar.checkbox("Població per lloc de neixament - Catalunya")
checklist["pob_esp"] = st.sidebar.checkbox("Població per lloc de neixament - Resta d'Espanya")
checklist["pob_est"] = st.sidebar.checkbox("Població per lloc de neixament - Estranger")
checklist["pob_nac_esp"] = st.sidebar.checkbox("Població per nacionalitat - Espanyola")
checklist["pob_nac_est"] = st.sidebar.checkbox("Població per nacionalitat - Estrangera")
checklist["mob_est_no_uni"] = st.sidebar.checkbox("Movilitat obliga per estudis no universitaris (Curs 2019/20)")
checklist["mob_est_no_uni_perc"] = st.sidebar.checkbox("Movilitat obliga per estudis no universitaris (Curs 2019/20) - Alumnes residents que estudien al mateix municipi")
checklist["hab_fam_tot"] = st.sidebar.checkbox("Habitatges familiars totals")
checklist["hab_fam_prin"] = st.sidebar.checkbox("Habitatges familiars principals")
checklist["hab_fam_vuits"] = st.sidebar.checkbox("Habitatges familiars buits")
checklist["hab_fam_lloguer"] = st.sidebar.checkbox("Habitatges familiars de lloguer")
checklist["hab_fam_61_90"] = st.sidebar.checkbox("Habitatges familiars de 61 a 90 m2")
checklist["hab_fam_91_120"] = st.sidebar.checkbox("Habitatges familiars de 91 a 120 m2")
checklist["ist"] = st.sidebar.checkbox("Index socioeconomic territorial (IST)")
checklist["llars_1_persona"] = st.sidebar.checkbox("Llars per grandaria de la llar - 1 persona")
checklist["llars_2_persona"] = st.sidebar.checkbox("Llars per grandaria de la llar - 2 persones")
checklist["llars_3_persona"] = st.sidebar.checkbox("Llars per grandaria de la llar - 3 persones")
checklist["llars_4m_persona"] = st.sidebar.checkbox("Llars per grandaria de la llar - 4 persones i més")
checklist["llars_parella"] = st.sidebar.checkbox("Llars per tipus de nucli - Parella sense fills")
checklist["llars_parella_fills"] = st.sidebar.checkbox("Llars per tipus de nucli - Parella amb fills")
checklist["llars_pare_mare_fills"] = st.sidebar.checkbox("Llars per tipus de nucli - Pare o Mare amb fills")
checklist["hab_fam_prin_prop"] = st.sidebar.checkbox("Habitatges familiars principals de propietat")
checklist["habitants_habitatge"] = st.sidebar.checkbox("Habitants per habitatge")

columns = [checkbox_column[k] for k, v in checklist.items() if v]

if len(cities) > 0 and len(columns) > 0:
    plot_cities_data(cities, columns)
elif len(cities) > 0:
    st.subheader('Dades Població')
    st.write(df_poblacio.loc[cities])

    st.subheader('Dades Demogràfiques')
    st.write(df_demografia.loc[cities])

    st.subheader('Preu lloguer última dècada')
    st.write(df_lloguer.loc[cities])

    st.subheader('Dades Edat-Genere')
    st.write(df_edat_sexe.loc[cities])

    st.subheader('Dades Demografia-Habitatges')
    st.write(df_demografia_habitatges.loc[cities])
elif len(columns) > 0:
    columnsPoblacio = [column for column in columns if column in df_poblacio.columns]
    if len(columnsPoblacio) > 0:
        st.subheader('Dades Població')
        st.write(df_poblacio[columnsPoblacio])

    columnsDemografia = [column for column in columns if column in df_demografia.columns]
    if len(columnsDemografia) > 0:
        st.subheader('Dades Demogràfiques')
        st.write(df_demografia[columnsDemografia])

    if checklist["preu_lloguer"]:
        st.subheader('Preu lloguer última dècada')
        st.write(df_lloguer)

    columnsEdatSexe = [column for column in columns if column in df_edat_sexe.columns]
    if len(columnsEdatSexe) > 0:
        st.subheader('Dades Edat-Genere')
        st.write(df_edat_sexe[columnsEdatSexe])

    columnsDemografiaHabitatges = [column for column in columns if column in df_demografia_habitatges.columns]
    if len(columnsDemografiaHabitatges) > 0:  
        st.subheader('Dades Demografia-Habitatges')
        st.write(df_demografia_habitatges[columnsDemografiaHabitatges])
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