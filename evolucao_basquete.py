import requests
import pandas as pd
import json
import os

def get_dados_notion():
    token = os.environ["token"]
    database_id = os.environ["database_id"]

    url = f'https://api.notion.com/v1/databases/{database_id}/query'
    
    r = requests.post(url, headers={
        'Authorization': f'Bearer {token}',
        'Notion-Version': '2021-08-16'
        })
    result_dict = r.json()
    return result_dict

dados_coletados = get_dados_notion()

def treated_data():
    global df_evolucao
    df_evolucao = pd.DataFrame(columns=['dia','nota','pai','calorias','tempo_jogado'])
    lista_dias = []
    for item in range(0,len(dados_coletados)-1):
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
    df_evolucao = df_evolucao.append(lista_dias, ignore_index=False)
    return df_evolucao
