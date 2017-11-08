import numpy as np
import matplotlib.pyplot as plt

from data_utils.stats import gaussian_kde


def bivariate_kdeplot(x, y, weights=None, xlim=None, ylim=None, stepsize=100j, bw='scott',
                      density_postprocess_fun=None, ax=None,
                      scatter=True, scatter_kws={'alpha': .05},
                      contourf=True, contourf_kws={'cmap': 'Blues', 'alpha': .75},
                      contour=True, contour_kws={'colors': 'k', 'alpha': .25}):
    if xlim is not None:
        xmin, xmax = xlim
    else:
        xmin, xmax = np.min(x), np.max(x)

    if ylim is not None:
        ymin, ymax = ylim
    else:
        ymin, ymax = np.min(y), np.max(y)

    xx, yy = np.mgrid[xmin:xmax:stepsize, ymin:ymax:stepsize]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([x, y])
    kernel = gaussian_kde(values, weights=weights, bw_method=bw)
    densities = np.reshape(kernel(positions).T, xx.shape)

    if density_postprocess_fun is not None:
        densities = density_postprocess_fun(densities)

    if ax is None:
        fig, ax = plt.subplots()

    if scatter:
        ax.scatter(x, y, **scatter_kws)

    if contourf:
        ax.contourf(xx, yy, densities, **contourf_kws)

    if contour:
        ax.contour(xx, yy, densities, **contour_kws)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
