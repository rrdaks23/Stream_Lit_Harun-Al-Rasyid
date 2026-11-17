import streamlit as st

st.set_page_config(page_title="Pengalaman & Riset", page_icon="🌍", layout="wide")

st.title("🌍 Pengalaman Lapangan & Metodologi Riset")
st.markdown("Ringkasan alur kerja penelitian dari akuisisi data lapangan hingga pemodelan komputasi.")

col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container(border=True):
        st.subheader("🛰️ Pemrosesan Cloud & Remote Sensing")
        st.markdown("""
        * Pemrosesan citra satelit multitemporal (**Sentinel-2 & Landsat**) secara terdistribusi melalui **Google Earth Engine (GEE)**.
        * Ekstraksi parameter biofisik seperti indeks vegetasi (**NDVI**) dan suhu permukaan daratan (**LST**) untuk analisis *Urban Heat Island* (UHI).
        * Pelatihan model *Machine Learning* (**Random Forest**) menggunakan Google Colab untuk estimasi biomassa dan tutupan lahan.
        """)

with col2:
    with st.container(border=True):
        st.subheader("🧭 Survei Lapangan & Konservasi Tanah dan Air")
        st.markdown("""
        * Validasi titik koordinat sampel lapangan dan pemetaan batas lahan menggunakan **GPS Garmin Montana** dan **QGIS**.
        * Pemodelan hidrologi Daerah Aliran Sungai (DAS) menggunakan metode **SCS-CN** untuk evaluasi limpasan permukaan.
        * Perencanaan teknik **Konservasi Tanah dan Air (KTA)** sipil maupun vegetatif berdasarkan tingkat bahaya erosi.
        """)