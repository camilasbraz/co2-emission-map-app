import streamlit as st
from PIL import Image 
import io

# URLs para ícone da página e imagem
favicon_url = "assets/favicon.ico"
imagem_url = 'assets/logo.png'

# Configuração da página
st.set_page_config(page_icon=favicon_url, page_title="CO2 Emission Worldwide | Camila Braz")

# Create a Streamlit app
st.title("CO2 Emissions Worldwide: Map analysis through the years.")
st.sidebar.image(imagem_url)
# , width = 300


with st.sidebar.expander("About this app"):
    st.write(
        "EDA Analysis automatized using Streamlit and the ydata_profiling package.\n\n"
        "Source code here: [GitHub Repository](https://github.com/camilasbraz/co2-emission-map-app)\n\n"
        "Contact: [camilabraz03@gmail.com](mailto:camilabraz03@gmail.com)\n\n"
        "Application and code under the MIT License"
    )


with st.sidebar.expander("About the datasets"):
    st.write(
        "[EDGAR](https://edgar.jrc.ec.europa.eu/dataset_ghg70#sources) is a multipurpose, independent, global database of anthropogenic emissions of greenhouse gases and air pollution on Earth. \
        EDGAR provides independent emission estimates compared to what reported by European Member States or by Parties under the United Nations Framework Convention\
        on Climate Change (UNFCCC), using international statistics and a consistent IPCC methodology. EDGAR provides both emissions as national totals and gridmaps at 0.1 \
        x 0.1 degree resolution at global level, with yearly, monthly and up to hourly data.\n\n"

        "Crippa, M., Guizzardi, D., Banja, M., Solazzo, E., Muntean, M., Schaaf, E., Pagani, F., Monforti-Ferrario, F., Olivier, J., Quadrelli, R., Risquez Martin, A., Taghavi-Moharamli,\
        P., Grassi, G., Rossi, S., Jacome Felix Oom, D., Branco, A., San-Miguel-Ayanz, J. and Vignati, E., CO2 emissions of all world countries – JRC/IEA/PBL 2022 Report, EUR 31182 EN,  \
        Publications Office of the European Union, Luxembourg, 2022, [doi:10.2760/730164, JRC130363](doi:10.2760/730164, JRC130363).\n\n"
        
        "Crippa, M., Guizzardi, D., Solazzo, E., Muntean, M., Schaaf, E., Monforti-Ferrario, F., Banja, M., Olivier, J.G.J., Grassi, G., Rossi, S., Vignati, E.,GHG emissions \
        of all world countries - 2021 Report, EUR 30831 EN, Publications Office of the European Union, Luxembourg, 2021, ISBN 978-92-76-41547-3, [doi:10.2760/173513](doi:10.2760/173513), JRC126363.\n\n"
    )


selected_year = st.slider("Select a Year", min_value=1970, max_value=2021)

image_url = f'maps/co2_map_{selected_year}.png'

full_page_image = Image.open(image_url)
st.image(image_url)

# Convert the image to bytes
img_bytes = io.BytesIO()
full_page_image.save(img_bytes, format='PNG')

# Create a download button for the image
st.download_button(
    label="Download the map",
    data=img_bytes.getvalue(),
    key="download_button",
    file_name=f"co2_emission_map_{selected_year}_camilasbraz.png",
)




