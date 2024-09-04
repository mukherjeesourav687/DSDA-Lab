import matplotlib.pyplot as plt

# Box plots
df.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False, figsize=(10, 8))
plt.show()

# Histograms
df.hist(edgecolor='black', figsize=(10, 8))
plt.show()
from pandas.plotting import scatter_matrix

# Scatter plot matrix
scatter_matrix(df, figsize=(12, 10), alpha=0.8, diagonal='kde')
plt.show()
