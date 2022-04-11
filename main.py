import streamlit as st

st.write("""
# Aplikasi Luas Segitiga
Program aplikasi sederhana untuk menghitung luas segitiga menggunakan Streamlit
""")

alas = st.number_input("Masukkan Alas", 0)
tinggi = st.number_input("Masukkan Tinggi", 0)
hitung = st.button("Hitung Luas")

if hitung:
    luas = alas * tinggi / 2
    st.snow()
    st.success(f"Luas Segitiga adalah {luas}")