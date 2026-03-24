def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    import numpy as np
    if len(y_true) != len(y_pred):
        return None
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    N = len(y_true)
    TP = len(y_pred[y_pred == y_true])
    FP = abs(TP - N)
    FN = abs(TP - N)

    F1_score = 2*(TP)/(2*TP + FP + FN)
    return F1_score