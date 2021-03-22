import streamlit as st 
import numpy as np 
import pandas as pd 
import time

import json
import seaborn as sns
import matplotlib 
import matplotlib.pyplot as plt
from matplotlib import style
matplotlib.use('Agg')
from fbprophet import Prophet

plt.style.use('ggplot')
plt.style.use('fivethirtyeight')
plt.rc('font', family='Malgun Gothic')

plt.rc('axes', unicode_minus=False)
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

df = pd.read_csv('data/seoulCOVID19.csv')


def main() :
    st.markdown('# 서울 코로나 확진자 예측 앱')
    st.sidebar.radio(' ', ['여행나라 현황', '감염경로 현황', '지역별 확진자 현황'])

    fig = plt.figure()
    sns.countplot(data = df, y ='여행력', order= df['여행력'].value_counts().head(15).index)
    st.pyplot(fig)

    fig1 = plt.figure(figsize=(10,10))
    sns.countplot(data = df, y ='지역', order= df['지역'].value_counts().index)
    st.pyplot(fig1)

    fig3 = plt.figure(figsize=(10,13))
    sns.countplot(data = df, y ='접촉력', order= df['접촉력'].value_counts().head(15).index)
    plt.xticks(rotation = 45)
    st.pyplot(fig3)

    fig7 = plt.figure(figsize=(5,10))
    plt.pie(df['상태'].value_counts(), labels = df['상태'].value_counts().index, autopct='%.2f', startangle=90, counterclock=False, wedgeprops={'width':0.7})
    st.pyplot(fig7)

    df.index = pd.DatetimeIndex(df['확진일'])
    day_df = df.resample('D').size()
    
    fig4 = plt.figure()
    plt.plot(day_df)
    st.pyplot(fig4)

    df_prophet_day = day_df.reset_index()
    df_prophet_day.columns = [ 'ds' , 'y' ]


    

    my_bar = st.progress(0)
    with st.spinner('Predict...') :
        time.sleep(5)
    for percent_complete in range(100):
        
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1) 




    # m = Prophet()
    # m.fit(df_prophet_day)
    # future = m.make_future_dataframe(periods= 365, freq='D')
    # forecast = m.predict(future)
  
    

    # fig5 = m.plot(forecast,xlabel='Date', ylabel='확진자')
    # st.pyplot(fig5)

    # fig6 = m.plot_components(forecast)
    # st.pyplot(fig6)






if __name__ == '__main__' :
    main() 