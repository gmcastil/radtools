# pylint: disable=C0103
"""
Provides tools for plotting SEE cross cross sections consistently

"""
import matplotlib.pyplot as plt

def plot_SEFI(data):
    """Plot multiple SEFI cross sections in a visually appealing way

    Args:
      data (list)

    """
    # Create a blank figure and some axes
    # For each cross section in data
    #   Determine what data are UB
    #   Plot the data and UB together (with different markers)
    #   Add the data to the legend
    # Set the axes limits, title, and scale
    # Show the legend
    fig = plt.figure()
    axes = fig.add_subplot(111)
    plt.show()

#def _get_upper_bounds(
