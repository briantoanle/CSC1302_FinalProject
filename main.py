import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


# raw collection of your choice (300 data points and 5 features aka 300 rows and 3 columns)
# source: https://archive.ics.uci.edu/ml/machine-learning-databases/00616/

# 2.1 read in the data
# we are only using the first 1000 lines of data
tetuan = pd.read_csv('Tetuan City power consumption.csv',nrows = 5000)
# 2.2 clean data, drop empty rows
tetuan = tetuan.dropna()

