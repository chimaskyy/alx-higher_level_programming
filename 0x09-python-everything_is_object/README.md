# Python - Everything is object

* Every object has an identity, a type and a value. An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The ‘is’ operator compares the identity of two objects; the id() function returns an integer representing its identity.
* An object is something variable can refer to
```
>>> name = 'Chiamaka'
Chiamaka
```
* class is a template for creating object while object is an instance of a class which has its own uniqe data.

* Immutable objects are objects that cannot be changed after they have been created(tuple, string) while mutable object can be changed after they have been created(list,sets).

* Object are accesed through reference in memory. Variables store reference to object(in memory) and not the object

* To check if two variable are identicle in memory the keyword ```is``` is used
```
>>> name = 'Jessica'
>>> name = name1
>>> name is name1
True
```
* Aliasing occurs when two different varaiable has same object in memory. Changes made to one affects the other
```
>>> name = 'Chiamaka'
>>> name2 = name
>>> name == name2
True
```
* To check if two variables are linked to the same object ```id()``` is used
```
>>> name = 'Chiamaka'
>>> name1 = 'Chiamaka'
>>> (id(name) == id(name1))
True
```

* In Python, function arguments are passed by object reference. When you pass a variable to a function, you are actually passing the reference to the object it points to. This means that if you modify the object inside the function, the changes will be reflected outside the function as well. However, if you reassign the reference inside the function, it won't affect the original variable outside the function. This behavior is consistent with the mutable and immutable nature of objects in Python.

* In Python, small integers (typically in the range of -5 to 256) are cached and reused for memory optimization. When you assign the same value to multiple variables, as in this case below, Python will often reuse the same memory location to store the value. ```a``` and ```b``` both point to the same integer object in memory which is ```6```
```
a = 6
b = 6
```
so when ```a = 6``` gets executed it only assigns the address of the inbuilt integer object 1 to a 
Lets observe the code below:
```
>>> a = 30
>>> id(a)
9793984
>>> b = 30
>>> id(b)
9793984
>>> a is b
True
```
Address of a and b here are the same.

Now lets observe with a number greater  than 256:
```
>>> a = 280
>>> id(a)
140215269865744
>>> b = 280
>>> id(b)
140215269865648
>>> a is b
False
>>> a == b
True
```
Here, we see that the two address are different, this means that a created an onject and b created a totally different object because 280 is above the range of builtin integer object.

Lets also try with integer below the inbuilt range:
```
>>> a = -10
>>> id(a)
140215269866032
>>> b = -10
>>> id(b)
140215268978800
>>> a is b
False
>>> a == b
True
```


