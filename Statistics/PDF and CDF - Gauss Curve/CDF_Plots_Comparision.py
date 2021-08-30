

# Libraries

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt



# Main Program ----------------------------------------------------------

# 1- Information

Title = "CDF Comparison - Normal Distribution"


x = np.arange(start= -5, stop= 5, step= 0.001)
#y = norm.pdf(x, loc= Mean, scale= StdDev)


# 2- Plotting

fig = plt.figure(figsize= (8, 4.5))
ax = fig.add_subplot(1, 1, 1)

ax.plot(x, norm.cdf(x, loc= 0, scale= 0.3),
        color= "blue", label= "Mean= 0; StdDev= 0.3")

ax.plot(x, norm.cdf(x, loc= 0, scale= 1),
        color= "red", label= "Mean= 0; StdDev= 1.0")

ax.plot(x, norm.cdf(x, loc= 0, scale= 2),
        color= "orange", label= "Mean= 0; StdDev= 2.0")

ax.plot(x, norm.cdf(x, loc= 2, scale= 0.5),
        color= "green", label= "Mean= 2; StdDev= 0.5")


ax.set_title(Title, fontsize= 16)

ax.set_xlabel("x")

ax.set_ylabel("CDF(x)")
ax.set_ylim(bottom= 0)

ax.grid(color= "grey", linestyle= "--", linewidth= 0.5)
ax.set_axisbelow(True)

plt.legend(loc= "best", framealpha= 1)

     
plt.tight_layout()
plt.savefig(Title, dpi= 240)
plt.show()
