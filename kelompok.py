import streamlit as st

st.title('Menghitung Jumlah Molaritas dan PPM ')

tab1, tab2, tab3=st.tabs(['informasi tentang PPM','kalkulator menghitung Molaritas','kalkulator menghitung ppm'])

with tab1:
    st.header('informasi tentang PPM')
    st.write('Satuan konsentrasi ppm (parts per million, "bagian per sejuta") adalah satuan yang dipakai sebagai satuan nirdimensi yang berasal dari pecahan yang sangat kecil, misalnya konsentrasi larutan atau kelimpahan partikel yang sangat kecil. ')

    
with tab2:
    st.header('kalkulator menghitung Molaritas')
    y=st.number_input('Masukkan masa padatan dari sampel yang telah dipilih dalam satuan mg:')
    x=st.number_input('Masukkan bobot molekul sampel dalam satuan mmol/mL:')    
    z=st.number_input('Masukkan volume dalam satuan mL')




    tombol = st.button('Hitung jumlah molaritas')
     
    if tombol:
        jumlahmolaritas=y/x*z
        st.success(f'jumlah molaritas adalah{jumlahmolaritas}') 