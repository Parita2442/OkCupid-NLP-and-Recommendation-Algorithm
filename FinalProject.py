# Importing libraries and mounting the drive

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from google.colab import drive
import seaborn as sns
import statsmodels.formula.api as smf
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
!pip install -U googlemaps
drive.mount('/content/drive')
data_folder = '/content/drive/MyDrive/Colab Notebooks/BA820/Data/'

data = pd.read_csv(data_folder+'okcupid_profiles.csv')

data.info()

data.head()

data.describe()

test
