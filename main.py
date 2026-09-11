from fastapi import FastAPI
from pydantic import BaseModel
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
    return places

@app.get("/places/{place_id}")
def get_place(place_id: int):
    for place in places:
        if place["id"] == place_id:
            return place
    return{"message":"Place not found"}

@app.post("/plan")
def create_plan(request: UserRequest):
    return {
        "message": "Plan Recieved",
        "days": request.days,
        "interest": request.interest
    }
