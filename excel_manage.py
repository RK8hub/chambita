import pandas as pd


def inyectar():
    data_list = []
    df = pd.read_excel('data/Levantamiento.xlsx')
    for i in range(len(df)):
        data_row: list = df.iloc[i].to_list()
        for e in data_row:
            if isinstance(e,float):
                data_row[data_row.index(e)] = 'empty'
        data_list.append(data_row)
    return data_list

def json_to_excel(ruta_json,ruta_excel_new):
    import pandas as pd
    import json

    # 1. Abrir el archivo JSON
    with open(f'{ruta_json}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. Convertir a DataFrame
    df = pd.json_normalize(data)
    df.fillna("empty", inplace=True)

    # 3. Guardar a Excel
    df.to_excel(f'{ruta_excel_new}.xlsx', index=False)
