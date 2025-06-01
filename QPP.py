import streamlit as st


import pickle
import numpy as np

#import model
log_model=pickle.load(open('log_model.pkl','rb'))
new_train3=pickle.load(open('new_train3.pkl','rb'))

st.title("Purchase Predictor")



#timeonsite
time=st.number_input("Time on site")

#page_viewed
page_viewed=st.number_input("Pages viewed")

#clickedad
Clicked_ad=st.selectbox('Clicked_ad',['no','yes'])

#Cart_value
Cart_value=st.number_input("Cart value")

#Browser_Refresh_Rate
Browser_Refresh_Rate=st.number_input("Browser refresh rate")
if st.button("Predict Purchase"):
     if Clicked_ad == 'yes':
        Clicked_ad = 1
     else:
        Clicked_ad = 0

     query=np.array([time,page_viewed,Clicked_ad,Cart_value,Browser_Refresh_Rate])
     query=query.reshape(1,5)
     st.title(log_model.predict(query))



