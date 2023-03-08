def same_structure_as(array1, array2):
    length1 = len(array1)
    length2 = len(array2)

    if length1 == length2:
        return True
    else:
        return False

def main():
    testlist1 =  [[1],[2],[3]]
    testlist2 = [[4],[5],[6]]

    TrueOrFalse = same_structure_as(testlist1, testlist2)

    print(TrueOrFalse)

main()