"""
파이썬 리스트
자료구조에서 중요
리스트 자료형(순서p, 중복o, 수정o, 삭제o)
"""

#선언
a=[]
b=list()
c=[70,75,80,85]
d=[1000, 10000, 'Ace', 'Base', 'Captine']
e=[1000, 10000, ['Ace', 'Base', 'Captine']]
f=[21.42, 'foobar', 3, 4, False, 3.14159]

#인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print(e[2][2])
print(list(e[2][2]))

#슬라이싱
print('>>>>>')
print('d-', d[0:3])
print(c+d)
print(c*3)
print(c[:3])
print(c[3:])
print()

a = [5,2,3,1,4]
print(a)
a.append(10)
print(a)
a.sort()
print(a)
a.reverse()
print(a)

print()
print()
print(a)
print(a.index(1))
print(a.index(5))
print()
print()


a.insert(2,7)
print(a)
del a[0]
print(a)
a.remove(7)
print(a)
print()

print(a.pop())
print(a)
print(a.count(4))
ex=[20,30]
a.extend(ex)
print(a)
print()
print()

sample=[1,2,3,4,5]
print(sample)
print(sample.index(4))
print(sample.index(1))

b=[1,2,3,4,5,6,7,8,9,10]
print(b.index(1))
print(b.index(5))

a=[1,2,3,4,5]
print(a)
print(a.index(4))
print()

print(a.pop())
print(a)
print()

print()
print(a.count(2))
print()

example=[10,20]
a.extend(example)
print(a)
