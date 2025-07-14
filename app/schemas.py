from pydantic import BaseModel
from datetime import date
from typing import Dict

class WheelSpecBase(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict

class BogieChecksheetBase(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: date
    bogieDetails: Dict
    bogieChecksheet: Dict
    bmbcChecksheet: Dict
