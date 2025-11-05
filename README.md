# Weather Data Analysis and Forecasting

## Project Overview
This project performs weather data analysis and forecasting using machine learning techniques. It automatically fetches historical 5 years weather data, analyzes data, plot temperature & rainfall trends, and predicts next 30 days weather conditions.

The system consists of two main parts:
1. **CSV File Formation Script** – collects the past 5 years data of real-time weather data using the open source Meteostat and saves it in a CSV file.
2. **Weather Analysis and Forecast Code Notebook** – reads the generated CSV file, performs exploratory data analysis (EDA), get trained for weather patterns via ML models like random forest, xGBoost and then predicts weather for next 30 days to forecast temperature and rainfall.



## What the Project Does
1. **Collects Weather Data:**
   - Fetches data such as temperature, rainfall, humidity, and wind speed and other featues for the last 5 years.
   - Saves the data in a structured CSV format for further use.

2. **Analyzes and Visualizes Weather Patterns:**
   - Performs exploratory data analysis (EDA) on the fetched dataset.
   - Generates visual insights such as temperature trends, rainfall distribution, and correlations between features.
     
3. **Predicts Next-Day Weather:**
   - Uses machine learning models both Regression & Classification models like(Random forest , SVR, XGBoost) to predict temperature and rainfall(Rain/no rain) for the next upcoming 30 days.
   - Evaluates model performance (RMSE , R2 , Precision , recall, F1 score,ROC AUC CURVES , Precision recall curves, confusion matrices ) and displays the prediction results in graph plots and stores it in a separate csv file.
     


## Tools and Technologies Used

| Category | Tools / Libraries |
|-----------|------------------|
| Programming Language | Python |
| Data manipulation| pandas, numpy |
| Visualization | matplotlib, seaborn |
| Machine Learning | scikit-learn (Regression Models, Classification Models) |
| Fetching Data | Metostat  |
| Date Handling | datetime, timedelta |
| File Handling | CSV module |



## Project Structure

├── Weather_Data_fetch.py
├── README.md
├── Weather_Analysis_and_Forcasting.ipynb




## How to Use

### Step 1: Generate the CSV File
Run the `Weather_Data_fetch.py` script to fetch and store weather data.

**What it does:**
- Connects to nearest weather stations across Mohali 
- Fetches weather data for the last 5 years for Mohali
- Creates a CSV file named `Weather_Data_fetch.csv` in your project directory



### Step 2: Update the File Path in the Notebook
Before running the `Weather_Analysis_and_Forcasting.ipynb`, confirm correct name of csv file.

If both files are in the same folder, you can simply keep the default filename `Weather_Data_fetch.csv`.


### Step 3: Run the Weather Analysis Notebook
Open `Weather_Analysis_and_Forcasting.ipynb` in Jupyter Notebook or VS Code and run all cells in order.

**The notebook will:**
- Load and display your weather data
- Perform exploratory data analysis (EDA) with visual graphs
- Train firstly regression model (Random Forest , SVR, XGboost and then followed by classification model (Random forest) to forecast next 30 days temperature and rainfall
- Display predictions and model performance metrics


## Features and Insights
- Automatic data fetching directly from the Meteostat.
- Data visualization of temperature, humidity, rainfall, and wind speed.
- Regression and classification based predictive modeling for next 30 days forecasting.
- Model evaluation with metrics such as MAE, RMSE, or R² score ,Precision, recall, F1 score,ROC AUC CURVES , Precision recall curves, confusion matrices .



## Output
After running the notebook, the output includes:
- Predicted temperature and rainfall for the next day.
- Comparative visualizations of R² score ,Precision, recall, F1 score,ROC AUC CURVES , Precision recall curves, confusion matrices.
- Evaluation results showing model accuracy.



## Customization
- To analyze a different city, change the `LOCATION` variable in `Weather_Data_fetch.py`.
- You can adjust the regression model or visualization settings directly in the notebook.



## Author
**Prabhleen Kaur Saini** - **ms23170@iisermohali.ac.in**
**Ridima Singh** - **ms23202@iisermohali.ac.in**
**Rimjhim Sarohi** - **ms23083@iisermohali.ac.in**

Developed using Python and Machine Learning

