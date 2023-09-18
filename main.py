from fastapi import FastAPI
import pandas as pd

app = FastAPI()

#uvicorn main:app --reload
#http://127.0.0.1:8000

#git status
#git add ""
#git commit -m ""
#git push origin main


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



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

@app.get("/genre/")
async def genre(genero:str):
    '''Devuelve el puesto en el que se encuentra un género sobre el ranking de los mismos 
    analizado bajo la columna PlayTimeForever.'''
    try:
        df = pd.read_json("DataSets/df_genre.json", lines=True)
        genero = genero.lower()  # Convertir a minúsculas

        # Verifico si el género existe
        if df[df['genres'] == genero].empty:
            return {"error": f"No se encontraron resultados para el género '{genero}'."}

        result = df['ranking'][df['genres'] == genero].iloc[0]
        return {"Genero": genero, "Ranking": result}
    except Exception as e:
        return {"error": str(e)}
    

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

@app.get("/userforgenre/")
async def userforgenre(genero:str):
    
    '''Esta funcion devuelve el top 5 de usuarios con más horas de juego 
    en el género dado, con su URL (del user) y user_id'''

    try:
        df = pd.read_json("DataSets/df_userforgenre.json", lines=True)
        genero = genero.lower()  # Convierto a minúsculas
        ranking = df[['ranking']][df['genres']==genero]
        user = df[['user_id']][df['genres']==genero]
        url = df[['user_url']][df['genres']==genero]
        
        # Verifico si el genero existe
        if ranking.empty or user.empty or url.empty:
            return {"error": f"No se encontraron resultados para el género '{genero}'."}
        
        # Creao un diccionario con los resultados
        resultados = {
            "Ranking": ranking.values.tolist(),
            "User_ID": user.values.tolist(),
            "User_URL": url.values.tolist()
                    }
        return resultados
    
    except Exception as e:
        return {"error": str(e)}
