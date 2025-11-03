import streamlit as st
import pandas as pd

st.title('Streamlit Text Input')
name = st.text_input("Enter your name : ")
if name:
    st.write(f"Hello, {name}")

age = st.slider("Select Your Age:",0,100,25)
st.write(f"Your Age is {age}")

options = ['python','c++','java','js']
choice = st.selectbox("choose your favorite language: ",options)
st.write(f"You seleted {choice}")

data = {
    "Name":['John', 'Jane', 'Jack', 'Jimmy', 'Jill'],
    "Age":[28,19,30,39,50],
    "City":['DELHI', 'KOCHI', 'MUMBAI', 'VENGARA', 'MALAPPURAM']
}
df = pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)

uploaded_file= st.file_uploader("choose a csv file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)