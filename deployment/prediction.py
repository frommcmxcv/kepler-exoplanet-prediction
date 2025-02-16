# import libraries
import streamlit as st
import pandas as pd
import pickle
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain

# Load model
with open('model_rf.pkl', 'rb') as file_1:
  model = pickle.load(file_1)

# Title
st.title('Predict using Machine Learning')
st.write('___')

rain(
    emoji=" ☆🪐",
    font_size=20,
    falling_speed=10,
    animation_length="2"
)

# Title
colored_header(label="Kepler Object of Interest Prediction",
               color_name="violet-70",
               description="")


def run():
    with st.form("my_form"):
        st.markdown("**Calculate the object**")
        koi_period = st.number_input(label="KOI Period",
                                    placeholder="Insert the orbital period (days) of the object around its star",
                                    value=None,
                                    min_value=0.000) # Periods can't be negative
            
        koi_period_err1 = st.number_input(label="KOI Period Error (+)",
                                            placeholder="Insert the positive error for KOI Period",
                                            value=None,
                                            min_value=0.000) # Errors are typically positive
            
        koi_period_err2 = st.number_input(label="KOI Period Error (-)",
                                            placeholder="Insert the negative error for KOI Period",
                                            value=None,
                                            max_value=0.000 # Errors are negative
                                            )
            
        koi_time0bk = st.number_input(label="KOI Time0BK",
                                        placeholder="Insert the time of transit center (BKJD)",
                                        value=None,
                                        min_value=0.000  # BKJD is non-negative
                                        )
            
        koi_time0bk_err1 = st.number_input(label="KOI Time0BK Error (+)",
                                            placeholder="Insert the positive error for KOI Time0BK",
                                            value=None,
                                            min_value=0.000,
                                            max_value=10.000
                                            )
            
        koi_time0bk_err2 = st.number_input(label="KOI Time0BK Error (-)",
                                            placeholder="Insert the negative error for KOI Time0BK",
                                            value=None,
                                            max_value=0.000)
            
        koi_impact = st.number_input(label="KOI Impact",
                                    placeholder="Insert the impact parameter",
                                    value=None,
                                    min_value=0.000,  # Minimum impact parameter
                                    max_value=1.000  # Maximum impact parameter (grazing orbit)
                                    )
            
        koi_impact_err2 = st.number_input(label="KOI Impact Error (-)",
                                            placeholder="Insert the negative error for KOI Impact",
                                            value=None,
                                            max_value=0.000)
            
        koi_duration = st.number_input(label="KOI Duration",
                                        placeholder="Insert the duration of transit (hours)",
                                        value=None,
                                        min_value=0.1, # Minimum duration set to 6 minutes
                                        max_value=100.0 # Maximum transit set to 100 hours)
                                        )  
            
        koi_duration_err1 = st.number_input(label="KOI Duration Error (+)",
                                            placeholder="Insert the positive error for KOI Duration",
                                            value=None,
                                            min_value=0.000,
                                            max_value=10.0)
            
        koi_duration_err2 = st.number_input(label="KOI Duration Error (-)",
                                            placeholder="Insert the negative error for KOI Duration",
                                            value=None,
                                            max_value=0.0)
            
        koi_depth = st.number_input(label="KOI Depth",
                                    placeholder="Insert the depth of transit (ppm)",
                                    value=None,
                                    min_value=0.1,  # Minimum depth for detection
                                    max_value=1000000.0  # Maximum depth (eclipsing binaries or large planets)
                                    )
            
        koi_depth_err1 = st.number_input(label="KOI Depth Error (+)",
                                        placeholder="Insert the positive error for KOI Depth",
                                        value=None,
                                        min_value=0.000,
                                        max_value=10.0)
            
        koi_depth_err2 = st.number_input(label="KOI Depth Error (-)",
                                        placeholder="Insert the negative error for KOI Depth",
                                        value=None,
                                        max_value=0.0)
            
        koi_prad = st.number_input(label="KOI Planet Radius",
                                    placeholder="Insert the radius of the planet (Earth radii)",
                                    value=None,
                                    min_value=0.1,  # 0.1 Earth radii # Minimum observed radius (e.g., Mars-sized planets)
                                    max_value=20.0  # 20 Earth radii # Maximum observed radiu (e.g., gas giants)
                                    )
            
        koi_prad_err1 = st.number_input(label="KOI Planet Radius Error (+)",
                                        placeholder="Insert the positive error for KOI Planet Radius",
                                        value=None,
                                        min_value=0.000,
                                        max_value=10.0)
            
        koi_prad_err2 = st.number_input(label="KOI Planet Radius Error (-)",
                                        placeholder="Insert the negative error for KOI Planet Radius",
                                        value=None,
                                        max_value=0.0)
            
        koi_teq = st.number_input(label="KOI Equilibrium Temperature",
                                    placeholder="Insert the equilibrium temperature (K)",
                                    value=None,
                                    min_value=50.0,  # Coldest exoplanets
                                    max_value=3000.0  # Hottest exoplanets
                                    )
            
        koi_insol = st.number_input(label="KOI Insolation",
                                    placeholder="Insert the insolation flux (Earth units)",
                                    value=None,
                                    min_value=0.01,  # Very low insolation
                                    max_value=10000.0  # Extremely high insolation (e.g., close-in planets)
                                    )
            
        koi_insol_err1 = st.number_input(label="KOI Insolation Error (+)",
                                        placeholder="Insert the positive error for KOI Insolation",
                                        value=None,
                                        min_value=0.000,
                                        max_value=10.0)
            
        koi_insol_err2 = st.number_input(label="KOI Insolation Error (-)",
                                        placeholder="Insert the negative error for KOI Insolation",
                                        value=None,
                                        max_value=0.0)
            
        koi_model_snr = st.number_input(label="KOI Model SNR",
                                        placeholder="Insert the signal-to-noise ratio",
                                        value=None)
            
        koi_steff = st.number_input(label="KOI Stellar Effective Temperature",
                                    placeholder="Insert the stellar effective temperature (K)",
                                    value=None,
                                    min_value=2500.0,  # Cool stars (e.g., red dwarfs)
                                    max_value=10000.0  # Hot stars (e.g., A-type stars)
                                    )
            
        koi_steff_err1 = st.number_input(label="KOI Stellar Effective Temperature Error (+)",
                                        placeholder="Insert the positive error for KOI Stellar Effective Temperature",
                                        value=None,
                                        min_value=0.000,
                                        max_value=10.0)
            
        koi_steff_err2 = st.number_input(label="KOI Stellar Effective Temperature Error (-)",
                                        placeholder="Insert the negative error for KOI Stellar Effective Temperature",
                                        value=None,
                                        max_value=0.0)
            
        koi_slogg = st.number_input(label="KOI Stellar Surface Gravity",
                                    placeholder="Insert the stellar surface gravity (log g)",
                                    value=None,
                                    min_value=3.0,  # Low gravity stars (giants)
                                    max_value=5.0  # High gravity stars (dwarfs)
                                    )
            
        koi_slogg_err1 = st.number_input(label="KOI Stellar Surface Gravity Error (+)",
                                        placeholder="Insert the positive error for KOI Stellar Surface Gravity",
                                        value=None,
                                        min_value=0.000,
                                        max_value=10.0)
            
        koi_slogg_err2 = st.number_input(label="KOI Stellar Surface Gravity Error (-)",
                                        placeholder="Insert the negative error for KOI Stellar Surface Gravity",
                                        value=None,
                                        max_value=0.0)
            
        koi_srad = st.number_input(label="KOI Stellar Radius",
                                    placeholder="Insert the stellar radius (Solar radii)",
                                    value=None,
                                    min_value=0.1,  # Smallest stars (red dwarfs)
                                    max_value=100.0  # Largest stars (supergiants)
                                    )
            
        koi_srad_err1 = st.number_input(label="KOI Stellar Radius Error (+)",
                                        placeholder="Insert the positive error for KOI Stellar Radius",
                                        value=None,
                                        min_value=0.000,
                                        max_value=10.0)
            
        koi_srad_err2 = st.number_input(label="KOI Stellar Radius Error (-)",
                                        placeholder="Insert the negative error for KOI Stellar Radius",
                                        value=None,
                                        max_value=0.0)
            
        ra = st.number_input(label="Right Ascension",
                            placeholder="Insert the right ascension (degrees)",
                            value=None)
            
        dec = st.number_input(label="Declination",
                                placeholder="Insert the declination (degrees)",
                                value=None)
            
        koi_kepmag = st.number_input(label="KOI Kepler Magnitude",
                                    placeholder="Insert the Kepler magnitude",
                                    value=None)
            
        submitted = st.form_submit_button("Submit")

    if submitted:
        df_inf = {
        'koi_period': koi_period,
        'koi_period_err1': koi_period_err1,
        'koi_period_err2': koi_period_err2,
        'koi_time0bk': koi_time0bk,
        'koi_time0bk_err1': koi_time0bk_err1,
        'koi_time0bk_err2': koi_time0bk_err2,
        'koi_impact': koi_impact,
        'koi_impact_err2': koi_impact_err2,
        'koi_duration': koi_duration,
        'koi_duration_err1': koi_duration_err1,
        'koi_duration_err2': koi_duration_err2,
        'koi_depth': koi_depth,
        'koi_depth_err1': koi_depth_err1,
        'koi_depth_err2': koi_depth_err2,
        'koi_prad': koi_prad,
        'koi_prad_err1': koi_prad_err1,
        'koi_prad_err2': koi_prad_err2,
        'koi_teq': koi_teq,
        'koi_insol': koi_insol,
        'koi_insol_err1': koi_insol_err1,
        'koi_insol_err2': koi_insol_err2,
        'koi_model_snr': koi_model_snr,
        'koi_steff': koi_steff,
        'koi_steff_err1': koi_steff_err1,
        'koi_steff_err2': koi_steff_err2,
        'koi_slogg': koi_slogg,
        'koi_slogg_err1': koi_slogg_err1,
        'koi_slogg_err2': koi_slogg_err2,
        'koi_srad': koi_srad,
        'koi_srad_err1': koi_srad_err1,
        'koi_srad_err2': koi_srad_err2,
        'ra': ra,
        'dec': dec,
        'koi_kepmag': koi_kepmag}

        df_inf = pd.DataFrame([df_inf])
        
        st.dataframe(df_inf)

        result = model.predict(df_inf)

        st.write('The object is predicted to be a', result)

if __name__ == "__main__":
    run()