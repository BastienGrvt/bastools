from ._imports import *


def subplots_grid(rows, cols, n_plots, plot_size=(5, 4), grid=True):
    """
    Crée une figure avec des subplots centrés sur la dernière ligne si incomplète.
    NB: vibe-coded method
    
    Args:
        rows (int): Nombre de lignes de la grille (N).
        cols (int): Nombre de colonnes de la grille (M).
        n_plots (int): Nombre total de subplots à tracer.
        plot_size (tuple): Taille (largeur, hauteur) de chaque subplot.
        
    Returns:
        fig: La figure matplotlib.
        axs: Une liste plate (1D) contenant les n_plots axes créés.
    """
    # 1. Gestion des erreurs de dimension
    if n_plots > rows * cols:
        raise ValueError(f"n_plots ({n_plots}) dépasse la capacité de la grille {rows}x{cols} ({rows*cols}).")

    # 2. Création de la figure avec la taille calculée intelligemment
    # On ajoute constrained_layout=True pour gérer automatiquement les espaces
    fig = plt.figure(figsize=(cols * plot_size[0], rows * plot_size[1]), constrained_layout=True)
    
    # 3. Création de la GridSpec avec résolution doublée
    # L'astuce : On crée 2*cols colonnes. Chaque plot standard prendra 2 unités de large.
    # Cela permet de centrer des éléments avec un décalage de "1 unité" (soit une demi-colonne réelle).
    gs = fig.add_gridspec(rows, 2 * cols)
    
    axs = []
    plots_remaining = n_plots

    for r in range(rows):
        # Combien de plots sur cette ligne ? (Max 'cols', ou le reste de 'n_plots')
        plots_this_row = min(plots_remaining, cols)
        
        if plots_this_row == 0:
            break
            
        # 4. Calcul du décalage pour centrer
        # Espace vide en unités de "demi-colonnes" = (Capacité Max - Utilisé)
        # Capacité max ligne = 2 * cols
        # Utilisé = 2 * plots_this_row
        # Marge à gauche = (Total - Utilisé) / 2
        empty_slots = (2 * cols) - (2 * plots_this_row)
        left_offset = empty_slots // 2
        
        for c in range(plots_this_row):
            # Calcul des indices de colonnes dans la grille haute résolution
            start_col = left_offset + (c * 2)
            end_col = start_col + 2
            
            # Création du subplot à l'emplacement précis
            ax = fig.add_subplot(gs[r, start_col:end_col])
            if grid:
                ax.grid()
            axs.append(ax)
        
        plots_remaining -= plots_this_row

    return fig, axs
