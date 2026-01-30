import streamlit as st
import numpy as np
from model import train

##Title
st.title("Hello World Ai App")
st.subheader("A simple regression model")

##Train the model
model=train()

#sidebar
st.sidebar.header("input Features")
input_value=st.sidebar.slider("select the value of x",1,10,1)

#prediction
input_array=np.array([[input_value]]) 
prediction=model.predict(input_array)

#Display the prediction
st.write(f'### input value : {input_value}')
st.write(f'### output value : {prediction[0]:.2f}')



             