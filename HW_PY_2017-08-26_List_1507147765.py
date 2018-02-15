inlist = [15, 14, 59, [59, 58, 19, [2, 9]], 35, 89, 101]
outlist = []

def unpack_list (nlist):
    for val in nlist:
        if type(val) == type(inlist):
            unpack_list(val)
        else:
            outlist.append(val)

unpack_list(inlist)
print(outlist)
