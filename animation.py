import streamlit as st
from PIL import Image
import io
import time
import os
import imageio
from selenium import webdriver

# ... (seu código existente)

# Diretório onde as imagens capturadas serão salvas
output_directory = "captured_images"
os.makedirs(output_directory, exist_ok=True)

# Caminho para o driver do navegador (por exemplo, ChromeDriver)
driver_path = "/path/to/chromedriver"

# Configurar opções do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Execute em segundo plano (sem janelas visíveis)
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

# Inicie o driver do Selenium com opções
driver = webdriver.Chrome(options=chrome_options)

# Inicie o aplicativo Streamlit localmente usando o Selenium
local_url = "http://localhost:8501"  # Atualize a porta se necessário
driver.get(local_url)

# Espere o Streamlit carregar completamente (ajuste o tempo conforme necessário)
time.sleep(5)

# Automatize a seleção dos anos e capture as imagens
for year in range(1970, 2022):
    # Interaja com o aplicativo para selecionar o ano
    st.slider("", min_value=1970, max_value=2021, value=year)
    
    # Captura de tela da janela do navegador (onde o Streamlit é exibido)
    screenshot = driver.get_screenshot_as_png()
    
    # Salve a captura de tela como uma imagem
    image_filename = os.path.join(output_directory, f"co2_map_{year}.png")
    with open(image_filename, "wb") as img_file:
        img_file.write(screenshot)

# Feche o driver do Selenium
driver.quit()

# Crie a animação a partir das imagens capturadas
image_files = [os.path.join(output_directory, f"co2_map_{year}.png") for year in range(1970, 2022)]
output_video = "co2_emission_animation.mp4"

with imageio.get_writer(output_video, fps=5) as video_writer:
    for image_file in image_files:
        image = imageio.imread(image_file)
        video_writer.append_data(image)

print("Animação concluída e salva como", output_video)
