import streamlit as st

st.title('Kalkukator ppm dari Molaritas ')

tab1, tab2, tab3, tab4=st.tabs(['Biodata Kelompok 7','Informasi Tentang ppm','Kalkulator ppm dari Molaritas','Rumus dan Contoh Soal'])

with tab1:
    st.header('Biodata kelompok')
    st.image('biodata kelompok 7.jpg')

with tab2:
    st.header('Informasi Tentang ppm')
    st.write('Satuan konsentrasi ppm (parts per million, "bagian per sejuta")pada dasarnya bertujuan untuk menghitung kadar kandungan yang terlarut dalam air, Dalam industri, ppm adalah satuan yang sering digunakan untuk mengukur kualitas produk dan bahan, serta kontrol kualitas dalam proses produksi, Penggunaan ppm memungkinkan untuk mendeteksi sejumlah sangat kecil dari bahan atau zat yang bisa berdampak signifikan terhadap lingkungan atau kesehatan manusia')
    st.image("gambar kimia orang.webp")
    
with tab3:
    st.header('kalkulator ppm Dari Molaritas ')
    y=st.number_input('Masukkan masa sampel dalam satuan mg:')
    x=st.number_input('Masukkan bobot molekul sampel dalam satuan mg/mmol:')    
    z=st.number_input('Masukkan volume dalam satuan mL')
    m=st.number_input('Masukan faktor pengali (jika Tidak ada Masukan Angka 1)')
    st.image("bird-colors.gif")


    tombol = st.button('Hitung jumlah Molaritas')
     
    if tombol:
        jumlahmolaritas=y/x/z/m
        st.success(f'jumlah Molaritas adalah{jumlahmolaritas}') 

    x=st.number_input('Masukkan molaritas dari sampel yang telah dipilih dalam satuan mmol/mL:')
    y=st.number_input('Masukkan volume titran dalam satuan mL:')    
    z=st.number_input('Masukkan bobot molekul dalam satuan mg/mmol')
    v=st.number_input('Masukkan volume sampel dalam satuan mL')
    st.image("bird-colors.gif")
    
    tombol = st.button('Hitung jumlah ppm')
     
    if tombol:
        jumlahppm=x*y*z/v/0.001
        st.success(f'jumlah ppm adalah{jumlahppm}') 

with tab4:
    st.header('Rumus dan Contoh Soal')
    st.image('rumus molaritas - Salin.jpg')
    st.image('rumus ppm.jpg')
    st.image('contoh soal molaritas 1.jpg')
    st.image('contoh soal ppm1.jpg')       