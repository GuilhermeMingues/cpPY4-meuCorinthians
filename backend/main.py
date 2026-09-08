from fastapi import FastAPI
from database import listar_jogadores

app = FastAPI()

@app.get("/")
def raiz():
    return {"message": "Bem-vindo à API do meu-Corinthians!"}

@app.get("/api/jogadores")
def jogadores():
    return listar_jogadores()