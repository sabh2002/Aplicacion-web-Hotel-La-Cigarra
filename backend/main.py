from fastapi import FastAPI
from routes.rutas_reservacion import reservacion

app = FastAPI()

app.include_router(reservacion)

@app.get('/')
async def inicio():
    return 'Pagina Principal'