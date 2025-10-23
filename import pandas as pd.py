import pandas as pd

import matplotlib.pyplot as plt

# Example data: average prices of vegetables (in USD)
data = {
    'Vegetable': ['Tomato', 'Potato', 'Carrot', 'Broccoli', 'Onion'],
    'Average Price': [2.5, 1.2, 1.8, 2.0, 1.5]
}

df = pd.DataFrame(data)

# Pie chart
plt.figure(figsize=(6,6))
plt.pie(df['Average Price'], labels=df['Vegetable'], autopct='%1.1f%%', startangle=140)
plt.title('Average Vegetable Prices')
plt.show()