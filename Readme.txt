Read about the project in detail in the "Technical report" PDF at:
https://drive.google.com/drive/folders/1sXtsmHbgv9tzUQ2QWe6BEQs94in5gbSA?usp=sharing
To run the project code:
1)	Download data into the same folder as the code files 
2)	The following libraries are needed before running the code files: 
	scikit-learn, xgboost, gluonts, mlforecast, window_ops, shapely, geopandas, 
	random, re, scipy, glob, pandas, numpy, matplotlib, seaborn, plotly, ipywidgets, datetime
3)	Run “Preprocessing.ipynb” to produce “burglaries_preprocessed.csv” (used in “Models.ipynb”) and “stop_and_search.csv” (used in “S&S preprocessing.py”)
4)	Run “S&S preprocessing.py” to produce “stop_and_search_preprocessed.csv” (used “S&S correlation analysis.ipynb”)
5)	Run “Models.ipynb” for the forecasting and allocation algorithms
6)	Run “S&S correlation analysis.ipynb” to examine the correlation between stop and search frequency and frequency of criminal activity
7)	The following Jupyter notebooks can be ran independently of the rest and are not essential to the forecasting and allocation parts of the project: 
	“Burglaries map.ipynb” (creates a map showing the approximate coordinates of all burglaries in Barnet), 
	“Exploratory vis.ipynb” (creates the exploratory visualizations we made in the beginning of the project”, and 
	“(experiment) deriving criminal hours s&s.ipynb” (trying to find the hours with most criminal activity stop and search data)

