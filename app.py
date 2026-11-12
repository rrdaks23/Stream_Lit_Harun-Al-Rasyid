import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman Utama
st.set_page_config(
    page_title="Portofolio Project & Coding",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- NAVIGASI SIDEBAR ---
st.sidebar.title("Navigasi Portofolio")
st.sidebar.markdown("---")
selected_page = st.sidebar.radio(
    "Pilih Halaman:",
    ["🏠 Beranda", "💻 Project Coding & Automation", "🌍 Project Lapangan & Spasial", "📞 Kontak & Tentang Saya"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tips:** Gunakan menu di atas untuk menjelajahi portofolio project analisis dan pemrograman saya.")

# ==========================================
# 1. HALAMAN BERANDA
# ==========================================
if selected_page == "🏠 Beranda":
    col1, col2 = st.columns([2, 1], gap="medium")
    
    with col1:
        st.title("Halo, Selamat Datang! 👋")
        st.markdown("""
        Selamat datang di web portofolio saya. Website ini dibangun menggunakan **Python** dan **Streamlit**, serta terhubung langsung dengan **GitHub** untuk menampilkan berbagai project pemrograman, analisis data spasial, dan studi lapangan yang telah saya kerjakan.
        
        **Fokus Keahlian & Minat:**
        * 🐍 **Pemrograman & Data Science:** Python, Google Colab, Automation, Machine Learning (Random Forest, dll.).
        * 🗺️ **Geospasial & Remote Sensing:** QGIS, ArcMap, Google Earth Engine API, Analisis NDVI/LST.
        * 💧 **Konservasi & Hidrologi:** Pemodelan Daerah Aliran Sungai (DAS), Konservasi Tanah dan Air (KTA), serta mitigasi lingkungan.
        """)
        
        st.markdown("### 🚀 Quick Stats")
        m1, m2, m3 = st.columns(3)
        m1.metric(label="Project Selesai", value="10+")
        m2.metric(label="Tools & Stack", value="Python, GEE, GIS")
        m3.metric(label="Status", value="Aktif & Terbuka Kolaborasi")

    with col2:
        st.markdown("### 📌 Navigasi Cepat")
        st.success("Jelajahi tab **Project Coding** untuk melihat script automasi dan machine learning, atau tab **Project Lapangan** untuk portofolio pemetaan dan studi kasus lingkungan.")

# ==========================================
# 2. HALAMAN PROJECT CODING & AUTOMATION
# ==========================================
elif selected_page == "💻 Project Coding & Automation":
    st.title("💻 Project Pemrograman & Automasi")
    st.markdown("Kumpulan skrip Python, pemrosesan data skala besar, dan model machine learning.")
    
    tab1, tab2 = st.tabs(["🤖 Machine Learning Spasial", "⚙️ Script Automasi Data"])
    
    with tab1:
        st.subheader("Random Forest untuk Analisis Biomassa & Lingkungan")
        st.markdown("""
        * **Deskripsi:** Pemodelan prediktif menggunakan Python di Google Colab dengan integrasi data citra satelit dan atribut spasial regresi.
        * **Tech Stack:** `Python`, `Google Earth Engine API`, `Scikit-learn`, `Pandas`
        """)
        
        df_dummy = pd.DataFrame({
            "Kecamatan/Wilayah": ["Wilayah A", "Wilayah B", "Wilayah C", "Wilayah D"],
            "Akurasi Model (%)": [85.4, 88.2, 91.0, 87.5]
        })
        fig = px.bar(df_dummy, x="Kecamatan/Wilayah", y="Akurasi Model (%)", color="Akurasi Model (%)", title="Perbandingan Akurasi Model Random Forest")
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Automasi Ekstraksi & Pengolahan Data Raster")
        st.markdown("""
        * **Deskripsi:** Skrip Python untuk otomatisasi unduh, kliping, dan ekspor data raster/tabular langsung ke Google Drive.
        * **Snippet Kode Utama:**
        """)
        st.code("""
        import geopandas as gpd
        import rasterio
        
        def process_spatial_data(shapefile_path):
            gdf = gpd.read_file(shapefile_path)
            print(f"Total fitur diproses: {len(gdf)}")
            return gdf.head()
        """, language="python")

# ==========================================
# 3. HALAMAN PROJECT LAPANGAN & SPASIAL
# ==========================================
elif selected_page == "🌍 Project Lapangan & Spasial":
    st.title("🌍 Project Lapangan & Analisis Spasial")
    st.markdown("Dokumentasi dan studi kasus project berbasis survei lapangan, analisis hidrologi, serta konservasi tanah dan air (KTA).")
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.markdown("### 💧 Analisis Hidrologi & DAS")
        st.markdown("""
        * **Studi Kasus:** Pemetaan kerentanan erosi dan zonasi penggunaan lahan menggunakan metode *Soil Conservation Service Curve Number* (SCS-CN).
        * **Output:** Peta tingkat bahaya erosi, rekomendasi tindakan konservasi tanah dan air, serta mitigasi limpasan permukaan.
        """)
        st.info("💡 *Gunakan GPS Garmin Montana / QGIS untuk validasi titik sampling lapangan.*")

    with col_p2:
        st.markdown("### 🌲 Monitoring Perubahan Tutupan Lahan")
        st.markdown("""
        * **Studi Kasus:** Evaluasi efektivitas kawasan penyangga ekosistem dan analisis Urban Heat Island (UHI) menggunakan deret waktu citra Sentinel & Landsat (2018–2026).
        * **Output:** Peta korelasi spasial antara indeks vegetasi (NDVI) dan suhu permukaan daratan (LST).
        """)
        st.warning("📊 *Dataset diproses secara terdistribusi menggunakan Google Earth Engine.*")

# ==========================================
# 4. HALAMAN KONTAK & TENTANG SAYA
# ==========================================
elif selected_page == "📞 Kontak & Tentang Saya":
    st.title("📞 Kontak & Kolaborasi")
    st.markdown("Tertarik untuk berdiskusi, berkolaborasi dalam project riset lingkungan, atau pengembangan web aplikasi data? Silakan hubungi saya melalui tautan di bawah ini:")
    
    col_c1, col_c2, col_c3 = st.columns(3)
    
    with col_c1:
        st.markdown("📧 **Email**")
        st.markdown("`aalrasyidharun420@gmail.com`")
        
    with col_c2:
        st.markdown("🐙 **GitHub**")
        st.markdown("[github.com/rrdaks23](https://github.com/rrdaks23)")
        
    with col_c3:
        st.markdown("💼 **LinkedIn**")
        st.markdown("[linkedin.com/in/harunalrasyid](https://linkedin.com)")
        
    st.markdown("---")
    st.caption("© 2026 • Dibangun dengan ❤️ menggunakan Python & Streamlit.")
