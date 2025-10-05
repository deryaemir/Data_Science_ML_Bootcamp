#############################################
# DATA VİSUALİZATİON: MATPLOTLIB & SEABORN
#############################################

#############################################
# MATPLOTLIB
#############################################
# Categorical variable: bar chart. countplot / bar
# Numerical variable: histogram (hist)(dağılım gösterir.), box plot (boxplot)(dağılım ve aykırı değerler)

#############################################
# Categorical Variable Visualization
#############################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)#üç nokta göstermesin diye bunu kullandık.
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
# value_counts(): The first function that should come to mind for categorical variables,
# because it describes (summarizes) the corresponding categorical variable.
df['sex'].value_counts().plot(kind='bar')
plt.show()

#############################################
# Numerical Variable Visualization
#############################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])# Outliers can be detected based on quartile (IQR) values.
plt.show()

#############################################
# Features of Matplotlib
#############################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
# By its structure, it allows data visualization in a layered manner.

#######################
# plot
#######################
# plot: The main function in Matplotlib used to create line charts for visualizing numerical data.


x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()
# If you run another data visualization code without closing the previous plot,
# it will be drawn on top of the previous visualization.

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()



#######################
# marker
#######################
# marker: Used to indicate data points on a plot with symbols such as circles, squares, or triangles.

y = np.array([13, 28, 11, 100])

plt.plot(y, marker='o')
plt.show()

plt.plot(y, marker='*')
plt.show()

markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']

#######################
# line
#######################

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashdot", color="r")
plt.plot(y,linestyle="dotted", color="b")
plt.show()

#######################
# Multiple Lines
#######################

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

#######################
# Labels
#######################

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
# Title
plt.title("Bu ana başlık")
# Naming the X-axis
plt.xlabel(" Naming the X-axis")
plt.ylabel("Naming the Y-axis")

plt.grid()
plt.show()

#######################
# Subplots
#######################

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)# The first plot in a one-row, two-column layout.
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 2, 2)# The second plot in a one-row, two-column layout.
plt.title("2")
plt.plot(x, y)
plt.show()


# Positioning 3 plots in one row and 3 columns.
# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(x, y)

# plot 3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)

plt.show()

#############################################
# SEABORN
#############################################
# Doing more with less effort.
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()
# Categorical Variable Visualization
df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)
plt.show()

df['sex'].value_counts().plot(kind='bar')
plt.show()


#############################################
# Numerical Variable Visualization
#############################################

sns.boxplot(x=df["total_bill"])
plt.show()

df["total_bill"].hist()
plt.show()

