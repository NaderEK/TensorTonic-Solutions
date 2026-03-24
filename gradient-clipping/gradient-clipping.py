import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    g = np.asarray(g)
    g_norm = np.linalg.norm(g)
    
    if g_norm == 0 or max_norm <=0 :
        return g
        
    g_clipped = np.where(g_norm <= max_norm, g, g*max_norm/g_norm)

    return g_clipped