from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal
from models import Place

app = FastAPI()

class UserRequest(BaseModel):
    days: int
    interest: str

@app.get("/")
def home():
    return{"message": "Welcome to Sanskritee"}

places = [
        {
            "id": 1,
            "name": "Bibi Ka Maqbara",
            "type": "Historical Monument"
        },
        {
            "id": 2,
            "name": "Daulatabad Fort",
            "type": "Fort"
        },
        {
            "id": 3,
            "name": "Ellora Caves",
            "type": "Heritage Site"
        }
    ]

@app.get("/places")
def get_places():
    db = SessionLocal()
    places = db.query(Place).all()
    db.close()

    return places

@app.get("/places/{place_id}")
def get_place(place_id: int):
    db = SessionLocal()
    place = db.query(Place).filter(Place.id == place_id).first()
    db.close()
    
    if place is None:
        return{"message":"Place not found"}

    return place

    

@app.post("/plan")
def create_plan(request: UserRequest):
    return {
        "message": "Plan Recieved",
        "days": request.days,
        "interest": request.interest
    }
