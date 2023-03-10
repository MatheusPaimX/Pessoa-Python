from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

class Pessoa(BaseModel):
    id: Optional[UUID] = uuid4()
    nome: str
    cpf: str
    cep: str
    