from fastapi import FastAPI
import pandas as pd

app = FastAPI()

#uvicorn main:app --reload
#http://127.0.0.1:8000

@app.get("/")
async def ruta_prueba():
    return {"Hola":"Chau"}


@app.get("/prueba/{id}")
async def ruta_prueba_2(id:int):
    return {"Hola":"chau",
            "pruebaaaaaa" : id}


@app.get("/hola/{id}")
async def ruta_prueba_2(id:int):
    return {"HolAAAAAAAAAAAa": id}


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

@app.get("/countreviews/")
async def countReviews(fecha_inicio_str: str, fecha_fin_str: str):
    '''Esta funcion devuelve la cantidad de usuarios que realizaron reviews entre las fechas dadas y,
    el porcentaje de recomendación de los mismos en base a reviews.recommend'''

    try:
        df = pd.read_json("DataSets/df_countreviews.json", lines=True)
    except Exception as e:
        return {"error": f"No se pudo leer el archivo JSON. Detalles: {e}"}

    if not fecha_inicio_str.count('/') == fecha_fin_str.count('/') == 2:
        return {"error": "El formato de fecha es incorrecto. Debe ser YYYY/MM/DD."}

    partes_inicio = fecha_inicio_str.split('/')
    partes_fin = fecha_fin_str.split('/')

    if not all(part.isdigit() for part in partes_inicio + partes_fin):
        return {"error": "Las fechas deben contener solo números."}

    if not (len(partes_inicio[0]) == len(partes_fin[0]) == 4 and 
            len(partes_inicio[1]) == len(partes_fin[1]) == 2 and 
            len(partes_inicio[2]) == len(partes_fin[2]) == 2):
        return {"error": "Las fechas deben estar en el formato YYYY/MM/DD."}

    condicion = (df['posted_ok'] >= fecha_inicio_str) & (df['posted_ok'] <= fecha_fin_str)
    recomendacion = df[condicion][df[condicion]['recommend']==True].shape[0]
    porc_recomendacion = recomendacion / df[condicion].shape[0] * 100

    return {"Cantidad de usuarios": df[condicion].shape[0], "Porcentaje de recomendación": round(porc_recomendacion, 2)}



@app.get("/sentiment_analysis/{año}")
async def sentiment_analysis(año:int):
    
    '''Esta funcion devuelve una lista con la cantidad de registros de reseñas de usuarios 
    que se encuentren categorizados con un análisis de sentimiento según el año de lanzamiento.
        Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}'''
    try:
        df = pd.read_json("DataSets/df_sentiment.json", lines=True)
        negativos = int(df['cantidad_0'][df['ano']==año].iloc[0])
        neutros = int(df['cantidad_1'][df['ano']==año].iloc[0])
        positivos = int(df['cantidad_2'][df['ano']==año].iloc[0])

        return {"Negativos ": negativos, "Neutros": neutros, "Positivos" : positivos}
    except Exception as e:
        return {"error", e}
