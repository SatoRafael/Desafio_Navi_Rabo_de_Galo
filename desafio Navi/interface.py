import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd

st.set_page_config(page_title="E-Cred", page_icon =":zap:", layout='wide')

# Funções

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Assets
lottie_1 = load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_8xw4cfyj.json')
lottie_2 = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_fgvoshwe.json')
lottie_3 = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_qwATcU.json')

# Cabeçalho
with st.container():
    st.subheader("E-Cred")
    st.title("Vantagens para o consumidor e produtor de energia.")
    st.write()
    st.write("[Learn More >](https://www.ccee.org.br/mercado/medicao)")

# Escopo
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Consumidor")
        st.write("##")
        st.write(
            """
            Vantagens:
            
             - Proteção e segurança financeira;
             - Estimulo na produção de energia verde;
             - Menor pegada de carbono;
             - Maior segurança elétrica;
             - Promove melhoria nos projetos de infraestrutura de distribuição;
            """
        )
    with right_column:
        st_lottie(lottie_1, height = 300, key='energy')

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_2, height = 300, key='painel')

    with right_column:
        st.header("Gerador Distribuído")
        st.write('##')
        st.write(
            """
            Vantagens:

            - Tokenização do excesso de energia produzido;
            - Maior liquidez;
            - Menor risco no vencimento de crédito;
            - Estimulo na maior produção de energia verde; 
            """
        )

with st.container():
    st.write("---")
    st.header("Projeto")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st_lottie(lottie_3, height = 200, key='business')
    with text_column:
        st.subheader("Modelo de Negócios")
        st. write(
            """
            [Aprenda mais a fundo como funciona o E-Credit:](https://www.youtube.com/watch?v=fH7gbibd9fI)


            """
        )



df = pd.read_excel("RankingB1-23-12-2021.xlsx") 


st.write("---")
st.title("""
          
          Calcule seus créditos disponíveis:""")

dist = list(df['Distribuidora'].unique())

with st.container():
    prod = st.slider("Produção (em kWh): ", min_value=0, max_value=1000, value=0, step=10)
    produzido = int(prod)
    
    horas = st.slider("Quantidade de horas: ", min_value=0, max_value=720, value=0, step=10)
    horario = int(horas)
    
    local = st.selectbox('Selecione sua distribuidora local:', dist)

    #periodo = st.selectbox('Qual o horário da produção?', ['Ponta', 'Intermediário', 'Fora'])

    if(st.button('Calcular créditos')):
        
        def calculo_credito(produzido,local,horario): ##Caso o cálculo seja feito para PJ, será necessário adicionar o período na função
            df_lp = df[df['Distribuidora']==local]
            res = produzido*horario*df_lp['Tarifa Convencional']
            return res.iloc[0]
        
        valor = calculo_credito(produzido,local,horario)
        st.write('Quantidade de créditos: ', round(valor,2))

    else: 
        st.write('Quantidade de créditos:')

    st.subtitle('Quais são as melhores taxas do país?')
    
    df_grouped = df.groupby(['UF']).mean().reset_index()
    del df_grouped['Ranking']
    dfs = df_grouped.sort_values('Tarifa Convencional').head(5)
    dft = df_grouped.sort_values('Tarifa Convencional').tail(5)

    dfgr = dfs.append(dft)
    #dfs.plot(x='UF', y=['Tarifa Convencional'], kind="bar")
    ax = sns.barplot(x="UF", y="Tarifa Convencional", data=dfgr)
    plt.show()
    #ax.bar_label(ax.containers[0])

    

st.write("---")
st.title("""
          
          Quer comprar créditos? Veja abaixo:""")
          
with st.container():
    vendedor = {'UF':['SP','RJ'],
                'Distribuidora':['Cedrap', 'Ceres'],
                'Quantidade disponível':[2321.34,765.34],
                'Período (dias)':[90,90],
                'Tipo de Produtor':['Pessoa Física','Pessoa Física']
                }
    tab_venda = pd.DataFrame(vendedor)
    st.dataframe(tab_venda)
    
    st.write('Para efetuar a compra e venda de créditos, é necessário estar cadastrado.')
    st.write('Já possui conta? Entre abaixo:')
    
    st.text_input('Login:')
    st.text_input('Senha:')
    
    st.button('Login')
    
    st.write('Não possui conta ainda? [Cadastre-se aqui](https://www.instagram.com/fea.dev/)')
