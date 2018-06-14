import numpy as np
import matplotlib.pyplot as plt
# you can define your python list called "pop", the gdp_cap is gotten from some source i can
# remember but you can generate yours or fetch from  whatever sources too

# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]') #set the label for the x-axis
plt.ylabel('Life Expectancy [in years]') #set the label for the y-axis
plt.title('World Development in 2007') # Set the title for the graph
plt.xticks([1000,10000,100000], ['1k','10k','100k']) # Set the x-axis figures to a certain form to aid readability

# Additional customizations
plt.text(1550, 71, 'India') #Set the specified cordinate to have the specified text
plt.text(5700, 80, 'China') #Set the specified cordinate to have the specified text

# Add grid() call
plt.grid(True) # Apply grid lines to our graph

# Show the plot
plt.show() # Used to show the graph and customizations described above
