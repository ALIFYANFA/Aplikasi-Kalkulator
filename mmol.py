 alifyanfa/aplikasi-kalkulatorimport streamlit as st

st.title('menghitung jumlah mmol dari suatu Gas mulia')

tabl, tab2=st(['informasi tentang Gas mulia','informasi nilai Ar Gas Mulia','kalkulator menghitung mol'])

with tab1:
    st.header('Informasi Tentang Gas Mulia')
    st.write('Gas Mulia atau Gas adi adalah Gas mulia adalah unsur kimia golongan 8 atau VIIIA di tabel periodik. Golongan ini disebut juga sebagai golongan helium atau neon dan golongan aerogen. Golongan ini terdiri dari unsur helium (He), Neon (Ne), argon (Ar), kripton (Kr), xenon (Xe), unsur radioaktif radon (Rn), dan unsur sintetis yang radioaktif oganeson (Og). Semua anggota unsur golongan 18 (VIIIA) merupakan gas mulia, bersifat nonlogam, dan berwujud gas pada suhu dan tekanan standar, kecuali oganeson (yang diprediksi akan berwujud padat dan bersifat seperti logam')

with tab2:
    st.header('Nilai Ar Suatu Gas Mulia')
    st.write('He = 4,0026') 
    st.write('Ne = 20,183')
    st.write('Ar = 39,948')
    st.write('Kr = 83,80')
    st.write('Xe = 131,30')
    st.write('Rn = (222)')
