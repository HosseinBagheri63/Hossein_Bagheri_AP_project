def pairwise_div(Lnum, Ldenom):
    assert not 0 in Ldenom, 'ldenom contains 0'
    return [Lnum[i] / Ldenom[i] for i in range(len(Lnum))]