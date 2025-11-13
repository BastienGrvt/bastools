from ._imports import *
import matplotlib as mpl
from matplotlib.lines import Line2D


def _get_colormap(L):
    """
    Generate a colormap and normalize it based on the range of values in L.

    Parameters:
    L (array): Array of parameter values used for colormap normalization.

    Returns:
    ScalarMappable: A colormap scalar mappable object.
    """
    # Use the 'coolwarm' colormap from Matplotlib
    cm = mpl.cm.coolwarm
    # Normalize the colormap based on the min and max values of L
    norm = mpl.colors.Normalize(vmin=np.min(L), vmax=np.max(L))
    # Create a ScalarMappable object for the colormap
    sm = mpl.cm.ScalarMappable(cmap=cm, norm=norm)
    sm.set_array(L)
    return sm, cm, norm



def _ax_colormap(
    ax,
    sm,
    foo,
    x_values,
    param_values,
    label=None,
    linestyle='-',
):
    # Loop over each parameter value and calculate the corresponding y_values values
    for param in param_values:
        y_values = [foo(x, param) for x in x_values]
        ax.plot(x_values, y_values, color=sm.to_rgba(param), linestyle=linestyle, label=label)
    return ax, y_values


def plot_colormap(
    x_min, x_max, N_x,
    param_min, param_max, N_param,
    foos,
    str_dict=None,
    cmap_name="viridis",
    log_bool=False,
):

    # Get the string parameters
    str_dict = str_dict or {}
    x_label = str_dict.get("x_label", "")
    y_label = str_dict.get("y_label", "")
    param_label = str_dict.get("param_label", "")
    title = str_dict.get("title", "")

    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    plt.subplots_adjust(hspace=0.3, wspace=0.3)


    # Define the parameter and x values
    x_values = np.logspace(np.log10(x_min), np.log10(x_max), N_x) if log_bool else np.linspace(x_min, x_max, N_x)
    param_values = np.linspace(param_min, param_max, N_param)

    # Get the colormap for plotting based on the parameter values
    sm, _, _ = _get_colormap(param_values)
    legend_handles = []
    
    for item in foos:
        linestyle = item.get("linestyle", "-")
        label = item.get("label", None)
        foo = item.get("foo", lambda x, param: 1)
        ax, _ = _ax_colormap(ax, sm, foo, x_values, param_values, linestyle=linestyle)
        if label is not None:
            proxy = Line2D([], [], linestyle=linestyle, color="black", label=label)
            legend_handles.append(proxy)

    # Add a colorbar to the plot
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label(param_label)
    # Customize the plot's appearance
    if legend_handles:
        ax.legend(handles=legend_handles)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    if log_bool:
        ax.set_xscale('log')
    ax.grid()
    return fig, ax, x_values, param_values
