import pandas as pd
import plotly.express as px
import os
import sklearn
from sklearn.preprocessing import MinMaxScaler
from coleta_de_dados import get_dados_notion, first_treatment

# credenciais para acessar API
token = os.getenv('NOTION_BASQUETE_TOKEN')
database_id = os.getenv('NOTION_DATABASE_ID')

# chamando as funções para retornar os dados raw
dados_coletados = get_dados_notion(token, database_id)
df_raw_data = first_treatment(dados_coletados)

def transform_data(df_raw_data):
    # corrigindo a data para datetime
    df_raw_data['dia'] = df_raw_data['dia'].apply(pd.to_datetime)

    # criando df_raw_data_sorted
    df_raw_data_sorted = df_raw_data.sort_values(by = 'dia', ascending= True)

    # Criando nova coluna com os dias desde a última vez que joguei
    df_raw_data_sorted['dias_desde_ultimo_jogo'] = df_raw_data_sorted['dia'].diff().dt.days

    # criando coluna com conceito
    dict_conceito = {
        1:'0_baixa',
        2:'0_baixa',
        3:'0_baixa',
        4:'0_baixa',
        5:'1_media',
        6:'1_media',
        7:'2_boa',
        8:'2_boa',
        9:'3_excelente',
        10:'3_excelente'
    }
    df_raw_data_sorted['conceito'] = df_raw_data_sorted['nota'].map(dict_conceito)

    # definindo algumas métricas
    dias_jogados = df_raw_data_sorted.count()[0]

    # dias que tive jogos com nota baixa
    dias_jogados_nota_baixa = df_raw_data_sorted.query('conceito == "0_baixa"').count()[0]
    porcent_dias_jogados_nota_baixa = (dias_jogados_nota_baixa/dias_jogados)*100

    # dias que tive jogos com nota media
    dias_jogados_nota_media = df_raw_data_sorted.query('conceito == "1_media"').count()[0]
    porcent_dias_jogados_nota_media = (dias_jogados_nota_media/dias_jogados)*100

    # dias que tive jogos com nota boa
    dias_jogados_nota_boa = df_raw_data_sorted.query('conceito == "2_boa"').count()[0]
    porcent_dias_jogados_nota_boa = (dias_jogados_nota_boa/dias_jogados)*100

    # dias que tive jogos com nota excelente
    dias_jogados_nota_excelente = df_raw_data_sorted.query('conceito == "3_excelente"').count()[0]
    porcent_dias_jogados_nota_excelente = (dias_jogados_nota_excelente/dias_jogados)*100

    # normalização dos dados para análise
    df_normalized = df_raw_data_sorted.copy()
    cols_to_normalize = ['nota', 'pai', 'calorias', 'tempo_jogado', 'dias_desde_ultimo_jogo']
    scaler = MinMaxScaler()
    df_normalized[cols_to_normalize] = scaler.fit_transform(df_normalized[cols_to_normalize])
    df_normalized = pd.DataFrame(df_normalized)
    
    return df_raw_data_sorted, list[dias_jogados, 
                                    dias_jogados_nota_baixa, 
                                    porcent_dias_jogados_nota_baixa,
                                    dias_jogados_nota_media,
                                    porcent_dias_jogados_nota_media,
                                    dias_jogados_nota_boa,
                                    porcent_dias_jogados_nota_boa,
                                    dias_jogados_nota_excelente,
                                    porcent_dias_jogados_nota_excelente],df_normalized