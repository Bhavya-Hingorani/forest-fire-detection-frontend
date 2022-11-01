import time

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import json

# callMeBack = '{\n  "Temperature": "38.671875"\n  "flameDetected": "1"\n}'

temperoryPayloads = []

def loadData():
    return

def payloadToJson(payload):
    temperoryPayloads.append(json.loads(payload))

def customCallback(client,userdata,message):
    print("callback came...")
    print(message.payload)
    payloadToJson(message.payload)

def awsSetup():
    myMQTTClient = AWSIoTMQTTClient("esp8266")
    myMQTTClient.configureEndpoint("a15nnjmmep15h-ats.iot.ap-south-1.amazonaws.com", 8883)
    myMQTTClient.configureCredentials("./AmazonRootCA1.pem","./363b250b3ae29bd15178cdab168e689e1e541eeb1f55822de9e0fedd517f1c8b-private.pem.key", "./363b250b3ae29bd15178cdab168e689e1e541eeb1f55822de9e0fedd517f1c8b-certificate.pem.crt")
    return myMQTTClient

def awsConnection(myMQTTClient):
    myMQTTClient.connect()
    print("Client Connected")

    myMQTTClient.subscribe("outTopic", 1, customCallback)
    print('waiting for the callback. Click to conntinue...')
    x = input()

    myMQTTClient.unsubscribe("outTopic")
    print("Client unsubscribed")

    myMQTTClient.disconnect()
    print("Client Disconnected")

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

def streamlitPage():

    df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [19.0454853, 72.8888644],
    columns=['lat', 'lon'])

    st.title("Real-Time Sensor data dashboard")
    placeholder = st.empty()

    for seconds in range(200):

        with placeholder.container():

            kpi1, kpi2, kpi3 = st.columns(3)

            kpi1.metric(
                label="Total sensor count",
                value=round(80),
            )
            
            kpi2.metric(
                label="Active sensor percentage",
                value=int(round((75/80)*100)),
            )
            
            kpi3.metric(
                label="Fire detected",
                value=f"false",
            )

            fig_col1, fig_col2 = st.columns(2)
            with fig_col1:
                st.markdown("### First Chart")
                fig = px.histogram(data_frame=df, x="lat")
                st.write(fig)
                
            with fig_col2:
                st.markdown("### Second Chart")
                st.map(df)

            st.markdown("### Detailed Data View")
            time.sleep(1) 

awsConnection(awsSetup())
loadData() 
streamlitPage()