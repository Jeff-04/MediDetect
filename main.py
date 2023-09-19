import subprocess
import time

def start_streamlit():
    streamlit_cmd = [
        "streamlit",
        "run",
        "web-based.py"  # Ganti dengan nama file Streamlit aplikasi kamu
    ]

    subprocess.Popen(streamlit_cmd)

def start_uvicorn():
    # uvicorn_cmd = [
    #     "uvicorn",
    #     "main:app",   # Ganti dengan module dan nama aplikasi kamu
    #     "--host", "127.0.0.1",
    #     "--port", "8000",
    #     "--reload"
    # ]
    
    # Direktori yang ingin Anda ubah ke dalamnya
    new_directory = "API"

    # Gunakan perintah 'cd' untuk mengganti direktori kerja
    # Gunakan '&&' untuk menggabungkan beberapa perintah dalam satu baris
    command = f"cd {new_directory} && uvicorn main:app --host 127.0.0.1 --port 8000 --reload"

    # Jalankan perintah menggunakan subprocess
    subprocess.call(command, shell=True)
    # subprocess.Popen(uvicorn_cmd)

if __name__ == "__main__":
    # Mulai Streamlit dalam subproses
    start_streamlit()

    # Tunggu sebentar agar Streamlit dapat mulai sebelum UVicorn
    time.sleep(5)

    # Mulai UVicorn dalam subproses
    start_uvicorn()