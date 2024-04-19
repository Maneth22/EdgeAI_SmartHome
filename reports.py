import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import notification as nt






def dropdown():
    chart_type = st.selectbox(label="Choose Your Chart",options=["Line-Chart","Area-Chart","Bar-Chart"])
    df = pd.DataFrame(np.random.rand(10,2), columns = ["Days","kWh"])
    if chart_type == "Line-Chart":
        st.line_chart(df)
    elif chart_type == "Area-Chart":
        st.area_chart(df)
    elif chart_type == "Bar-Chart":
        st.bar_chart(df)





    # if selected == "Area-Chart":    
    #     st.area_chart(df)
    # if selected == "Bar-Charts":    
    #     st.bar_chart(df)








