# Python - Everything is object

* Every object has an identity, a type and a value. An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The ‘is’ operator compares the identity of two objects; the id() function returns an integer representing its identity.
* An object is something variable can refer to
```
>>> name = 'Chiamaka'
Chiamaka
```
* class is a template for creating object while object is an instance of a class which has its own uniqe data.

* Immutable objects are objects that cannot be changed after they have been created while mutable object can be changed after they have benn created(list,sets).

* Object are accesed through reference in memory. Variables store reference to object(in memory) and not the object

* To check if two variable are identicle the keyword ```is``` is used
```
>>> name = 'Jessica'
>>> name = name1
>>> name is name1
True
```
* Aliasing occurs when two different varaiable has same object in memory. Cahnges made to one affects the other
```
>>> name = 'Chiamaka'
>>> name2 = name
>>> name = name2
True
```
* To check if two variables are linked to the same object ```id()``` is used
```
>>> name = 'Chiamaka'
>>> name1 = 'Chiamaka'
>>> (id(name) == id(name1))
False
```
name and name1 reference different object i.e they are stored in different memory.

* In Python, function arguments are passed by object reference. When you pass a variable to a function, you are actually passing the reference to the object it points to. This means that if you modify the object inside the function, the changes will be reflected outside the function as well. However, if you reassign the reference inside the function, it won't affect the original variable outside the function. This behavior is consistent with the mutable and immutable nature of objects in Python.

