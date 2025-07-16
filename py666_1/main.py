'''data=[frozenset([1,2,3])].append(4)
print(data)'''
'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_vers(self):
        print(vars(self))
p=Person('Alice',25)
p.show_vers()'''
'''def Dynamic_update():
    x=10
    print('修改前',x)
    print('修改后',x)
Dynamic_update()'''
'''code=compile('x+y*2','<string>','eval')
x=3
y=4
print(eval(code))'''
'''def paginate(total_items,total_pages):
    pages,remaining=divmod(total_items,total_pages)
    return pages+(1 if remaining else 0)'''
'''gen=('hello\nworn')
print(repr(gen))'''

'''class Bankaccount():
    def __init__(self,owner:str):
        self.owner=owner
        self.__banance=0
    @property
    def banance(self):
        return self.__banance
    @banance.setter
    def banance(self,value):
        if value<0:
            self.__banance='余额不能为负数'
        else:
            self.__banance=value
ban=Bankaccount('xiaobu')
ban.banance=-9
print(ban.banance)'''

'''class Shape:
    def area(self):
        raise NotImplementedError
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return round(self.radius**2*3.14,2)
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return round(self.width*self.height,2)
shapes=[Circle(3),Rectangle(10,29)]
for s in shapes:
    print(s.area())'''

'''class Mysequence:
    def __init__(self,data):
        self.data=data
    def __len__(self):
        return len(self.data)
    def __getitem__(self,index):
        return self.data[index]
    #def __contains__(self,count):
     #   return count in self.data

seq=Mysequence([1,90,33,44,5])
print(seq[1:2])
print(1 in seq)'''

'''class Person:
    def __init__(self,x,y):
        self.x,self.y=x,y
    def __add__(self,other):
       return (self.x+other.x,self.y+other.y)
    def __mul__(self,other):
        return self.x*other.x,self.y*other.y
p1=Person(1,2)
p2=Person(3,4)
print(p1+p2)'''

'''class GameCharacter:
    def __init__(self,name,level=1):
        self.level=level
        self.name=name
        self.__inventory=[]
    def add_item(self,item):
        return self.__inventory.append(item)
    def save(self):
        return {'name':self.name,
                'level':self.level,
                'inventory':self.__inventory}
    @classmethod
    def load(cls,data):
         character=data['name'],data['level']
         for item in data['inventory']:
             character.add_item(item)
             return character'''

'''class DynameicAttributes:
    def __getattr__(self,name):
        return f'Attr_{name}'

obj=DynameicAttributes()
print(obj.hello)'''



