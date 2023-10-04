## Exploring the Historical Global Carbon Dioxide Emission with Python and Streamlit

Recently, I've been following the work of the PythonMaps profile, which creates incredible maps using Python (I highly recommend following them on social media to keep up with their creations). In one of their posts, they created a map of global carbon dioxide emissions for the year 2018, which I found extremely interesting! As a result, I decided to create my own application based on this visualization to practice my skills in spatial data analysis and scaling in Python, as well as to work on a beautiful and useful project to analyze and investigate the annual global carbon dioxide emissions throughout history.

The result is a Streamlit application that allows you to explore carbon dioxide emissions over time. By selecting the year using a slider, you can visualize the year-by-year variation in emissions by country, as well as emission flows between nations. You can view data from 1971 to 2021 and download the map in PNG format.

The visualizations presented are powered by data from EDGAR, a global, independent, and multi-purpose database on anthropogenic greenhouse gas emissions and air pollution on Earth. It provides data in various formats, and the one used in the application includes coordinates with latitude and longitude, along with a CO2 emission value in tons. Combining this information with the Matplotlib and Geopandas libraries, it was possible to create beautiful and informative maps.

The main challenge was the volume of data in this dataset; each year is represented by a file with over 4 million rows. To process all this information, I explored the functionalities of Spark, Dask, and Polars. All three showed significant improvements in performance and speed compared to Pandas.

You can access the application at this link: https://lnkd.in/dikdcwyi, and the code is available on my GitHub: https://lnkd.in/daQFcNcB.
