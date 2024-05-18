import streamlit as st

st.title('Menghitung Jumlah Molaritas dan PPM ')

tab1, tab2, tab3=st.tabs(['informasi tentang PPM','kalkulator menghitung Molaritas','kalkulator menghitung ppm dari Molaritas'])

with tab1:
    st.header('informasi tentang PPM')
    st.write('Satuan konsentrasi ppm (parts per million, "bagian per sejuta") adalah satuan yang dipakai sebagai satuan nirdimensi yang berasal dari pecahan yang sangat kecil, misalnya konsentrasi larutan atau kelimpahan partikel yang sangat kecil. ')
    def set_bg_hack_url():
    st.markdown(
         f"""
         <style>
        .stApp {{
             background: url("https://id.images.search.yahoo.com/images/view;_ylt=AwrKGE.WC0hmt6UNxBbNQwx.;_ylu=c2VjA3NyBHNsawNpbWcEb2lkA2U4YjY2MzYzOTYzODY0NzZlNTExMDczYWZiNmU5MTBhBGdwb3MDMTMEaXQDYmluZw--?back=https%3A%2F%2Fid.images.search.yahoo.com%2Fsearch%2Fimages%3Fp%3Dbackground%2Bkeren%2Bkimia%26ei%3DUTF-8%26type%3DE210ID885G0%26fr%3Dmcafee%26fr2%3Dp%253As%252Cv%253Ai%252Cm%253Asb-top%26tab%3Dorganic%26ri%3D13&w=600&h=598&imgurl=i.pinimg.com%2Foriginals%2F78%2F6c%2Fe6%2F786ce640340c245624e09b1e7c2ff7a3.jpg&rurl=https%3A%2F%2Fwww.background.id%2Fbackground-ppt-kimia-aesthetic&size=44.0KB&p=background+keren+kimia&oid=e8b6636396386476e511073afb6e910a&fr2=p%3As%2Cv%3Ai%2Cm%3Asb-top&fr=mcafee&tt=Unduh+500+Gratis+Background+Ppt+Kimia+Aesthetic+Terbaik&b=0&ni=90&no=13&ts=&tab=organic&sigr=je0rZOwKnyPe&sigb=DH9AVLp7NiTb&sigi=UtnznEQ2A4gh&sigt=C7jDZNL9YZcR&.crumb=VizfcaQeZeM&fr=mcafee&fr2=p%3As%2Cv%3Ai%2Cm%3Asb-top&type=E210ID885G0");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url()
    
with tab2:
    st.header('kalkulator menghitung Molaritas ')
    y=st.number_input('Masukkan masa padatan dari sampel yang telah dipilih dalam satuan mg:')
    x=st.number_input('Masukkan bobot molekul sampel dalam satuan mg/mmol:')    
    z=st.number_input('Masukkan volume dalam satuan mL')




    tombol = st.button('Hitung jumlah molaritas')
     
    if tombol:
        jumlahmolaritas=y/x/z
        st.success(f'jumlah molaritas adalah{jumlahmolaritas}') 





with tab3:
    st.header('kalkulator menghitung PPM dengan diketahui molaritas')
    x=st.number_input('Masukkan molaritas dari sampel yang telah dipilih dalam satuan mmol/mL:')
    y=st.number_input('Masukkan volume titran dalam satuan mL:')    
    z=st.number_input('Masukkan bobot molekul dalam satuan mg/mmol')
    v=st.number_input('Masukkan volume sampel dalam satuan mL')


    tombol = st.button('Hitung jumlah PPM')
     
    if tombol:
        jumlahPPM=x*y*z/v/0.001
        st.success(f'jumlah PPM adalah{jumlahPPM}') 



