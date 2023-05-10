def mystery(sequence):
    return sequence == sorted(sequence) #returns true or false depending on how elements are arranged descending or ascending

series = mystery([0,2,9,9])
print(series)