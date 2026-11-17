import streamlit as st
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Portofolio Project & Coding",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1. Render peta Esri World Imagery (Leaflet) di dalam iframe tersembunyi (height=0)
esri_bg_html = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <style>
    html, body, #map { margin: 0; padding: 0; width: 100%; height: 100%; }
  </style>
</head>
<body>
  <div id="map"></div>
  <script>
    var map = L.map('map', {
      center: [-0.2202, 100.6308], // Koordinat Kota Payakumbuh
      zoom: 13,
      zoomControl: false,
      attributionControl: false
    });
    L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 19
    }).addTo(map);
  </script>
</body>
</html>
"""
components.html(esri_bg_html, height=0)

# 2. CSS untuk memperluas iframe peta ke seluruh layar & membuat kontainer teks semi-transparan
st.markdown("""
<style>
    iframe[height="0"] {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw !important;
        height: 100vh !important;
        z-index: 0;
        border: none;
        pointer-events: none;
    }
    [data-testid="stAppViewContainer"] {
        background: transparent;
    }
    [data-testid="stHeader"] {
        background: rgba(255, 255, 255, 0.6);
    }
    [data-testid="stMainBlockContainer"], .block-container {
        position: relative;
        z-index: 1;
        background-color: rgba(255, 255, 255, 0.88);
        border-radius: 16px;
        padding: 2rem 2.5rem;
        margin-top: 1.5rem;
        margin-bottom: 2rem;
        backdrop-filter: blur(4px);
    }
</style>
""", unsafe_allow_html=True)

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