from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_columnn, relationship
from workout_api.contribut.models import BaseModel

class CategoriaModel(baseModel):
    __tablename__ = 'Categorias'

    pk_id: Mapped[int] = mapped_columnn(Integer, primary_key=True)
    nome: Mapped[str] = mapped_columnn(String(50), unique=True, nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')