
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


# Visualization of continuous variable
def continuous_viz(dataframe, column):

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 8))

    # Create kernel density plot
    ax1 = sns.kdeplot(data = dataframe, x = column, ax = ax1)

    # Create Q-Q plot
    ax2 = sm.qqplot(dataframe[column], fit = True, line = 's', ax = ax2)

    # Show plots
    return plt.show()



