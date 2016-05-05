student = ['fu','li',1,2,3,'xing','kntao']
cource = ('English','Chinese','maths','geography','biology')
print(student)
student.pop()
print(student)
student.pop(2)
print(student)
student.insert(0,'felen')
print(student)
student.append('felen')
print(student)
print(len(student))
student.append(cource)
print(student)
print(len(student))

E:\PY>python ListTuple.py
['fu', 'li', 1, 2, 3, 'xing', 'kntao']
['fu', 'li', 1, 2, 3, 'xing']
['fu', 'li', 2, 3, 'xing']
['felen', 'fu', 'li', 2, 3, 'xing']
['felen', 'fu', 'li', 2, 3, 'xing', 'felen']
7
['felen', 'fu', 'li', 2, 3, 'xing', 'felen', ('English', 'Chinese', 'maths', 'geography', 'biology')]
8
