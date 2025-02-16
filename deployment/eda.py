# Import libraries
import streamlit as st
from streamlit_extras.let_it_rain import rain
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout='centered',
                   page_title='Kepler Exoplanets Prediction')

rain(
    emoji=" ☆🪐",
    font_size=20,
    falling_speed=5,
    animation_length="2"
)

def run():
    # Show image
    st.image('https://www.nasa.gov/wp-content/uploads/2023/03/742541main_Kepler-62MorningStar-1_full.jpg',
            caption='Seen in the foreground is Kepler-62f, a newfound habitable exoplanet')

    # Set page title
    st.title('Kepler Object of Interest Prediction')

    st.markdown('''
                
                The search for habitable planets besides our own has captivated humanity for decades. Whether driven 
                by curiosity about extraterrestrial life or the need for a potential future home, this pursuit has gained 
                urgency as Earth's resources face increasing strain. Climate change, pollution, and resource depletion 
                threaten the planet's habitability, while the distant future holds the inevitability of the Sun expanding 
                into a red giant, making Earth uninhabitable. NASA’s goal these days is to find unmistakable signs of 
                current life outside of Earth.

                Kepler space telescope was launched in 2009 with the purpose of searching for exoplanets, especially 
                those in the habitable zone of their stars. The spacecraft, although officially retired in 2018, collected 
                an immense amount of data which continues to be analysed to this day. This project focuses on 
                classifying Kepler’s objects of interest (KOIs) as either exoplanets, candidate of exoplanets, or false positives caused by phenomena like binary stars or noise.  

                This project develops a machine learning classification model to identify whether Kepler’s object of interest is 
                exoplanet, candidate of exoplanet, or not.
                ''')

    st.write('___')

    # Load data
    st.write('## Dataset')
    st.write('')
    st.markdown('''
                The Dataset used herein extracted from NASA Expolanet Archive.
                https://exoplanetarchive.ipac.caltech.edu/docs/API_kepcandidate_columns.html
            
                ''')

    st.write('___')




    # Exploratory Data Analysis 1
    st.write('## Kepler Object of Interest Disposition')
    st.write('')

    st.markdown('''
                A Kepler Object of Interest("**KOI**) is a star observed by the Kepler space
                telescope that is suspected of hosting one or more transit planets.
                
                Scientists configure three different categories based on Kepler's object of interest.

                - A candidate exoplanet means that the exoplanet that shows characteristics consistent
                with being a planet but has not yet been fully verified. (0)
                
                - A confirmed exoplanet (1) is a celestial body that has been verified as a planet
                through multiple independent methods or observations.

                - False Positive means that Kepler incorrectly identify its object to be exoplanet.
                
                The following chart will show the percentage of each category.
                ''')
    df=pd.read_csv('cumulative.csv')

    fig = px.pie(
        df,
        names='koi_disposition',  # Column containing categories
        color_discrete_sequence=['#9191E9', '#C2AFF0', '#686868', '#457EAC'],  # Custom colors
    )

    fig.update_traces(textinfo='percent+label')  # Show percentage and labels
    st.plotly_chart(fig)

    st.write('___')



    # Exploratory Data Analysis 2
    st.write('## Exoplanets Size Distribution')
    st.write('')
    st.markdown('''
                The size of all confirmed exoplanets vary, to the ones that have
                similar radius to Earth or a huge exoplanet like that is of Jupiter.
                
                
                It begs the question: How many confirmed exoplanets are Earth-sized,
                super-Earths, mini-neptune, or gas giants?"
                ''')


    df_filtered = df[df['koi_disposition'] == 'CONFIRMED']

    def categorize_planet_radius(radius):
        if 0.8 <= radius <= 1.25:
            return 'Earth-sized'
        elif 1.25 < radius <= 2.0:
            return 'Super-Earth'
        elif 2.0 < radius <= 4.0:
            return 'Mini-Neptune'
        elif radius > 4.0:
            return 'Gas Giant'
        else:
            return 'Unknown'

    df_filtered['planet_category'] = df_filtered['koi_prad'].apply(categorize_planet_radius)

    fig2 = px.pie(
        df_filtered,
        names='planet_category',  # Column containing categories
        color_discrete_sequence=['#FC9601', '#842539', '#D14009', '#457EAC', '#FFE484'],  # Custom colors
    )

    fig2.update_traces(textinfo='percent+label')  # Show percentage and labels
    st.plotly_chart(fig2)


    st.write('___')

    # Exploratory Data Analysis 3
    st.write('## Are There Any Habitable Exoplanets?')
    st.write('')

    st.markdown('''
                The amount of energy from a star that reaches the surface of a planet or exoplanet (insolation flux)
                determines how habitable an exoplanet is. If the planet is close to its star, it will benefit from
                more energy but it will also has a hotter surface, making the planet too hot for life.
                However, if the planet is too far from its star, it will be too cold for form of life to exist.

                The ideal measurement to insolation flux of exoplanet is equal to 1. Insolation Flux = 1 means that
                the planet is receiving the same amount of energy as Earth does from the Sun. This is often used as
                a baseline for Earth-like conditions, and it could indicate that the planet is in the habitable zone
                of its star, similar to Earth.

                It's important to note that this analysis uses simplified measure (koi_insol) to determine whether an
                exoplanet is habitable or not. To fully understand if an exoplanet is habitable or not, there are
                several factors need to be measured. However, this analysis could serve as a preliminary analysis or assumption.
                ''')

    def habitable_category(insolation_flux):
        if insolation_flux == 1:
            return 'Potentially Habitable'
        elif insolation_flux > 1:
            return 'High Energy'
        elif insolation_flux < 1:
            return 'Low Energy'
        else:
            return 'Unknown'

    df_filtered['habitable_category'] = df_filtered['koi_insol'].apply(habitable_category)

    count_category_influx = df_filtered['habitable_category'].value_counts() # Count category of koi_influx
    count_category_influx_df = count_category_influx.reset_index()
    count_category_influx_df.columns = ['Category', 'Count']  # Rename columns

    fig = px.bar(
        count_category_influx_df,
        x='Category',  # Use the renamed column
        y='Count',     # Use the renamed column
        labels={'Category': 'Category', 'Count': 'Count'}  # Set axis labels
    )

    st.plotly_chart(fig)

if __name__ == "__main__":
    run()