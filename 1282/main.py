def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    res = []
    groups = {}
    for i in range(len(groupSizes)):
        # step 1: check if group exists
        if groupSizes[i] not in groups.keys():
            groups[groupSizes[i]] = []
        # step 2: add to group
        groups[groupSizes[i]].append(i)
        # step 3: check if group is full and add to solutions if so
        if len(groups[groupSizes[i]]) == groupSizes[i]:
            res.append(groups[groupSizes[i]].copy())
            groups[groupSizes[i]] = []
    return res
