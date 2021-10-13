


import streamlit as st
from datetime import datetime
import client
##import graphs
##from PIL import Image
##import card

################### title 

st.markdown("<h1 style='text-align: center; color: #942953 '>On Route/h1>", unsafe_allow_html = True)

##title_image = Image.open("./src/img/skyline.png")
##st.image(title_image)


st.markdown("What's ***'On Route'***?")
st.markdown("Description")

###################  TEXT_IMPUT

form = st.form(key='my_form')
initial_address = form.text_input(label='Insert initial address')
waipoint_1 = form.text_input(label='Insert first stop')
waipoint_2 = form.text_input(label='Insert second stop')
final_address = form.text_input(label='Insert final address')


submit_button = form.form_submit_button(label='Submit')


#st.sidebar.title('Direccion de salida')
#adress_initial=st.text_input('Introduzca direccion inicial')

#st.sidebar.title('Direccion 2')
#adress2=st.text_input('Introduzca direccion parada 1')

#st.sidebar.title('Direccion 3')
#adress3=st.text_input('Introduzca direccion parada 2')

#st.sidebar.title('Direccion final')
#adress_final=st.text_input('Introduzca direccion final')


###################  MAP 
if submit_button:
    now = datetime.now()
    directions_result = client.gmaps.directions(initial_address,
                                     final_address,
                                     waypoints=[waipoint_1, waipoint_2],
                                     mode="driving",
                                     departure_time=now)
    print(directions_result)



