
##need to cd to the directory of the py file using Powershell
###PS C:\Users\Dandan> cd "C:\Users\Dandan\Desktop\UCI Continue Ed\Intro to Python Programming"
###Then exe:streamlit run GUI_App_Enrollment.py

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Title and description
#st.title(" La Sierra University Enrollment Prediction")
st.markdown(
    "<h2 style = 'text-align: center; color: black;'> La Sierra University Enrollment Prediction</h2>",
    unsafe_allow_html=True
)
# Path to your image
image_path = r"C:\Users\Dandan\Desktop\UCI Continue Ed\Intro to Python Programming\LaSierraUniv.jpg"

# Display the image
st.image(
    image_path,  # Provide the absolute path to the image
    caption="La Sierra University",  # Add an optional caption
    use_container_width=True  # Resize the image to fit the app's width
)

# Additional content
st.write("Welcome to the La Sierra University Streamlit application!")



# Some additional content

st.write("""
This app uses a simple linear regression model to predict future student enrollments based on historical data.
Input your enrollment data below to generate predictions for upcoming years.
""")

# Example data
example_data = pd.DataFrame({
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Enrollment": [2100, 2300, 2400, 2300, 2300, 2200, 2100, 2000, 1810, 1650]
})

# Use the example data directly
data = example_data
st.success("Example data loaded!")

# Validate that the data has the required columns
if "Year" not in data.columns or "Enrollment" not in data.columns:
    st.error("The data must have 'Year' and 'Enrollment' columns!")
    st.stop()

# Validate that the data is not empty
if data.empty:
    st.error("The data is empty! Something went wrong with loading the example data.")
    st.stop()

# Display the data
st.write("### Historical Enrollment Data")
st.write(data)

# Prepare data for modeling
X = np.array(data["Year"]).reshape(-1, 1)
y = np.array(data["Enrollment"])

# Input for future years
future_years = st.number_input("How many years into the future would you like to predict?", min_value=1, value=5)


model = LinearRegression()
model.fit(X, y)

# Generate predictions for future years
last_year = data["Year"].iloc[-1]
future_years_array = np.arange(last_year + 1, last_year + 1 + future_years).reshape(-1, 1)
future_predictions = model.predict(future_years_array)

# Display predictions
st.write("### Predicted Enrollment for Future Years")
future_df = pd.DataFrame({
    "Year": future_years_array.flatten(),
    "Predicted Enrollment": future_predictions.astype(int)
})
st.write(future_df)

# Plot results
st.write("### Enrollment Trends")
st.line_chart(pd.concat([
    data.set_index("Year"),
    future_df.set_index("Year")
]))