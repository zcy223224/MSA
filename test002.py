import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def auto_label(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height), # put the detail data
                    xy=(rect.get_x() + rect.get_width() / 2, height), # get the center location.
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def auto_text(rects):
    for rect in rects:
        plt.text(x=rect.get_x()+0.1, y=rect.get_height(), s=rect.get_height(), ha='left', va='bottom')


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

index = np.arange(len(labels))
width = 0.2

fig, ax = plt.subplots()
rect1 = ax.bar(index - width / 2, men_means, color ='lightcoral', width=width, label ='Men')
rect2 = ax.bar(index + width / 2, women_means, color ='springgreen', width=width, label ='Women')

ax.set_title('Scores by gender')
ax.set_xticks(ticks=index)
ax.set_xticklabels(labels)
ax.set_ylabel('Scores')

ax.set_ylim(0, 50)
# auto_label(rect1)
# auto_label(rect2)
auto_text(rect1)
auto_text(rect2)

ax.legend(loc='upper right', frameon=False)
fig.tight_layout()
plt.savefig('2.tif', dpi=300)
plt.show()