import streamlit as st

st.title('menghitung jumlah mmol dari suatu Alkali Tanah')

tabl, tab2, tab3=st.tabs(['informasi tentang Alkali Tanah','informasi nilai Ar Alkali Tanah','kalkulator menghitung mmol'])

with tab1:
     st.header('informasi tentang Alkali Tanah')
     st.write('Alkali Tanah merupakan keluarga unsur kimia yang menunjukkan pola dalam konfigurasi elektron. Secara keseluruhan, alkali tanah bersifat basa dan banyak ditemukan di dalam mineral tanah. Kelimpahan alkali tanah cukup banyak dan bentuknya berupa senyawa')

with tab2:
     st.header('Nilai Ar Alkali Tanah')
     st.write('Be =9,0122') 
     st.write('Mg =24,312')
     st.write('Ca =40,08')
     st.write('Sr =87,62')
     st.write('Ba =137,34')
     st.write('Ra =226')

with tab3:
    st.header('kalkulator menghitung mmol')
    options=st.multiselect(
        'nama alkali tanah',
        ['Be','Mg','Ca','Sr','Ba','Ra'])
    y=st.number_input('Masukkan masa padatan dari unsur alkali tanah yang telah dipilih dalam satuan mg:')
    y=st.number_input('Masukkan masa atom relatif Alkali Tanah (Ar) yang telah dipilih dalam satuan mg/mmol:')    




     tombol = st.button('Hitung jumlah mmol dari suatu Alkali Tanah')
     
     if tombol:
        jumlah_mmol=y/z
        st.success(f'jumlah mmol adalah{options}{jumlah_mmol}') 