import streamlit as st
import pandas as pd

st.title("Student Information Form")

name = st.text_input("Enter Your Name:")
fname = st.text_input("Enter Your Father's Name:")
adr = st.text_area("Enter Your Address:")
class_level = st.selectbox("Select Your Class:", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

submit_button = st.button("Submit Information")

if submit_button:
    st.subheader("Your Submitted Information:")
    st.markdown(f"*Name:* {name}")
    st.markdown(f"*Father's Name:* {fname}")
    st.markdown(f"*Address:* {adr}")
    st.markdown(f"*Class:* {class_level}")

    student_data = pd.DataFrame({
        'Name': [name],
        'Father\'s Name': [fname],
        'Address': [adr],
        'Class': [class_level]
    })
    st.subheader("Data in DataFrame:")
    st.dataframe(student_data)
    st.success("Information submitted successfully!")