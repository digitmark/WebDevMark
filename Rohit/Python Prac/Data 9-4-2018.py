Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ("Enter your name")
Enter your name
>>> fruits = ["apple","mango","banana"]
>>> fruits
['apple', 'mango', 'banana']
>>> fruits.append("jackfruit")
>>> fruits
['apple', 'mango', 'banana', 'jackfruit']
>>> for x in fruits
SyntaxError: invalid syntax
>>> for x in fruits:
	print(x)

	
apple
mango
banana
jackfruit
>>> for fruits
SyntaxError: invalid syntax
>>> for fruits:
	
SyntaxError: invalid syntax
>>> 
>>> clear
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> fruits
['apple', 'mango', 'banana', 'jackfruit']
>>> fruits.sort()
>>> fruits
['apple', 'banana', 'jackfruit', 'mango']
>>> fruits.reverse()
>>> fruits
['mango', 'jackfruit', 'banana', 'apple']
>>> print(len(fruits))
4
>>> names = {"Rohit","Penguin","Panda","Sneha"}
>>> names
{'Penguin', 'Rohit', 'Sneha', 'Panda'}
>>> for x in names
SyntaxError: invalid syntax
>>> for x in names:
	print(x)

	
Penguin
Rohit
Sneha
Panda
>>> print("Rohit" in names)
True
>>> names.update("Doggo")
>>> names
{'o', 'Sneha', 'Penguin', 'g', 'Rohit', 'D', 'Panda'}
>>> names.remove("D","o","g")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    names.remove("D","o","g")
TypeError: remove() takes exactly one argument (3 given)
>>> names.pop("D","o","g")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    names.pop("D","o","g")
TypeError: pop() takes no arguments (3 given)
>>> names
{'o', 'Sneha', 'Penguin', 'g', 'Rohit', 'D', 'Panda'}
>>> names.add{"Doggo"}
SyntaxError: invalid syntax
>>> names.add("Doggo")
>>> names
{'o', 'Sneha', 'Doggo', 'Penguin', 'g', 'Rohit', 'D', 'Panda'}
>>> names.pop("D")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    names.pop("D")
TypeError: pop() takes no arguments (1 given)
>>> names.union(["D","o","g"])
{'o', 'Sneha', 'Doggo', 'Penguin', 'g', 'Rohit', 'D', 'Panda'}
>>> names
{'o', 'Sneha', 'Doggo', 'Penguin', 'g', 'Rohit', 'D', 'Panda'}
>>> names.clear("D")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    names.clear("D")
TypeError: clear() takes no arguments (1 given)
>>> names.remove("D")
>>> names.remove('D')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    names.remove('D')
KeyError: 'D'
>>> names.discard('D')
>>> names
{'o', 'Sneha', 'Doggo', 'Penguin', 'g', 'Rohit', 'Panda'}
>>> names.discard(["o","g"])
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    names.discard(["o","g"])
TypeError: unhashable type: 'list'
>>> names.discard(['o','g'])
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    names.discard(['o','g'])
TypeError: unhashable type: 'list'
>>> names.discard("o","g")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    names.discard("o","g")
TypeError: discard() takes exactly one argument (2 given)
>>> names.discard(['o','g'])
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    names.discard(['o','g'])
TypeError: unhashable type: 'list'
>>> names.discard("o")
>>> names.discard("g")
>>> names
{'Sneha', 'Doggo', 'Penguin', 'Rohit', 'Panda'}
>>> names.pop()
'Sneha'
>>> names
{'Doggo', 'Penguin', 'Rohit', 'Panda'}
>>> names.add("Sneha")
>>> names
{'Sneha', 'Doggo', 'Penguin', 'Rohit', 'Panda'}
>>> colleges = {
	"Hinduja" : "Charni road",
	"Mithibai" : "Vile parle",
	"Dalmia" : "Malad"
	}
>>> colleges
{'Hinduja': 'Charni road', 'Mithibai': 'Vile parle', 'Dalmia': 'Malad'}
>>> print(colleges)
{'Hinduja': 'Charni road', 'Mithibai': 'Vile parle', 'Dalmia': 'Malad'}
>>> print(colleges[])
SyntaxError: invalid syntax
>>> print(colleges[1])
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(colleges[1])
KeyError: 1
>>> x = colleges("Dalmia")
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    x = colleges("Dalmia")
TypeError: 'dict' object is not callable
>>> x = colleges["Dalmia"]
>>> print(x)
Malad
>>> x = colleges.get("Hinduja")
>>> print(x)
Charni road
>>> colleges["Mithibai"] = "Andheri"
>>> print(colleges)
{'Hinduja': 'Charni road', 'Mithibai': 'Andheri', 'Dalmia': 'Malad'}
>>> for x in colleges
SyntaxError: invalid syntax
>>> for x in colleges:
	print(x)

	
Hinduja
Mithibai
Dalmia
>>> 
KeyboardInterrupt
>>> for x in colleges:
	print(colleges[x])

	
Charni road
Andheri
Malad
>>> for x in colleges:
	print(x),
	print(colleges[x])

	
Hinduja
(None,)
Charni road
Mithibai
(None,)
Andheri
Dalmia
(None,)
Malad
>>> for x in colleges:
	print(x)
	print(colleges[x])

	
Hinduja
Charni road
Mithibai
Andheri
Dalmia
Malad
>>> for x in colleges:
	print(x) ":" print(colleges[x])
	
SyntaxError: invalid syntax
>>> for x in colleges:
	print(x ":" colleges[x])
	
SyntaxError: invalid syntax
>>> for x in colleges:
	print(x : colleges[x])
	
SyntaxError: invalid syntax
>>> for x in colleges:
	print(x , colleges[x])

	
Hinduja Charni road
Mithibai Andheri
Dalmia Malad
>>> for x in colleges:
	print(x [print(":")] colleges[x])
	
SyntaxError: invalid syntax
>>> for x in colleges:
	print(x)

	
Hinduja
Mithibai
Dalmia
>>> for x in colleges.values():
	print(x)

	
Charni road
Andheri
Malad
>>> for x,y in colleges.items():
	print(x,y)

	
Hinduja Charni road
Mithibai Andheri
Dalmia Malad
>>> print(len(colleges))
3
>>> 
>>> colleges["Jai Hind"] = "Churchgate"
>>> for x,y in colleges.items():
	print(x,y)

	
Hinduja Charni road
Mithibai Andheri
Dalmia Malad
Jai Hind Churchgate
>>> del colleges["Dalmia"]
>>> for x,y in colleges.items():
	print(x,y)

	
Hinduja Charni road
Mithibai Andheri
Jai Hind Churchgate
>>> 
