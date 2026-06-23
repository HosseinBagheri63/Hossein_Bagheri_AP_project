''' function with bug:
def flatten(lst):
    if not lst:
        return []
    if isinstance(lst[0], list):
        return flatten(lst[0])
    else:
        return [lst[0]] + flatten(lst[1:])
'''
def flatten(lst):
    if not lst:
        return []
    res=[]
    for thing in lst:
        if isinstance(thing, list):
            res.extend(flatten(thing))
        else:
            res.append(thing)
    return res
#باگ تابع اولیه: اگر اولین عضو لیست یک، یک لیست باشد تابع فقط فلت شده عضو اول لیست اصلی را برمیگرداند
