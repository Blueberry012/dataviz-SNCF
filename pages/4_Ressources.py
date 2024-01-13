import streamlit as st
import pandas as pd
import plotly.express as px

# Titre de l'application
st.title("Bases de données")

# Ajouter une image avec redimensionnement et placement spécifique
image = 'image/sncf.png'

# Affichage de l'image avec une taille personnalisée et placement dans le coin supérieur droit
st.image(image, width=100, use_column_width=False, clamp=True)

def afficher_frequentation_gares():
    st.header("Frequentation des gares")
    data_freq_gares = pd.read_csv('data/frequentation-gares.csv', sep=';')
    st.write(data_freq_gares)

def afficher_horaires_gares():
    st.header("Horaires des gares")
    data = pd.read_csv('data/horaires-des-gares.csv', sep=';', names=['Gare', 'Jour de la semaine', 'Horaire en jour férié','Horaire en jour normal'] , skiprows=1)
    st.write(data)

def afficher_liste_gares():
    st.header("Liste des gares")
    data_gares = pd.read_csv('data/liste-des-gares.csv', sep=';')
    st.write(data_gares)

def afficher_repartition_utilisation():
    st.header("Repartition de l'utilisation des moyens d'acces")
    data = pd.read_csv('data/repartition-des-moyens-dacces.csv', sep=';')
    st.write(data)

def afficher_repartition_distances():
    st.header("Repartition des distances d'acces a la gare")
    data = pd.read_csv('data/repartition-des-distances-dacces.csv',sep=';')
    st.write(data)

def afficher_regularite_mensuelle_intercites():
    st.header("regularite mensuelle intercites")
    data = pd.read_csv('data/regularite-mensuelle-intercites.csv', sep=';')
    st.write(data)

def afficher_regularite_mensuelle_TGV():
    st.header("regularite mensuelle TGV")
    data = pd.read_csv('data/regularite-mensuelle-tgv-aqst.csv', sep=';')
    st.write(data)

afficher_frequentation_gares()
afficher_horaires_gares()
afficher_liste_gares()
afficher_repartition_utilisation()
afficher_repartition_distances()
afficher_regularite_mensuelle_TGV()
afficher_regularite_mensuelle_intercites()