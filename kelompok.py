import streamlit as st


st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("background steamlit.jpeg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)



st.title('Kalkukator ppm dari Molaritas ')

tab1, tab2, tab3, tab4, tab5, tab6=st.tabs(['Biodata Kelompok 7','informasi tentang ppm','kalkulator Molaritas','kalkulator ppm dari Molaritas','Contoh Soal Molaritas','Contoh Soal ppm'])

with tab1:
    st.header('Biodata kelompok')
    st.image('biodata kelompok 7.jpg')

with tab2:
    st.header('informasi tentang ppm')
    st.write('Satuan konsentrasi ppm (parts per million, "bagian per sejuta") adalah satuan yang dipakai sebagai satuan nirdimensi yang berasal dari pecahan yang sangat kecil, misalnya konsentrasi larutan atau kelimpahan partikel yang sangat kecil. ')
    st.image("gambar kimia orang.webp")
    
with tab3:
    st.header('kalkulator Molaritas ')
    y=st.number_input('Masukkan masa padatan dari sampel yang telah dipilih dalam satuan mg:')
    x=st.number_input('Masukkan bobot molekul sampel dalam satuan mg/mmol:')    
    z=st.number_input('Masukkan volume dalam satuan mL')
    st.image("bird-colors.gif")


    tombol = st.button('Hitung jumlah molaritas')
     
    if tombol:
        jumlahmolaritas=y/x/z
        st.success(f'jumlah molaritas adalah{jumlahmolaritas}') 


with tab4:
    st.header('kalkulator ppm dari molaritas')
    x=st.number_input('Masukkan molaritas dari sampel yang telah dipilih dalam satuan mmol/mL:')
    y=st.number_input('Masukkan volume titran dalam satuan mL:')    
    z=st.number_input('Masukkan bobot molekul dalam satuan mg/mmol')
    v=st.number_input('Masukkan volume sampel dalam satuan mL')
    m=st.number_input('masukan faktor pengali')
    st.image("bird-colors.gif")
    
    tombol = st.button('Hitung jumlah ppm')
     
    if tombol:
        jumlahppm=x*y*z*m/v/0.001
        st.success(f'jumlah ppm adalah{jumlahppm}') 

with tab5:
    st.header('Contoh Soal Molaritas')
    st.image('contoh soal molaritas 1.jpg')

with tab6:
    st.header('Contoh Soal ppm')
    st.image('contoh soal ppm1.jpg')       