import streamlit as st

st.title('test')

st.header('Aplikasi penjumlahan bilangan numerik',divider='rainbow')

angka_pertama = st.number_input('masukkan angka pertama')
st.write('the first number is',angka_pertama)

angka_kedua = st.number_input('masukkan angka kedua')
st.write('the second number is',angka_kedua)

operasi_matematika = angka_pertama * angka_kedua
st.write(f"angka pertama {angka_pertama} x angka kedua {angka_kedua} = {operasi_matematika}")