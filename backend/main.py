from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import listar_jogadores, listar_favoritos, adicionar_favorito, remover_favorito

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/jogadores")
def jogadores():
    return listar_jogadores()

class FavoritoInput(BaseModel):
    jogador_id: int

@app.post("/api/favoritos")
def  favoritar(favorito: FavoritoInput):
    adicionar_favorito(favorito.jogador_id)
    return {"message": "Jogador adicionado aos favoritos."}

@app.delete("/api/favoritos/{jogador_id}")
def desfavoritar(jogador_id: int):
    remover_favorito(jogador_id)
    return {"message": "Jogador removido dos favoritos."}

@app.get("/api/favoritos")
def favoritos():
    return listar_favoritos()