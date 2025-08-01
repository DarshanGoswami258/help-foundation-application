
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# First let's load the instances that we created

with open('scaler.joblib','rb') as file:
    scale = joblib.load(file)

with open('pca.joblib','rb') as file:
    scale = joblib.load(file)

with open('final_model.joblib','rb') as file:
    scale = joblib.load(file)

def prediction(input_list):
    scaled_input = scale.transform([input_list])
    pca_input = pca.transform(scaled_input)
    output = model.predict(pca_layout)[0]

    if output==0:
        return 'Developed'
    elif output==1:
        return 'Under-Developed'
    else:
        return 'Developing'

def main():
    st.title('HELP NGO FOUNDATION')
    st.subheader('This application will give the status of a country based on socio_economic and health factours')

    gdp = st.text_input('Enter the GDP per population of a Country')
    inc = st.text_input('Enter the per capital income of a Country')
    imp = st.text_input('Enter the Import in terms of % of GDP')
    exp = st.text_input('Enter the Exports in terms of % of GDP')
    inf = st.text_input('Enter the inflation rate in a country (%)')

    hel = st.text_input('Enter the expenditure on health in terms % of GDP')
    ch_m = st.text_input('Enter the no of deaths per 1000 births for < 5 yrs')
    fer = st.text_input('Enter the avg children born to a women in a country')
    lf = st.text_input('Enter the avg life expectancy in a country')

    in_data = [ch_m, exp, hel, imp, inc, inf,lf, fer,gdp]

    if st.button('predict'):
        response = prediction(in_data)
        st.sucess(response)

if __name__=='__main__':
    main()
