class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #circular sandwich = 0
        #square sandwich = 1 
        # number of sandwiches = number of students
        count = 0
        san = 0
        while count < len(students):
            if sandwiches[san] == students[0]:
                san += 1
                students.pop(0)
                count = 0
            else:
                aux = students.pop(0)
                students.append(aux)
                count += 1

       #return # of students who can't eat
        return len(students)