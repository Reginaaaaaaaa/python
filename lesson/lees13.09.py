k = int(input())
def convert_time(t):
    days = t//(24*60*60)
    t = t%(24*60*60)
    hours = t//(60*60)
    t = t%(60*60)
    minutes = t//60
    t = t%60
    return str(days)+":"+str(hours)+":"+str(minutes)+":"+str(t)
print(convert_time(k))



