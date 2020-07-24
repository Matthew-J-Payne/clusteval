#-----------------------------------------------
# Name        : dbscan.py
# Author      : E.Taskesen
# Contact     : erdogant@gmail.com
# Licence     : MIT
#-----------------------------------------------

from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt


def plot_dendrogram(*args, **kwargs):
    """Plot dendrogram using specific input parameters.

    Parameters
    ----------
    Z : array-like
        Generated by linkage method: Z = linkage(X, method='ward', metric='euclidean')
    labels : list, (default: None)
        Plot the labels. When None: the index of the original observation is used to label the leaf nodes.
    max_d : Float, (default: None)
        Height of the dendrogram to make a horizontal cut-off line.
    truncate_mode : string, (default: None)
        Truncation is used to condense the dendrogram, which can be based on: 'level', 'lastp' or None
    show_contracted : bool, (default: True)
        The heights of non-singleton nodes contracted into a leaf node are plotted as crosses along the link connecting that leaf node.
    annotate_above : float, (default: 0)
        Annotate samples above this threshold.
    orientation : string, (default: 'top')
        Direction of the dendrogram: 'top', 'bottom', 'left' or 'right'
    leaf_font_size : int, (default: 12)
        Font size labels.
    leaf_rotation : int, (default: 90)
        Rotation of the labels [0-360].
    no_plot : bool, (default = False)
        Plot the dendrogram.

    Returns
    -------
    ddata : dict
        Dictionary containing information regarding the dendrogram.
        'color_list': A list of color names.
        'ivl' : A list of labels corresponding to the leaf nodes.
        'icoord', 'dcoord', 'leaves'

    """
    max_d = kwargs.pop('max_d', None)
    if max_d and ('color_threshold' not in kwargs): kwargs['color_threshold'] = max_d
    annotate_above = kwargs.pop('annotate_above', 0)

    # Compute the dendrogram
    ddata = dendrogram(*args, **kwargs)

    # Plot the dendrogram
    if not kwargs.get('no_plot', False):
        # Extract coordinates and colors
        for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
            x = 0.5 * sum(i[1:3])
            y = d[1]

            # Annotate above threshold
            if y > annotate_above:
                plt.plot(x, y, 'o', c=c)
                plt.annotate("%.3g" % y, (x, y), xytext=(0, -5), textcoords='offset points', va='top', ha='center')

        # Plot horizontal line
        if max_d: plt.axhline(y=max_d, c='k')
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('Samples')
        plt.ylabel('distance')

    # Return
    return ddata
