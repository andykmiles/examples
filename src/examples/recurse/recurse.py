# recursion examples


def countZZ(zz_string):
    """recursively find zz"""
    if "zz" not in zz_string:
        return 0
    # look in first 2 positions
    count_zz = 0 if zz_string[0:2].find("zz") == -1 else 1
    # find returns position found; if not found, -1
    # convert to an offset to skip over zzz
    # show how it works; delete next line before submission
    print(count_zz, zz_string)
    # skip along the string, but adding one to avoid counting
    # where there is an odd number of z's
    return count_zz + countZZ(zz_string[count_zz + 1:])


print(countZZ("szzzzlzz"))

# -----

def elimDuplicates(dup_analysis):
    if len(dup_analysis) > 1:
        if dup_analysis[0] != dup_analysis[1]:
            return dup_analysis[0] + elimDuplicates(dup_analysis[1:])
        return elimDuplicates(dup_analysis[1:])
    else:
        return dup_analysis

print(elimDuplicates("gttfrrssfww"))
