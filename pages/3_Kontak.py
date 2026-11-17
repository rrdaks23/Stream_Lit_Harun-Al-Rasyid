import streamlit as st

st.set_page_config(page_title="Kontak & Kolaborasi", page_icon="📞", layout="wide")

st.title("📞 Kontak & Kolaborasi")
st.markdown("Tertarik untuk berdiskusi, berkolaborasi dalam project riset lingkungan, atau pengembangan web aplikasi data? Silakan hubungi saya melalui tautan di bawah ini:")

col_c1, col_c2, col_c3 = st.columns(3)

with col_c1:
    with st.container(border=True):
        st.markdown("📧 **Email**")
        st.markdown("`aalrasyidharun420@gmail.com`")

with col_c2:
    with st.container(border=True):
        st.markdown("🐙 **GitHub**")
        st.markdown("[github.com/rrdaks23](https://github.com/rrdaks23)")

with col_c3:
    with st.container(border=True):
        st.markdown("💼 **LinkedIn**")
        st.markdown("[linkedin.com/in/harunalrasyid](https://linkedin.com)")

st.divider()

st.subheader("✉️ Kirim Pesan Langsung")
with st.form("form_kontak"):
    nama = st.text_input("Nama Anda")
    email = st.text_input("Email Anda")
    pesan = st.text_area("Pesan atau Topik Kolaborasi")
    kirim = st.form_submit_button("Kirim Pesan")
    if kirim:
        if nama and email and pesan:
            st.success(f"Terima kasih {nama}! Pesan Anda telah dicatat. Untuk respons cepat, Anda juga dapat menghubungi email di atas.")
        else:
            st.warning("Mohon lengkapi seluruh kolom sebelum mengirim pesan.")

st.caption("© 2026 • Dibangun dengan ❤️ menggunakan Python & Streamlit.")