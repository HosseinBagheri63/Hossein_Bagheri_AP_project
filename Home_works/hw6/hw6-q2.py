def deep_sum(data):
    sum=0
    for thing in data:
        if type(thing)==list:
            sum+=deep_sum(thing)
        elif type(thing)==int:  
            sum+=thing
    return sum