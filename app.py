import streamlit as st
from pathlib import Path
from PIL import Image, UnidentifiedImageError
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Portofolio Project & Coding",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1. Render peta Esri World Imagery (Leaflet)
esri_bg_html = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <style>
    html, body, #map {
      margin: 0;
      padding: 0;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
    }
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

    // Otomatis muat ulang seluruh tile satelit begitu ukuran iframe melebar ke layar penuh
    const resizeObserver = new ResizeObserver(() => {
      map.invalidateSize();
    });
    resizeObserver.observe(document.getElementById('map'));
  </script>
</body>
</html>
"""
components.html(esri_bg_html, height=0)

# 2. CSS untuk menempatkan iframe peta di lapisan paling belakang & membuat latar belakang Streamlit transparan
st.markdown("""
<style>
    /* Paksa semua variasi selektor iframe Streamlit menjadi latar belakang layar penuh */
    iframe[title="st.iframe"],
    [data-testid="stIFrame"],
    .stHtml iframe,
    iframe[height="0"] {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: -1 !important;
        border: none !important;
        pointer-events: none !important;
    }

    /* Hilangkan ruang kosong sisa komponen HTML di atas judul */
    [data-testid="stElementContainer"]:has(iframe) {
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Buat seluruh lapisan dasar Streamlit transparan agar peta di z-index: -1 terlihat */
    .stApp,
    [data-testid="stApp"],
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        background: transparent !important;
        background-color: transparent !important;
    }

    [data-testid="stHeader"] {
        background: rgba(255, 255, 255, 0.5) !important;
    }

    /* Kontainer konten utama semi-transparan di atas peta (tanpa z-index agar tidak mengunci iframe) */
    [data-testid="stMainBlockContainer"],
    .block-container {
        background-color: rgba(255, 255, 255, 0.85) !important;
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
        try:
            img = Image.open(FOTO_PATH)
            st.image(img, use_container_width=True)
        except UnidentifiedImageError:
            st.warning("⚠️ File `assets/foto_profil.jpg` rusak atau bukan format JPG/PNG yang valid.")
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