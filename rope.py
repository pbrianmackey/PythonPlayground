def BuildList(ropeList): 
    if not ropeList:
        return
    ropeCount = len(ropeList)
    result.append(ropeCount)

    smallest = min(ropeList)
    working_set = []
    for i in ropeList:
        rope = i - smallest
        if rope > 0:
            working_set.append(rope)
    BuildList(working_set)

if __name__ == '__main__':
    a = [3, 3, 2, 9, 7]
    result = []
    BuildList(a)
    print(result)