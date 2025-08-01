import streamlit as st
import pandas as pd
import pickle as pk


model=pk.load(open('model.pkl','rb'))
sc=pk.load(open('sc.pkl','rb'))


st.header('Loan Prediction app')


no_of_dep=st.slider('Choose no of dependents',0,5)
grad=st.selectbox('Choose Education',['Graduated','Not Graduated'])
self_emp=st.selectbox('Self Employed',['Yes','No'])
Annual_Income=st.slider('Choose Annual_Income',0,10000000)
Loan_Amount=st.slider('Choose Loan Amount',0,10000000)
Loan_term=st.slider('Choose Loan Term',0,20)
cibil_score=st.slider('Choose Cibil Score',0,1000)
Assets=st.slider('Choose Assets',0,10000000)


if grad =='Graduated':
    grad_s=0
else:
    grad_s=1

if self_emp == 'No':
    emp_s=1
else:
    emp_s=0

if st.button('Predict'):
    pred_data=pd.DataFrame([[no_of_dep,grad_s,emp_s,Annual_Income,Loan_Amount,Loan_term,cibil_score,Assets]],columns=['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','cibil_score','assets'])

    pred_data_scaled=sc.transform(pred_data)
    predict=model.predict(pred_data_scaled)

    if predict[0] == 1:
        st.markdown('Loan is Approved')
    else:
        st.markdown('Loan is Rejected')