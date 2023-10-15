import streamlit as st
import pickle
import numpy as np
import pandas as pd

hide_st_style = """
                <style>
                #MainMenu {visibilty:hidden;}
                .st-emotion-cache-cio0dv.ea3mdgi1{visibilty:hidden;}
                footer {visibilty:hidden;}
                <style>
                """
st.markdown(hide_st_style,unsafe_allow_html=True)

pipe = pickle.load(open("loan_pipe.pkl","rb"))
df = pickle.load(open("loan_data.pkl","rb"))
st.image("Photo.png")
st.title("Loan Status Predictor")

col1, col2, col3 = st.columns(3)

#Gender
with col1:
    Gender = st.selectbox("Gender",["Male","Female"])
# Married
with col2:
    Married = st.selectbox("Married",df["Married"].unique())
#Dependents
with col3:
    Dependents = st.selectbox("Dependents",[0,1,2,3,"3+"])
# Education
with col1:
    Education = st.selectbox("Education",df["Education"].unique())
# Self_Employed
with col2:
    Self_Employed = st.selectbox("Self Employed",["No","Yes"])
#ApplicantIncome
with col3:
    ApplicantIncome = st.number_input("Applicant Income ($)",min_value=0)
#CoapplicantIncome
with col1:
    CoapplicantIncome = st.number_input("Coapplicant Income ($)",min_value=0)
# LoanAmount
with col2:
    LoanAmount = st.number_input("Loan Amount ($)",min_value=0)
# Loan_Amount_Term	
with col3:
    Loan_Amount_Term = st.number_input("Loan Amount Term (Months)",min_value=0)
# Credit_History	
with col1:
    Credit_History = st.selectbox("Credit History",[0,1])
# Property_Area
with col2:
    Property_Area = st.selectbox("Property Area",df["Property_Area"].unique())
# Button
if st.button("Check_Status"):
    if Dependents  == "3+":
        Dependents = 4
    else:
        Dependents = Dependents
    data = [[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]]
    query = pd.DataFrame(data,columns=["Gender","Married","Dependents","Education","Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History","Property_Area"])
    
    if pipe.predict(query)[0] == 1:
        st.success("Loan is Approved")
        st.balloons()
    else:
        st.warning("Loan is not Approved")
    

