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
    st.markdown("## Reports")
    rpt.dropdown()
