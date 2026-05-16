import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CalVegWatch", layout="wide")

st.title("🌳 CalVegWatch")
st.subheader("Vegetation Encroachment Risk Detection — California Transmission Lines")

# Load data
df = pd.read_csv(r"D:\Profession\My_Space\DS\ML\My_Projects\Vegetation_Encroachment_Risk_Detection_California_Transmission_Lines\outputs\predictions.csv")

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Segments", "6,667")
col2.metric("High Risk", "100")
col3.metric("Medium Risk", "112")
col4.metric("Low Risk", "6,455")

st.markdown("---")

# Map — load pre-saved HTML directly
st.markdown("### 🗺️ Risk Map")
with open(r"D:\Profession\My_Space\DS\ML\My_Projects\Vegetation_Encroachment_Risk_Detection_California_Transmission_Lines\outputs\risk_map.html", encoding='utf-8') as f:
    map_html = f.read()
st.components.v1.html(map_html, height=600)

st.markdown("---")

# Feature charts
st.markdown("### 📊 Feature Analysis by Risk Category")

col1, col2 = st.columns(2)
with col1:
    fig1 = px.box(df, x='risk_category', y='NDVI', color='risk_category',
                  title='NDVI by Risk Category',
                  color_discrete_map={'High':'red','Medium':'orange','Low':'green'})
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.box(df, x='risk_category', y='slope', color='risk_category',
                  title='Slope by Risk Category',
                  color_discrete_map={'High':'red','Medium':'orange','Low':'green'})
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    fig3 = px.histogram(df, x='landcover', color='risk_category',
                        title='Land Cover Distribution by Risk',
                        color_discrete_map={'High':'red','Medium':'orange','Low':'green'})
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    fig4 = px.scatter(df, x='NDVI', y='slope', color='risk_category',
                      title='NDVI vs Slope',
                      color_discrete_map={'High':'red','Medium':'orange','Low':'green'})
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# High risk table
st.markdown("### 🔴 Top 20 High Risk Segments")
high_risk = df[df['risk_category'] == 'High'][['kV', 'NDVI', 'slope', 'landcover', 'risk_score']].sort_values('risk_score', ascending=False).head(20)
st.dataframe(high_risk, use_container_width=True)