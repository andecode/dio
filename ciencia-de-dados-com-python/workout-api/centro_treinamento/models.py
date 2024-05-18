from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_columnn, relationship
from workout_api.contribut.models import BaseModel

class CentroTreinamentoModel(baseModel):
    __tablename__ = 'centros_treinamento'

    pk_id: Mapped[int] = mapped_columnn(Integer, primary_key=True)
    nome: Mapped[str] = mapped_columnn(String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_columnn(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_columnn(String(30), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='centros_treinamento')