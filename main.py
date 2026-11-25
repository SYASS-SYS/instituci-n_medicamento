from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import Base, engine, get_db
from models import Medicamento
from schemas import MedicamentoCreate, MedicamentoResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Farmacia",
    description="API para administrar los medicamentos ",
    version="1.0.0"
)

@app.get("/")
def inicio():
    return {"mensaje": "API de Farmacia funcionando"}

@app.post("/medicamentos", response_model=MedicamentoResponse, status_code=201)
def registrar_medicamento(datos: MedicamentoCreate, db: Session = Depends(get_db)):
    nuevo = Medicamento(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@app.get("/medicamentos", response_model=list[MedicamentoResponse])
def consultar_medicamentos(db: Session = Depends(get_db)):
    return db.query(Medicamento).order_by(Medicamento.id).all()


@app.get("/medicamentos/categoria/{categoria}", response_model=list[MedicamentoResponse])
def filtrar_por_categoria(categoria: str, db: Session = Depends(get_db)):
    return (
        db.query(Medicamento)
        .filter(func.lower(Medicamento.categoria) == categoria.lower())
        .order_by(Medicamento.id)
        .all()
    )

@app.get("/medicamentos/{medicamento_id}", response_model=MedicamentoResponse)
def consultar_medicamento(medicamento_id: int, db: Session = Depends(get_db)):
    medicamento = db.query(Medicamento).filter(Medicamento.id == medicamento_id).first()
    if medicamento is None:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    return medicamento

@app.put("/medicamentos/{medicamento_id}", response_model=MedicamentoResponse)
def actualizar_medicamento(
    medicamento_id: int,
    datos: MedicamentoCreate,
    db: Session = Depends(get_db)
):
    medicamento = db.query(Medicamento).filter(Medicamento.id == medicamento_id).first()
    if medicamento is None:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")

    for campo, valor in datos.model_dump().items():
        setattr(medicamento, campo, valor)

    db.commit()
    db.refresh(medicamento)
    return medicamento

@app.delete("/medicamentos/{medicamento_id}")
def eliminar_medicamento(medicamento_id: int, db: Session = Depends(get_db)):
    medicamento = db.query(Medicamento).filter(Medicamento.id == medicamento_id).first()
    if medicamento is None:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")

    db.delete(medicamento)
    db.commit()
    return {"mensaje": "Medicamento eliminado correctamente"}
