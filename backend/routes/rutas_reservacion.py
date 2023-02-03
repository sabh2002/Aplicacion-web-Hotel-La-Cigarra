from fastapi import APIRouter

reservacion = APIRouter()

@reservacion.get('/reservaciones')
async def reservaciones():
    return "Pagina de Reservaciones"