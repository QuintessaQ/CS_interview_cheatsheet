## OOP problem
1. the benefit of objected oriented language
	- Objects created for Object Oriented Programs can easily be reused in other programs.
	- Large programs are very difficult to write. Object Oriented Programs force designers to go through an extensive planning phase, which makes for better designs with less flaws. In addition, once a program reaches a certain size, Object Oriented Programs are actually easier to program than non-Object Oriented ones.
	- Great software maintenance
	https://www.cs.drexel.edu/~introcs/Fa15/notes/06.1_OOP/Advantages.html?CurrentSlide=3
2. what is encapsulation and polymorphism and benefits
	- Encapsulation: Binding the data with the code that manipulates it. It keeps the data and the code safe from external interference.
	- Benefit of encapsulation :
		1) It improves maintainability and flexibility and re-usability.
		2) The fields can be made read-only (If we don’t define setter methods in the class) or write-only (If we don’t define the getter methods in the class).
		3) User would not be knowing what is going on behind the scene.
	- **Polymorphism** is the capability of a method to do different things based on the object that it is acting upon. In other words, polymorphism allows people define one interface and have multiple
	implementations. There are two different polymorphisms: runtime polymorphism and compile time polymorphism
	- Benefit of polymorphism:
		1) The basic reason behind polymorphism is that we can implement different behaviors of the same object depending upon the reference type passed to an object.
		2) jdbc, servlets, jsp have come through polymorphism, if not there we have to remember all dependent classes related to DB, Servers...to use in our java coding
		3) Polymorphism enables us to best core java training in Bangalore define one or more methods to have the same name but differs in number of parameters and method types.
3. the difference between Java function call and Python function call ????
	-Python and Java call methods similarly: If you have an object x and method foo , you go x.foo()
	-Python also has a library of global functions that are not methods of objects. One such function is len, which returns the length of its argument.
4. difference between interface and abstract class
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
5. https://realpython.com/oop-in-python-vs-java/
