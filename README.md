# WEATHER-DATA-ANALYSIS-AND-FORECASTING-MODEL
This project analyzes the past week's weather data to predict future conditions such as temperature, rainfall, wind speed, and humidity. Using machine learning algorithms,it identifies patterns and trends to forecast the next day's or eighth day's weather with improved accuracy.  
The Weather Data Analysis and Forecasting Model is a data-driven project designed to analyze past weather trends and forecast future conditions using machine learning techniques. The project begins by collecting raw weather data stored in CSV format and transforming it into a clean, structured dataset suitable for analysis. Temperature and rainfall columns are converted into numeric types, missing values are handled, and the data is stored in a local SQLite database for easy access and reproducibility.

Once the data is prepared, the project performs detailed analysis and visualization of temperature and rainfall patterns over the past week. Various statistical summaries such as mean, median, and standard deviation are calculated, and short-term trends are visualized using Matplotlib plots. This provides insights into recent weather behavior before moving into predictive modeling.

For forecasting, the project uses multiple regression models including Linear Regression, Decision Tree Regressor, and Support Vector Regressor (SVR). The models are evaluated based on metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² score to determine which performs best. The best-performing models are then used to predict the next day’s (8th day) weather, providing automated forecasts for both temperature and rainfall.

The model also incorporates feature engineering by creating lag and rolling window features that help capture temporal dependencies in weather data. This enhances the model’s predictive accuracy. All predictions and model performance results are stored and displayed for further analysis.

This project has been developed using Python, Pandas, NumPy, Matplotlib, and Scikit-learn, with SQLite3 for database management. All experiments and models are implemented within Jupyter Notebooks in VS Code, providing an interactive environment for analysis, visualization, and forecasting.

The repository maintains a clear version history, showing a step-by-step development process from initial setup and CSV formation to database integration, feature engineering, model evaluation, and final prediction logic. Each commit represents meaningful progress, ensuring transparency and reproducibility in the workflow.

Overall, this project demonstrates how data preprocessing, statistical analysis, and machine learning can be combined to build an intelligent weather forecasting system capable of learning from historical data and predicting future trends with accuracy.
