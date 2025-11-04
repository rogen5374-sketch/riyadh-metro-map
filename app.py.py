import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# تحميل البيانات
data = pd.read_excel("Book 1(ورقة1).xlsx")

# إعداد الخريطة (متمركزة على الرياض)
riyadh_center = [24.7136, 46.6753]
m = folium.Map(location=riyadh_center, zoom_start=12)

# إنشاء النقاط للمحطات
for station, group in data.groupby('station'):
    lat = group['lat'].mean()
    lon = group['lon'].mean()
    color = group['color'].iloc[0]

    # إعداد النص داخل النافذة المنبثقة
    popup_text = f"<b>{station}</b><br>"
    for _, row in group.iterrows():
        popup_text += f"{row['name']} ({row['category']})<br>⭐ {row['rating']} | 📍 {row['distance']} كم<br><br>"

    # إضافة النقطة للخريطة
    folium.CircleMarker(
        location=[lat, lon],
        radius=7,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.9,
        popup=folium.Popup(popup_text, max_width=300)
    ).add_to(m)

# واجهة Streamlit
st.title("خريطة مترو الرياض التفاعلية 🚇")
st.write("اضغط على المحطة لعرض الكافيهات والمطاعم القريبة 🍽️☕")

# عرض الخريطة
st_data = st_folium(m, width=800, height=600)
