
## Python Basics
* **Operators**
  Some basic operators:
  
  Operator | Description | Example
  ---- | ---- | ----
  and | Returns True if both statements are true | x<5 and x<10
  or | Returns True if one of the statements is true | x<5 or x<4
  not | Reverse the results, returns False if the result is true | not(x<5 and x<10)
  is | Returns true if both variables are the same object | x is y
  is not | Returns true uf both variables are not the same object | x is not y
  in | Returns True if a sequence with the specified value is present in the object | x in y
  not in | Returns True if a sequence with the specified value is not present in the object | x not in y 
  

* **Data types**

   * **String**:
      String literals in python are surrounded by either single quotation marks, or double quotation marks
      
      Example 1:
      ```python
      print('hello')
      print("hello")
      ```
      
      Example 2:
      ```python
      a = 'Hello world'
      print(a[1])
      #Result: e
      ```
      
      Example 3:
      ```python
      a = 'Dipae'
      print(len(a)) #length of string
      #Result: 5
      ```
      
      Example 4:
      ```python
      a = '  Hello, World!  '
      print(a.strip())
      #Result: 'Hello, World!'
      ```
      
      Example 5:
      ```python
      a = 'Hello, World'
      print(a.split(","))
      #Result ['Hello',' World!']
      ```
      
      Example 6:
      ```python
      txt = "Dipae is the best uni"
      if 'Dipae' in text:
        print('True')
      #Result: 'True'
      ```
      
      Example 7:
      ```python
      txt = 'Dipae'
      print(f"{text} is the best uni")
      #Result: 'Dipae is the best uni'
      ```
      
   * **Lists**:
      List is a collection which is ordered and changeable. Allows duplicate members.
      Example:
      ``` python
      thislist = ["apple", "banana", "cherry"]
      print(thislist[0]) 
      #Result: "apple"
      ```
      Some usefull list functions:
      
      Function name | Usage
      ------ | -----
      append() | Adds an element at the end of the list
      index() | Returns the index of the fist element with the specified value
      insert() | Adds an element at the specified position
      pop() | Removes the element at the specified position
      remove() | Removes the item with the specified value
      sort() | Sorts the list
      
   * **Sets**:
      Set is a collection which is unordered and unindexed. No duplicate members.
      Example:
      ```python
       thisset = {"apple", "banana", "cherry"}
       print(thisset[0])
       #Result: "apple"
      ````
      Some usefull set functions:
      
      Function name | Usage 
      ------ | ----- 
      add() | Adds an element to the set 
      difference() | Returns a set containing the difference between two or more sets
      pop() | Removes an element from the set 
      remove() | Removes the specified element 
      
  * **Dictionaries**:
      Dictionary is a collection which is unordered, changeable and indexed. No duplicate members
      Example:
      ```python
      thisdict = {
        "uni" : "Dipae",
        "trash" : "Pithia",
        "dad" : "Peris"
      }
      print(thisdict['uni'])
      #Result: "Dipae"
      ```
      Some usefull dictionary functions:
      
      Function name | Usage
      ------ | -----
      get() | Returns the value of the specified key
      pop() | Removes the element with the specified key
      update() | Updates the dictionary with the specified key-value pairs
      
* **Loops**

  Examples of loops
  
  ### While loop:
    
    Example 1: 
    ```python
      i = 1
      while 1 < 6:
        print(i)
        i += 1
      else:
        print('i is no loger less then 6')
    ```
    
    Example 2:
    ```python
      while True:
        print('This is like my suffering.It never ends')
    ```     
  
  ### For loop:
  
     Example 1:
     
     ```python
     fruits = ['apple','banana']
     for fruit in fruits:
      print(fruit)
     #Result: 'apple' 'banana'
     ```
      
    Example 2:
    
    ```python
    for i in range(4):
      print(i)
    #Result: 0 1 2 3
    ```
      
    Example 3:
    
    ```python
    fruits = ['apple','banana']
    for num,fruit in enumerate(fruits):
      print(num)
      print(fruit)
    #Result: 0 apple 1 banana
    ```
 * **Functions**
 
    Example 1:
      ```python
      def function():
        print('Hello')
      
      function()
      #Result: 'Hello'
      ```
    Example 2:
    ```python
    def function(name='test'):
      print(name)
    
    function() #prints 'test'
    function('test2') #prints 'test2'
    ```
    
 * **Classes**
    Class example
    
    ```python
    class Person:
      def __init__(name,age) #Constructor
        self.name = name
        self.age = age
      def func(self):
        print(f'Dipae is de best. from {self.name}')
      
    p = Person("Dad",45)
    p.func()
    ```
    
* **Exception handling**

    The try block lets you test a block of code for errors.
    The except block lets you handle the error.
    The finally block lets you execute code, regardless of the result of the try- and except blocks.
    
    Example 1:
    ```python
    try:
      print(x)
    except:
      print('Exception was thrown')
    ```
    
    Example 2:
    ```python 
      try:
        print(x)
      except NameError:
        print('Variable x is not defined')
      except:
        print('Something went wrong')
    ```
    
    Example 3:
    ```python
    try:
      print(x)
    except:
      print('Something went wrong')
    finally:
      print('The try-exept is finished')
    ```
    
## Full tutorials can be found here:
[Python tutorial](https://www.w3schools.com/Python/default.asp)

[Automate the boring stuff with python](https://automatetheboringstuff.com/2e/)
