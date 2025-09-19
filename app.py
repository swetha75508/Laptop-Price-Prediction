import streamlit as st
import pandas as pd
import numpy as np
import pickle

# load model
with open("xgb_pipe(1).pkl", "rb") as file:
    model = pickle.load(file)

# ----------------- PAGE CONFIG -----------------
st.set_page_config(page_title="Laptop Price Dashboard", layout="wide")

# Custom CSS for blurred background
page_bg = """
<style>
.stApp {
    background: url("https://res.cloudinary.com/druw9hy64/image/upload/v1758266349/laptop_lzs0pz.jpg") no-repeat center center fixed;
    background-size: cover;
}
.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-color: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(12px);
    z-index: -1;
}
/* Sidebar blur effect */
[data-testid="stSidebar"] {
    background-color: rgba(30, 30, 30, 0.55) !important;
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255,255,255,0.2);
}
[data-testid="stSidebar"] * {
    color: white !important;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.title("Laptop Price Dashboard & Predictor")
st.markdown("Predict laptop prices interactively and view quick insights based on your inputs.")

# ----------------- SIDEBAR INPUT -----------------
st.sidebar.header("Laptop Specifications")

company = st.sidebar.selectbox("Company", ['Dell', 'HP', 'Apple', 'Lenovo', 'Acer', 'Asus', 'MSI','LG', 'Microsoft', 'Google', 'Samsung', 'Razer', 'Toshiba'])
typename = st.sidebar.selectbox("Type", ['Notebook', 'Gaming', 'Ultrabook', 'Workstation','2 in 1 Convertible'])
cpu_brand = st.sidebar.selectbox("CPU Brand", ['Intel Core i3', 'Intel Core i5', 'Intel Core i7',
                                               'Other Intel Processor', 'AMD Processor'])
gpu_brand = st.sidebar.selectbox("GPU Brand", ['Intel', 'Nvidia', 'AMD','ARM'])
os = st.sidebar.selectbox("Operating System", ['Windows', 'Mac', 'Linux','Chrome', 'Other/No OS'])

ram = st.sidebar.selectbox("RAM (GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.sidebar.number_input("Weight (kg)", min_value=0.5, max_value=5.0, step=0.1)
touchscreen = st.sidebar.radio("Touchscreen", ['Yes', 'No'])
ips = st.sidebar.radio("IPS Display", ['Yes', 'No'])
ppi = st.sidebar.selectbox("PPI (Pixel Per Inch)", list(range(100, 501, 10)))
hdd = st.sidebar.selectbox("HDD (GB)", [0, 128, 256, 512, 1024, 2048])
ssd = st.sidebar.selectbox("SSD (GB)", [0, 128, 256, 512, 1024])


# ----------------- PREPARE INPUT -----------------
input_data = {
    'Company': company,
    'TypeName': typename,
    'Cpu Brand': cpu_brand,
    'Gpu Brand': gpu_brand,
    'OS': os,
    'Ram' : ram,
    'Weight': weight,
    'Touchscreen' : 1 if touchscreen == 'Yes' else 0,
    'IPS' : 1 if ips == 'Yes' else 0,
    'PPI' : ppi,
    'HDD' : hdd,
    'SSD' : ssd
}
input_df = pd.DataFrame([input_data])


# ----------------- PREDICTION -----------------
st.header("Price Prediction")
if st.button("Predict"):
    log_price = model.predict(input_df)[0]
    price = round(np.exp(log_price))
    st.success(f"Predicted Price is : ₹{price:,.0f}")