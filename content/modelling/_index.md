+++

title = "Software Modelling with UML"
description = "Crash course on software modelling via UML"
outputs = ["Reveal"]

+++

# Software Modelling with UML

{{% import path="reusable/header.md" %}}

---

## Modelling in Engineering

_Architects_ and _civil engineers_ create __models__ of the things they are going to build

{{% multicol %}}
{{% col %}}
![](./model-bridge.jpg)
Model of a Bridge
{{% /col %}}
{{% col %}}
![](./model-building.webp)

Model of a Building
{{% /col %}}
{{% /multicol %}}

---

## Model in Statistics / Machine Learning

In _statistics_ (and _machine learning_) a __model__ is a _mathematical representation_ of a real-world process
<br> (commonly attained by _fitting_ a parametric _function_ over a _sample_ of _data_ describing the process)

![](./model-statistics.webp)

e.g.: __$f(x) = \beta_0 + \beta_1 x $__ where __$f$__ is the amount of minutes played, and __$x$__ is the age

---

## What is a model?

(cf. <https://plato.stanford.edu/entries/models-science/>)

> A __model__ is a _simplified_ _representation_ of something complex

### What are models useful for?

- __Understanding__ of the real world, via _simplification_ and _abstraction_ (i.e., by removing details)
    + think about the many [models of the atom](https://en.wikipedia.org/wiki/History_of_atomic_theory) (Bohr, Rutherford, etc.), or the wooden miniature of a bridge

- __Explain__ a _phenomenon_ by fitting the model onto the _observed_ data, to reconstruct the process
    + think about the [attachment theory](https://en.wikipedia.org/wiki/Attachment_theory) in psychology

- __Predicting__ the _dynamic_ behaviour of a system (possibly, before/without building the system)
    + think about the [weather forecast](https://en.wikipedia.org/wiki/Weather_forecasting), or, again, the wooden miniature of a bridge

---

## Models are simplifications

(cf. <https://en.wikipedia.org/wiki/All_models_are_wrong>)

> "_All_ models are __wrong__, but _some_ are __useful__" — George Box

- Each model is _stressing some aspects_ of the real world, and _ignoring others_
- Focus on the _purpose_ and the _context_ of a model:
    * if the goal is __understanding__, the model should be _simple_ and _intuitive_
    * if the goal is __prediction__, the model should be _accurate_ and _precise_

### Example

- __Newton's Laws__: they are not fully correct (Einstein’s relativity refined them)
    * but they are still useful for _engineering_ and _daily_ physics

---

## Why do engineers model systems?

- Models allow engineers to _design_ and _study_ a system __before__ building it

- Building is commonly more _expensive_ and _time-consuming_ than _modelling_

- Models can __verify__ (to some extent) the system they want to create, _before_ fully building it

- Models allow designers to __take design decisions__ _early_, and _cheaply_

- Models can be used to __represent__ and __communicate__ the design of a system
    + useful for _collaboration_ and _documentation_...
    + ... which in turn allow new people to _join_ the project

---

## What about _software_?

- Writing _software_ _implies_ __modelling__ the world and __representing__ it in a formal way
    + so, in a sense, the _source code_ is a _model_ of the _world_ (or, at least, of the _problem_)

- Yet, the _source code_ of a project can easily grow in __complexity__
    + think about _large projects_ with __millions of LoC__:
        1. how can a person keep them _all_ in their _mind_?
        2. how could that person _transfer_ all that _knowledge_ to _others_?

- Indeed, as software projects tend to grow complex, the aforementioned motivations for modelling apply to _software_ as well
    + we need _more abstract_ (than code) and _visual_ ways to __represent__ _software systems_

> Software systems are commonly modelled using the __Unified Modelling Language__ (UML)

---

## The Unified Modelling Language (UML)

(cf. <https://en.wikipedia.org/wiki/Unified_Modeling_Language>)

- __General-purpose__, _graphical_, modeling _language_ in the field of software engineering
    + intended to provide a _(semi)-formal_ way to _visualize_ the design of a software system

- UML is a __standard__ ([ISO/IEC 19501:2005](https://www.iso.org/standard/32620.html)) managed by the [Object Management Group](https://www.omg.org/) (OMG) since 1997

- Actually, nowadays, most practitioners do _not_ properly use UML, but instead produce _informal diagrams_
    + more or less inspired by UML, but __not__ _strictly_ _following_ the _standard_

- In any case, the focus is on giving a __graphical__ language to represent various aspects of a software system

---

## What can UML represent?

- UML can represent _many_ aspects of a software system, via as many _sorts_ of __diagrams__
    + broadly categorized in __structural__ and __behavioural__ diagrams

{{% multicol %}}
{{% col %}}
![](https://upload.wikimedia.org/wikipedia/commons/e/ed/UML_diagrams_overview.svg)
{{% /col %}}
{{% col %}}
- __Class__ Diagrams: overview on the _classes_ and their _relationships_
- __Sequence__ Diagrams: _interactions_ between _objects_ in a _time sequence_
- __Activity__ Diagrams: _flow_ of _control_ in a _process_
- __State__ Diagrams: _transitions_ between _states_ of an _object_
- __Component__ Diagrams: architectural _components_ and their _relationships_
- __Deployment__ Diagrams: _physical_ _deployment_ of _artifacts_ on _nodes_
- __Use Case__ Diagrams: _actors_ and _use cases_ they _interact_ with
{{% /col %}}
{{% /multicol %}}

---

# Class Diagrams

- Modelling the _structure_ of a system
- Focus on _classes_ and their _relationships_

---

## Class Diagrams Overview

(cf. <https://en.wikipedia.org/wiki/Class_diagram>)

{{< plantuml >}}
@startuml
class Class {
    - __another_private_field
    # _overridden_protected_method
    + public_field: int
    + property: str
    + method(arg)
}

abstract AbstractClass {
    - __private_field: dict
    # _protected_field: set
    + {abstract} abstract_method()
}

interface Interface {
   + method(arg)
   + concrete_method()
}

class SubClass {
    +overridden_method()
    +additional_method()
}

enum Enum {
    +OPTION_ONE
    +OPTION_TWO
    +OPTION_THREE
}

class Container {
    - __items
    + add(item)
    + remove(item)
    + clear()
}

class Item

class Composed {
    + component1
    + component2
}

class Component

class Related {
    + method(Associated)
}

class Associated {
    + method() -> Related
}

AbstractClass <|-- Class: extends
Class <|-- SubClass: extends
Interface <|.. Class: implements
Container "1" o-- "0..*" Item: aggregation
Composed "1" *-- "2" Component: composition
Related "1" -- "1..*" Associated : relation / association
@enduml
{{< /plantuml >}}

---

## Class Diagram Example

(Remark: this is not a "good" diagram from a real system, but just an example to show the graphical syntax)

{{< plantuml >}}
@startuml
enum Status {
  + MISSING
  + AVAILABLE
  + BORROWED
  + LATE
}

' Abstract class for library items
abstract class LibraryItem {
    - __id: str
    + title: str
    + author: str
    + state: Status
    + {abstract} get_info() -> str
    + front: Page
    + back: Page
}

' Interface for borrowable items
interface Borrowable {
    + borrow(member: Member) -> bool
    + return_item() -> bool
}

' Concrete classes
class Book extends LibraryItem {
    - __isbn: str
    + genre: str
    + get_info() -> str
}

class Magazine extends LibraryItem {
    - __issue_number: int
    + category: str
    + get_info() -> str
}

Borrowable <|-- LibraryItem

' Container class for library items
class Library {
    - __items: list[LibraryItem]
    + add_item(item: LibraryItem) -> None
    + remove_item(item: LibraryItem) -> None
    + find_item(title: str) -> LibraryItem
}

' Library aggregates library items
Library "1" o-- "0..*" LibraryItem : manages

' Loan relationship
class Loan {
    + item: LibraryItem
    + due_date: str
    + renew() -> bool
}


Loan "1" -- "1" LibraryItem

' Composition: A library item is composed of front and back pages
class Page {
    + content: str
}
LibraryItem "1" *-r- "2" Page

LibraryItem -l- Status
@enduml
{{< /plantuml >}}

---

## Class Diagram Explained (pt. 1)

1. Focus on __classes__ (here intended as _data types_)
    + report class _names_
    + report _sort_ of classes (e.g. `abstract`, `interface`, `enum`, `class`)
        ![](https://www.plantuml.com/plantuml/svg/Iyv9B2vMS0QHN5o9ISKbHOd99GeGKKSe5ogRcLUIMfIMc9ogu0bZSN6bvfNcAhW22IukPx0ctQBeZCoKbDIyM5rK0m00)
        + `enum`s are types whose values are _fixed_ and _enumerated_

2. Focus on __relationships__ among classes
    - _inheritance_ a.k.a. "extends" (solid line with a triangle)
        ![](https://www.plantuml.com/plantuml/svg/Iyv9B2vM22ujI2ro1ZEvO299O3uN5vASJOrkaIwIL6PUIMfHMc9oAiI0aCg2L1In9B085rmIOG281m00)
    - _implementation_ a.k.a. "implements" (dashed line with a triangle)
        ![](https://www.plantuml.com/plantuml/svg/SoWkIImgAStDuSf9JIjHACbNACfCpoXHICaiIaqkoSpFuqhEIImkLd06aLoPUIMfHMc9oQaAdZ0M5vobO5EZfmTLw92Qbm8q5000)
    - _aggregation_ (solid line with a white diamond): the container may exist without items
        ![](https://www.plantuml.com/plantuml/svg/oqbDAr4eoLSeoapFA55moInAJIx9pC_ZuahEIImkLd3Epoj9pCnBBOBoFKjISxcuuA8AIWeAXaeA-RgwkWfA1jfAO7a0)
    - _composition_ (solid line with a filled diamond): the composed entity cannot exist without the component
        ![](https://www.plantuml.com/plantuml/svg/JOqn2W8m34NtdEAJKUdG6nJq8gMDMcWJQUBzTH4wFjw3LppgZi-QDEKH2CCUprVWFhQq6AP4RLPtt6ozpQMVgA91z3TW83CkAILmllBH5D7-Utm1)
    - _association_ (solid line, with or without arrow): any other relevant sort of symmetric (no arrow) or asymmetric (with arrow) relation
        ![](https://www.plantuml.com/plantuml/svg/SoWkIImgAStDuSf9JIjHACbNACfCpoXHSCaiIaqkoSpFu-9ApaaiBbPmpibCpIk1Se9JYyfIYxYu888AkhfsK24hXUJ4d9nYBeVKl1IWeG00)

---

## Class Diagram Explained (pt. 2)

![](https://www.plantuml.com/plantuml/svg/TOv12i8m44NtdcB0ZIBf9Jn8cKv634HQcj5DoTqD5KF39viaF2PldaHEYUxxkPs872rh-B3f-0WQVI7dGcPJCVMLtMXvJp581SEm_zsIiGN9zBj7SE44kd6ctULSq_bIUyx-ScrJApxMLjOFHYasuv9-DYujFfwIhIoMwV_gEd4KlFaB)

3. Focus on the __attributes__ of each class
    - _private_ attributes (beginning with a `-`, or red square)
    - _protected_ attributes (beginning with a `#`, or yellow diamond)
    - _public_ attributes (beginning with a `+`, or green square)
    - _abstract_ attributes (italics)
    - _static_ or _class_ attributes (underline)
    - _fields_ or _properties_, i.e. attributes without parentheses (beginning with a unfilled symbol)
    - _methods_ or _functions_, i.e. attributes with parentheses (beginning with a filled symbol)


---

## Class Diagram Explained (pt. 3)

### Common questions

- should you include _type_ information in attributes? $\Rightarrow$ __not mandatory__, _but recommended_
- should you include _visibility_ information in attributes? $\Rightarrow$ __yes__
- should you include Python's _underscore prefixes_ for visibility (`_` or `__`)in the diagram $\Rightarrow$ __as you like__
- should you include _all_ attributes?
    + if you're willing to provide a _complete model_ of the code's _structure_ $\Rightarrow$ __yes__
    + if you're willing to provide an _overview_ of the _public API_ $\Rightarrow$ __public attributes only__
    + if you're willing to an _overview_ of the types $\Rightarrow$ __no__

---

# Sequence Diagrams

- Modelling the _interaction_ among the components of a system
- Focus on _objects_ / _components_ and their _interactions_ over _time_
    * i.e., _who_'s sending _which message_ to _whom_, _when_

---

## Sequence Diagrams Overview

{{% multicol %}}
{{% col class="col-4" %}}
(cf. <https://en.wikipedia.org/wiki/Sequence_diagram>)
{{< plantuml >}}
@startuml
hide footbox

actor Actor
participant Participant
database Database

activate Actor
Actor -> Participant: request
activate Participant

Participant -> Database: query
activate Database

note right of Actor
vertical bars represent
participants's control flow,
which are synchronous
end note

Database -> Database: internal\nprocedure
activate Database
deactivate Database

Database --> Participant: results
deactivate Database

Participant --> Actor: response
deactivate Participant

== New situation ==

alt response is ok
    Actor -> Participant: another request
    activate Participant

    Participant -> Participant: stateless\nprocedure
    Participant -> Actor: another response
    deactivate Participant

else response has error
    Actor --> Participant: shut down
    destroy Participant
    create participant "Another Participant" as Participant2
    Actor --> Participant2: start another participant
end
@enduml
{{< /plantuml >}}

{{% /col %}}
{{% col %}}
- The diagram is _vertical_, each column corresponds to the __life-line__ of a _participant_

- The vertical axis corresponds to __time__, the lower, the later

- __Participants__ can be objects or entities of any sort (e.g. OOP objects, infrastructural components, etc.)
    + special icons may be used for special participants, such as _actors_ or _databases_
    + participants are assumed to be _already_ __up and running__ at the beginning of the sequence
        - yet they can be created and destroyed during the sequence

- Horizontal arrows represent __messages__ sent from one participant to another
    + the _label_ of the arrow is the _message_ itself
        * an informal description of the _message_ can be used too, but formal is better
    + straight line is for _requests_, dashed line is for _responses_

- White vertical bars on a participant's life-line represent the __control flows__
    + i.e., the participant is _active_ during that time
        * this is way to stress the _duration_ of activities
    + participants get _activated_ starting to __process__ some received message, _deactivated_ when done

- _Branching_ (if) or _loops_ are represented via ad-hoc __frames__

- Double horizontal lines may be used to denote a __new__ interaction sequence

{{% /col %}}
{{% /multicol %}}

---

## Sequence Diagram Example in OOP (pt. 1)
### Visualising the [Iterator Pattern](https://refactoring.guru/design-patterns/iterator) (compliant to Python's [iterator protocol](https://realpython.com/python-iterators-iterables/))

{{% multicol %}}
{{% col %}}
#### Classes
```python
class MyIterator:
    def __init__(self, items):
        self.__items = items
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__items):
            raise StopIteration
        current_item = self.__items[self.__index]
        self.__index += 1
        return current_item
```

```python
class MyCollection:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __iter__(self):
        return MyIterator(self.items)
```

#### Sequence described in the diagram

```python
collection = MyCollection()
collection.add("A")
collection.add("B")
collection.add("C")

iterator = iter(collection)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
```
{{% /col %}}
{{% col %}}
{{< plantuml >}}
@startuml
hide footbox

participant "Client" as Client
participant "MyCollection" as Collection
participant "MyIterator" as Iterator

== Initialization ==
activate Client
Client -> Collection: add("A")
Client -> Collection: add("B")
Client -> Collection: add("C")

== Retrieving the Iterator ==
Client -> Collection: iter()
activate Collection
create Iterator
Collection -> Iterator: Create Instance
Collection --> Client: return Instance
deactivate Collection

== Iterating Over Elements ==
loop
    Client -> Iterator: next()
    activate Iterator
    Iterator -> Iterator: Check if more elements
    alt More Elements Available
        Iterator --> Client: return Current Item
    else No More Elements
        Iterator --> Client: raise StopIteration
        deactivate Iterator
    end
end
destroy Iterator

@enduml
{{< /plantuml >}}
{{% /col %}}
{{% /multicol %}}

---
## Sequence Diagram Example in OOP (pt. 2)

- Participants are __named__ after _classes_, yet they refer to _instances_ of those classes

- Arrows are __named__ after _method calls_ when possible

- The following pieces of code are completely equivalent in Python:

{{% multicol %}}
{{% col %}}
```python
iterator = iter(collection)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
```
{{% /col %}}
{{% col %}}
```python
for item in collection:
    print(item)
```
{{% /col %}}
{{% /multicol %}}

---

## Sequence Diagram Example in Distributed Systems

{{< plantuml >}}
@startuml
hide footbox

actor User
participant "Web Browser" as Browser
participant "Web Server" as Server
database "Database" as DB
actor Admin
participant "Email Service" as EmailService

activate User
User -> Browser: Request Page
activate Browser
Browser -> Server: HTTP GET /homepage
activate Server
Server -> DB: Query User Data
activate DB
DB --> Server: User Data Response
deactivate DB
Server --> Browser: HTML Content
deactivate Server
Browser --> User: Render Page
deactivate Browser

== User Authentication Flow ==
User -> Browser: Enter Credentials
activate Browser
Browser -> Server: POST /login
activate Server
alt Valid Credentials
    Server -> DB: Validate User
    activate DB
    DB --> Server: Success
    deactivate DB
    Server --> Browser: Set Auth Token
else Invalid Credentials
    Server --> Browser: Authentication Error
end
deactivate Server
Browser --> User: Show Login Result
deactivate Browser

== Additional Features ==
User -> Browser: Perform an Action
activate Browser
Browser -> Server: Request Action
activate Server
par Parallel Processing
    Server --> DB: Write Logs
    activate DB
    Server --> DB: Process Request
    deactivate DB
end
Server --> Browser: Action Success
deactivate Server
Browser --> User: Display Confirmation
deactivate Browser

== Object Creation & Deletion ==
create EmailService
EmailService <- Admin: deploy
User -> Browser: Create New Account
activate Browser
Browser -> Server: Register User
activate Server
Server -> DB: Insert New User
activate DB
DB --> Server: Confirmation
deactivate DB
Server -> EmailService: Send Welcome Email
activate EmailService
Server --> Browser: Registration Successful
deactivate Server
Browser --> User: Show Confirmation
deactivate Browser

EmailService --> User: Welcome Email
deactivate EmailService

@enduml
{{< /plantuml >}}

---

# State Diagram

- Modelling the _state_ of an _object_ and the _transitions_ among them
- Focus on _classes_ and how method calls affect their _fields_/_properties_

---

## State Diagram Overview

{{% multicol %}}
{{% col %}}
{{< image width="100%" src="https://www.plantuml.com/plantuml/svg/NP6zRiCm38HtFSKXIt-GPCYOeKZ7pXth3e9DsqGTqf3P57txC8uCnmOqYAVlI94y3HQJ_PwxyDHHRJ15ugOrL9oeD5O9mH4ZR3w4ZME7prkuGHnmKt24jJp0JyH8phnHEbF57isc-yrTKTHQIalFUnPN-264hzTlx7PlKqtEdw4BYOKmgluyPP_qCNpqQT_hm4Q5h8bSoHbBKPnXbNNYm_plGXwn_Be0EzKUpxod_JPNGv_qeZyiJI6YkFTSjb4QUbday6QFg5dc1aKT7JUazJIJVxBb5BVXZws5A2eQoiIziGhOZmMI2ivIEFdDztq5" >}}
{{% /col %}}
{{% col %}}

{{% /col %}}
{{% /multicol %}}

---

# Activity Diagram

TBD

---

# Components Diagram

TBD

---

# PlantUML

TBD

---

{{% import path="reusable/back.md" %}}