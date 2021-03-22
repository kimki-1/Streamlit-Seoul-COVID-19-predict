import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt 
from datetime import datetime
import pandas as pd 
import numpy as np 

# API 호출을 위한 라이브러리 임포트 
import requests

# 프로펫 라이브러리 임포트
from fbprophet import Prophet

def main() :

    res = requests.get('http://openapi.seoul.go.kr:8088/52547970526b67773131396f4e734266/json/Corona19Status/1/99/')

    res_data = res.json()
    st.write(res_data)

    for data in res_data :
        st.write( data )

    

if __name__ == '__main__' :
    main() 
