## OOP problem
### **objected oriented language**
- advantages
    - Objects created for Object Oriented Programs can easily be reused in other programs.
    - Large programs are very difficult to write. Object Oriented Programs force designers to go through an extensive planning phase, which makes for better designs with less flaws. In addition, once a program reaches a certain size, Object Oriented Programs are actually easier to program than non-Object Oriented ones.
    - modularity, extensibility, and reusability   
        - Object-orientedprogrammingis modular, as it provides separation of duties in object-based program development. It is also extensible, as objects can be extended to include new attributes and behaviors. Objects can also be reused within an across applications. Because of these three factors
    - Great software maintenance
        - Since the design is modular, part of the system can be updated in case of issues without a need to make large-scale changes.

- disadvantages
    - Larger program size
        - Object-oriented programs typically involve more lines of code than procedural programs.
    - Steep learning curve
        - The thought process involved in object-oriented programming may not be natural for some people, and it can take time to get used to it. It is complex to create programs based on interaction of objects. Some of the key programming techniques, such as inheritance and polymorphism, can be challenging to comprehend initially.
    - Slower programs
        - Object-oriented programs are typically slower than procedure- based programs, as they typically require more instructions to be executed.
    - Not suitable for all types of problems
        - There are problems that lend themselves well to functional-programming style, logic-programming style, or procedure-based programming style, and applying object-oriented programming in those situations will not result in efficient programs.

### **Java v.s. Python OOP**
- declare a class
    - python can declare it anywhere; java classes are defined in files with the same name as the class. So, you have to save this class in a file named Car.java. Only one class can be defined in each file.
- attributes
    - variables associated with specific objects
    - java declare it in class body, outside any methods, with definite type
    - python declare & defines it inside `__init__()`, equivalent of java's constructor, prefixing variable names with `self`, variables are loosely typed, can also create instance variables outside of `__init__()`, but not best practice
    - python class variable: declared outside a method but in class. But change `my_car.wheels` will not change `Car.wheels`
        ```
        class Car:
            wheels = 0
            ...

        my_car = Car()
        Car.wheels #0
        my_car.wheels #0
        ```
    - java static attribute: ~ class variables
- public vs. private
    - java attributes usually private or protected (limit access to classes in the same package, if subclass need direct access to them). Limit access from code outside the class
    - python has non-public instance variale, beginning with single underscore, e.g. ``self._cupholder = 6``, but only a naming convention, can still access it directly, but will issue a warning in IDE
    - can use double underscore, ``self.__cupholder = 6``, will get error when accessing it with `my_car.__cupholder`. 





### **functional v.s. imperative programming**


### **what is encapsulation and polymorphism and benefits**
- Encapsulation: Binding the data with the code that manipulates it. It keeps the data and the code safe from external interference.
- Benefit of encapsulation 
    - It improves maintainability and flexibility and re-usability.
    - The fields can be made read-only (If we don’t define setter methods in the class) or write-only (If we don’t define the getter methods in the class).
    - User would not be knowing what is going on behind the scene.
- **Polymorphism** is the capability of a method to do different things based on the object that it is acting upon. In other words, polymorphism allows people define one interface and have multiple
implementations. There are two different polymorphisms: runtime polymorphism and compile time polymorphism
- Benefit of polymorphism:
    - The basic reason behind polymorphism is that we can implement different behaviors of the same object depending upon the reference type passed to an object.
    - jdbc, servlets, jsp have come through polymorphism, if not there we have to remember all dependent classes related to DB, Servers...to use in our java coding
    - Polymorphism enables us to best core java training in Bangalore define one or more methods to have the same name but differs in number of parameters and method types.

### **the difference between Java function call and Python function call ????**
- Python and Java call methods similarly: If you have an object x and method foo , you go x.foo()
- Python also has a library of global functions that are not methods of objects. One such function is len, which returns the length of its argument.

### **class vs. superclass**
- subclass (child): the class that inherits from another class
- superclass (parent): the class being inherited from
- If you don't want other classes to inherit from a class, use the `final` keyword



### **difference between interface and abstract class**
- Interface:
    - cannot provide any code at all, just the signature - A class may implemented several interfaces
    - cannot have instance variables
    - must be public or none
    - cannot contains constructor
    - slow
- Abstract class:
    - can provide complete default code and/or just the details that have to be overriden. - in case of abstract class, a class may only extend only one abstract class.
    - an abstract class can have non-abstract methods
    - an abstract class can have instance variables
    - contain constructor
    - fast
### https://realpython.com/oop-in-python-vs-java/
https://github.com/careercup/CtCI-6th-Edition/tree/master/Java/Ch%2015.%20Threads%20and%20Locks