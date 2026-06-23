def deep_max_depth(data):
    max_depth=0
    for thing in data:
        if type(thing)==list:
            max_depth=max(max_depth,deep_max_depth(thing)+1)
    return max_depth