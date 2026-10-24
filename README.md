# Flight Price Prediction
Transportation such as ships and airplanes has provided us with many benefits. For example, these transportations enable us to ship trade items from one country to another, thereby improving the economy of the country. Besides, they also encourage the development of the tourism sector. Airfare price is often an important factor for those individuals who wish to travel around with low budget. 

## Objective & Research Questions 🤔
<ul>
<li>To analyse the flight booking dataset obtained from <a href="https://www.easemytrip.com/">“Ease My Trip”</a> website. The possible related research questions could be:</li> 
<ul>
  <li> Does price vary with Airlines? </li> 
  <li> How is the price affected when tickets are bought in just 1 or 2 days before departure?</li> 
  <li> Does ticket price change based on the departure time and arrival time?</li> 
  <li> How the price changes with change in Source and Destination?</li> 
  <li> How does the ticket price vary between Economy and Business class?</li> 
</ul>
  <li>To build regression model that could predict the airfare price. </li>
</ul>

## Source of Dataset 📅
The dataset was <a href="https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction"> provided by Shubham Bathwal on Kaggle</a>. It contains information about flight booking options from the website Easemytrip for flight travel between India's top 6 metro cities. There are 300,153 datapoints and 10 features in the cleaned dataset.
<ol>
<li> Airline: The name of the airline company is stored in the airline column. It is a categorical feature having 6 different airlines.</li>
<li> Flight: Flight stores information regarding the plane's flight code. It is a categorical feature.</li>
<li> Source City: City from which the flight takes off. It is a categorical feature having 6 unique cities.</li>
<li> Departure Time: This is a derived categorical feature obtained created by grouping time periods into bins. It stores information about the departure time and have 6 unique time labels.</li>
<li> Stops: A categorical feature with 3 distinct values that stores the number of stops between the source and destination cities.</li>
<li> Arrival Time: This is a derived categorical feature created by grouping time intervals into bins. It has six distinct time labels and keeps information about the arrival time.</li>
<li> Destination City: City where the flight will land. It is a categorical feature having 6 unique cities.</li>
<li> Class: A categorical feature that contains information on seat class; it has two distinct values: Business and Economy.</li>
<li> Duration: A continuous feature that displays the overall amount of time it takes to travel between cities in hours.</li>
<li>Days Left: This is a derived characteristic that is calculated by subtracting the trip date by the booking date.</li>
<li> Price: Target variable stores information of the ticket price.</li>
</ol>

## Explanatory Data Analysis 👀
* It is found that only Vistara and Air India provide flight with business class, but the maximum price for the business flight of the Vistara is higher than that of the business flight of the Air India.
* When we compared the maximum economy flight price from each airline, we found that economy flight ticket from the AirAsia, GO First, and Indigo offered the same lowest price, which is $1,105.00.
* The maximum duration for flight with no stops is only 3.58 hours. The flight was AI-773 from Air_India which fled from Kolkata at evening and arrived Mumbai at night.
* Flight with business class, two or more stops and early morning departure time have the highest maximum price as compared to other flights. There is no business class flight with two or more stops that depart at late night.
* The flight price became higher when the days left before departure is getting lesser.

## Model Selection & Evaluation 🔎
### Why Log Transformation in Ridge, Lasso, and Elastic Net
Linear models assume a linear relationship between input features and the target variable, along with homoscedastic (constant variance) normally distributed errors. In flight booking datasets, ticket prices exhibit extreme right-skewness driven by high-tier business class fares and last-minute booking spikes. Without transformation, these large target values disproportionately dominate the loss function, forcing linear models to chase extreme outliers at the expense of regular pricing brackets. Applying a natural logarithm transformation to the target variable compresses this heavy tail, normalizes error distributions, and stabilizes variance, allowing linear algorithms to learn balanced coefficients across both economy and business pricing tiers.

### Why Data Split into Train, Test, and Validate
Splitting data into training, validation, and testing sets prevents overfitting and provides an unbiased evaluation of generalization performance.

### Why the Final Model is Random Forest
* Linear models with log transformations struggle to capture non-linear interactions and complex decision boundaries inherent in airline pricing dynamics—such as non-linear price jumps as departure dates near or complex interactions between specific airlines, routes, and seat classes. A tuned Random Forest Regressor handles these multi-dimensional, non-linear interactions natively by constructing an ensemble of decision trees that partition feature spaces recursively. By averaging predictions across hundreds of decorrelated trees with tuned hyperparameters (max_features=0.5, n_estimators=200), the Random Forest mitigates overfitting, handles collinear categorical features robustly, and achieves superior predictive accuracy compared to penalized linear baselines.
  
* Below is the screencast of how the developed streamlit app run on my local PC.   

https://user-images.githubusercontent.com/57357735/198346386-9e855d47-7c62-4dba-b439-95808707ab45.mp4

## Recommendation 📥
* We could implement other ML algorithms, such as KNeighborsRegressor, or support vector regressor.
* Ensemble methods such as stacking regressor could be used to check if the model performance could be further improved.  
* Randomized Search could be used to tune the hyperparameters to see if the hyperparameter combination is the same. 
