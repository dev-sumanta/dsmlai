# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:09:42 2017

@author: Samar
"""

from operator import attrgetter, itemgetter, methodcaller


class Student:
        def __init__(self, n, g, a):
                self.name = n
                self.grade = g
                self.age = a

        # repr(instance of this class will use this def)
        # and eval(repr(instance)) will give back the instance
        def __repr__(self):
            return "Student('{0}', '{1}', {2})".format(
                    self.name, self.grade, self.age)

        # print will use this - if this were not there
        # then print would have used repr only
        def __str__(self):
            return self.name + ' - ' + self.grade + ' , ' + str(self.age)

        def weighted_grade(self):
                return 'CBA'.index(self.grade) / float(self.age)

        def __getitem__(self, index):
            if (index == 0):
                return self.name
            if(index == 1):
                return self.grade
            if(index == 2):
                return self.age


student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
        Student('dave', 'C', 10),
        Student('dave', 'B', 12)
]

print(sorted(student_objects, key=lambda student: student.age))

# sort by grade descendnig, then by age
print(sorted(sorted(student_objects,
                    key=lambda stdnt: stdnt. grade, reverse=True),
      key=lambda stdnt: stdnt.age))

print(sorted(student_objects, key=itemgetter(2)))
print(sorted(student_objects, key=attrgetter('age')))
print(sorted(student_objects, key=attrgetter('grade', 'age')))
print(sorted(
        sorted(student_objects, key=attrgetter('age'), reverse=True),
        key=attrgetter('grade'), reverse=True))

print([(student.name, student.weighted_grade())
      for student in student_objects])

print(sorted(student_objects, key=methodcaller('weighted_grade')))
