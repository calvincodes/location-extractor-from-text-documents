import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('DT', 'RF', 'SVM ',
           'Linear', 'Logistic')
y_pos = np.arange(len(objects))
performance = [0.9624301120374741, 0.9624301120374741, 0.9587387423604193, 0.8283492345819937, 0.9575079789558318]


plt.bar(y_pos, performance, align='center', alpha=0.5,
        width=0.3)
plt.bar(y_pos, performance, color=['black', 'red', 'green', 'blue', 'cyan'])
plt.ylim(0.75,1)
plt.xticks(y_pos, objects)
plt.xlabel('Classifier')
plt.ylabel('Scores')
plt.title('Classifiers with scores')

plt.show()