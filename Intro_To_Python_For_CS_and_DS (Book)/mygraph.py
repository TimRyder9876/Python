import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
rolls = [random.randrange(1, 7) for i in range(600)]
values, frequencies = np.unique(rolls, return_counts=True)
print(values)
print(frequencies)
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style("whitegrid") 
sns.barplot(x = values, y = frequencies, hue = 12, palette = 'bright') 
