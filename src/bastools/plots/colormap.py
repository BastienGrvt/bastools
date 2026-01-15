from ._imports import *
from matplotlib.lines import Line2D


def _get_colormap(param_range, cmap_name="coolwarm", is_log=False):
    """
    Build ScalarMappable for colormap.
    """

    cm = plt.get_cmap(cmap_name)
    
    if is_log:
        norm = mpl.colors.LogNorm(vmin=np.min(param_range), vmax=np.max(param_range))
    else:
        norm = mpl.colors.Normalize(vmin=np.min(param_range), vmax=np.max(param_range))
        
    sm = mpl.cm.ScalarMappable(cmap=cm, norm=norm)
    sm.set_array(param_range)
    return sm



def _plot_colormap(
    ax,
    sm,
    func,
    x_range,
    param_range,
    label=None,
    linestyle='-',
):
    # Loop over each parameter value and calculate the corresponding y_values values
    for param in param_range:
        y_values = [func(x, param) for x in x_range]
        ax.plot(x_range, y_values, color=sm.to_rgba(param), linestyle=linestyle, label=label)
    return ax, y_values


def plot_colormap_old(
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


def plot_colormap(
    x_config,       
    param_config, 
    funcs,       
    config_plot=None,
    cmap_name="coolwarm",
):
    """
    Plot functions f(x, p) using a colormap to visualize parameter evolution.

    Args:
        x_config (dict): {'values': array, 'is_log': bool} for the absiss.
        param_config (dict): {'values': array, 'is_log': bool} for the parameter.
        funcs (list[dict]): List of {'func': f(x,p), 'label': str, 'linestyle': str}.
        config_plot (dict): Labels for 'title', 'x_label', 'y_label', 'param_label'.
        cmap_name (str): Matplotlib colormap (default: "coolwarn").

    Returns:
        tuple: (fig, ax, x_range, param_range).
    """
    # Get plot configuration
    config_plot = config_plot or {}
    x_label = config_plot.get("x_label", "")
    y_label = config_plot.get("y_label", "")
    param_label = config_plot.get("param_label", "")
    title = config_plot.get("title", "")

    fig, ax = plt.subplots(1, 1, figsize=(7, 5))

    # Set x values
    if "x_range" not in x_config:
        raise ValueError("x_config must contain the key 'x_range'.")
    x_range = x_config["x_range"]
    x_is_log = x_config.get("is_log", False)

    # Set param values
    if "param_range" not in param_config:
        raise ValueError("param_config must contain the key 'param_range'.")
    param_range = param_config["param_range"]
    param_is_log = param_config.get("is_log", False)

    # Build colormap
    sm = _get_colormap(param_range, cmap_name=cmap_name, is_log=param_is_log)
    
    legend_handles = [ ]
    
    # Loop on functions
    funcs = funcs if isinstance(funcs, list) else [ funcs ]
    for item in funcs:
        if "func" not in item:
            raise ValueError("Please provide a valid function via the key 'func'.")
        func = item["func"] 
        linestyle = item.get("linestyle", "-")
        label = item.get("label", None)
        ax, _ = _plot_colormap(ax, sm, func, x_range, param_range, linestyle=linestyle) 
        if label is not None:
            proxy = Line2D([], [], linestyle=linestyle, color="black", label=label)
            legend_handles.append(proxy)

    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label(param_label)
    if legend_handles:
        ax.legend(handles=legend_handles)
   
    # Set plot
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)    
    if x_is_log:
        ax.set_xscale('log') 
    ax.grid(True, alpha=0.3)
    
    return fig, ax, x_range, param_range


