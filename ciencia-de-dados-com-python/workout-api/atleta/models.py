from datetime import datetime
from sqlalchemy import Datetime, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_columnn, relationship
from workout_api.contribut.models import BaseModel

class AtletaModel(baseModel):
    __tablename__ = 'atletas'

    pk_id: Mapped[int] = mapped_columnn(Integer, primary_key=True)
    nome: Mapped[str] = mapped_columnn(String(50), nullable=False)
    cpf: Mapped[str] = mapped_columnn(String(11), nullable=False)
    idade: Mapped[int] = mapped_columnn(Integer, nullable=False)
    peso: Mapped[float] = mapped_columnn(Float, nullable=False)
    altura: Mapped[float] = mapped_columnn(Float, nullable=False)
    sexo: Mapped[str] = mapped_columnn(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_columnn(Datetime.nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
    categoria_id = Mapped[int] = mapped_columnn(ForeignKey('Categorias.pk_id'))
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta')
    centro_treinamento_id = Mapped[int] = mapped_columnn(ForeignKey('centro_treinamento.pk_id'))
