from pydantic import BaseModel, Field, ConfigDict

class MedicamentoCreate(BaseModel):
    nombre: str = Field(min_length=1, max_length=120)
    principio_activo: str = Field(min_length=1, max_length=120)
    presentacion: str = Field(min_length=1, max_length=100)
    cantidad_disponible: int = Field(ge=0)
    categoria: str = Field(min_length=1, max_length=80)

class MedicamentoResponse(MedicamentoCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
