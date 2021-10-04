## OOP problem
### **objected oriented language**
- advantages
    - Objects created for Object Oriented Programs can easily be reused in other programs.
    - Large programs are very difficult to write. Object Oriented Programs force designers to go through an extensive planning phase, which makes for better designs with less flaws. In addition, once a program reaches a certain size, Object Oriented Programs are actually easier to program than non-Object Oriented ones.
    - modularity, extensibility, and reusability   
        - Object-oriented programming is modular, as it provides separation of duties in object-based program development. It is also extensible, as objects can be extended to include new attributes and behaviors. Objects can also be reused within an across applications. Because of these three factors
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
        - static is used for a constant variable or a method that is same for every instance of a class
        -  ``Non-static variable cannot be referenced from a static context``
            ```
            class MyProgram
            {
                int count = 0;
                public static void main(String[] args)
                {
                    System.out.println(count);
                }
            }
            ```
        - static methods
            - They can directly call other static methods only.
            - They can access static data directly.
    - python class method & static method
        - class method
            - The @classmethod decorator is a built-in function decorator that is an expression that gets evaluated after your function is defined. The result of that evaluation shadows your function definition. 
            - A class method receives the class as an implicit first argument, just like an instance method receives the instance 
            - A class method is a method that is bound to the class and not the object of the class.
            - They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
            - It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that will be applicable to all the instances.
        - static method
            - A static method is also a method that is bound to the class and not the object of the class.
            - A static method can’t access or modify the class state.
            - It is present in a class because it makes sense for the method to be present in class.
        - A class method takes cls as the first parameter while a static method needs no specific parameters.
        - A class method can access or modify the class state while a static method can’t access or modify it.
        - In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
        - We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.
        - 
            ```
            from datetime import date
            
            class Person:
                def __init__(self, name, age):
                    self.name = name
                    self.age = age
                
                # a class method to create a Person object by birth year.
                @classmethod
                def fromBirthYear(cls, name, year):
                    return cls(name, date.today().year - year)
                
                # a static method to check if a Person is adult or not.
                @staticmethod
                def isAdult(age):
                    return age > 18
            
            person1 = Person('mayank', 21)
            person2 = Person.fromBirthYear('mayank', 1996)
            
            print (person1.age)
            print (person2.age)
            
            # print the result
            print (Person.isAdult(22))
            ```
    - decorator
        -  decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
        - https://realpython.com/primer-on-python-decorators/#simple-decorators
        - decorators wrap a function, modifying its behavior.
        - syntactic sugar
            - @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee). 
            - 
                ```
                from datetime import datetime
                def not_during_the_night(func):
                    def wrapper():
                        if 7 <= datetime.now().hour < 22:
                            func()
                        else:
                            pass  # Hush, the neighbors are asleep
                    return wrapper

                def say_whee():
                    print("Whee!")

                say_whee = not_during_the_night(say_whee)
                ```
            - 
                ```
                def my_decorator(func):
                    def wrapper():
                        print("Something is happening before the function is called.")
                        func()
                        print("Something is happening after the function is called.")
                    return wrapper

                @my_decorator
                def say_whee():
                    print("Whee!")
                ```
- public vs. private
    - java attributes usually private or protected (limit access to classes in the same package, if subclass need direct access to them). Limit access from code outside the class, but can use setters and getters
    - python has non-public instance variable, beginning with single underscore, e.g. ``self._cupholder = 6``, but only a naming convention, can still access it directly, but will issue a warning in IDE
    - can use double underscore, ``self.__cupholder = 6``, will get error when accessing it with `my_car.__cupholder`. When Python sees an attribute with double underscores, it changes the attribute by prefixing the original name of the attribute with an underscore, followed by the class name. So we can do `my_car._Car__cupholders`.
- access control
    - python can delete attributes, `del my_car.year`
    - **Properties** allow functions to be declared in Python classes that are analogous to Java getter and setter methods. Names of the decorated functions are all the same --> they control access to the same variable
    - Some commonly used decorators that are even built-ins in Python are @classmethod, @staticmethod, and @property. The @classmethod and @staticmethod decorators are used to define methods inside a class namespace that are not connected to a particular instance of that class. The @property decorator is used to customize getters and setters for class attributes. Expand the box below for an example using these decorators.
        ```
        class Car:
            def __init__(self, color, model, year):
                self.color = color
                self.model = model
                self.year = year
                self._voltage = 12
        
            @property
            def voltage(self):
                return self._voltage
        
            @voltage.setter
            def voltage(self, volts):
                print("Warning: this can cause problems!")
                self._voltage = volts
        
            @voltage.deleter
            def voltage(self):
                print("Warning: the radio will stop working!")
                del self._voltage
        ...
        >>> my_car.voltage # Python calls .voltage() decorated with @property.

        >>> my_car.voltage = 6 #Python calls .voltage() decorated with @voltage.setter.
        Warning: this can cause problems!

        >>> del my_car.voltage #Python calls .voltage() decorated with @voltage.deleter.
        Warning: the radio will stop working!
        ```

- self & this
    - `this` is implicit in java code, e.g. in setter
        ```
        public void setColor(){
            this.color = color;
            // or..
            color = newColor;
        }
        ```
    - `self` is required if declaring instance variable, otherwise python will create a local variable instead of an attribute

- methods and functions
    - A function is a piece of code that is called by name. 
    - A method is a piece of code that is called by a name that is associated with an object, can operate on data that is contained within the class
    - python has functions but java doesn't
    - python can declare a function anywhere, not in a class; can't alter/store any data in any class, but can use local & global variables
    - every line of java belongs to a class, functions can't exist outside of a class
    - static method in java ~ function, callable anywhere without first creating an instance of the class

- inheritance and polymorphism
    - inheritance allows objects to derive attributes and functionality from other objects, creating a hierarchy moving from more general objects to more specific.
    - polymorphism allows two or more objects to behave like one another, which allows them to be used interchangeably. For example, if a method or function knows how to paint a Vehicle object, then it can also paint a Car or Boat object, since they inherit their data and behavior from the Vehicle.
    - python supports multiple inheritance
        ```
        class Car(Vehicle, Device):
            def __init__(self, color, model, year):
                Vehicle.__init__(self, color, model)
                Device.__init__(self)
                self.year = year
        ```
    - `super` keyword and `super()`
        - `super()` calls parent class constructor 
        - `super` refers to parent class object, e.g. `super.maxSpeed`
       
    - java only supports single inheritance, but can implements different interfaces, each class and interface needs to live in its own file.
        ```
        public interface Device {
            int getVoltage();
        }

        public class Car extends Vehicle implements Device {
            private int voltage;
            private int year;

            public Car(String color, String model, int year) {
                super(color, model);
                this.year = year;
                this.voltage = 12;
            }

            @Override
            public int getVoltage() {
                return voltage;
            }
        }
        ```
    - Interfaces only define the methods—they cannot define instance data or implementation details.

- types and polymorphism
    - polymorphism: Every class and interface in Java is a type. Therefore, if two Java objects implement the same interface, then they are considered to be the same type with respect to that interface.
    - python: duck typing. Instead of identifying objects by type, Python examines their behavior. “walks like a duck and quacks like a duck, then it’s a duck.”
    
- default methods
    - All Java classes descend from the Object class, which contains a set of methods every other class inherits. Subclasses can either override them or keep the defaults. 
        ```
        class Object {
        boolean equals(Object obj) { ... }    
        int hashCode() { ... }    
        String toString() { ... }       
        }
        ```
    - python has a set of common dunder (double underscore) methods
        - ``__repr__()`` string represention of object, unambigous, ~hashCode()
        - ``__str__()`` readable, ~toString()
         >>>  print(str(my_car))
        -  ``__eq__(self, other)`` could be overriden for customized equality, otherwise `==` just compares addresses
    - python hash(object)
        - Only immutable objects can be hashed.
            - Hashable 
                – bool, int, long, float, string, unicode, tuple
            - Non–Hashable 
                – lists, set, dictionary, bytearray
                - throws `TypeError`

        - Numeric values which are equal will have same has value irrespective of their data types. 
            - For example, 2 and 2.0 have same hash value.
        
- operator overloading
    - Python’s dunder methods allow you to implement operator overloading, something that Java doesn’t offer at all.
        ```
        class Car:
            def __init__(self, color, model, year):
                self.color = color
                self.model = model
                self.year = year

            def __str__(self):
                return f'Car {self.color} : {self.model} : {self.year}'

            def __eq__(self, other):
                return self.year == other.year

            def __lt__(self, other):
                return self.year < other.year

            def __add__(self, other):
                return Car(self.color + other.color, 
                   self.model + other.model, 
                   int(self.year) + int(other.year))
        ...
        >>> my_car < your_car
        ```
- reflection
    - Reflection refers to examining an object or class from within the object or class
        ```
        >>> print(type(my_car))
        <class 'car.Car'>
        >>> print(isinstance(my_car, Car))
        True

        Car car = new Car("yellow", "beetle", 1969);
        System.out.println(car.getClass());
        System.out.println(car instanceof Car);

        ```
- Examining an Object’s Attributes
    - ``dir(my_car)`` in python view every attribute and function contained in any object
    - ``getattr()`` returns specific details of a given attribute or function
        ```
        >>> print(getattr(my_car, "__format__"))
        <built-in method __format__ of Car object at 0x7fb4c10f5438>
        ```
    - ``.getFields()`` in java retrieves a list of all publicly accessible attributes. 
    - ``.getDeclaredMethods()`` retrives public methods
    - ``.getDeclaredMethods()`` returns an array of Method objects. The Method object itself has a method called ``.invoke()``, which will call the Method, can return ``method.invoke(object)`` instead.
    - python can just add ``()``, 

### **functional v.s. imperative programming**
- functional programming: 
    - a form of declarative programming
    - avoid changing state and mutable data
    - lazy evaluation
    - support parallel programming
    - no side effect
    - 不变性带来的另一个好处是：由于（多个线程之间）不共享状态，不会造成资源争用(Race condition)，也就不需要用锁来保护可变状态，也就不会出现死锁，这样可以更好地并发起来，尤其是在对称多处理器（SMP）架构下能够更好地利用多个处理器（核）提供的并行处理能力。


### **what is encapsulation and polymorphism and benefits**
- Encapsulation: Binding the data with the code that manipulates it. It keeps the data and the code safe from external interference.
- Benefit of encapsulation 
    - It improves maintainability and flexibility and re-usability.
    - The fields can be made read-only (If we don’t define setter methods in the class) or write-only (If we don’t define the getter methods in the class).
    - User would not be knowing what is going on behind the scene.
- **Polymorphism** is the capability of a method to do different things based on the object that it is acting upon. In other words, polymorphism allows people define one interface and have multiple implementations. There are two different polymorphisms: runtime polymorphism and compile time polymorphism
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


## **Java Concepts**
### **integer cache**
-  Integer objects are cached internally and reused via the same referenced objects.
- applicable for Integer values in range between –127 to +127 
- Integer caching works only on autoboxing. Integer objects will not be cached when they are built using the constructor
- There is a lookup to IntegerCache.cache before constructing a new Integer instance
    ```
    public static Integer valueOf(int i) {
        if (i >= IntegerCache.low && i <= IntegerCache.high)
            return IntegerCache.cache[i + (-IntegerCache.low)];
        return new Integer(i);
    }
    ```
- Therefore
    ```
    Integer integer1 = 3;
    Integer integer2 = 3;
    //integer1 == integer2

    Integer integer3 = 300;
    Integer integer4 = 300;
    //whereas integer3 != integer4
    ```
### **autoboxing**
- automatic conversion that the Java compiler makes between the primitive types and their corresponding object wrapper classes
- ``Integer a = 10;``
-  ``Character c = 'a'``
- The Java compiler applies unboxing when an object of a wrapper class is
    - Passed as a parameter to a method that expects a value of the corresponding primitive type.
    - Assigned to a variable of the corresponding primitive type. 
    - 
        ```
        Integer i = new Integer(-8);

        // 1. Unboxing through method invocation
        int absVal = absoluteValue(i);

        List<Double> ld = new ArrayList<>();
        ld.add(3.1416);    // Π is autoboxed through method invocation.

        // 2. Unboxing through assignment
        double pi = ld.get(0);
        ```
- `Integer.valueOf(i)` convert i to Integer type
- `Integer i; i.intValue();` convert i to int


### **generics**
- It would be nice if we could write a single sort method that could sort the elements in an Integer array, a String array, or an array of any type that supports ordering.
- All generic method declarations have a type parameter section delimited by angle brackets (< and >) that precedes the method's return type ( < E > in the next example).
- 
    ```
    // generic method printArray
    public static < E > void printArray( E[] inputArray ) {
        // Display array elements
        for(E element : inputArray) {
            System.out.printf("%s ", element);
        }
        System.out.println();
    }
    ```
- Bounded Type Parameters
    - To declare a bounded type parameter, list the type parameter's name, followed by the extends keyword, followed by its upper bound.
    - ``public static <T extends Comparable<T>> T maximum(T x, T y, T z) ``
- generic class
    - class name is followed by a type parameter section.
    - type parameter section of a generic class can have one or more type parameters separated by commas.
    - 
    ```
    public class Box<T> {
        ...
    }

    Box<Integer> integerBox = new Box<Integer>();
    Box<String> stringBox = new Box<String>();
    ```

### **interface vs abstract class**
- Interface:
    - cannot provide any code at all, just the signature - A class may implemented several interfaces
    - cannot have instance variables
    - must be public or none
    - cannot contains constructor
    - slow
- Abstract class:
    - can provide complete default code and/or just the details that have to be overriden. 
    - in case of abstract class, a class may only extend only one abstract class.
    - An abstract class cannot be used to create objects (to access it, it must be inherited from another class). 
    - An abstract method can only be used in an abstract class, and it does not have a body. 
    - an abstract class can have non-abstract methods
    - an abstract class can have instance variables
    - contain constructor
    - fast
- 
```
abstract class Shape  
{ 
    // declare fields 
    String objectName = " "; 
      
    Shape(String name) 
    { 
        this.objectName = name; 
    } 
      
    // declare non-abstract methods 
    // it has default implementation 
    public void moveTo(int x, int y) 
    { 
        System.out.println(this.objectName + " " + "has been moved to"
                                   + " x = " + x + " and y = " + y); 
    } 
      
    // abstract methods which will be 
    // implemented by its subclass(es) 
    abstract public double area(); 
    abstract public void draw(); 
} 

class Rectangle extends Shape  
{ 
      
    int length, width; 
      
    // constructor 
    Rectangle(int length, int width, String name) 
    { 
        super(name); 
        this.length = length; 
        this.width = width; 
    } 
      
    @Override
    public void draw()  
    { 
        System.out.println("Rectangle has been drawn ");  
    } 
      
    @Override
    public double area()  
    { 
        return (double)(length*width); 
    } 
}

interface Shape 
{ 
    // abstract method 
    void draw(); 
    double area(); 
} 
  
class Rectangle implements Shape  
{ 
    ...
}
```

### Java reserved keywords
- https://www.w3schools.com/java/java_ref_keywords.asp
- 
| \ | Class  | Package | Subclass (same pkg) | Subclass (diff pkg) | World
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| public  | + | + | + | + | + |
| protected  | + | + | + | + |  |
| no modifier (default) | + | + | + |  |  |
| private | + |  | |  |  |

-  `abstract` non-access modifier
-  `byte` A data type that can store whole numbers from -128 and 127
- `case` Marks a block of code in switch statements
- `switch` Selects one of many code blocks to be executed
    ```
    int day = 4;
    switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    }
    ```
- `try` ... `catch` ... `finally`
    ```
    try {
    //  Block of code to try
    }
    catch(Exception e) {
    //  Block of code to handle errors
    }
    finally {
    //Statements to be executed no matter exception occurs or not.
    }
    ```
- `enum`
    ```
    enum Level {
        LOW,
        MEDIUM,
        HIGH
    }
    Level myVar = Level.MEDIUM;
    ```
- `final` a non-access modifier used for classes, attributes and methods, which makes them non-changeable (impossible to inherit or override)
- `import` Used to import a package, class or interface
- `super` Refers to superclass (parent) objects
- `synchronized` a non-access modifier, which specifies that methods can only be accessed by one thread at a time
- `volatile` indicates that an attribute is not cached thread-locally, and is always read from the "main memory"


### Java garbage collector
- Java programs perform automatic memory management. 
- Java programs compile to bytecode that can be run on a Java Virtual Machine, or JVM for short. When Java programs run on the JVM, objects are created on the heap, which is a portion of memory dedicated to the program. 
- Eventually, some objects will no longer be needed. The garbage collector finds these unused objects and deletes them to free up memory.
- unreferenced objects are identified and marked as ready for garbage collection

### Miscellaneous 
- `==` checks for object references and `equals()`checks for values
- pass by reference or value
    - python 
        - pases by Object Reference
        - Mutable objects:
            - list, dict, set, byte array
            -  call by reference
            - when their values are changed inside the function, then it will also be reflected outside the function.
        - Immutable objects:
            - int, float, complex, string, tuple, frozen set [note: immutable version of set], bytes.
            - call-by-value 
            - you can not change the value of the immutable objects being passed to the function
    - Java is always pass-by-value. 
        - Unfortunately, when we deal with objects we are really dealing with object-handles called references which are passed-by-value as well. This terminology and semantics easily confuse many beginners.

        - 
        ```
            public static void main(String[] args) {
                Dog aDog = new Dog("Max");
                Dog oldDog = aDog;

                // we pass the object to foo
                foo(aDog);
                // aDog variable is still pointing to the "Max" dog when foo(...) returns
                aDog.getName().equals("Max"); // true
                aDog.getName().equals("Fifi"); // false
                aDog == oldDog; // true
            }

            public static void foo(Dog d) {
                d.getName().equals("Max"); // true
                // change d inside of foo() to point to a new Dog instance "Fifi"
                d = new Dog("Fifi");
                d.getName().equals("Fifi"); // true
            }
        ```
        - In the example above aDog.getName() will still return "Max". The value aDog within main is not changed in the function foo with the Dog "Fifi" as the object reference is passed by value. If it were passed by reference, then the aDog.getName() in main would return "Fifi" after the call to foo.
        - 
        ```
            public static void main(String[] args) {
                Dog aDog = new Dog("Max");
                Dog oldDog = aDog;

                foo(aDog);
                // when foo(...) returns, the name of the dog has been changed to "Fifi"
                aDog.getName().equals("Fifi"); // true
                // but it is still the same dog:
                aDog == oldDog; // true
            }

            public static void foo(Dog d) {
                d.getName().equals("Max"); // true
                // this changes the name of d to be "Fifi"
                d.setName("Fifi");
            }
        ```
- hash table
    - disadvantages
        - You cannot use a null value as a key.
        - Collisions cannot be avoided when generating keys using hash functions. 
        - Collisions occur when a key that is already in use is generated.
        - If the hashing function has many collisions, this can lead to performance decrease.
    - summary
        - Hash tables are used to store data using a pair of keys and values.
        - A hash function uses a mathematical algorithm to calculate the hash value.
        - A collision occurs when the same hash value is generated for more than one value.
        - Chaining solves collision by creating linked lists.
        - Probing solves collision by finding empty slots in the hash table.
        - Linear probing searches for the next free slot to store the value starting from the slot where the collision occurred.
        - Quadratic probing uses polynomial expressions to find the next free slot when a collision occurs.
        - Double hashing uses a secondary hash function algorithm to find the next free slot when a collision occurs.
        - Hash tables have better performance when compared to other data structures.
        - The average time complexity of hash tables is O (1)
        - A dictionary data type in python is an example of a hash table.
        - Hash tables support insert, search and delete operations.
- python generator
    - generator functions are a special kind of function that return a lazy iterator. 
        - These are objects that you can loop over like a list. 
        - However, unlike lists, lazy iterators do not store their contents in memory. 
    - Using Generators
        - Example 1: Reading Large Files
            - 
                ```
                def csv_reader(file_name):
                    for row in open(file_name, "r"):
                        yield row
                csv_gen = csv_reader("some_csv.txt")
                row_count = 0

                for row in csv_gen:
                    row_count += 1

                print(f"Row count is {row_count}")
                ```
            - otherwise, could have memory error or slow
        - generator expression/comprehension
            - use the generator without calling a function
            - ``csv_gen = (row for row in open(file_name))``
        - Using yield will result in a generator object.
        - Using return will result in the first line of the file only.
        - Instead of using a for loop, you can also call next() on the generator object directly. 
            - This is especially useful for testing a generator in the console:
            - 
                ```
                >>> gen = infinite_sequence()
                >>> next(gen)
                0
                >>> next(gen)
                1
                >>> next(gen)
                2
                >>> next(gen)
                3
                ```
    - Understanding Generators
        -  yield indicates where a value is sent back to the caller, but unlike return, you don’t exit the function afterward.
        - The state of the function is remembered. That way, when next() is called on a generator object (either explicitly or implicitly within a for loop), the previously yielded variable num is incremented, and then yielded again. 
    - Building Generators With Generator Expressions
        - 
            ```
                nums_squared_lc = [num**2 for num in range(5)] #list
                sys.getsizeof(nums_squared_lc) #87624 bytes
                nums_squared_gc = (num**2 for num in range(5)) #generator
                sys.getsizeof(nums_squared_lc) #120
            ```
    - Understanding the Python Yield Statement
        - When you call special methods on the generator, such as next(), the code within the function is executed up to yield.
        - When the Python yield statement is hit, the program suspends function execution and returns the yielded value to the caller. 
        - In contrast, return stops function execution completely.
        - When a function is suspended, the state of that function is saved. 
        - This includes any variable bindings local to the generator, the instruction pointer, the internal stack, and any exception handling. 
    - Using Advanced Generator Methods
        - How to Use `.send()`
            - 
                ```
                def infinite_palindromes():
                    num = 0
                    while True:
                    if is_palindrome(num):
                        i = (yield num)
                        if i is not None:
                            num = i
                    num += 1

                pal_gen = infinite_palindromes()
                for i in pal_gen:
                    digits = len(str(i))
                    pal_gen.send(10 ** (digits))
            
                ```
            - The program only yields a value once a palindrome is found. 
            - It uses len() to determine the number of digits in that palindrome. 
            - Then, it sends 10 ** digits to the generator. 
            - This brings execution back into the generator logic and assigns 10 ** digits to i. 
            - Since i now has a value, the program updates num, increments, and checks for palindromes again.
            - Once your code finds and yields another palindrome, you’ll iterate via the for loop. 
            - This is the same as iterating with next(). 
            - The generator also picks up at line 5 with i = (yield num). 
            - However, now i is None, because you didn’t explicitly send a value.
        - How to Use `.throw()`
            - 
                ```
                pal_gen = infinite_palindromes()
                for i in pal_gen:
                    print(i)
                    digits = len(str(i))
                    if digits == 5:
                        pal_gen.throw(ValueError("We don't like large palindromes"))
                    pal_gen.send(10 ** (digits))
                ```
    - How to Use `.close()`
        - `.close()` allows you to stop a generator. 
        - 
            ```
            pal_gen = infinite_palindromes()
            for i in pal_gen:
                print(i)
                digits = len(str(i))
                if digits == 5:
                    pal_gen.close()
                pal_gen.send(10 ** (digits))
            ```
- python metaclass
    - https://realpython.com/python-metaclasses/
    - 
        ```
        >>> class Foo:
        ...     pass
        ...
        >>> x = Foo()

        >>> type(x)
        <class '__main__.Foo'>

        >>> type(Foo)
        <class 'type'>
        >>> type(type)
        <class 'type'>
        ```
        - type is a metaclass, of which classes are instances.
        - x is an instance of class Foo.
        - Foo is an instance of the type metaclass.
        - type is also an instance of the type metaclass, so it is an instance of itself.
    - Defining a Class Dynamically
        - The built-in type() function, when passed one argument, returns the type of an object. 
        - For new-style classes, that is generally the same as the object’s __class__ attribute
        - You can also call type() with three arguments—type(<name>, <bases>, <dct>):
            - <name> specifies the class name. This becomes the __name__ attribute of the class.
            - <bases> specifies a tuple of the base classes from which the class inherits. This becomes the __bases__ attribute of the class.
            - <dct> specifies a namespace dictionary containing definitions for the class body. This becomes the __dict__ attribute of the class.
        - Calling type() in this manner creates a new instance of the type metaclass. 
        - In other words, it dynamically creates a new class.
        - 
            ```
            >>> Foo = type('Foo', (), {})
            >>> x = Foo()
            >>> x
            <__main__.Foo object at 0x04CFAD50>
            #equivalent to
            >>> class Foo:
            ...     pass
            ```
        - 
            ```
            >>> def f(obj):
            ...     print('attr =', obj.attr)
            ...
            >>> Foo = type(
            ...     'Foo',
            ...     (),
            ...     {
            ...         'attr': 100,
            ...         'attr_val': f
            ...     }
            ... )

            >>> x = Foo()
            >>> x.attr
            100
            >>> x.attr_val()
            attr = 100
            ```
- python static emethod & class method
    - class method

            - The @classmethod decorator is a built-in function decorator that is an expression that gets evaluated after your function is defined. 
            - A class method receives the class as an implicit first argument, just like an instance method receives the instance 
        - 
            ```
            class C(object):
                @classmethod
                def fun(cls, arg1, arg2, ...):
                ....
            ```
            - fun: function that needs to be converted into a class method
            - returns: a class method for function.
        - properties
            - A class method is a method that is bound to the class and not the object of the class.
            - They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
            - It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that will be applicable to all the instances.
        - 
    - static method
        - A static method is also a method that is bound to the class and not the object of the class.
        - A static method can’t access or modify the class state.
    - 
        ```
        # Python program to demonstrate
        # use of class method and static method.
        from datetime import date

        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            
            # a class method to create a Person object by birth year.
            @classmethod
            def fromBirthYear(cls, name, year):
                return cls(name, date.today().year - year)
            
            # a static method to check if a Person is adult or not.
            @staticmethod
            def isAdult(age):
                return age > 18

        person1 = Person('mayank', 21)
        person2 = Person.fromBirthYear('mayank', 1996)

        print (person1.age)
        print (person2.age)

        # print the result
        print (Person.isAdult(22))


        ```

### random links
- https://realpython.com/oop-in-python-vs-java/
- https://github.com/careercup/CtCI-6th-Edition/tree/master/Java/Ch%2015.%20Threads%20and%20Locks
- https://blog.csdn.net/longyulu/article/details/9159589

https://medium.com/@lokeshsharma596/is-python-call-by-value-or-call-by-reference-2dd7db74dbd0