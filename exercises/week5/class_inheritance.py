# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:55:47 2017

@author: Atlas
Understand class Inheritance
"""

class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2 #obj.a
        self.b = 3 #obj.b
        self.d = 12
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5 #obj.c Because there is c attribute in class b
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        self.d = 6 #obj.d Uses its own attribute Unless an inheritance is called later.
        B.__init__(self)

    def z(self):
        print("D.z")

obj = D()
        
print("This is obj.a", obj.a)

print("This is onj.b", obj.b)

print("This is obj.c", obj.c)

print("This is obj.d", obj.d)

print("This is obj.x()", obj.x())

print("This is obj.y()", obj.y()) #Weird. I expected it come out as B.y. 
                                # Because this inherits others initializes.
                                
print("This is onj.z()", obj.z())


