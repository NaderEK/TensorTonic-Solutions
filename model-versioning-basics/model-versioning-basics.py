def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    # Write code here
    best = sorted(models, key=lambda x: (x['accuracy'], -x['latency'], x['timestamp']))[-1]
    
    return best['name']