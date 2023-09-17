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
            "pruebaaaaaaaaaaaaaaaaaa" : id}


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

        return {"Negativos": negativos, "Neutros": neutros, "Positivos" : positivos}
    except Exception as e:
        return {"error", e}
