from ._imports import *


def sci_notation(mu, sigma, n=2):
    """
    Return scientific notation in LaTeX format: mu^{\pm sigma} * 10^n
    """
    # Set the digits number
    decimals = max(0, n - 1)
    # Exponent calculation
    if mu == 0:
        exponent = 0
    else:
        exponent = int(math.floor(math.log10(abs(mu))))
    m = mu / 10**exponent
    s = sigma / 10**exponent 
    # Check non-zero uncertainties
    min_resolution = 10**(-decimals)
    if sigma > 0 and round(s, decimals) == 0:
        s = min_resolution
    return fr'${m:.{decimals}f}^{{\pm {s:.{decimals}f}}} \cdot 10^{{{exponent}}}$'


