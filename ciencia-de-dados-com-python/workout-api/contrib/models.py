from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    id: Mapped[UUID] =  mapped_columnn[PG_UUID(as_uuid=True),  default=uuid4, nullable=False]