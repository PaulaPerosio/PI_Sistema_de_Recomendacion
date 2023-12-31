from fastapi import FastAPI
import pandas as pd
import numpy as np


app = FastAPI(title='Información y recomendación de video juegos',
            description='Proyecto individual 1: Machine Learning Operations (MLOps), by: Paula Perosio')


@app.get("/")
async def Inicio():
    return {"API de video juegos. Coloque '/docs' en la barra de direcciones y luego presione enter"}

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.get("/userdata/")
async def userdata(user_id : str ):
    '''Devuelve la cantidad de dinero gastado, el porcentaje de recomendación
    y la cantidad de juegos consumidos por el usuario ingresado'''

    try:
        df_1 = pd.read_json("DataSets/df_user_price.json", lines=True)
        dinero_gastado = df_1['price'][df_1['user_id']==user_id]

        df_2 = pd.read_json("DataSets/df_porc_recomm.json", lines=True)
        recomendacion = df_2['Recomendacion'][df_2['user_id']==user_id]

        df_3 = pd.read_json("DataSets/df_item_user_group.json", lines=True)
        cantidad_item_id = df_3['Cantidad_item_id'][df_3['user_id']==user_id]

        # Verifico si el genero existe
        if dinero_gastado.empty or recomendacion.empty or cantidad_item_id.empty:
            return {"error": f"No se encontraron resultados para el usuario '{user_id}'."}

        resultado = {
                     "Usuario": user_id,
                     "Dinero gastado": float(dinero_gastado.iloc[0]),
                     "Porcentaje de recomendacion": float(recomendacion.iloc[0]),
                     "Cantidad de items": int(cantidad_item_id.iloc[0])
                    }

        return resultado

    except Exception as e:
        return {"error": str(e)}

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.get("/countreviews/")
async def countReviews(fecha_inicio_str: str, fecha_fin_str: str):
    '''Devuelve la cantidad de usuarios que realizaron reseñas y 
    su porcentaje de recomendación; entre las fechas ingresadas'''

    try:
        df = pd.read_json("DataSets/df_countreviews.json", lines=True)

        # Verifica el formato 'aaaa-mm-dd'
        if not fecha_inicio_str.count('-') == fecha_fin_str.count('-') == 2:
            return {"error": "El formato de fecha es incorrecto. Debe ser YYYY-MM-DD."}
        
        # Verifico si las fechan existen
        if df[df['posted_ok'] == fecha_inicio_str].empty:
            return {"error": f"La fecha '{fecha_inicio_str}' de inicio no existe."}
        
        if df[df['posted_ok'] == fecha_fin_str].empty:
            return {"error": f"La fecha '{fecha_fin_str}' de fin no existe."}

        condicion = (df['posted_ok'] >= fecha_inicio_str) & (df['posted_ok'] <= fecha_fin_str)
        recomendacion = df[condicion][df[condicion]['recommend']==1].shape[0]
        porc_recomendacion = recomendacion / df[condicion].shape[0] * 100

        resultado = {
                     "Cantidad de usuarios": df[condicion].shape[0],
                     "Porcentaje de recomendación": round(porc_recomendacion, 2)
                    }
        
        return resultado

    except Exception as e:
        return {"error": str(e)}


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.get("/genre/")
async def genre(genero:str):
    '''Devuelve el puesto en el que se encuentra el género ingresado 
    en comparación con los demás géneros 
    en función a la cantidad de horas que han sido jugadas'''
    
    try:
        df = pd.read_json("DataSets/df_genre.json", lines=True)
        genero = genero.lower()  # Convertir a minúsculas

        # Verifico si el género existe
        if df[df['genres'] == genero].empty:
            return {"error": f"No se encontraron resultados para el género '{genero}'."}

        result = df['ranking'][df['genres'] == genero]

        resultados = {
            "Genero": genero,
            "Ranking": result.shape[0]
                    }
        return resultados
    
    except Exception as e:
        return {"error": str(e)}
    

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.get("/userforgenre/")
async def userforgenre(genero:str):
    '''Devuelve un top 5 de usuarios y su URL en función 
    a la cantidad de horas de juego en el género dado'''

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
    
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.get("/developer/")
async def developer(desarrollador:str):
    '''Devuelve la cantidad de juegos y el porcentaje de contenido Free por año 
    de la empresa desarrolladora ingresada'''

    try:
        df = pd.read_json("DataSets/df_developer.json", lines=True)
        desarrollador = desarrollador.lower()  # Convierto a minúsculas
        
        # Filtro el DF por desarrollador y verifico si el desarrollador existe
        df_filtrado = df[df['developer'] == desarrollador]

        if df_filtrado.empty:
            return {"error": f"No se encontraron resultados para el desarrollador '{desarrollador}'."}
        
        # Agrupo por año y cuento los registros
        registros = df_filtrado.groupby('año')['item_id'].count().reset_index(name='cantidad_item')
        
        # Cuento los registros donde el precio = cero
        free = df_filtrado[df_filtrado['price'] == 0.0].groupby('año')['price'].count().reset_index(name='contenido_free')
        
        # Combino ambos DataFrames
        resultados = registros.merge(free, on='año', how='left')
        
        # Calculo el porcentaje de contenido gratuito
        resultados['porcentaje_free'] = (resultados['contenido_free'] / resultados['cantidad_item']) * 100
        
        # Si no hay valores price, le ongo cero
        resultados['porcentaje_free'].fillna(0, inplace=True)
        
        # Diccionario de resultados
        resultados_dict = {
            "Año": resultados['año'].tolist(),
            "Cantidad de Items": resultados['cantidad_item'].tolist(),
            "Porcentaje de contenido Free": resultados['porcentaje_free'].tolist()
        }
        return resultados_dict
    
    except Exception as e:
        return {"error": str(e)}

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.get("/sentiment_analysis/")
async def sentiment_analysis(año_str:str):
    '''Devuelve la cantidad de reseñas de usuarios positivas, negativas y neutras  
        según el año de lanzamiento'''

    try:
        # Convierto el año a entero
        año = int(año_str)
        
        df = pd.read_json("DataSets/df_sentiment.json", lines=True)
        
        # Verifico que el año este en el DataFrame
        if año not in df['ano'].unique():
            return {"error": f"No se encontraron registros para el año {año}"}

        negativos = int(df['cantidad_0'][df['ano']==año].iloc[0])
        neutros = int(df['cantidad_1'][df['ano']==año].iloc[0])
        positivos = int(df['cantidad_2'][df['ano']==año].iloc[0])

        return {"Negativos": negativos, "Neutros": neutros, "Positivos" : positivos}
    
    except Exception as e:
        return {"error": str(e)}
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.get("/recomendacion_juego/")
async def recomendacion_juego(item_id:int):
    ''' Devuelve una recomendación de 5 juegos similares al juego/item ingresado'''

    try:
        df = pd.read_json("DataSets/df_modelo.json")

        # Verifico que el item este en el DataFrame
        if item_id not in df.index:
            return {"error": f"No se encontraron registros para el item {item_id}"}

        columnas = df.columns.tolist()

        # Determino las caracteristicas relevantes de cada item
        caracteristicas = df[columnas].values
        # Determino las caracteristicas del item ingresado
        caract_item = df[df.index == item_id].values[0]

        # Calculo la similitud del coseno con los otros items
        similitudes = np.dot(caracteristicas, caract_item) / (np.linalg.norm(caracteristicas, axis=1) * 
                                                            np.linalg.norm(caract_item))
        
        # agrego al df una columna que indique las similitudes de cada item con el item ingresado
        df['Similitudes'] = similitudes

        # Ordeno los items por similitud en orden descendente
        df = df.sort_values(by='Similitudes', ascending=False)

        return {"Juegos similares recomendados": df.index[1:6].tolist()}
    
    except Exception as e:
        return {"error": str(e)}