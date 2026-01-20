from ._imports import *


def sci_notation(mu, sigma, n=2):
    r"""
    Return scientific notation in LaTeX format: mu^{+/- sigma} * 10^n
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


# NOTE: GEMINI GENERATED MUST CHECK
def smart_tqdm(iterable, *args, **kwargs):
    """
    Wrapper intelligent pour tqdm qui gère automatiquement l'argument 'leave'.
    - Boucle principale : leave=True (reste affichée)
    - Boucles imbriquées : leave=False (disparaissent à la fin)
    """
    # Si l'utilisateur n'a pas forcé le 'leave', on décide pour lui
    if "leave" not in kwargs:
        # On regarde s'il y a déjà des barres tqdm actives via _instances
        # Si len > 0, c'est qu'on est déjà dans une boucle -> on nettoiera (False)
        # Sinon, on est le chef -> on laisse (True)
        kwargs["leave"] = (len(tqdm._instances) == 0)
        
    return tqdm(iterable, *args, **kwargs)
