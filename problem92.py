"""
We're given a hashmap associating each courseId key with a list of courseIds values,
 which represents that the prerequisites of courseId are courseIds.
 Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
"""

def solution(course_map):
    # just go over all the keys in the map, store them in a list, sort and return it
    print('Course map here is  : {}'.format(course_map))
    complete_course_set = set()
    for course_id, course_prerequisites  in course_map.items():
        print('Looping over : {}'.format(course_id))
        for course in course_prerequisites:
            if course not in course_map:
                return []
            else:
                complete_course_set.add(course)
        complete_course_set.add(course_id)
    return sorted(complete_course_set)


if __name__ == '__main__':
    course_map = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
    print(solution(course_map))