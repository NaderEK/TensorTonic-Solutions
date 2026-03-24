def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    first_k = recommended[:k]
    relevant_set = set(relevant)
    num_relvant = 0
    for r in first_k:
        if r in relevant_set:
            num_relvant+=1
    N = len(relevant)
    precision = num_relvant/k
    recall = num_relvant/N

    return [precision, recall]