import requests
import pandas as pd
import os

# função pra conectar na API do notion
def get_dados_notion(token, database_id):
    url = f'https://api.notion.com/v1/databases/{database_id}/query'
    r = requests.post(url, headers={
        'Authorization': f'Bearer {token}',
        'Notion-Version': '2021-08-16'
        })
    result_dict = r.json()
    return result_dict

# função para tratamento básico dos dados coletados
def first_treatment(dados_coletados):
    global df_evolucao
    lista_dias = []
    for item in range(0, len(dados_coletados['results'])):
        dia = dados_coletados['results'][item]['properties']['dia']['date']['start']
        nota = dados_coletados['results'][item]['properties']['nota']['number']
        pai = dados_coletados['results'][item]['properties']['pai']['number']
        calorias = dados_coletados['results'][item]['properties']['calorias']['number']
        tempo_jogado = dados_coletados['results'][item]['properties']['tempo jogado (min)']['number']
        animo_pra_jogar = dados_coletados['results'][item]['properties']['animo pra jogar']['number']
        sentimento_do_dia = dados_coletados['results'][item]['properties']['sentimento no dia']['select']['name']
        lista_dias.append({'dia':dia, 
                           'nota':nota, 
                           'pai':pai, 
                           'calorias':calorias, 
                           'tempo_jogado':tempo_jogado,
                           'animo_pra_jogar':animo_pra_jogar,
                           'sentimento_do_dia':sentimento_do_dia})
    df_evolucao = pd.DataFrame(lista_dias)
    return df_evolucao

# credenciais para acessar API
token = os.getenv('NOTION_BASQUETE_TOKEN')
database_id = os.getenv('NOTION_DATABASE_ID')

# chamando funções de coleta e tratamento dos dados
def raw_data(token, database_id):
    global df_raw_data
    dados_coletados = get_dados_notion(token, database_id)
    df_raw_data = first_treatment(dados_coletados)

    return df_raw_data