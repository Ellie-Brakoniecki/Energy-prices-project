# Energy-prices-project
An analysis of the question "How have increasing energy prices impacted the unemployment rate across different economic sectors in Great Britain?

The analysis is in a jupyter notebook - folder `src/analysis.ipynb`

**Running the dashboard**
To run the dashboard run `python dashboard.py` in the terminal and open the weblink generated
![image](https://github.com/Ellie-Brakoniecki/Energy-prices-project/assets/112866399/61921b2d-6e38-4dd2-be53-8d52a1879a5c)


Research Report: Impact of Rising Energy Prices on Unemployment Rates Across Economic Sectors in Great Britain

# Introduction

The cost of living has become a pressing concern in Great Britain, especially in the wake of rising energy prices. This research aims to explore the impact of escalating energy costs on unemployment rates across different economic sectors. By employing data analytics and machine learning models, this study aims to provide insights that could inform policy making in mitigating the economic hardships faced by much of the public.

# methodology

Two primary datasets were collected: 

Quarterly energy prices (Electricity and Gas) from 2004 to Q1 2023.

Unemployment rates across various economic sectors for the same period. 

See Data source section below

# data preprocessing

Data cleaning involved: 

Handling missing values

Feature engineering to align both datasets. 

Standardizing quarters for unemployment data to match energy prices.

# exploratory data analysis

Descriptive statistics and visualizations were created using Python libraries like Pandas, Matplotlib, and Seaborn. These visuals showcased trends over time and correlations between energy prices and unemployment rates.



# Machine Learning Model

We used both ARIMA (AutoRegressive Integrated Moving Average) and Random Forest models for our analysis. ARIMA models were chosen for their strength in time-series forecasting, particularly their ability to model temporal trends and seasonality. Random Forest was used as a complementary model to predict unemployment rates based on energy prices. These two models collectively provide a robust analytical framework to understand the intricate relationship between energy prices and unemployment rates.

# Findings from EDA and ML Model

Key Findings include:

Negative Correlation: Contrary to initial hypotheses, our analysis found a weak negative correlation between rising energy prices and unemployment rates in several sectors. This suggests that other factors may be playing a significant role in influencing unemployment rates in these sectors.

Model Performance: The ARIMA models provided forecasts for future unemployment rates. Additionally, a Random Forest model was employed, which showed a decent level of prediction accuracy with an Rsquared value of 0.71.

# Interactive Dashboard

An interactive dashboard was built using Plotly Dash to visualise the data. The dashboard provides real-time insights into how changes in energy prices could potentially affect unemployment rates in different sectors. The dashboard serves as a practical tool to assess the current state of energy prices and unemployment, offering a more dynamic way to visualise the data. 





# Conclusion and Recommendations

Our analysis found a complex relationship between rising energy prices and unemployment rates across various sectors in the British economy. Contrary to initial expectations, our models indicated a negative correlation between energy prices and unemployment rates, particularly in sectors like manufacturing and construction. This suggests that the impact of rising energy prices on unemployment is not straightforward and likely influenced by multiple factors, possibly with a lag effect, as our data only extends to Q1 2023.

Given these complexities, we recommend that any policy aimed at mitigating the effects of rising energy costs should be sector-specific and consider a range of economic variables. Further investigation is also needed to determine the time lag between changes in energy prices and their impact on employment.

# Limitations and further work

Time Constraints: Due to limited time, the models used could benefit from further tuning for improved accuracy.

Seasonal Variations: Investigate the seasonal variations in unemployment rates to ascertain if the effect of energy prices could be influenced by seasonality.

Additional Models: In future, other machine learning models like Gradient Boosting and XGBoost could be explored for better performance.

Additional Time-Series Models: For future work, it would be beneficial to explore other time-series models like Exponential Smoothing State Space Model (ETS), Seasonal Decomposition of Time Series (STL), and Long Short-Term Memory (LSTM) networks for potentially improved forecasting performance.

Code Documentation: Write comprehensive code documentation and a README file for better understanding and reproducibility of the project.

Dashboard Enhancements: Improve the interactive dashboard to include more visualizations, such as heatmaps and correlation matrices, to better understand the complex relationships between variables.

# data sources

Energy Prices Over Time: . Quarterly prices of electricity, gas since 2004 broken down by size of consumer 

Unemployment Rates by Sector: . Monthly (3 month average) unemployment rates for different economic sectors in Great Britain (quarterly data before 2018).


