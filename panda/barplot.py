# Problem Statement: Comparing categorical data using a bar chart.
# Question: Which category has the highest value in the given dataset?

import matplotlib.pyplot as plt



categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
plt.xlabel("Categories")
plt.ylabel("Values")

plt.title("Bar Chart")
plt.show()
