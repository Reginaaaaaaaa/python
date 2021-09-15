def sort_list(elements):
    for i in range (len(elements)):
        for j in range(len(elements)-i-1):
            if elements[j]>elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
    return elements