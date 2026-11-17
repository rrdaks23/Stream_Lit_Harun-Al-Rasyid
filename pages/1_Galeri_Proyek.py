import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from data.projects import PROJECTS

st.set_page_config(page_title="Galeri Proyek", page_icon="💻", layout="wide")

BASE_DIR = Path(__file__).parent.parent

st.title("💻 Galeri Project & Studi Kasus")
st.markdown("Kumpulan skrip Python, pemodelan machine learning, dan analisis spasial.")

# --- FILTER KATEGORI ---
kategori_list = ["Semua"] + sorted(list(set(p["kategori"] for p in PROJECTS)))
pilihan_kategori = st.selectbox("Filter berdasarkan kategori:", kategori_list)

filtered_projects = (
    PROJECTS if pilihan_kategori == "Semua"
    else [p for p in PROJECTS if p["kategori"] == pilihan_kategori]
)

st.divider()

# --- RENDER KARTU PROYEK ---
for proj in filtered_projects:
    with st.container(border=True):
        col_img, col_desc = st.columns([1, 2], gap="medium")
        
        with col_img:
            thumb_path = BASE_DIR / proj["thumbnail"]
            if thumb_path.exists():
                st.image(str(thumb_path), use_container_width=True)
            else:
                st.caption(f"🖼️ Pratinjau gambar: `{proj['thumbnail']}`")

        with col_desc:
            st.subheader(proj["judul"])
            st.caption(f"Kategori: **{proj['kategori']}** | Tahun: **{proj['tahun']}**")
            st.write(proj["ringkasan"])
            st.markdown(f"**Output Utama:** {proj['output']}")
            st.markdown("**Tech Stack:** " + " ".join([f"`{t}`" for t in proj["tools"]]))

            # Tautan GitHub / Google Colab
            btn_col1, btn_col2 = st.columns(2)
            if proj["repo_url"]:
                btn_col1.link_button("🐙 Lihat Kode di GitHub", proj["repo_url"])
            if proj["colab_url"]:
                btn_col2.link_button("📒 Buka di Google Colab", proj["colab_url"])

        # --- LIVE DEMO / OUTPUT INTERAKTIF KHUSUS ---
        if proj["demo_type"] == "plotly_rf":
            with st.expander("📊 Lihat Grafik Perbandingan Akurasi Model"):
                df_dummy = pd.DataFrame({
                    "Kecamatan/Wilayah": ["Wilayah A", "Wilayah B", "Wilayah C", "Wilayah D"],
                    "Akurasi Model (%)": [85.4, 88.2, 91.0, 87.5]
                })
                fig = px.bar(
                    df_dummy,
                    x="Kecamatan/Wilayah",
                    y="Akurasi Model (%)",
                    color="Akurasi Model (%)",
                    title="Perbandingan Akurasi Model Random Forest"
                )
                st.plotly_chart(fig, use_container_width=True)

        elif proj["demo_type"] == "code_snippet":
            with st.expander("⚙️ Lihat Snippet Kode Automasi"):
                st.code("""
import geopandas as gpd
import rasterio

def process_spatial_data(shapefile_path):
    gdf = gpd.read_file(shapefile_path)
    print(f"Total fitur diproses: {len(gdf)}")
    return gdf.head()
                """, language="python")