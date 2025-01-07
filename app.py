import pandas as pd
import plotly.express as px
import streamlit as st
        
st.header("Análise de Dados de Veículos")

car_data = pd.read_csv('vehicles.csv')

hist_button = st.button('Criar histograma')

if hist_button: 
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button: 
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Odomômetro vs Preço")
    st.plotly_chart(fig_scatter, use_container_width=True)