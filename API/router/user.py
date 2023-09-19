from fastapi import APIRouter
import schemas
import joblib
import json

router = APIRouter(
    tags=["User"]
)

@router.post('/detection')
def post(request : schemas.user):
    if request.Fever == "Ya":
        request.Fever = 1
    else:
        request.Fever = 0

    if request.Cough == "Ya":
        request.Cough = 1
    else:
        request.Cough = 0

    if request.Fatigue == "Ya":
        request.Fatigue = 1
    else:
        request.Fatigue = 0

    if request.Dificulty_Breathing == "Ya":
        request.Dificulty_Breathing = 1
    else:
        request.Dificulty_Breathing = 0

    if request.Blood_Pressure == "Normal":
        request.Blood_Pressure = 2
    elif request.Blood_Pressure == "Tinggi":
        request.Blood_Pressure = 0
    else:
        request.Blood_Pressure = 1
    
    if request.Cholesterol_Level == "Normal":
        request.Cholesterol_Level = 2
    elif request.Cholesterol_Level == "Tinggi":
        request.Cholesterol_Level = 0
    else:
        request.Cholesterol_Level = 1

    if request.Gender == "Pria":
        request.Gender = 1
    else:
        request.Gender = 0
    
    # Memuat kembali model
    loaded_model = joblib.load('Machine-learning/model.pkl')

    # # Memuat kembali LabelEncoder
    scaler = joblib.load('Machine-learning/min_max.pkl')
    loaded_encoder_target = joblib.load("Machine-learning/label_enc_target.pkl")

    # 	Klasifikasi menggunakan model machine learning
    new_age = scaler.transform([[request.Age]])
    new_data = [int(request.Fever), int(request.Cough), int(request.Fatigue), int(request.Dificulty_Breathing), new_age[0], int(request.Gender), int(request.Blood_Pressure), int(request.Cholesterol_Level)]
    prediksi = loaded_model.predict([new_data])
    prediksi_new = loaded_encoder_target.inverse_transform(prediksi)
    return str(prediksi_new[0])

@router.get('/get_data')
def get_data():
    json_file_path = "Machine-learning/Disease_symptom_and_patient_profile_dataset.json"
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        return data

