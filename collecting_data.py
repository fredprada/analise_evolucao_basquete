import pandas as pd

def treated_data():
    # reading the data
    global df_raw
    arquivo_base = "dataset_compras.xlsx - Sheet1.csv"
    df_raw = pd.read_csv(arquivo_base)

    return df_raw