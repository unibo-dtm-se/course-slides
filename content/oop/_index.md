+++

title = "Object-Oriented Programming"
description = "Crash course on object-oriented programming in Python"
outputs = ["Reveal"]

+++

# Object-Oriented Programming (OOP)

{{% import path="reusable/header-dp.md" %}}

---

## Many programming paradigms

(cf. <https://en.wikipedia.org/wiki/Programming_paradigm>)

- **Imperative programming**: programs are made by __instructions__ that change the state of the program.
- **Procedural programming**: programs are made by __blocks__ of code that can be reused.
- **Functional programming**: programs are made by __functions__ that transform data.
- **Logic programming**: programs are made by __rules__ that define relationships between data.
- **Object-oriented programming**: programs are made by __objects__ that interact with each other.

{{% fragment %}}
> Mainstream programming languages are actually _blending_ multiple paradigms
- e.g., Python is considered imperative, functional, and object-oriented
{{% /fragment %}}

---

## Why object-oriented programming?

(cf. <https://en.wikipedia.org/wiki/Object-oriented_programming>)

- **By far** the _most used_ programming paradigm nowadays, both in industry and academia
- **Fundamental** for understanding _modern_ programming languages, and their _libraries_
- Most commonly, the __design__ phase of SE involves designing _objects_, and their _behaviours_, and their _interactions_

--- 

## Three dimensions of software design

- **Structure**: how is the software _organised_? how is _information_ organized?
- **Behaviour**: what does the software _do_? how does it transform _data_?
- **Interaction**: how/when do different pieces of software _communicate_ to _cooperate_? 

{{% fragment %}}
> OOP nicely addresses all three dimensions
{{% /fragment %}}

---

## Key principles of OOP

- __Everything__ is an _object_

- A __program__ is a _bunch of objects_ telling each other what to do by __sending messages__

- Every object can have its own __memory__ (state) composed by other objects

- Every object is an _instance_ of a __class__

- Every object has an __interface__, which defines what messages it can receive
    + and so what the __type__ of the object is

---

## Key principles of OOP, in practice

- An object is a _container_ of __attributes__. These can be of 3 sorts:
    * __fields__, i.e. _variables_ that store object-specific _data_ 
        + (these constitute the aforementioned memory/state)
    * __methods__, i.e. _functions_ that can read/write the other members of the object 
        + (these constitute the aforementioned "messages that can be received" by the object)
    * __properties__, i.e. methods that can be accessed _as if_ they were fields

- Classes are _blueprints_ for objects
    + they describe what _attributes_ an object will have
    + each __member__ of a class defines an _attribute_ that _all_ objects of that class will have

- Objects are __created__ as _instances_ of classes
    + each class has a _constructor_, i.e. a magic function which creates an _instance_ of the class
    + the constructor is in charge of _initializing_ the object's _attributes_

- Objects can __use__ _other objects_, by _calling_ their methods or _accessing_ their fields or properties
    + (this is what the aforementioned "sending messages" is about)
    + the _data_ stored in objects' fields are indeed _other objects_
    + the _methods_ of an object are functions which can accept as _arguments_, and return them as _results_ 
    
---

## Example: the `Light` class

{{% multicol %}}
{{% col %}}
### Class definition
```python
class Light:
    def __init__(self, initially_on: bool):
        self.state = initially_on

    @property
    def is_off(self) -> bool:
        return not self.state

    @is_off.setter
    def is_off(self, value: bool):
        self.state = not value

    def switch(self):
        self.state = not self.state

    def to_string(self) -> str:
        return f"Light(state={'on' if self.state else 'off'})"
```
### Usage
```python
l = Light(True)
print(l.to_string()) # Light(state=on)
l.switch()
print(l.to_string()) # Light(state=off)
l.state = True
print(l.to_string()) # Light(state=on)
l.is_off = True
print(l.to_string()) # Light(state=off)
print(l.is_off) # True
```
{{% /col %}}
{{% col %}}
### Aspects to notice

Object of type `Light` have:

-  a __field__ `state` _storing_ a _boolean_
    + which is `True` if that light is on, `False` otherwise  

- a _settable_ __property__ `is_off` corresponding to the opposite of `state`

- a __method__ `switch` that toggles the `state` of the light

- a constructor `__init__` that initializes the `state` of the light to its initial value (`initially_on`)
    + this is invoked via the name of the class, e.g. `Light)`

{{% /col %}}
{{% /multicol %}}

--- 

## What is `self`?

- You can think about a class as group of functions, which all have an _implicit_ first argument, `self`
    + this is a reference to the _instance_ of the class that is being manipulated
    + it is _not_ passed explicitly when calling the method

- Via `self`, you can access the _other attributes_ of an object, from within a method of that object
    + e.g., `self.state` in the `switch` method of the `Light` class

- The name `self` is a convention, but you can use any name you want
    + but it is _strongly_ recommended to stick to `self` for readability
    + the following class is equivalent to the `Light` class above, by simply renaming `self` to `this`:
        ```python
        class Light:
            def __init__(this, initially_on: bool):
                this.state = initially_on

            @property
            def is_off(this) -> bool:
                return not this.state

            # etc.
        ```

- You can imagine that variable self is _automatically_ passed to the method when it is called
    + e.g., `l.switch()` is equivalent to `Light.switch(l)`

---

{{% section %}}

## Examples of entities which can be modelled 

- A memory cell
    + Example method: "assign the current value to value X"
- A counter
    + Example method: "increment"
- A calculator
    + Example methods: "input digit X", "calculate", "store"
- A geometric figure in a CAD program
    + Example method: "translate in the XY plane by (dx, dy)"
- A button
    + Example method: "press"
- A database
    + Example method: "insert a new record R"

---

## Example 1: Memory Cell

```python
class MemoryCell:
    def __init__(self, initial_value: int):
        self.value = 0
        self.assign(initial_value)

    def assign(self, value: int):
        if not in range(0, 256):
            raise ValueError("Value must in the [0, 255] range")
        self.value = value
```

---

## Example 2: Counter

```python
class Counter:
    def __init__(self, initial_value: int = 0):
        self.value = initial_value

    def increment(self, delta: int = 1):
        self.value += delta

    def decrement(self, delta: int = 1):
        self.increment(-delta)
```

---

## Example 3: Calculator

```python
class Calculator:

    def __init__(self):
        self.expression = ""

    def __ensure_is_digit(self, value: int | str):
        if isinstance(value, str):
            value = int(value)
        if value not in range(10):
            raise ValueError("Value must a digit in [0, 9]: " + value)
        return value

    def __append(self, value):
        self.expression += str(value)
    
    def digit(self, value: int | str):
        value = self.__ensure_is_digit(value)
        self.__append(value)
    
    def input(self, symbol):
        self.__append(symbol[0])

    def clear(self):
        self.expression = ""
    
    def compute_result(self) -> int | float:
        try:
            from math import sqrt, cos, sin
            result = eval(self.expression)
            if isinstance(result, Number):
                self.expression = str(result)
                return result
            else:
                raise ValueError("Result is not a number: " + str(result))
        except Exception as e:
            expression = self.expression
            self.expression = ""
            raise ValueError("Invalid expression: " + expression) from e
```

{{% /section %}}

---

## Encapsulation and Information Hiding

### What: [Encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming))

> The idea of presenting a _consistent interface_ [of an object, to its users] that is __independent__ of its _internal implementation_

### How: [Information Hiding](https://en.wikipedia.org/wiki/Information_hiding)

> A means to achieve encapsulation, by __restricting/controlling__ access to the _internal_ details of an object

- Commonly achieved by separating how an object is __used__ from how it is _implemented_
    + e.g., by providing a _public_ interface, and _private_ implementation details

- Commonly involves enforcing some __invariants__ on the object's state
    + e.g., by ensuring that some attributes are _always_ in a certain range...
    + ... or that some attributes are _always_ consistent with each other

---

## Why Encapsulation Matters?

### Encapsulation helps to
- protect data from accidental modification
- ensure controlled access through defined methods
- improve maintainability by allowing internal implementation changes without affecting external usage
- create modular, reusable, and scalable code

### Example in real life
- a car’s accelerator pedal: you control speed without directly modifying the engine parameters

--- 

{{% section %}}

## Example: Encapsulation in the `Light` class

Let's suppose that
- the intensity of the light bulb must be implemented as a __byte__ (`0` to `255`) where:
    + 0 means the light is off
    + 255 means the light is at its maximum intensity
- yet we may want the intensity to be _perceived_ as a __percentage__ (`0.0` to `100.0`) by the user
- the user may also want to have a _read-only_ __property__ to know if the light _is on_ (intensity > 0)
- the user should __not__ be able to go _beyond_ the `0—100%` range when setting the intensity
- switching the light on/off should work as follows:
    1. if the intensity is > 0, it should be set to 0
    2. if the intensity is 0, it should be set to the last value it had before being switched off
    3. the first time the light is switched on, intensity should be set to `100%`

---

## Example: Encapsulation in the `Light` class

```python
class Light:
    def __init__(self, initially_on: bool):
        self.__intensity: int = int(initially_on * 255)
        self.__last_intensity: int = 255
    
    @property
    def is_on(self) -> bool:
        return self.__intensity > 0

    @property
    def intensity(self) -> float:
        return self.__intensity / 255 * 100
    
    @intensity.setter
    def intensity(self, value: float):
        if not 0 <= value <= 100:
            raise ValueError("Intensity must be in the [0, 100] range")
        self.__intensity = int(value / 100 * 255)

    def switch(self):
        if self.__intensity > 0:
            self.__last_intensity = self.__intensity
            self.__intensity = 0
        else:
            self.__intensity = self.__last_intensity

    def to_string(self) -> str:
        return f"Light(intensity={self.__intensity})"
```

### Usage

```python
l = Light(initially_on=False)
print(l.to_string()) # Light(intensity=0)
l.intensity = 50
print(l.to_string()) # Light(intensity=127)
l.switch()
print(l.to_string()) # Light(intensity=0)
print(l.is_on)       # False
print(l.intensity)   # 0.0
l.switch()
print(l.to_string()) # Light(intensity=127)
l.intensity = 150    # ValueError: Intensity must be in the [0, 100] range
print(l.__intensity) # AttributeError: 'Light' object has no attribute '__intensity'
```

---
 
## Aspects to notice

- The `intensity` and `last_intensity` attributes are _private_ (i.e., their names start with `__`)
    + this means that they are _not_ accessible from outside the class
    + this is a way to enforce _information hiding_

- The technical detail "intensity is represented as a byte" is _hidden_ from the user
    + the user only sees the intensity as a percentage

- The invariant "intensity must be in the [0, 100] range" is _enforced_ by the setter of the `intensity` property
    + if the user tries to set an intensity outside this range, a `ValueError` is raised
    + as that's the _only_ way to set the intensity, the invariant is _always_ respected

{{% /section %}}

---

## Identity and Equality

### Identity

- Two objects are _identical_ if they are the _same_ object in memory
    + i.e., if they have the _same_ memory address

- This is checked using the `is` operator
    + e.g., `a is b` returns `True` if `a` and `b` are the _same_ object

### Equality

- Two objects are _equal_ if they have the _same_ _value_
    + i.e., if their attributes are _recursively equal_

- This is checked using the `==` operator
    + yet, the operator only works if the object's class has a `__eq__` method which defines what equality means for that class

---

## Example: Complex Numbers

```python
class Complex:
    def __init__(self, real: float, imag: float):
        self.re = real
        self.im = imag

    def __eq__(self, other):
        return other is not None and hasattr(other, 're') and self.re == other.re and hasattr(other, 'im') and self.im == other.im
```

### Usage

{{% multicol %}}
{{% col %}}
```python
a = Complex(1, 2) # (1 + i * 2)
b = a
c = Complex(1, 2) # (1 + i * 2)
d = Complex(2, 1) # (2 + i * 1)
```
{{% /col %}}
{{% col %}}
```python
print(a is a) # True
print(a is b) # True
print(a is c) # False
print(a is d) # False
```
{{% /col %}}
{{% col %}}
```python
print(a == a) # True
print(a == b) # True
print(a == c) # True
print(a == d) # False
```
{{% /col %}}    
{{% /multicol %}}

---

## How to write good `__eq__` methods

1. No object is equal to `None`: `x == None` should always return `False`
    - always check if the other object is `None`, returning `False` if it is
        + this is to avoid `NoneType` errors

2. Check whether the _other_ object is an instance of the same class of the current object
    - this is to avoid `AttributeError` errors
    - e.g., `isinstance(other, CurrentClass)` or `type(other) == type(self)` or `isinstance(other, type(self))`

2. Alternatively, check whether the _other_ has the same attributes as the current object
    - this is to avoid `AttributeError` errors
    - e.g., `hasattr(other, 'attribute')` for each attribute of the current object that you want to compare

3. Compare the attributes of the _other_ object with the attributes of the current object
    - this is to define what equality means for the class
    - e.g., `self.attribute == other.attribute` for each attribute of the current object that you want to compare

---

## Example: Sets of Complex Numbers

```python
a = Complex(1, 2) # (1 + i * 2)
b = a
c = Complex(1, 2) # (1 + i * 2)
d = Complex(2, 1) # (2 + i * 1)

s = {a, b, c, d}
print(len(s)) # TypeError: unhashable type: 'Complex'
```

---

## Hashable objects

(cf. <https://www.pythonmorsels.com/what-are-hashable-objects/>)

- Long and complex discussion

- Put simply, you need objects to be __hashable__ in order for them to be used within a `set` or a `dict`

- An object is hashable if it has a `__hash__` method that returns a _semi-unique_ hash value for that object
    + a __hash value__ is an integer that is used to quickly compare objects
    + if two objects are equal, their hash values _must_ be the same
    + if two objects are _not_ equal, their hash values _should_ be different (but __collisions__ may occur)

### Rules of thumb for implementing the `__hash__` method

- Always implement the `__hash__` method if you implement the `__eq__` method (and _vice versa_)
- To compute some hash value, pass a __tuple__ to the `hash()` function, containing all and only the attributes that you compared in the `__eq__` method
    + e.g., `hash((self.attribute1, self.attribute2))`

---

## Example: Hashable Complex Numbers

```python
class Complex:
    def __init__(self, real: float, imag: float):
        self.re = real
        self.im = imag

    def __eq__(self, other):
        return other is not None and hasattr(other, 're') and self.re == other.re and hasattr(other, 'im') and self.im == other.im

    def __hash__(self):
        return hash((self.re, self.im))
```

### Usage

{{% multicol %}}
{{% col %}}
```python
a = Complex(1, 2) # (1 + i * 2)
b = a
c = Complex(1, 2) # (1 + i * 2)
d = Complex(2, 1) # (2 + i * 1)
```
{{% /col %}}
{{% col %}}
```python
s = {a, b, c, d}
print(len(s)) # 2
print(s) # {<__main__.Complex object at 0x78d202e09520>, <__main__.Complex object at 0x78d202e09580>}
```
{{% /col %}}    
{{% /multicol %}}