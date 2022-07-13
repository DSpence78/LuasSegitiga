import streamlit as st

st.write("""
# Aplikasi Luas Segitiga
Program aplikasi sederhana untuk menghitung luas segitiga menggunakan Streamlit
""")

alas = float(st.text_input("Masukkan Alas", 0))
tinggi = float(st.text_input("Masukkan Tinggi", 0))
hitung = st.button("Hitung Luas")

if hitung:
    luas = alas * tinggi / 2
    st.balloons()
    st.success("Luas Segitiga adalah %.3f" % luas)