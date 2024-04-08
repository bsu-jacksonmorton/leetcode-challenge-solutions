class Solution:
    '''
    runtime: O(n)
    space: O(1)
    '''
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)
        while sandwiches:
            if counts[sandwiches[0]] == 0: # no one wants that sandwhich... :(
                break
            elif students[0] == sandwiches[0]:
                students.pop(0)
                counts[sandwiches[0]] -= 1
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
        return len(students)
