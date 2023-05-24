import requests
import pandas as pd
import json
import os

def get_dados_notion():

    token = os.environ.get('NOTION_BASQUETE_TOKEN')
    database_id = os.environ.get('NOTION_DATABASE_ID')
    # token = 'secret_bvnt24V0DBdNO0Ds83Id9PAa5Ls5PpiRv1KmcZBichf'
    # database_id = '8b5657acc52345d8af9bc77b8aba8cc3'

    url = f'https://api.notion.com/v1/databases/{database_id}/query'
    
    r = requests.post(url, headers={
        'Authorization': f'Bearer {token}',
        'Notion-Version': '2021-08-16'
        })
    result_dict = r.json()
    return result_dict

dados_coletados = get_dados_notion()

def treated_data(dados_coletados):
    global df_evolucao
    # df_evolucao = pd.DataFrame(columns=['dia','nota','pai','calorias','tempo_jogado'])
    lista_dias = []
    for item in range(0, len(dados_coletados['results'])):
        dia = dados_coletados['results'][item]['properties']['dia']['date']['start']
        nota = dados_coletados['results'][item]['properties']['nota']['number']
        pai = dados_coletados['results'][item]['properties']['pai']['number']
        calorias = dados_coletados['results'][item]['properties']['calorias']['number']
        tempo_jogado = dados_coletados['results'][item]['properties']['tempo jogado (min)']['number']
        lista_dias.append({'dia':dia, 
                           'nota':nota, 
                           'pai':pai, 
                           'calorias':calorias, 
                           'tempo_jogado':tempo_jogado})
    # df_evolucao = df_evolucao.append(lista_dias)
    df_evolucao = pd.DataFrame(lista_dias)
    return df_evolucao