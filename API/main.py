from fastapi import FastAPI
from router import user
import schemas

app = FastAPI()

app.include_router(user.router)

@app.get('/')
def index():
    return {
        "Project Name" : "MediDetect (API)",
        "Details" : "MediDetect adalah sistem inovatif yang dirancang untuk mendeteksi penyakit dengan akurasi tinggi berdasarkan gejala yang dimasukkan. Dengan memanfaatkan teknologi kecerdasan buatan, MediDetect menganalisis gejala yang diberikan oleh pengguna dan membandingkannya dengan basis data penyakit yang luas. Sistem ini memberikan informasi cepat dan andal tentang kemungkinan penyakit yang mungkin dihadapi pengguna, membantu dalam diagnosis awal dan tindakan yang diperlukan. Dengan antarmuka yang intuitif, MediDetect memberikan solusi yang efektif dan praktis untuk deteksi dini penyakit, memberikan dampak positif pada kesehatan masyarakat dan memberi pengguna kendali lebih atas kesehatan mereka.",
        "Variabels" : {
            "Disease" : "The name of the disease or medical condition.",
            "Fever" : "Indicates whether the patient has a fever (Yes/No).",
            "Cough" : "Indicates whether the patient has a cough (Yes/No).",
            "Fatigue" : "Indicates whether the patient experiences fatigue (Yes/No).",
            "Difficulty Breathing" : "Indicates whether the patient has difficulty breathing (Yes/No).",
            "Age" : "The age of the patient in years.",
            "Gender" : "The gender of the patient (Male/Female).",
            "Blood Pressure" : "The blood pressure level of the patient (Normal/High).",
            "Cholesterol Level" : "The cholesterol level of the patient (Normal/High)."
        }
    }
