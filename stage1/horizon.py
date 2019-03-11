import os
import numpy as np
import matplotlib.pyplot as plt

# x = [u'INFO', u'CUISINE', u'TYPE_OF_PLACE', u'DRINK', u'PLACE', u'MEAL_TIME', u'DISH', u'NEIGHBOURHOOD']
# y = [160, 167, 137, 18, 120, 36, 155, 130]

x = (u'DT', u'RF', u'SVM ',
           u'Linear', u'Logistic')
y = [0.962, 0.962,
     0.958, 0.832, 0.958]

fig, ax = plt.subplots()
width = 0.6 # the width of the bars
ind = np.arange(len(y))  # the x locations for the groups
ax.barh(ind, y, color=['cyan', 'orange', 'Navy', 'blue',
                       'gray'])
ax.set_yticks(ind+width/2)
ax.set_yticklabels(x, minor=False)
plt.title('title')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([0.75, 1.00])
for i, v in enumerate(y):
    ax.text(v, i + 0.2, str(v), color='blue',
            fontweight='bold')
plt.show()
plt.savefig(os.path.join('test.png'), dpi=300, format='png', bbox_inches='tight') # use format='svg' or 'pdf' for vectorial picture