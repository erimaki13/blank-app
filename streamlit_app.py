import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import io

st.set_page_config(page_title="クラウド仮想ブラウザ", layout="wide")
st.title("🌐 クラウド経由 仮想ブラウザ")

if "driver" not in st.session_state:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1280,800")
    
    # 自動検出設定
    st.session_state.driver = webdriver.Chrome(options=chrome_options)

driver = st.session_state.driver

url_input = st.text_input("アクセスしたいURLを入力してください:", value="https://google.com")

if st.button("ページを読み込む"):
    if url_input:
        try:
            with st.spinner("クラウド側でWebページにアクセス中..."):
                driver.get(url_input)
                png_data = driver.get_screenshot_as_png()
                image = Image.open(io.BytesIO(png_data))
                st.image(image, use_container_width=True)
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
