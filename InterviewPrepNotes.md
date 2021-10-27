# Prepartion material for technical interviews
## Object Oriented Programming
<span style="color:#6897bb">**Definition**</span>
**Polymorphism** - Allows the behaviour and state of an object to take on many forms.
Can be static or dynamic. Static means that it is decided at compile time whereas dynamic is runtime.
Static example: overloading a method. Dynamic example: overriding a method.

<span style="color:#6897bb">**Definition**</span>
**Inheritance** - One class acquires the properties of another. Represents an "Is a" relationship. In Java, 
one class inherits properties of another using `extends` keyword. 

<span style="color:#6897bb">**Definition**</span>
**Abstraction** - User has information on what an object does but not how it does it i.e. implementation
details are hidden.

<span style="color:#6897bb">**Definition**</span>
**Encapsulation** - This is also known as data-hiding. Can achieve this in Java by making all state `private`
and setting `public` getters and setters.

<span style="color:#6897bb">**Definition**</span>
**Abstract class** - A class with at least one abstract method. It cannot be instantiated.

<span style="color:#6897bb">**Definition**</span>
**Interface** - A construct that is implemented by a class. It contains all abstract methods and any state 
must be `static final` i.e. constant. It can extend or be extended by another interface. 

<span style="color:#d33348">**Key point**</span>
Once a class implements an interface, it assumes responsibility of implementing every abstract method - however it may become an 
abstract class and only implement some or none of the abstract methods. In order to then instantiate, another
class would need to extend this abstract class and assume responsibility for full implementation.

<span style="color:#6897bb">**Definition**</span>
**Enums** - An enum is a construct used to hold constant values. It can thus be used if a program uses a
variable which should only take values from a preset list rather than say using a `String`.

## Basic datastructures
<span style="color:#6897bb">**Definition**</span>
**Hash table / HashMap** - stores key value pairs and hashes the key to find the memory location of the value.

<span style="color:#6897bb">**Definition**</span>
**HashSet** - similar to a hash table and actually uses HashMap in Java. 
It will associate the element you add with the key and the value will be some constant.

<span style="color:#6897bb">**Definition**</span>
**Array** - sequence of memory locations to hold elements.

<span style="color:#6897bb">**Definition**</span>
**Linked list** - list defined by nodes. Node has a value and pointer to the next node.

<span style="color:#6897bb">**Definition**</span>
**Binary tree** - A tree with one root node, only one route from root to every node, every node has one parent and each node
has no more than two children.

## Top algorithms to know
<span style="color:#6897bb">**Definition**</span>
**Tree algorithms**

<span style="color:#6897bb">**Definition**</span>
**Binary search**

<span style="color:#6897bb">**Definition**</span>
**Sorting**

Comparison based sorts have a fastest average time: **O(nlog(n))**

**Insertion sort** - sorted and unsorted parts of array. Take elements from unsorted part and place in 
correct position in the sorted part. 

- Worst case time complexity **O(n^2)**
- Memory usage = **O(1)**

**Selection sort** - repeatedly finds minimum element from unsorted part and appends to end of sorted
part. 

- Worst case (and best) time complexity = **O(n^2)**
- Memory usage = **O(1)**

**Bubble sort** - Repeatedly swap adjacent elements if they're in the wrong order. After every pass, 
the maximum element reaches the end. It repeats until no swaps are made.

- Worst case time complexity = **O(n^2)**
- Memory usage = **O(1)**

**Merge sort** - Repeatedly half the array and merge the two sorted halves. It will go down to single 
element arrays e.g. [1] and [2] and then merges them all together. This is a top-down approach and is recursive. 
There is an iterative bottom-up approach by starting with all sub arrays of length 1 and merges until there is
only one array left.

- Worst case (and best) time complexity = **O(nlog(n))**
- Memory usage = **O(n)**

**Quick sort** - The pivot value divides the array into two parts (values less than it, to the left, and values
greater than it, to the right). Recursively, we find the pivot for each sub-array until all arrays contains only one element.

- Worst case (and best) time complexity = **O(nlog(n))**
- Memory usage = **O(log(n))**

<span style="color:#6897bb">**Definition**</span>
**Two pointers**

## Testing
<span style="color:#6897bb">**Definition**</span>
**Unit testing** - done to formally check that a program works. In Java you can use `JUnit` testing suites. Generally,
you will compute something using your program and use an assertion to check that it is what you expected.

## Software Development Lifecycle
<span style="color:#6897bb">**Definition**</span>
**Waterfall**:

1) Idea for project
2) All requirements gathered and spec produced
3) Software written to the spec
4) Tested against spec
5) Bug report and fixes made
6) The software is delivered.

It is usually used for critical applications where the requirements are known well and fixed from the start.

<span style="color:#6897bb">**Definition**</span>
**Iterative**

1) Idea for project
2) Initial requirements gathered
3) Make a plan for the iteration
4) Code the features in this iteration
5) Deliver the features
6) Repeat steps 2 - 5 until the software is ready to be delivered.

Most common form is Agile development - the iterations are called sprints. Day to day tasks are placed into 
a scrum. Daily scrum meetings outline the scrum work for the day.

## Solid Principles
<span style="color:#b6d668">**Good practice**</span>
**Single Responsibility** - one class / method should serve one purpose.

<span style="color:#b6d668">**Good practice**</span>
**Open-Closed principle** - entities should be open for extension but closed for modification.

<span style="color:#b6d668">**Good practice**</span>
**Liskov Substitution principle** - subclasses should be substitutable for the base/parent class. Works with interfaces
i.e. any class that implements the interface is substitutable for another class. 

<span style="color:#b6d668">**Good practice**</span>
**Interface segregation principle** - should not be forced to implement an interface that it doesn't use.
Do multiple interfaces rather than one general one.

<span style="color:#b6d668">**Good practice**</span>
**Dependency inversion principle** - high level modules should not depend on low level modules. Both should depend on abstractions.
Example, suppose a method in class A takes a parameter which is of type class B - this violates the dependency inversion principle.
Instead, make an interface which class B implements and pass this interface.