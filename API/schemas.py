from pydantic import BaseModel

class user(BaseModel):
    Fever: str
    Cough: str
    Fatigue: str
    Dificulty_Breathing: str
    Age: int
    Gender: str
    Blood_Pressure: str
    Cholesterol_Level: str
