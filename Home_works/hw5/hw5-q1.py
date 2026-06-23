def pairwise_div(Lnum, Ldenom):
    if 0 in Ldenom:
        raise ValueError("Ldenom contains 0")
    
    return [Lnum[i] / Ldenom[i] for i in range(len(Lnum))]
pairwise_div([1,1,1],[0,0,0])