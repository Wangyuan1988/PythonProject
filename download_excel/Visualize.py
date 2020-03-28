"""
Horizontal bar plots
====================

"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


sns.set(style="whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(16, 25))

# Load the example car crash dataset
# crashes = sns.load_dataset("car_crashes").sort_values("total", ascending=False)

crashes =  pd.read_excel('price.xlsx')


# Plot the total crashes
sns.set_color_codes("pastel")
sns.barplot(x="total", y="range", data=crashes,label="Total", color="b")


# Plot the crashes where alcohol was involved
sns.set_color_codes("muted")
g = sns.barplot(x="count", y="range", data=crashes,label="count", color="b")



# ax=g

# for p in ax.patches:
#              ax.annotate("%.2f" % p.get_width(), (p.get_x() + p.get_height() / 2., p.get_width()),
#                  ha='center', va='center', fontsize=11, color='gray', xytext=(0, 20),
#                  textcoords='offset points')

                 # Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 500), ylabel="",xlabel="price")
sns.despine(left=True, bottom=True)