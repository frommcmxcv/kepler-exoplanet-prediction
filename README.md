# Kepler Exoplanets Prediction Project

Huggingface: https://huggingface.co/spaces/frommcmxcv/kepler-exoplanet-prediction

## Project Overview
This project aims to predict exoplanet candidates from the Kepler dataset using machine learning models. It covers the entire pipeline from data exploration and preprocessing to model training, evaluation, and interpretation.

## Datasets Used
- **Source:** Kaggle, originally sourced from NASA's Kepler Exoplanet Archive
- **Type:** Tabular data with features such as orbital period, stellar mass, and flux.

## 🛠️ Tools & Technologies
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost, RF
- **Modeling Techniques:** K-Nearest Neighbour, Support Vector Machine, Decision Tree, Random Forest, XGBoost

## Project Workflow
1. **Exploratory Data Analysis (EDA):**
   - Analyzed distributions, correlations, and outliers.
   - Visualized key features impacting predictions.
2. **Data Preprocessing:**
   - Handled missing values and standardized features.
   - Applied feature engineering techniques.
3. **Model Training & Evaluation:**
   - Built and compared models using cross-validation.
   - Evaluated performance with metrics such as accuracy, precision, recall, and ROC-AUC.

## Results & Findings
- The **Random Forest** model achieved the highest accuracy with optimized hyperparameters.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the notebook:
   ```bash
   jupyter notebook
   ```

## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests.

---
**Happy Exploring! 🚀**
