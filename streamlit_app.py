import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('model.pkl', 'rb')) 
#Our trained model is loaded from model.pkl file

col0, col1, col2, col3, col4, col5, col6 = st.columns(7)
with col0:
    st.write('')
with col1:
    st.write('')
with col2:
    st.write('')    
with col3:
    st.title("Iris") 
    # in the app layout, the title Iris is centred...
with col4:
    st.write('')
with col5:
    st.write('')
with col6:
    st.write('')
    # this part in the code simply focuses on app layout.

col7, col8, col9 = st.columns(3)
with col7:
    st.write('')    
with col8:
    st.markdown("<h6 style='text-align: center;'>Welcome to Iris. A simple web app to predict Iris species</h6>", unsafe_allow_html=True)
    # A message that welcomes the user to  the app. 
with col9:
    st.write('')


s_length = st.slider('Enter Sepal Length', 4.0, 8.0)
s_width = st.slider('Enter Sepal Width', 2.0, 5.0)
p_length = st.slider('Enter Petal Length', 1.0, 7.0)
p_width = st.slider('Enter Petal Width', 0.1, 3.0)

#using widgets called sliders so that user can input the varying lengths. The range should align with what has been used to train the model.


col10, col11, col12, col13, col14 = st.columns(5)
with col10:
    st.write('')
with col11:
    st.write('')    
with col12:
    predict_btn = st.button('Predict Iris Species')
with col13:
    st.write('')
with col14:
    st.write('')

# species_names = ['Iris-setosa','Iris-versicolor','Iris-virginica']

if(predict_btn):
    inp1 = float(s_length)
    inp2 = float(s_width)
    inp3 = float(p_length)
    inp4 = float(p_width)
    
    X = [inp1, inp2, inp3, inp4]

    species = model.predict(X)

    # predicted_species = species_names[species_index]

    col15, col16, col17 = st.columns(3)
    with col15:
        st.write('')    
    with col16:
        st.text(f"Predicted Iris Species: {species[0]}")
    with col17:
        st.write('')


