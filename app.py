import streamlit as st
import pickle
import numpy as np
import pandas as pd
model=pickle.load(open("model.pkl",'rb'))
d={'M':1,"L":2,'H':3}
def predict(new_data):
    predict=model.predict(new_data)
    st.write(predict[0])
def main():
    st.title("Predictive Maintenance in Manufacturing")
    st.write("This is an model which is reducet the downtime for maintenance by predict the maintenance need at earlier")
    i=st.text_input("Enter type of the machine M or L or H")
    AT=st.text_input("Enter Air temperature[k]")
    PT=st.text_input("Enter Process temperature[k]")
    RS=st.text_input("Enter Rotational Speed[rpm]")
    To=st.text_input("Enter Torque[nm]")
    TW=st.text_input("ToolWear[min]")
    if i in d:
        i=d[i]
    new_data = pd.DataFrame([[i,AT,PT,RS,To,TW]], columns=["Type","Air temperature [K]","Process temperature [K]","Rotational speed [rpm]","Torque [Nm]","Tool wear [min]"])
    v=""
    if st.button('Perticition'):
        v=predict(new_data)
if __name__=='__main__':
    main()
