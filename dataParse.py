import streamlit as st
import requests
from flask import request, jsonify
import plotly.express as px
import pandas as pd
import json
import threading

#sidebar 1
with st.sidebar:
    selected = option_menu(
        menu_title = "Smart Home",
        options=["Dashboard","Notifications","Reports"],
        menu_icon=None,
        icons=["speedometer","bell","file-earmark"],
        default_index=0,
    )
    
    
    st.markdown('<div style="height: 200px;"></div>', unsafe_allow_html=True)
    
if selected == "Dashboard":
    st.markdown("## Dashboard")
    #db.dash_page()
if selected == "Notifications":
    st.markdown("## Notifications")
    nt.notify()
if selected == "Reports":
    st.markdown("## Reports")rpt.dropdown()


FinalTemp =[]




df_Current = pd.read_csv("Current.csv")
df_Temp = pd.read_csv("Temp.csv")

df_Temp["Temperature"] = df_Temp["Humidity"]


fig_col1, fig_col2 = st.columns(2)
with fig_col1:
                placeholder = st.empty()
                st.markdown("### Temperature Chart")
                fig = px.line(data_frame=df_Temp, y="Temperature", x="Time")
                st.write(fig)
                
with fig_col2:
                CurrentViewer = st.empty()
                st.markdown("### Current Chart")
                fig2 = px.density_heatmap(data_frame=df_Current, y="Current", x="Time")
                st.write(fig2)

#
# def thread_liveTemp():
#     tempThread =threading.Thread(target=getTemp)
#     #add_report_ctx(tempThread)
#     tempThread.start()
#     thread_liveTemp()
#     placeholder.write(FinalTemp)
#
#
#     #http://127.0.01:5000/ is from the flask api
#     response = requests.get("http://127.0.0.1:5000/send_data")
#     if response.status_code == 200:
#         try:
#             # Try to parse response JSON
#             data = response.json()
#             print(data)
#             st.write('Received data:', data)
#         except json.decoder.JSONDecodeError as e:
#             st.error('Failed to decode JSON: {}'.format(e))
#     else:
#         st.error('Failed to send request. Status code: {}'.format(response.status_code))
