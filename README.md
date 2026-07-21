# bastools

Personal Python utilities for scientific plotting, formatting and data handling.
Mainly LLM-generated with post-correction.

## installation

PyPI:
```
pip install bastools
```

Or with uv:
```
uv add bastools
```

Or from source:

```
git clone https://github.com/BastienGrvt/bastools
cd bastools
uv sync
```

## Minimal example

```python
import bastools as bst

# Grid of subplots, last row auto-centered
fig, axs = bst.subplots_grid(2, 3, n_plots=5, plot_size=(5, 4))

# Format a measurement with its uncertainty
label = bst.sci_notation(1.234e-3, 5.6e-5, n=2)

axs[0].set_title(label)
fig.savefig("figure.png", dpi=300, bbox_inches="tight")
```

## Available tools

**Plots** (`bastools.plots`)

- `subplots_grid(rows, cols, n_plots, plot_size, grid)` - matplotlib subplot grid with automatic centering of incomplete rows
- `plot_colormap(...)` - plot a family of curves colored by a parameter, with linear or log colorbar

**Helpers** (`bastools.helpers`)

- `set_not_none(class_parent, **kwargs)` - assign keyword arguments to an object, skipping `None` values
- `get_not_none(arg, arg_type)` - return the argument if set, else a default of the given type
- `sci_notation(mu, sigma, n)` - format a value and its uncertainty in scientific notation
- `smart_tqdm(iterable, *args, **kwargs)` - `tqdm` wrapper that auto-detects nesting and sets `leave` accordingly
- `wsl_show(fig, file_path)` - save a matplotlib figure and open it from WSL
- `wsl_open(file_path)` - open a file with the Windows default application from WSL

**Draw** (`bastools.draw`)

- `svg_draw(x_min, x_max, N, unit_size, foo, file_path)` - render a 1D function as an SVG path

## Requirements

Python >= 3.13 - numpy, scipy, matplotlib, tqdm, rich, svgwrite

## License

Apache-2.0 - see [LICENSE](LICENSE).
