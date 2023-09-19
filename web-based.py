import streamlit as st
from streamlit_option_menu import option_menu
import requests
import json

st.set_page_config(layout='wide')

# Styling Text
st.markdown("""
<style>
.text-font {
    font-size:18px !important;
    allign='justify';
}
[class='css-1gwfbz0 ef3psqc6']{
    align='center';
}
</style>
""", unsafe_allow_html=True)

if 'menu' not in st.session_state:
    st.session_state['menu'] = None

buffer, col1 = st.columns([2, 6])
st.markdown("<hr>", unsafe_allow_html=True)


with buffer:
    st.image("image/LOGO.png", width=250)

with col1:
    st.write("")
    selected = option_menu(
        menu_title = None,
        options = ['Home', 'Detection', 'Info'],
        icons = ["house", "info-circle", "card-checklist"],
        menu_icon = 'cast',
        orientation = "horizontal",
        styles={
        "container" : {"background-color" : '#F2F6FF', 'color' : 'white'},
        "nav-link-selected": {"background-color": '#F2F6FF', 'color' : '#8AB4F8'},
        "nav-link" : {"--hover-color": "#F2F6FF"}
        }
    )
    if selected == "Home":
        st.session_state['menu'] = "Home"
    elif selected == "Detection":
        st.session_state['menu'] = "Detection"
    elif selected == "Info":
        st.session_state['menu'] = "Info"

if st.session_state['menu'] == "Detection":
    buffer, col1, col2 = st.columns([1, 5, 1])
    with col1:
        placeholder_1 = st.empty()

        with placeholder_1.form("deteksi"):
            st.markdown("<h1 align='center'>Medical Detection</h1>", unsafe_allow_html=True)
            Age = st.number_input(label="Age", max_value=100, step = 1)
            col1_1, col2_2 = st.columns([5, 5])
            with col1_1:
                Fever = st.selectbox("Fever", ['Yes', 'No'])
                Fatigue = st.selectbox("Fatigue", ['Yes', 'No']) 
                Cholesterol = st.selectbox("Cholesterol Level", ['Normal', 'High'])
            with col2_2:
                Cough = st.selectbox("Cough", ['Yes', 'No'])
                Breathing = st.selectbox("Difficulty Breathing", ['Yes', 'No'])
                Blood = st.selectbox("Blood Pressure", ['Normal', 'High'])
            Gender = st.selectbox("Gender", ['Male', 'Female'])

            submit = st.form_submit_button("Deteksi")
            if submit:
                data_input = {
                    "Fever": str(Fever),
                    "Cough": str(Cough),
                    "Fatigue": str(Fatigue),
                    "Dificulty_Breathing": str(Breathing),
                    "Age": int(Age),
                    "Gender": str(Gender),
                    "Blood_Pressure": str(Blood),
                    "Cholesterol_Level": str(Cholesterol)
                }

                res = requests.post(url="http://127.0.0.1:8000/detection", data=json.dumps(data_input))
                
                st.success(f"{res.text} disease detected")

elif st.session_state['menu'] == "Home":
    buffer, col1, col2 = st.columns([.5, 4, 5], gap='small')
    with col2:
        st.image("image/beranda.png", width=800)
    with col1:
        st.markdown("<h1>Medical Detection</h1>\n<p>Automatic disease detection system</p>", unsafe_allow_html=True)
        st.markdown("<p class='text-font', align='justify'>MediDetect is an innovative system designed to detect diseases with high accuracy based on the symptoms entered. By utilizing artificial intelligence technology, MediDetect analyzes the symptoms provided by the user and compares them with an extensive database of diseases. The system provides quick and reliable information on possible diseases that the user may be facing, aiding in early diagnosis and necessary action. With an intuitive interface, MediDetect provides an effective and practical solution for early disease detection, making a positive impact on public health and giving users more control over their health.", unsafe_allow_html=True)

elif st.session_state['menu'] == "Info":
    st.markdown("<h1 align='center'>Medical Detection (MediDetect)", unsafe_allow_html=True)
    st.write("")
    buffer, col1, col2 = st.columns([1.5, 7, 1.5])
    with col1:
        st.markdown("<p style='text-align:center; font-size:20px;'> Medical Detection Is a system used to detect symptoms of AI-based diseases that are integrated with APIs. The API can be accessed below...", unsafe_allow_html=True)
        with st.expander("Selengkapnya"):
            st.write("http://127.0.0.1:8000")