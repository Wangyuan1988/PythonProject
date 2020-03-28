import seaborn as sns
import matplotlib.pyplot as plt

x_axis = ["A", "B","C","D","E","F"]
y_axis = [78.5, 79.6, 81.6, 75.4, 78.3, 79.6]

plt.ylabel('Accuracy')
plt.title('Accuracy of Classifier')

g=sns.barplot(x_axis, y_axis, color="red")
ax=g
#annotate axis = seaborn axis
for p in ax.patches:
             ax.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center', fontsize=11, color='gray', xytext=(0, 20),
                 textcoords='offset points')
_ = g.set_ylim(0,120) #To make space for the annotations