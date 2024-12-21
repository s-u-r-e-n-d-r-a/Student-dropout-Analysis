# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:34:01 2023

@author: Vijesh Pethuram K
"""


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.header("Customized Analysis 📈")
dataset=st.file_uploader("Upload your own dropout data to analyze",type='.csv')

if dataset is not None:
    df = pd.read_csv(dataset)


    st.dataframe(df)
    colum=list(df.columns)
    target=st.selectbox('Choose a target: ',colum)
    col2=colum.copy()
    col2.remove(target)
    x_var=st.selectbox('Choose a X variable: ',col2)
    y_var=st.selectbox('Choose a Y variable: ',col2)
    
    fig=px.scatter(df,x=x_var,y=y_var,color=target)
    st.plotly_chart(fig)
    
else:
    st.write("Please upload your data to continue.")
    
