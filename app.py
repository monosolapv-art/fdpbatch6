import streamlit as st
st.title("Students registration form")   
name = st.text_input(" Enter name of student")
branch = st.selectbox("Select branch", ["CSE", "ECE", "MECH", "CIVIL", "EEE"])
marks = st.number_input(" Enter your marks",0,100)
age = st.slider("Select your age", 20, 100, 18)
skills = st.multiselect("Select your skills", ["Python", "Java", "C++", "JavaScript", "HTML", "CSS"])   
gender = st.radio("Select your gender", ["Male", "Female", "Other"])   
option_subjects = st.checkbox("do you want to choose optional subjects?, ["cloude computing", "data science", "cyber security", "ai", "iot"])   "),   
if st.button("Submit"): 
    st.success("registered successfully!")    
    st.write( name)
    st.write( branch)
    st.write( marks)    
