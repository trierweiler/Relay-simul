#Streamlit examples

# Importing libraries
from datetime import time, datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st

st.markdown('>Aqui é possível usar texto em markdown :sunglasses:')
st.latex(r'''
         a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
         \LaTeX equation
         ''')

# =============================================================================
# # Localização do painel
# =============================================================================
U1 = [-25.407655, -54.592723]
U2 = [-25.407705, -54.592358]
U3 = [-25.407804, -54.592055]
U4 = [-25.407904, -54.591800]
U5 = [-25.408097, -54.591545]
U6 = [-25.408214, -54.591238]
U7 = [-25.408253, -54.590887]
U8 = [-25.408319, -54.590508]
U9 = [-25.408356, -54.590182]
U9A = [-25.408432, -54.589847]
U10 = [-25.408526, -54.589393]

map_data = pd.DataFrame({'lat': [U1[0],
                                 U2[0],
                                 U3[0],
                                 U4[0],
                                 U5[0],
                                 U6[0],
                                 U7[0],
                                 U8[0],
                                 U9[0],
                                 U9A[0]],
                         'lon': [U1[1],
                                 U2[1],
                                 U3[1],
                                 U4[1],
                                 U5[1],
                                 U6[1],
                                 U7[1],
                                 U8[1],
                                 U9[1],
                                 U9A[1]] })
if st.checkbox('Ver no mapa'):

    st.map(map_data)


# lay-out
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

# example of progress bar
# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'





genre = st.radio(
"What's your favorite movie genre",
('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")
    
    
    
option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)



options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)



age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')


values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)



appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)




start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)