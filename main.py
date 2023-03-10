from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from models import Pessoa

app = FastAPI()

db: List[Pessoa] = [
	Pessoa(
		id=UUID("3e0d828d-edcf-4270-b267-30dc015f8aa2"), 
      	nome = "Matheus",
     	cpf = "100.200.300-40", 
      	cep = "10020500",
		)
]


@app.post("/pessoas")
async def criar_pessoa(pessoa: Pessoa):
	if len(pessoa.cpf)!= 14 :
		raise HTTPException(
			status_code=404,
			detail=f"O cpf tem que ter 14 dígitos"
		)
	elif len(pessoa.cep) != 8:
		raise HTTPException(
			status_code=404,
			detail=f"O cep tem que ter 8 dígitos"
		)
	else:
		db.append(pessoa)
		return pessoa

@app.get("/pessoas")
async def ver_pessoas():
	return db

@app.get("/pessoas/{pessoa_id}")
async def ver_pessoa_por_id(pessoa_id: UUID):
	for pessoa in db:
		if pessoa.id == pessoa_id:
			return pessoa

@app.delete("/pessoas/{pessoa_id}")
async def deletar_pessoa(pessoa_id: UUID):
	for pessoa in db:
		if pessoa.id == pessoa_id:
			db.remove(pessoa)
			return
      	