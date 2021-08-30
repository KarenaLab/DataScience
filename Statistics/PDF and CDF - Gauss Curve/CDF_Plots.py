

# Libraries

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt



# Main Program ----------------------------------------------------------

# 1- Information

Title = "CDF - Cumulative Normal Distribution Function"

Mean = 0
StdDev = 1

x = np.arange(start= -5, stop= 5, step= 0.001)
y = norm.cdf(x, loc= Mean, scale= StdDev)


# 2- Plotting

fig = plt.figure(figsize= (8, 4.5))
ax = fig.add_subplot(1, 1, 1)

ax.plot(x, y)

ax.set_title(Title, fontsize= 16)

ax.set_xlabel("x")


ax.set_ylabel("CDF(x)")
ax.set_ylim(bottom= 0)

ax.grid(color= "grey", linestyle= "--", linewidth= 0.5)
ax.set_axisbelow(True)


plt.tight_layout()
plt.savefig(Title, dpi= 240)
plt.show()
