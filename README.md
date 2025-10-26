# Weather Data Analysis and Forecasting

## Project Overview
This project performs weather data analysis and forecasting using machine learning techniques. It automatically fetches recent weather data, analyzes historical trends, and predicts next-day weather conditions (temperature and rainfall).

The system consists of two main parts:
1. **CSV File Formation Script** – collects the past 7 days of real-time weather data using the WeatherAPI and saves it in a CSV file.
2. **Weather Analysis and Forecast Code Notebook** – reads the generated CSV file, performs exploratory data analysis (EDA), visualizes weather patterns, and builds predictive models to forecast the next day's temperature and rainfall.



## What the Project Does
1. **Collects Weather Data:**
   - Fetches data such as temperature, rainfall, humidity, and wind speed for the last 7 days.
   - Saves the data in a structured CSV format for further use.

2. **Analyzes and Visualizes Weather Patterns:**
   - Performs exploratory data analysis (EDA) on the fetched dataset.
   - Generates visual insights such as temperature trends, rainfall distribution, and correlations between features.

3. **Predicts Next-Day Weather:**
   - Uses machine learning models (like Linear Regression, Decision Tree, or SVM) to predict temperature and rainfall for the next day (Day 8).
   - Evaluates model performance and displays the prediction results.



## Tools and Technologies Used

| Category | Tools / Libraries |
|-----------|------------------|
| Programming Language | Python |
| Data Handling | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Machine Learning | scikit-learn (Regression Models) |
| API Access | requests (WeatherAPI.com) |
| Date Handling | datetime, timedelta |
| File Handling | CSV module |



## Project Structure

├── CSV File Formation.py
├── README.md
├── Weather Analysis and Forecast Code.ipynb




## How to Use

### Step 1: Generate the CSV File
Run the `CSV File Formation.py` script to fetch and store weather data.

**What it does:**
- Connects to WeatherAPI.com
- Fetches weather data for the last 7 days for the given location (`Mohali` by default)
- Creates a CSV file named `weather_data.csv` in your project directory

> Make sure to replace the `API_KEY` in the script with your own key from WeatherAPI.com.


### Step 2: Update the File Path in the Notebook
Before running the `Weather Analysis and Forecast Code.ipynb`, update the CSV file path inside the notebook to match the location where your generated CSV file is saved.

If both files are in the same folder, you can simply keep the default filename `weather_data.csv`.


### Step 3: Run the Weather Analysis Notebook
Open `Weather Analysis and Forecast Code.ipynb` in Jupyter Notebook or VS Code and run all cells in order.

**The notebook will:**
- Load and display your weather data
- Perform exploratory data analysis (EDA) with visual graphs
- Train a regression model to forecast next-day (Day 8) temperature and rainfall
- Display predictions and model performance metrics



## Features and Insights
- Automatic data fetching directly from the WeatherAPI.
- Data visualization of temperature, humidity, rainfall, and wind speed.
- Regression based predictive modeling for next-day forecasting.
- Model evaluation with metrics such as MAE, RMSE, or R² score.



## Output
After running the notebook, the output includes:
- Predicted temperature and rainfall for the next day.
- Comparative visualizations of actual vs. predicted values.
- Evaluation results showing model accuracy and error scores.



## Customization
- To analyze a different city, change the `LOCATION` variable in `CSV File Formation.py`.
- To use your own dataset, replace the CSV file path in the analysis notebook.
- You can adjust the regression model or visualization settings directly in the notebook.



## Author
**Prabhleen Kaur Saini** - **ms23170@iisermohali.ac.in**
**Ridima Singh** - **ms23202@iisermohali.ac.in**
**Rimjhim Sarohi** - **ms23083@iisermohali.ac.in**

Developed using Python and Machine Learning

