from fastapi import FastAPI
from pydantic import BaseModel

class Livro(BaseModel):
    titulo: str
    autor: str
    data_lancamento: int

app = FastAPI()

dicionario = {}

@app.get("/livros")
def listar_livros():
    return dicionario

@app.post("/adicionar_livros")
def add_livro(id: int, livro: Livro):
    dicionario[id] = livro.model_dump()
    return {
        "retorno": "Livro adicionado",
        "livro": livro[id]
    }

@app.put("/atualizar_livros/{id}")
def atualizar_livros(id: int, livro: Livro):
    dicionario[id] = livro.model_dump()
    return {
        "retorno": "Livro atualizado",
        "livro": livro[id]
    }

@app.delete("/deletar_livros/{id}")
def deletar_livros(id: int):
    dicionario.pop(id)