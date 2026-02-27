import streamlit as st
import random
import time

# Sayfa Tasarımı
st.set_page_config(page_title="Emir'in Oyun Merkezi", page_icon="🎮")

st.title("🎮 EMİR'İN OYUN VE ŞANS MERKEZİ")
st.sidebar.header("Menü")
secim = st.sidebar.selectbox("Bir Oyun Seç", ["Sayı Tahmin Oyunu", "Karar Çarkı", "Zar At"])

if secim == "Sayı Tahmin Oyunu":
    st.header("🔢 Sayı Tahmin Oyunu")
    st.write("1 ile 100 arasında bir sayı tuttum. Bakalım bulabilecek misin?")
    
    # Oyunun rastgele sayısını hafızada tutmak için session_state kullanıyoruz
    if 'gizli_sayi' not in st.session_state:
        st.session_state.gizli_sayi = random.randint(1, 100)
        st.session_state.deneme = 0

    tahmin = st.number_input("Tahminin nedir?", min_value=1, max_value=100, step=1)
    
    if st.button("TAHMİN ET"):
        st.session_state.deneme += 1
        if tahmin < st.session_state.gizli_sayi:
            st.warning("Daha YÜKSEK bir sayı söyle! 📈")
        elif tahmin > st.session_state.gizli_sayi:
            st.warning("Daha DÜŞÜK bir sayı söyle! 📉")
        else:
            st.success(f"TEBRİKLER! {st.session_state.deneme}. denemede buldun! 🎉")
            st.balloons()
            # Oyunu sıfırla
            if st.button("Yeniden Oyna"):
                st.session_state.gizli_sayi = random.randint(1, 100)
                st.session_state.deneme = 0

elif secim == "Karar Çarkı":
    st.header("🎡 Karar Verici")
    st.write("Kararsız mı kaldın? Soruyu yaz, Emir senin yerine karar versin!")
    
    soru = st.text_input("Neye karar veremiyorsun? (Örn: Ne yemek yiyelim?)")
    secenekler = st.text_area("Seçenekleri aralarına virgül koyarak yaz", "Lahmacun, Pizza, Burger, Ev Yemeği")
    
    if st.button("KADERİNİ BELİRLE"):
        liste = [s.strip() for s in secenekler.split(",")]
        with st.spinner('Çark dönüyor...'):
            time.sleep(2)
            sonuc = random.choice(liste)
            st.info(f"Sonuç: **{sonuc}**")
            st.snow() # Bu sefer kar yağsın!

elif secim == "Zar At":
    st.header("🎲 Zar Atma")
    if st.button("ZARLARI FIRLAT"):
        zar1 = random.randint(1, 6)
        zar2 = random.randint(1, 6)
        st.markdown(f"### 🎲 {zar1} - {zar2}")
        if zar1 == zar2:
            st.success("ÇİFT GELDİ! 🔥")
