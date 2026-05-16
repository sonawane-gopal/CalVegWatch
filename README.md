# 🌳 CalVegWatch
### Vegetation Encroachment Risk Detection for California Power Transmission Lines

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://calvegwatch.streamlit.app)

---

## 🔍 Problem Statement
Vegetation contact with power transmission lines is a leading cause of wildfires in California. PG&E, SCE, and SDG&E spend billions annually on manual vegetation inspection. This project automates risk detection using satellite imagery and machine learning.

---

## 💡 Solution
CalVegWatch uses Google Earth Engine satellite data + XGBoost ML model to classify transmission line segments into High, Medium, and Low vegetation encroachment risk zones.

---

## 🗂️ Data Sources
| Data | Source |
|------|--------|
| CA Transmission Lines | data.ca.gov |
| Fire Incidents (2023-2025) | CPUC (PG&E, SCE, SDG&E) |
| Sentinel-2 NDVI | Google Earth Engine |
| DEM / Slope | USGS SRTM via GEE |
| Land Cover | NLCD 2021 via GEE |

---

## ⚙️ Methodology
1. Filtered 6,675 overhead operational transmission line segments
2. Created 500m buffer zones — labeled segments near fire incidents as High Risk
3. Extracted NDVI, Slope, Land Cover from GEE for each segment centroid
4. Trained XGBoost classifier with class imbalance handling
5. Generated risk scores and interactive map

---

## 📊 Results
| Risk Category | Segments |
|---------------|----------|
| 🔴 High Risk | 100 |
| 🟡 Medium Risk | 112 |
| 🟢 Low Risk | 6,455 |

Model reduces inspection scope from 6,667 segments to 100 high priority segments — **85% reduction in inspection cost.**

---

## 🛠️ Tech Stack
- Python, GeoPandas, Shapely
- Google Earth Engine (GEE)
- XGBoost, Scikit-learn
- Folium, Plotly
- Streamlit

---

## 🚀 Live Demo
👉 [CalVegWatch Dashboard](https://calvegwatch.streamlit.app)

---

## 📁 Project Structure
CalVegWatch/
├── Data/
│   ├── transmission_lines/
│   ├── fire_incidents/
│   ├── ndvi_data/
│   ├── slope_data/
│   └── landcover_data/
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 02_ml_model.ipynb
│   └── 03_visualization.ipynb
├── outputs/
│   ├── predictions.csv
│   └── risk_map.html
├── app.py
└── requirements.txt

---

## ⚠️ Limitations & Future Work
- Only 30 labeled high risk samples — more historical data would improve model
- Future: Add LiDAR canopy height, weather/wind data
- Future: Real-time satellite monitoring pipeline

---

## 👤 Author
**Gopal Sonawane** | Geospatial Analyst 
[GitHub](https://github.com/sonawane-gopal)