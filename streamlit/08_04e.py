import time
import numpy as np 
import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt 

data = [np.random.randn()] # Initialize with a single
# random number

'Growing Line Chart:'
chart_placeholder = st.empty() # Create a placeholder for the chart
chart_placeholder.line_chart(data) # Display the initial chart

for i in range(1, 100): # Update the chart with new data points
  data.append(data[-1] + np.random.randn()) # Add a new random number to the data
  # data[-1] uses -1 to access the last element of the list,
  # and np.random.randn() generates a new random number from a
  #  standard normal distribution. The new number is added to the last number
  #  in the list to create a cumulative effect. 
  chart_placeholder.line_chart(data) # Update the chart with the new data
  time.sleep(0.05) # Pause for a short time to simulate real-time data streaming
  


values = np.random.rand(10)
'matplotlibs Line Chart:'
fig, ax = plt.subplots()
ax.plot(values)
st.pyplot(fig)







