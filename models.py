from sqlalchemy import Column, Integer, String
from database import Base

class Medicamento(Base):
    __tablename__ = "medicamentos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False, index=True)
    principio_activo = Column(String(120), nullable=False)
    presentacion = Column(String(100), nullable=False)
    cantidad_disponible = Column(Integer, nullable=False, default=0)
    categoria = Column(String(80), nullable=False, index=True)
