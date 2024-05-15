from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=10)]