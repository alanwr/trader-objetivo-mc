# -*- coding: utf-8 -*-
# Commented out IPython magic to ensure Python compatibility.
#%writefile app.py 
import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Path settings
current_dir = Path(__file__).parent if "__file__" in locals() els Path.cwd()
logo = current_dir / "APP_MC" / "01 Logo_TO.png"

logo = Image.open(logo)


st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.image('logo')

st.title("Análise estatística")

# Adicionando o selectbox à sidebar
st.sidebar.title("Selecione o Trade System")
opcoes = ['BB - Fechou Fora, Fechou Dentro', 'Canal de Keltner', 'Cão Farejador', 'Cruzamento Di+ Di-', 'Cruzamento MMA 17x34', 'Dave Landry', 
'Estocástico Lento 70x30', 'Estocástico Lento 80x20', 'Gambitti', 'Gasparini', 'HiLo 7 períodos', 'IFR2 (Larry Connors)', 
'IFR2 com filtro IFR14', 'IFR4 (Larry Connors)', 'InsideBar', 'Joe Biden (com filtro MMA 20)', 'Joe Biden (sem filtros)', 
'Linha das sombras', 'Máximas e Mínimas', 'Medias 3 min/max ( Larry Williams)', 'Perdigão', 'Preço de Fechamento de Reversão', 
'Sistema MMA 9', 'Stop ATR 10 períodos', 'Terminator (Larry Connors)', 'Tik Tok (com filtro)', 'TikTok', 'Turtle' ]
opcao_selecionada = st.sidebar.selectbox("Escolha uma opção:", opcoes)

st.sidebar.title("Time Frame")
time_frame = st.sidebar.selectbox("Escolha o Time Frame", ["Diário", "60 m"])

# Adicionando campos de data
st.sidebar.title("Período")
data_inicio = st.sidebar.date_input("Data início")
data_fim = st.sidebar.date_input("Data término")

amostra = 200

# Atribuir a base de dados ao sistema operacional selecionado
if st.sidebar.button("EXECUTAR"):    
    if opcao_selecionada == "Sistema MMA 9":
        df = pd.read_excel('/APP_MC/gasparini.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Canal de Keltner":
        df = pd.read_excel('/content/APP_MC/D Canal de Keltner.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Cão Farejador":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Cao Farejador.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Cruzamento MMA 17x34":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Cruzamento MM 17 x 34.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Dave Landry":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Dave Landry.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Cruzamento Di+ Di-":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Di+Di-.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Estocástico Lento 80x20":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Estoc Lento 8p 8020.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Estocástico Lento 70x30":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Estocastico Lento 70 - 30.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "BB - Fechou Fora, Fechou Dentro":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Fechou Fora Fechou Dentro.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "HiLo 7 períodos":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D HiLo 7P.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "IFR2 com filtro IFR14":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D IFR2 25 IFR14 50.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "IFR2 (Larry Connors)":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D IFR2.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "IFR4 (Larry Connors)":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D IFR4.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "InsideBar":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D InsideBar.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Joe Biden (sem filtros)":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D JOE sem filtro.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Linha das sombras":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Linha da sombra.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Máximas e Mínimas":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Máximas e Mínimas.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Medias 3 min/max ( Larry Williams)":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Medias 3 Larry.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Perdigão":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Perdigão.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Preço de Fechamento de Reversão":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D PFR.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Stop ATR 10 períodos":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Stop ATR 10p.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Terminator (Larry Connors)":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Terminator.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Tik Tok (com filtro)":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Tik Tok Filtro Solar.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "TikTok":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D TikTok.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Turtle":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D Turtle.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Joe Biden (com filtro MMA 20)":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/D zJoe Biden.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Gambitti":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/Dz Gambitti 0,5.xlsx')
        amostra = int(df.shape[0] * 0.15)
    elif opcao_selecionada == "Gasparini":
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/Gasparini.xlsx')
        amostra = int(df.shape[0] * 0.15)

    else:
        df = pd.read_excel('C:/Users/alan/trade/APP_MC/gasparini.xlsx')

    st.sidebar.title(opcao_selecionada)
     # Mostrando a opção selecionada pelo usuário
    st.write("Sistema:", opcao_selecionada, "Time Frame:", time_frame , "Período de:", data_inicio, "até", data_fim)
    # código para configurar a df e fazer os cálculos
    # importa a tabela

    
    amostra1 = amostra + 1
    random_rows = df.sample(amostra)
    random_rows["Lucro Acumulado"] = random_rows["Lucro"].cumsum()
    random_rows['Contagem'] = range(1,amostra1)


    contagem_lucro_positivo = (random_rows["Lucro"] > 0).sum()
    media_lucro = df[df["Lucro"] > 0]["Lucro"].mean()
    media_prejuizo = df[df["Lucro"] < 0]["Lucro"].mean()
    payoff = media_lucro/-media_prejuizo
    tx_erro = 1-contagem_lucro_positivo/amostra
    exp_mat = (media_lucro * (1 - tx_erro) + media_prejuizo * tx_erro)/100
    expmat_total = exp_mat * amostra

    
    # Cálculo básico
    st.markdown("Taxa de acerto = **{:.2f}%**".format(round(contagem_lucro_positivo/amostra*100, 2)))
    st.markdown("PayOff = **{:.2f}**".format(round(payoff, 2)))
    st.markdown("Expectativa Matemática = **{:.2f}%** por trade".format(round(exp_mat, 2)))
    st.markdown("Expectativa Matemática Total = **{:.2f}%**".format(round(expmat_total, 2)))


    #calculando Drawdown
    random_rows["Lucro Acumulado"] = random_rows["Lucro"].cumsum()
    random_rows["Drawdown"] = random_rows["Lucro Acumulado"].cummin() - random_rows["Lucro Acumulado"]
    
    st.title("Curva de Capital")
    # plotando gráfico
    fig, ax = plt.subplots()
    ax.plot(random_rows['Contagem'], random_rows['Lucro Acumulado'])
    st.pyplot()
  
    # TESTE MONTE CARLO configuração do teste
    n_simulacoes = 100

    # cria um vetor para armazenar os resultados
    resultados = np.zeros((n_simulacoes, amostra))

    # loop para simulações
    for i in range(n_simulacoes):
        # gera amostras aleatórias
        random_rows = df.sample(amostra)
        random_rows["Lucro Acumulado"] = random_rows["Lucro"].cumsum()
       # armazena os resultados
        resultados[i, :] = random_rows["Lucro Acumulado"]
    st.title("Monte Carlo")
    # plotando gráfico
    plt.figure()
    plt.plot(resultados.T)
    
    st.pyplot()
    pass
