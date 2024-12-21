# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:02:18 2023

@author: Vijesh Pethuram K
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import pickle
import numpy as np

st.set_page_config(page_title='Student Dropout Prediction')
st.title("Welcome to Student Dropout Prediction")
st.subheader('Find out whether a student will Dropout or Graduate instantly!')
st.header("")
st.subheader('Enter Student age:')
j=st.slider("Age",0,100,16)
st.subheader('Gender:')
h=st.radio("(Male/Female)",["Male", "Female"])
st.subheader('Enter Marital Status:')
a=st.radio("(Married/Unmarried)",["Married", "Unmarried"])
st.subheader('Pays Tuition fees regularly?')
g=st.radio("Is the student paying tuition fees regularly?",["Yes", "No"])
st.subheader('Preferred attendance timing:')
b=st.radio("(Day/Evening)",["Daytime", "Evening"])
st.subheader('Does the sudent have any Scholarship?')
i=st.radio("(If the student has scholarship)",["Yes", "No"])
st.subheader('Have any Previous qualification?')
c=st.radio("(If they have any previous educational qualificatons)",["Yes", "No"])
st.subheader('Displaced from other locations?')
d=st.radio("(If they got transferred)",["Yes", "No"])
st.subheader('Have any Special Educational needs?')
e=st.radio("(If any)",["Yes", "No"])
st.subheader('Is the students\' family in debt?')
f=st.radio("(If the student has any educational loans)",["Yes", "No"])
st.subheader('Is the student currently studying in ICSE?')
k=st.radio("(If the student studies in ICSE Board)",["Yes", "No"])
col1,col2=st.columns(2)
with col1:
    st.subheader("Enter Unemployment Rate: ")
    l=st.number_input("Unemployment Rate",0,100)
with col2:
    st.header("")
    st.metric("Current Unemployment Rate: ","12%","2%")


submit=st.button("Check for Dropout")

if submit:
    if a=="Married":
        a1=1
    else :
        a1=0
    if b=="Daytime":
        b1=0
    else :
        b1=1
    if c=="Yes":
        c1=1
    else :
        c1=0
    if d=="Yes":
        d1=1
    else :
        d1=0
    if e=="Yes":
        e1=1
    else :
        e1=0
    if f=="Yes":
        f1=1
    else :
        f1=0
    if g=="Yes":
        g1=1
    else :
        g1=0
    if h=="Male":
        h1=0
    else :
        h1=1
    if i=="Yes":
        i1=1
    else :
        i1=0
    j1=j
    if k=="Yes":
        k1=1
    else :
        k1=0
    l1=l
    
    
        
       
    st.title("Predicted Results 📃")    
    try:
        loaded_model=pickle.load(open("/mount/src/studentdropoutanalysis/Dropout_model.sav" ,'rb'))
    except Exception as e:
        st.error("Sorry! The Model could not be loaded correctly as Pickle filea are not supported on the Streamlit hosting server.)")
        raise e

    def droppred(inputarr):
        nparr=np.asarray(inputarr)
        print(nparr)
        nparr=nparr.astype('float32')
        nparr=nparr.reshape(1,-1)
        pred=loaded_model.predict(nparr)
        return pred
    
    res=droppred([a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1])
    if(res[0]==0):
        st.balloons()
        st.header("Congratulations 🎉")
        st.success("The student is most likely to graduate.")
    else:
        st.header("Sorry! 😢")
        st.warning("The student is most likely to dropout. Kindly pay attention to him.")  

