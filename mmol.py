import streamlit as st

st.header('Kelompok 7')
st.image('biodata kelompok 7.jpg')
st.title('Kalkukator ppm dari Molaritas ')

tab1, tab2, tab3=st.tabs(['Informasi Tentang ppm','Kalkulator Molaritas','Kalkulator ppm'])


with tab1:
    st.header('Informasi Tentang ppm')
    st.write('Molaritas adalah satuan konsentrasi larutan yang menyatakan jumlah mol zat terlarut dalam satu liter larutan. Satuan ini sering digunakan dalam industri kimia maupun farmasi untuk membuat sebuah larutan.')
    st.write('Satuan konsentrasi ppm (parts per million, "bagian per sejuta") pada dasarnya bertujuan untuk menghitung kadar kandungan yang terlarut dalam air. Dalam industri, ppm adalah satuan yang sering digunakan untuk mengukur kualitas produk dan bahan, serta kontrol kualitas dalam proses produksi. Penggunaan ppm memungkinkan untuk mendeteksi sejumlah sangat kecil dari bahan atau zat yang bisa berdampak signifikan terhadap lingkungan atau kesehatan manusia.')

    st.image("gambar kimia orang.webp")

with tab2:

    st.image('rumus molaritas - Salin.jpg')
   
    st.header('Kalkulator Molaritas ')
    y=st.number_input('Masukkan Massa (mg):')
    x=st.number_input('Masukkan Bobot Molekul (mg/mmol):')    
    z=st.number_input('Masukkan Volume (mL):')
    m=st.number_input('Masukan Faktor Pengali (Jika tidak ada masukkan angka 1):')
    st.image("bird-colors.gif")


    tombol = st.button('Hitung Jumlah Molaritas')
     
    if tombol:
        jumlahmolaritas=y/x/z/m
        st.success(f'Jumlah Molaritas adalah {jumlahmolaritas} mmol/mL') 

    st.image('contoh soal molaritas 1.jpg')


with tab3:
    st.image('rumus ppm.jpg')

    st.header('Kalkulator ppm')
    x=st.number_input('Masukkan Molaritas (mmol/mL):')
    y=st.number_input('Masukkan Volume Titran (mL):')    
    z=st.number_input('Masukkan BM (Bobot Molekul) (mg/mmol):')
    v=st.number_input('Masukkan Volume Sampel (mL):')
    st.image("bird-colors.gif")
    
    tombol = st.button('Hitung Jumlah ppm')
     
    if tombol:
        jumlahppm=x*y*z/v/0.001
        st.success(f'Jumlah ppm adalah {jumlahppm} mg/mL') 

    st.image('contoh soal.jpg')
