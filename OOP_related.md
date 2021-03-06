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

- public vs. private
    - java attributes usually private or protected (limit access to classes in the same package, if subclass need direct access to them). Limit access from code outside the class, but can use setters and getters
    - python has non-public instance variale, beginning with single underscore, e.g. ``self._cupholder = 6``, but only a naming convention, can still access it directly, but will issue a warning in IDE
    - can use double underscore, ``self.__cupholder = 6``, will get error when accessing it with `my_car.__cupholder`. When Python sees an attribute with double underscores, it changes the attribute by prefixing the original name of the attribute with an underscore, followed by the class name. So we can do `my_car._Car__cupholders`.
- access control
    - python can delete attributes, `del my_car.year`
    - **Properties** allow functions to be declared in Python classes that are analogous to Java getter and setter methods. Names of the decorated functions are all the same --> they control access to the same variable
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
         >>>  print(str(my_car)
        -  ``__eq__(self, other)`` could be overriden for customized equality, otherwise `==` just compares addresses
        
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
    - can provide complete default code and/or just the details that have to be overriden. - in case of abstract class, a class may only extend only one abstract class.
    -  An abstract class cannot be used to create objects (to access it, it must be inherited from another class). 
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

### random links
- https://realpython.com/oop-in-python-vs-java/
- https://github.com/careercup/CtCI-6th-Edition/tree/master/Java/Ch%2015.%20Threads%20and%20Locks
- https://blog.csdn.net/longyulu/article/details/9159589