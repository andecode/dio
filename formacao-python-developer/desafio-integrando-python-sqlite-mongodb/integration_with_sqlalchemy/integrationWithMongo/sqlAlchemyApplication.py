from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "cliente_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="Cliente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname}"
class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_adress = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("cliente_account.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="address")

    def __repr__(self):
        return f"Address (id={self.id}, email_address={self.email_adress})"


print(Cliente.__tablename__)
print(Address.__tablename__)

# Conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de daddos
Base.metadata.create_all(engine)

# investiga o esquema do banco de dados
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("cliente_account"))

print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    anderson = Cliente(
        name='anderson',
        fullname='Anderson Martins',
        address=[Address(email_address='andersonm@email.com')]
    )

    maria = Cliente(
        name='maria',
        fullname='Maria Jose',
        address=[Address(email_address='mariajose@email.com'),
                 Address(email_address='mariajo@email.org')]
    )

    patrick = Cliente(name='alberto', fullname='alberto souza')

    # enviando para o BD (persistência de dados)
    session.add_all([anderson, maria, alberto])

    session.commit()
