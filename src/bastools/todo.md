# Plot module `plot.py`

- Set clean argument for plot colormap: `plot_colormap(bound_x, N_x, bound_param, N_param, ...)`
    - Put everything in a dict `param_dict` (`foo` `param_min`/`param_max` and not if `None`)
    - Consequence on full-repeater code
    - Consequence on `q_elink` module

- Set a general plot class with simple plot + `plot_colormap` + `subplot_grid`
