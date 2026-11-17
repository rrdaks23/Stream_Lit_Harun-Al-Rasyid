import streamlit as st
from pathlib import Path
import folium
from streamlit_folium import st_folium

st.subheader("🛰️ Lokasi & Basis Spasial — Kota Payakumbuh")

m = folium.Map(
    location=[-0.2202, 100.6308],
    zoom_start=13,
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Tiles &copy; Esri &mdash; Source: Esri, Maxar, Earthstar Geographics, and the GIS User Community"
)

folium.Marker(
    location=[-0.2202, 100.6308],
    popup="Kota Payakumbuh, Sumatera Barat",
    tooltip="Kota Payakumbuh",
    icon=folium.Icon(color="green", icon="leaf")
).add_to(m)

# returned_objects=[] mencegah halaman reload ulang saat peta digeser/di-zoom
st_folium(m, use_container_width=True, height=320, returned_objects=[])

# Path dinamis agar aman saat deploy di Windows maupun Linux (Streamlit Cloud)
BASE_DIR = Path(__file__).parent
FOTO_PATH = BASE_DIR / "assets" / "foto_profil.jpg"
CV_PATH = BASE_DIR / "assets" / "Harun_CV.pdf"

st.sidebar.info("💡 **Tips:** Pilih halaman di atas untuk menjelajahi galeri project analisis, riset lapangan, dan kontak.")

# --- HERO SECTION ---
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.title("Halo, Selamat Datang! 👋")
    st.markdown("""
    Selamat datang di web portofolio saya. Website ini dibangun menggunakan **Python** dan **Streamlit**, 
    serta terhubung langsung dengan **GitHub** untuk menampilkan berbagai project pemrograman, 
    analisis data spasial, dan studi lapangan yang telah saya kerjakan.
    """)

    # Tombol Unduh CV jika file sudah tersedia di folder assets/
    if CV_PATH.exists():
        with open(CV_PATH, "rb") as pdf_file:
            st.download_button(
                label="📄 Unduh CV (PDF)",
                data=pdf_file,
                file_name="CV_Harun_Al_Rasyid.pdf",
                mime="application/pdf"
            )

    st.subheader("Fokus Keahlian & Minat")
    st.markdown("""
    * 🐍 **Pemrograman & Data Science:** Python, Google Colab, Automation, Machine Learning (Random Forest, dll.).
    * 🗺️ **Geospasial & Remote Sensing:** QGIS, ArcMap, Google Earth Engine API, Analisis NDVI/LST.
    * 💧 **Konservasi & Hidrologi:** Pemodelan Daerah Aliran Sungai (DAS), Konservasi Tanah dan Air (KTA), serta mitigasi lingkungan.
    """)

with col2:
    if FOTO_PATH.exists():
        st.image(str(FOTO_PATH), use_container_width=True)
    else:
        st.info("📌 Letakkan foto profil Anda di `assets/foto_profil.jpg` agar tampil di sini.")
    
    st.success("Gunakan menu **Galeri Proyek** di sidebar kiri untuk melihat studi kasus coding, machine learning, dan pemetaan spasial.")

st.divider()

# --- QUICK STATS ---
st.subheader("🚀 Quick Stats")
m1, m2, m3 = st.columns(3)
m1.metric(label="Project Selesai", value="10+")
m2.metric(label="Tools & Stack", value="Python, GEE, GIS")
m3.metric(label="Status", value="Aktif & Terbuka Kolaborasi")