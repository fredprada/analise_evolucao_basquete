import os
import streamlit as st
from pymongo import MongoClient
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import datetime
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from calendar import monthrange
from datetime import timezone, timedelta

######################################################################################################################################
def connect_to_mongodb():
    """
    Function to connect to mongoDB.
    """
    global collection
    client = os.getenv('CLIENT_TOKEN')
    myclient = MongoClient(client)
    db = myclient.get_database('db_evolucao_basquete')
    collection = db.collection_evolucao_basquete
    return collection

######################################################################################################################################
def database_insertion(list_to_add):
    """
    Function to insert the information that the player have put on the forms.
    """
    connect_to_mongodb()
    st.sidebar.text('Inserção em progresso')
    collection.insert_many(list_to_add)

# ######################################################################################################################################
# def database_deletion(id):
#     """
#     Function to delete a row from the database.
#     """
#     connect_to_mongodb()
#     collection.delete_one({ '_id' : f'ObjectId({id})'})

######################################################################################################################################
def retrieve_data_from_mongodb():
    """
    Function to get all information from mongodb.
    """
    collection = connect_to_mongodb()
    data_list = []
    data_list = [x for x in collection.find()]
    return data_list

######################################################################################################################################
def transform_to_dataframe():
    """
    Transforms the information collected from mongoDB into a dataframe to be displayed.
    """
    data_list = retrieve_data_from_mongodb()
    df_data_list = pd.DataFrame(data_list)
    return df_data_list

######################################################################################################################################
def data_transformation(dataframe):
    """
    Edit the columns, create new metrics and separate into new dataframes
    """
    global dict_df_data_list
    # Transforming all empty into nan
    dataframe_transf = dataframe.fillna(value=np.nan)

    # Editing the types of the columns
    dataframe_transf['dia'] = dataframe_transf['dia'].astype('datetime64[ns]')
    dataframe_transf['hora_do_jogo'] = pd.to_datetime(dataframe_transf['hora_do_jogo'], errors='coerce').dt.time
    dataframe_transf['tempo_de_descanso'] = pd.to_numeric(dataframe_transf['tempo_de_descanso'], errors='coerce')
    dataframe_transf['nota'] = pd.to_numeric(dataframe_transf['nota'], errors='coerce')
    dataframe_transf['pai'] = pd.to_numeric(dataframe_transf['pai'], errors='coerce')
    dataframe_transf['calorias'] = pd.to_numeric(dataframe_transf['calorias'], errors='coerce')
    dataframe_transf['tempo_jogado'] = pd.to_numeric(dataframe_transf['tempo_jogado'], errors='coerce')
    dataframe_transf['animo_pra_jogar'] = pd.to_numeric(dataframe_transf['animo_pra_jogar'], errors='coerce')

    # Creating new metric "calorias_por_min"
    dataframe_transf['calorias_por_min'] = dataframe_transf['calorias']/dataframe_transf['tempo_jogado']

    # Creating a new column with the week number
    dataframe_transf['numero_da_semana'] = dataframe_transf['dia'].apply(lambda x: datetime.date.isocalendar(x)[1])

    # Separating into the player's dataframe_transfs
    df_data_list_fred = dataframe_transf.query('jogador == "Fred"').sort_values(by='dia', ascending=False)
    df_data_list_bia = dataframe_transf.query('jogador == "Bia"').sort_values(by='dia', ascending=False)
    dict_df_data_list = {}
    dict_df_data_list['Bia'] = df_data_list_bia
    dict_df_data_list['Fred'] = df_data_list_fred
    return dict_df_data_list

######################################################################################################################################
def main_metrics(dataframe, player):
    today = datetime.datetime.now() - datetime.timedelta(hours=3)
    current_week = datetime.date.isocalendar(today)[1]

    if player == 'Fred':
        dict_df_data = data_transformation(dataframe)
        specific_dataframe = dict_df_data['Fred']
    elif player == 'Bia':
        dict_df_data = data_transformation(dataframe)
        specific_dataframe = dict_df_data['Bia']
    
    ######################################################################################################################################
    # Games played
    qtd_de_jogos = len(specific_dataframe['dia'])

    df_current_week = specific_dataframe[specific_dataframe['numero_da_semana'] == current_week]
    jogos_essa_semana = len(df_current_week)

    df_last_week = specific_dataframe[specific_dataframe['numero_da_semana'] == current_week - 1]
    jogos_semana_passada = len(df_last_week)

    jogos_por_semana = pd.DataFrame(specific_dataframe['numero_da_semana'].value_counts())
    jogos_por_semana = jogos_por_semana.reset_index()
    jogos_por_semana = jogos_por_semana.rename(columns={'numero_da_semana':'numero_da_semana','count':'qtd'})
    jogos_por_semana = jogos_por_semana.sort_values(by='numero_da_semana')

    ######################################################################################################################################
    # Adicionando métricas no dicionário de métricas
    dict_metricas = {}
    dict_metricas['qtd_de_jogos'] = qtd_de_jogos
    dict_metricas['jogos_essa_semana'] = jogos_essa_semana
    dict_metricas['jogos_semana_passada'] = jogos_semana_passada
    dict_metricas['jogos_por_semana'] = jogos_por_semana

    return dict_metricas

######################################################################################################################################
def get_numeric_stats(dataframe, player):
    today = datetime.datetime.now() - datetime.timedelta(hours=3)
    current_week = datetime.date.isocalendar(today)[1]

    if player == 'Fred':
        dict_df_data = data_transformation(dataframe)
        specific_dataframe = dict_df_data['Fred']
    elif player == 'Bia':
        dict_df_data = data_transformation(dataframe)
        specific_dataframe = dict_df_data['Bia']

    def calculo_numeric_stats(df, lista_metricas_numericas):
        dict_metric_stats = {}
        df_cleaned = df.dropna(subset=lista_metricas_numericas)

        for metrica in lista_metricas_numericas:
            metrica = str(metrica)
            metric_soma = sum(df[metrica])
            metric_soma_essa_semana = sum(df.query(f'numero_da_semana == {current_week}')[metrica])
            metric_soma_semana_passada = sum(df.query(f'numero_da_semana == {current_week-1}')[metrica])
            metric_media = round(df[metrica].mean(), 1)
            metric_media_essa_semana = round(df.query(f'numero_da_semana == {current_week}')[metrica].mean(), 1)
            metric_media_semana_passada = round(df.query(f'numero_da_semana == {current_week-1}')[metrica].mean(), 1)
            metric_max = df[metrica].max()
            metric_max_essa_semana = df.query(f'numero_da_semana == {current_week}')[metrica].max()
            metric_max_semana_passada = df.query(f'numero_da_semana == {current_week-1}')[metrica].max()
            metric_max_index = df[metrica].idxmax()
            metric_max_dia = df.loc[metric_max_index, 'dia'].date().strftime('%d/%m/%Y')
            metric_min = df_cleaned[metrica].min()
            metric_min_essa_semana = df.query(f'numero_da_semana == {current_week}')[metrica].min()
            metric_min_semana_passada = df.query(f'numero_da_semana == {current_week-1}')[metrica].min()
            metric_min_index = df_cleaned[metrica].idxmin()
            metric_min_dia = df.loc[metric_min_index, 'dia'].date().strftime('%d/%m/%Y')

            dict_metric_stats[metrica] = {
                f'{metrica}_soma': metric_soma,
                f'{metrica}_soma_essa_semana': metric_soma_essa_semana,
                f'{metrica}_soma_semana_passada': metric_soma_semana_passada,
                f'{metrica}_media': metric_media,
                f'{metrica}_media_essa_semana': metric_media_essa_semana,
                f'{metrica}_media_semana_passada': metric_media_semana_passada,
                f'{metrica}_max': metric_max,
                f'{metrica}_max_essa_semana': metric_max_essa_semana,
                f'{metrica}_max_semana_passada': metric_max_semana_passada,
                f'{metrica}_max_dia': metric_max_dia,
                f'{metrica}_min': metric_min,
                f'{metrica}_min_essa_semana': metric_min_essa_semana,
                f'{metrica}_min_semana_passada': metric_min_semana_passada,
                f'{metrica}_min_dia': metric_min_dia
            }

        return dict_metric_stats

    lista_metricas_numericas = ['pai', 'nota', 'calorias', 'tempo_jogado', 'animo_pra_jogar', 'tempo_de_descanso', 'calorias_por_min']
    dict_numeric_stats = {}
    result = calculo_numeric_stats(specific_dataframe, lista_metricas_numericas)
    dict_numeric_stats['specific_dataframe'] = result

    return dict_numeric_stats

######################################################################################################################################
def plotting_calendar_current_month(dataframe, player):
    today = datetime.datetime.now() - datetime.timedelta(hours=3)

    if player == 'Fred':
        dict_df_data = data_transformation(dataframe)
        specific_dataframe = dict_df_data['Fred']
    elif player == 'Bia':
        dict_df_data = data_transformation(dataframe)
        specific_dataframe = dict_df_data['Bia']

    def label_month(year, month, ax, i, j, cl="black"):
        months = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
        month_label = f"{months[month-1]} {year}"
        ax.text(i, j, month_label, color=cl, va="center")

    def label_weekday(ax, i, j, cl="black"):
        x_offset_rate = 1
        for weekday in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]:
            ax.text(i, j, weekday, ha="center", va="center", color=cl)
            i += x_offset_rate
            ax.add_patch(
                patches.Rectangle(
                (i - 1.5, j - 0.5),
                1,
                1,
                edgecolor="gray",
                facecolor="gray",
                alpha=0.1,
                fill=True,
                )
            )

    def label_day(ax, day, i, j, cl="black"):
        ax.text(i, j, int(day), ha="center", va="center", color=cl)

    def pintar_dias_jogados(ax, i, j):
        ax.add_patch(
            patches.Rectangle(
                (i - 0.5, j - 0.5),
                1,
                1,
                edgecolor="blue",
                facecolor="blue",
                alpha=0.1,
                fill=True,
            )
        )

    def pintar_dias_nao_jogados(ax, i, j):
        ax.add_patch(
            patches.Rectangle(
                (i - 0.5, j - 0.5),
                1,
                1,
                edgecolor="red",
                facecolor="yellow",
                alpha=0.1,
                fill=True,
            )
        )

    def check_dias_jogados(year, month, day, weekday):
        if (month, day) in lista_dias_jogados:
            return True

    def check_dias_nao_jogados(year, month, day, weekday):
        if (month, day) in lista_dias_nao_jogados_no_mes:
            return True

    def check_color_day(year, month, day, weekday):
        if weekday == 6:  # Sunday
            return "gray"
        if weekday == 5:  # Saturday
            return "gray"
        return "black"

    def month_calendar(ax, year, month, fill):
        date = datetime.datetime(year, month, 1)
        weekday, num_days = monthrange(year, month)
        # adjust by 0.5 to set text at the ceter of grid square
        x_start = 1 - 0.5
        y_start = 5 + 0.5
        x_offset_rate = 1
        y_offset = -1

        label_month(year, month, ax, x_start, y_start + 2)
        label_weekday(ax, x_start, y_start + 1)

        j = y_start

        for day in range(1, num_days + 1):
            i = x_start + weekday * x_offset_rate
            color = check_color_day(year, month, day, weekday)

            if fill and check_dias_jogados(year, month, day, weekday):
                pintar_dias_jogados(ax, i, j)

            if fill and check_dias_nao_jogados(year, month, day, weekday):
                pintar_dias_nao_jogados(ax, i, j)

            label_day(ax, day, i, j, color)
            weekday = (weekday + 1) % 7
            if weekday == 0:
                j += y_offset

    def main(year, month, grid=True, fill=True):
        fig = go.Figure()
        ax = fig.add_subplot()
        ax.axis([0, 7, 0, 7])
        ax.axis("off")

        if grid:
            ax.axis("on")
            ax.grid(grid)
            for tick in ax.xaxis.get_major_ticks():
                tick.tick1line.set_visible(False)
                tick.tick2line.set_visible(False)
                tick.label1.set_visible(False)
                tick.label2.set_visible(False)
            for tick in ax.yaxis.get_major_ticks():
                tick.tick1line.set_visible(False)
                tick.tick2line.set_visible(False)
                tick.label1.set_visible(False)
                tick.label2.set_visible(False)
        month_calendar(ax, year, month, fill)
        
        # Convert the figure to a NumPy array
        image_array = pio.to_image(fig, format="png")
        return image_array

    if __name__ == "__main__":
        today = datetime.datetime.now() - datetime.timedelta(hours=3)
        
        # Pegando só os dias jogados de todos os meses
        lista_dias_jogados = [(i.date().month, i.date().day) for i in specific_dataframe['dia']]
        # Pegando só os dias não jogados no mês atual
        start_of_month = datetime.date(today.year, today.month, 1)
        filtered_dates = [(index, date) for index, date in specific_dataframe['dia'].iteritems() if date.month == today.month]
        lista_dias_nao_jogados_no_mes = [(date.month, date.day) for date in pd.date_range(start_of_month, today) if date not in [date for _, date in filtered_dates]]
        year = datetime.date.today().year
        month = datetime.date.today().month

        # Generate the calendar as a NumPy array
        image_array = main(year, month, grid=True, fill=True)
    
    return image_array