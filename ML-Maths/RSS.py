from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

model = LinearRegression()

model.fit(X, y)

y_prediction = model.predict(X)

rss = sum((y - y_prediction)**2)

# TODO complete this.