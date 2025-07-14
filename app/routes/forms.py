from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/forms/wheel-specifications")
def submit_wheel_spec(data: schemas.WheelSpecBase, db: Session = Depends(get_db)):
    existing = db.query(models.WheelSpecification).filter_by(formNumber=data.formNumber).first()
    if existing:
        raise HTTPException(
            status_code=400, detail=f"Form with this formNumber '{data.formNumber}' already exists.")
    
    
    db_form = models.WheelSpecification(**data.dict())
    db.add(db_form)
    db.commit()
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": data.formNumber,
            "submittedBy": data.submittedBy,
            "submittedDate": str(data.submittedDate),
            "status": "Saved"
        }
    }

@router.post("/api/forms/bogie-checksheet")
def submit_bogie_checksheet(data: schemas.BogieChecksheetBase, db: Session = Depends(get_db)):
    # Check for duplicate formNumber
    existing = db.query(models.BogieChecksheet).filter_by(formNumber=data.formNumber).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail=f"A record with formNumber '{data.formNumber}' already exists."
        )
    
    db_form = models.BogieChecksheet(**data.dict())
    db.add(db_form)
    db.commit()
    return {
        "success": True,
        "message": "Bogie checksheet submitted successfully.",
        "data": {
            "formNumber": data.formNumber,
            "inspectionBy": data.inspectionBy,
            "inspectionDate": str(data.inspectionDate),
            "status": "Saved"
        }
    }

@router.get("/api/forms/wheel-specifications")
def get_wheel_spec(formNumber: str, submittedBy: str, submittedDate: str, db: Session = Depends(get_db)):
    results = db.query(models.WheelSpecification).filter_by(
        formNumber=formNumber,
        submittedBy=submittedBy,
        submittedDate=submittedDate
    ).all()
    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": [r.__dict__ for r in results]
    }
