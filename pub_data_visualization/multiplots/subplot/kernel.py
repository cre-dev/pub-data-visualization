
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kde
#


def kernel(ax,
           X,
           Y,
           ):
    """
        Draws in a subplot the 2d kernel of a set of points.
 
        :param ax: The ax to fill
        :param X: X-coordinates of the points
        :param Y: Y-coordinates of the points
        :type ax: matplotlib.axes._subplots.AxesSubplot
        :type X: np.array
        :type Y: np.array
        :return: None
        :rtype: None
    """ 
    
    x = X.values.reshape(-1)
    y = Y.values
    data = np.array([x, y]).T
    k = kde.gaussian_kde(data.T)
    nbins = 100
    xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))
    ax.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.cm.BuGn_r)
    ax.contour(xi,
               yi,
               zi.reshape(xi.shape),
               )
