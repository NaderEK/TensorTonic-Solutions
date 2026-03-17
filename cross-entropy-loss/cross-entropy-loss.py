import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_pred, y_true = np.asarray(y_pred), np.asarray(y_true)
    if y_pred.shape[0] != y_true.shape[0]:
        return None
    N = y_true.shape[0]
    correct_probs = []

    for true, probs in zip(y_true, y_pred):
        correct_probs.append(probs[true])
    loss = - np.sum(np.log(correct_probs))/N

    return loss