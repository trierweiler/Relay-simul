# -*- coding: utf-8 -*-
"""
Relé de proteção do TAP-02
"""

# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st

# =============================================================================
# Functions
# =============================================================================


# =============================================================================
# # Page title
# =============================================================================
st.title('Proteção do TAP-02')

# =============================================================================
# Dados técnicos
# =============================================================================
expander_6 = st.beta_expander(label='Dados técnicos')
with expander_6:
    st.write('Dados do relé')
    st.text('Marca: Siemens')
    st.text('Modelo: 7UT63')
    
    st.write('Dados do TA-02')
    st.text('Primário: 525 kV, Y aterrado')
    st.text('Secndário: 13,8 kV, Y aterrado')
    
    st.write('RTCs')
    st.text('06TA02: 1200/5 A')
    st.text('86TA02: 1200/5 A')
    st.text('52-A2: 2000/5 A')
    st.text('Neutro 13,8 kV: 2000/5 A')

# =============================================================================
# Diagrama unifilar
# =============================================================================
expander_1 = st.beta_expander(label='Diagrama unifilar')
with expander_1:
    image = Image.open('/src/unifilar.jpg')
    st.image(image)

# =============================================================================
# # Relay settings table
# =============================================================================
expander_2 = st.beta_expander(label='Ajustes')
with expander_2:
    st.write("Ajustes:")
    dict_ajustes = {'Parâmetro': ['Pick-up (pu)', 'Tempo de operação (s)'],
                    'Valor': [0.5, 11] }
    df_ajustes = pd.DataFrame(dict_ajustes)
    st.table(df_ajustes)
    
    # Validate parameters
    if dict_ajustes['Valor'][1] > 10:
        st.write(ValueError('O tempo de operação deve ser no máximo 10 s'))


# =============================================================================
# Configuração pré-falta
# =============================================================================
expander_3 = st.beta_expander(label='Configuração pré-falta')
with expander_3:
    
    c1, c2, c3 = st.beta_columns(3)
    sampling_freq = c1.number_input(label='Taxa de amostragem (kHz)',
                                    min_value=1,
                                    max_value=20,
                                    value=10)
    
    dt = 1 / (sampling_freq*1000) # sampling period in seconds
    t_final = 1    # end of simulation
    t_vec = np.arange(start=0, stop=t_final, step=dt) # time array
    
    
    
# =============================================================================
# # Corrente do TC 06TA2
# =============================================================================
    st.subheader('Corrente do TC 06TA2')
    c1, c2, c3 = st.beta_columns(3)
    
    c1.write('Fase A')
    tc_06ta2_r_mag = c1.number_input(label='Mag (A)',
                                     min_value=1,
                                     max_value=4000,
                                     value=500,
                                     step=100,
                                     key='tc_06ta2_r_mag')
    tc_06ta2_r_f = c1.number_input(label='f (Hz)',
                                   min_value=55,
                                   max_value=65,
                                   value=60,
                                   key='tc_06ta2_r_f')
    tc_06ta2_r_phi = c1.number_input(label='Fase (°)',
                                     min_value=-180,
                                     max_value=180,
                                     value=0,
                                     key='tc_06ta2_r_phi')
    
    c2.write('Fase B')
    tc_06ta2_s_mag = c2.number_input(label='Mag (A)',
                                     min_value=1,
                                     max_value=4000,
                                     value=500,
                                     step=100,
                                     key='tc_06ta2_s_mag')
    tc_06ta2_s_f = c2.number_input(label='f (Hz)',
                                   min_value=55,
                                   max_value=65,
                                   value=60,
                                   key='tc_06ta2_s_f')
    tc_06ta2_s_phi = c2.number_input(label='Fase (°)',
                                     min_value=-180,
                                     max_value=180,
                                     value=-120,
                                     key='tc_06ta2_s_phi')
    
    c3.write('Fase C')
    tc_06ta2_t_mag = c3.number_input(label='Mag (A)',
                                     min_value=1,
                                     max_value=4000,
                                     value=500,
                                     step=100,
                                     key='tc_06ta2_t_mag')
    tc_06ta2_t_f = c3.number_input(label='f (Hz)',
                                   min_value=55,
                                   max_value=65,
                                   value=60,
                                   key='tc_06ta2_t_f')
    tc_06ta2_t_phi = c3.number_input(label='Fase (°)',
                                     min_value=-180,
                                     max_value=180,
                                     value=120,
                                     key='tc_06ta2_t_phi')
    
    tc_06ta2_r_phi = tc_06ta2_r_phi*np.pi/180
    tc_06ta2_s_phi = tc_06ta2_s_phi*np.pi/180
    tc_06ta2_t_phi = tc_06ta2_t_phi*np.pi/180
    
    tc_06ta2_r = [tc_06ta2_r_mag*np.sin(2*np.pi*tc_06ta2_r_f*t + tc_06ta2_r_phi) \
                  for t in t_vec]
    tc_06ta2_s = [tc_06ta2_s_mag*np.sin(2*np.pi*tc_06ta2_s_f*t + tc_06ta2_s_phi) \
                  for t in t_vec]
    tc_06ta2_t = [tc_06ta2_t_mag*np.sin(2*np.pi*tc_06ta2_t_f*t + tc_06ta2_t_phi) \
                  for t in t_vec]
        
# =============================================================================
# # Corrente do TC 86TA2
# =============================================================================
    st.subheader('Corrente do TC 86TA2')
    c1, c2, c3 = st.beta_columns(3)
    
    c1.write('Fase A')
    tc_86ta2_r_mag = c1.number_input(label='Mag (A)',
                                     min_value=1,
                                     max_value=4000,
                                     value=500,
                                     step=100,
                                     key='tc_86ta2_r_mag')
    tc_86ta2_r_f = c1.number_input(label='f (Hz)',
                                   min_value=55,
                                   max_value=65,
                                   value=60,
                                   key='tc_86ta2_r_f')
    tc_86ta2_r_phi = c1.number_input(label='Fase (°)',
                                     min_value=-180,
                                     max_value=180,
                                     value=0,
                                     key='tc_86ta2_r_phi')
    
    c2.write('Fase B')
    tc_86ta2_s_mag = c2.number_input(label='Mag (A)',
                                     min_value=1,
                                     max_value=4000,
                                     value=500,
                                     step=100,
                                     key='tc_86ta2_s_mag')
    tc_86ta2_s_f = c2.number_input(label='f (Hz)',
                                   min_value=55,
                                   max_value=65,
                                   value=60,
                                   key='tc_86ta2_s_f')
    tc_86ta2_s_phi = c2.number_input(label='Fase (°)',
                                     min_value=-180,
                                     max_value=180,
                                     value=-120,
                                     key='tc_86ta2_s_phi')
    
    c3.write('Fase C')
    tc_86ta2_t_mag = c3.number_input(label='Mag (A)',
                                     min_value=1,
                                     max_value=4000,
                                     value=500,
                                     step=100,
                                     key='tc_86ta2_t_mag')
    tc_86ta2_t_f = c3.number_input(label='f (Hz)',
                                   min_value=55,
                                   max_value=65,
                                   value=60,
                                   key='tc_86ta2_t_f')
    tc_86ta2_t_phi = c3.number_input(label='Fase (°)',
                                     min_value=-180,
                                     max_value=180,
                                     value=120,
                                     key='tc_86ta2_t_phi')
    
    tc_86ta2_r_phi = tc_86ta2_r_phi*np.pi/180
    tc_86ta2_s_phi = tc_86ta2_s_phi*np.pi/180
    tc_86ta2_t_phi = tc_86ta2_t_phi*np.pi/180
    
    tc_86ta2_r = [tc_86ta2_r_mag*np.sin(2*np.pi*tc_86ta2_r_f*t + tc_86ta2_r_phi) \
                  for t in t_vec]
    tc_86ta2_s = [tc_86ta2_s_mag*np.sin(2*np.pi*tc_86ta2_s_f*t + tc_86ta2_s_phi) \
                  for t in t_vec]
    tc_86ta2_t = [tc_86ta2_t_mag*np.sin(2*np.pi*tc_86ta2_t_f*t + tc_86ta2_t_phi) \
                  for t in t_vec]
        
# =============================================================================
# # Corrente do TC 52-A2
# =============================================================================
    st.subheader('Corrente do TC 52-A2')
    c1, c2, c3 = st.beta_columns(3)
    
    c1.write('Fase A')
    tc_52a2_r_mag = c1.number_input(label='Mag (A)',
                                     min_value=1,
                                     max_value=4000,
                                     value=1000,
                                     step=100,
                                     key='tc_52a2_r_mag')
    tc_52a2_r_f = c1.number_input(label='f (Hz)',
                                   min_value=55,
                                   max_value=65,
                                   value=60,
                                   key='tc_52a2_r_f')
    tc_52a2_r_phi = c1.number_input(label='Fase (°)',
                                     min_value=-180,
                                     max_value=180,
                                     value=0,
                                     key='tc_52a2_r_phi')
    
    c2.write('Fase B')
    tc_52a2_s_mag = c2.number_input(label='Mag (A)',
                                     min_value=1,
                                     max_value=4000,
                                     value=1000,
                                     step=100,
                                     key='tc_52a2_s_mag')
    tc_52a2_s_f = c2.number_input(label='f (Hz)',
                                   min_value=55,
                                   max_value=65,
                                   value=60,
                                   key='tc_52a2_s_f')
    tc_52a2_s_phi = c2.number_input(label='Fase (°)',
                                     min_value=-180,
                                     max_value=180,
                                     value=-120,
                                     key='tc_52a2_s_phi')
    
    c3.write('Fase C')
    tc_52a2_t_mag = c3.number_input(label='Mag (A)',
                                     min_value=1,
                                     max_value=4000,
                                     value=1000,
                                     step=100,
                                     key='tc_52a2_t_mag')
    tc_52a2_t_f = c3.number_input(label='f (Hz)',
                                   min_value=55,
                                   max_value=65,
                                   value=60,
                                   key='tc_52a2_t_f')
    tc_52a2_t_phi = c3.number_input(label='Fase (°)',
                                     min_value=-180,
                                     max_value=180,
                                     value=120,
                                     key='tc_52a2_t_phi')
    
    tc_52a2_r_phi = tc_52a2_r_phi*np.pi/180
    tc_52a2_s_phi = tc_52a2_s_phi*np.pi/180
    tc_52a2_t_phi = tc_52a2_t_phi*np.pi/180
    
    tc_52a2_r = [tc_52a2_r_mag*np.sin(2*np.pi*tc_52a2_r_f*t + tc_52a2_r_phi) \
                  for t in t_vec]
    tc_52a2_s = [tc_52a2_s_mag*np.sin(2*np.pi*tc_52a2_s_f*t + tc_52a2_s_phi) \
                  for t in t_vec]
    tc_52a2_t = [tc_52a2_t_mag*np.sin(2*np.pi*tc_52a2_t_f*t + tc_52a2_t_phi) \
                  for t in t_vec]
    
# =============================================================================
# Configuração da Falta
# =============================================================================
expander_4 = st.beta_expander(label='Configuração da Falta')
with expander_4:
    
    c1, c2, c3 = st.beta_columns(3)
    
    pre_fault = c1.number_input(label='Tempo pré-falta (ms)',
                                    min_value=40,
                                    max_value=300,
                                    value=100)
    fault_location = c2.selectbox('Local da falta:',
                                  ['Interna', 'Externa'])
    fault_type = c3.selectbox('Tipo da falta:',
                              ['Circuito aberto L',
                               'Circuito aberto L-L',
                               'Curto-circuito L',
                               'Curto-circuito L-L',
                               'Curto-circuito L-L-L'])
    
    # =============================================================================
    # Gerar oscilografia da falta
    # =============================================================================
    t_vec_fault_start_pos = int(pre_fault /1000 / dt) # posição do vetor tempo no início da falta
    fault_created = False # Flag to indicate if the fault has been configured and applied
    t_fault_end = t_vec[-t_vec_fault_start_pos]
    t_fault = np.arange(start=0, stop=t_fault_end, step=dt) # time array for calculating the fault
    
    fault_created = st.button(label='Criar falta', key='criar_falta')
    
    if (fault_type == 'Circuito aberto L') & fault_created:
        
        last_value = tc_06ta2_r[t_vec_fault_start_pos]
        tc_06ta2_r_fault = last_value * np.exp(-500*t_fault)
        tc_06ta2_r[t_vec_fault_start_pos:] = tc_06ta2_r_fault
        
        last_value = tc_86ta2_r[t_vec_fault_start_pos]
        tc_86ta2_r_fault = last_value * np.exp(-500*t_fault)
        tc_86ta2_r[t_vec_fault_start_pos:] = tc_86ta2_r_fault
        
        last_value = tc_52a2_r[t_vec_fault_start_pos]
        tc_52a2_r_fault = last_value * np.exp(-500*t_fault)
        tc_52a2_r[t_vec_fault_start_pos:] = tc_52a2_r_fault
        
    if (fault_type == 'Circuito aberto L-L') & fault_created:
        
        last_value = tc_06ta2_r[t_vec_fault_start_pos]
        tc_06ta2_r_fault = last_value * np.exp(-500*t_fault)
        tc_06ta2_r[t_vec_fault_start_pos:] = tc_06ta2_r_fault
        
        last_value = tc_06ta2_s[t_vec_fault_start_pos]
        tc_06ta2_s_fault = last_value * np.exp(-500*t_fault)
        tc_06ta2_s[t_vec_fault_start_pos:] = tc_06ta2_s_fault
        
        last_value = tc_86ta2_r[t_vec_fault_start_pos]
        tc_86ta2_r_fault = last_value * np.exp(-500*t_fault)
        tc_86ta2_r[t_vec_fault_start_pos:] = tc_86ta2_r_fault
        
        last_value = tc_86ta2_s[t_vec_fault_start_pos]
        tc_86ta2_s_fault = last_value * np.exp(-500*t_fault)
        tc_86ta2_s[t_vec_fault_start_pos:] = tc_86ta2_s_fault
        
        last_value = tc_52a2_r[t_vec_fault_start_pos]
        tc_52a2_r_fault = last_value * np.exp(-500*t_fault)
        tc_52a2_r[t_vec_fault_start_pos:] = tc_52a2_r_fault
        
        last_value = tc_52a2_s[t_vec_fault_start_pos]
        tc_52a2_s_fault = last_value * np.exp(-500*t_fault)
        tc_52a2_s[t_vec_fault_start_pos:] = tc_52a2_s_fault
        
    cond_1 = (fault_type == 'Curto-circuito L-L-L')
    cond_2 = fault_created
    cond_3 = (fault_location =='Interna')
    if  cond_1 & cond_2 & cond_3:
        
        short_circuit_level = 3 #current increases 3 times when a short-circuit occurs (arbitrary, needs correction with the protection study)
        
        after_pre_fault = tc_06ta2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_06ta2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_06ta2_s[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_06ta2_s[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_06ta2_t[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_06ta2_t[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_86ta2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_86ta2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_86ta2_s[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_86ta2_s[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_86ta2_t[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_86ta2_t[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_52a2_r[t_vec_fault_start_pos:]
        fault_values = [ 0 * x for x in after_pre_fault ]
        tc_52a2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_52a2_s[t_vec_fault_start_pos:]
        fault_values = [ 0 * x for x in after_pre_fault ]
        tc_52a2_s[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_52a2_t[t_vec_fault_start_pos:]
        fault_values = [ 0 * x for x in after_pre_fault ]
        tc_52a2_t[t_vec_fault_start_pos:] = fault_values
        
    cond_1 = (fault_type == 'Curto-circuito L-L-L')
    cond_2 = fault_created
    cond_3 = (fault_location =='Externa')
    if  cond_1 & cond_2 & cond_3:
        
        short_circuit_level = 1.4 #current increases 3 times when a short-circuit occurs (arbitrary, needs correction with the protection study)
        
        after_pre_fault = tc_06ta2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_06ta2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_06ta2_s[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_06ta2_s[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_06ta2_t[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_06ta2_t[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_86ta2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_86ta2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_86ta2_s[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_86ta2_s[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_86ta2_t[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_86ta2_t[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_52a2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_52a2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_52a2_s[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_52a2_s[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_52a2_t[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_52a2_t[t_vec_fault_start_pos:] = fault_values
        
    cond_1 = (fault_type == 'Curto-circuito L-L')
    cond_2 = fault_created
    cond_3 = (fault_location =='Interna')
    if  cond_1 & cond_2 & cond_3:
        
        short_circuit_level = 3 #current increases 3 times when a short-circuit occurs (arbitrary, needs correction with the protection study)
        
        after_pre_fault = tc_06ta2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_06ta2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_06ta2_s[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_06ta2_s[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_86ta2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_86ta2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_86ta2_s[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_86ta2_s[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_52a2_r[t_vec_fault_start_pos:]
        fault_values = [ 0 * x for x in after_pre_fault ]
        tc_52a2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_52a2_s[t_vec_fault_start_pos:]
        fault_values = [ 0 * x for x in after_pre_fault ]
        tc_52a2_s[t_vec_fault_start_pos:] = fault_values
        
    cond_1 = (fault_type == 'Curto-circuito L-L')
    cond_2 = fault_created
    cond_3 = (fault_location =='Externa')
    if  cond_1 & cond_2 & cond_3:
        
        short_circuit_level = 1.4 #current increases 3 times when a short-circuit occurs (arbitrary, needs correction with the protection study)
        
        after_pre_fault = tc_06ta2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_06ta2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_06ta2_s[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_06ta2_s[t_vec_fault_start_pos:] = fault_values
        tc_06ta2_t[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_86ta2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_86ta2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_86ta2_s[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_86ta2_s[t_vec_fault_start_pos:] = fault_values
        tc_86ta2_t[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_52a2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_52a2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_52a2_s[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_52a2_s[t_vec_fault_start_pos:] = fault_values
        
    cond_1 = (fault_type == 'Curto-circuito L')
    cond_2 = fault_created
    cond_3 = (fault_location =='Interna')
    if  cond_1 & cond_2 & cond_3:
        
        short_circuit_level = 3 #current increases 3 times when a short-circuit occurs (arbitrary, needs correction with the protection study)
        
        after_pre_fault = tc_06ta2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_06ta2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_86ta2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_86ta2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_52a2_r[t_vec_fault_start_pos:]
        fault_values = [ 0 * x for x in after_pre_fault ]
        tc_52a2_r[t_vec_fault_start_pos:] = fault_values
        
    cond_1 = (fault_type == 'Curto-circuito L-L')
    cond_2 = fault_created
    cond_3 = (fault_location =='Externa')
    if  cond_1 & cond_2 & cond_3:
        
        short_circuit_level = 1.4 #current increases 3 times when a short-circuit occurs (arbitrary, needs correction with the protection study)
        
        after_pre_fault = tc_06ta2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_06ta2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_86ta2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_86ta2_r[t_vec_fault_start_pos:] = fault_values
        
        after_pre_fault = tc_52a2_r[t_vec_fault_start_pos:]
        fault_values = [ short_circuit_level * x for x in after_pre_fault ]
        tc_52a2_r[t_vec_fault_start_pos:] = fault_values
    
    fault_created = False

# =============================================================================
# Oscilografia
# =============================================================================
expander_5 = st.beta_expander(label='Oscilografia')
with expander_5:
    st.header('Oscilografia')
    fig, axes = plt.subplots(nrows=9, ncols=1, sharex=True, figsize=(10,6),
                             sharey=True)
    # plotting
    axes[0].plot(pd.DataFrame({'IA-06TA2': tc_06ta2_r}, index=t_vec))
    axes[1].plot(pd.DataFrame({'IB-06TA2': tc_06ta2_s}, index=t_vec))
    axes[2].plot(pd.DataFrame({'IC-06TA2': tc_06ta2_t}, index=t_vec))
    axes[3].plot(pd.DataFrame({'IA-86TA2': tc_86ta2_r}, index=t_vec))
    axes[4].plot(pd.DataFrame({'IB-86TA2': tc_86ta2_s}, index=t_vec))
    axes[5].plot(pd.DataFrame({'IC-86TA2': tc_86ta2_t}, index=t_vec))
    axes[6].plot(pd.DataFrame({'IA-52-A2': tc_52a2_r}, index=t_vec))
    axes[7].plot(pd.DataFrame({'IB-52-A2': tc_52a2_s}, index=t_vec))
    axes[8].plot(pd.DataFrame({'IC-52-A2': tc_52a2_t}, index=t_vec))
    # labeling
    axes[0].set_ylabel('IA-06TA2 [A]', rotation=0, ha='right')
    axes[1].set_ylabel('IB-06TA2 [A]', rotation=0, ha='right')
    axes[2].set_ylabel('IC-06TA2 [A]', rotation=0, ha='right')
    axes[3].set_ylabel('IA-86TA2 [A]', rotation=0, ha='right')
    axes[4].set_ylabel('IB-86TA2 [A]', rotation=0, ha='right')
    axes[5].set_ylabel('IC-86TA2 [A]', rotation=0, ha='right')
    axes[6].set_ylabel('IA-52-A2 [A]', rotation=0, ha='right')
    axes[7].set_ylabel('IB-52-A2 [A]', rotation=0, ha='right')
    axes[8].set_ylabel('IC-52-A2 [A]', rotation=0, ha='right')
    # griding
    for ax in range(9):
        axes[ax].set_xticks(np.arange(0, t_final+.1, step=0.1))
        axes[ax].grid(which='both')
    
    st.write(fig)
