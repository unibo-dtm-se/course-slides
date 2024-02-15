+++

title = "Introduction to Software Engineering"
description = "QA, reproducibility, TDD"
outputs = ["Reveal"]

+++

# Introduction to Software Engineering

{{% import path="reusable/header.md" %}}

---

## Relevant nomenclature (pt. 1)

> __Computer Science__ (CS) is the study of _computation_, 
> i.e. the _automatic_ manipulation of _information_ via __algorithms__

(intuitive definition provided by the teacher)

> An __algorithm__ is a _finite_ set of _well-defined_
> rules for the solution of a __problem__ in a _finite_
> number of _steps_

(from [IEEE Standard Glossary](https://ieeexplore.ieee.org/document/159342))

---

## Relevant nomenclature (pt. 2)

> A __problem__ is a _well-defined_ specification of a result to be attained 
> (_output_) from starting from some _initial_ information or preconditions (_input_)

(intuitive definition provided by the teacher)

- e.g. finding the _shortest path_ between two a source `S` and a destination `D` in a _graph_
- e.g. producing a `T`-jam flavored _cheesecake_ for `N` guests
- e.g. generating an aggregate report of _sales_ given a _database_ of _transactions_

---

## Relevant nomenclature (pt. 3)

![Concept of an algorithm](./input-processing-output.png)

- _Processing_ is any operation aimed at transforming input into output when solving a problem
    + it may leverage some _storage_ (e.g. to keep track of _intermediate_ results)

- When both input and output are _data_, and the process is _automatic_, we are talking about _computation_

- Algorithms are a way to _express_ computation in a _formal_ way
    + __formal__ $\approx$ _unambiguous_, _precise_, _rigorous_
        * i.e. such that a _machine_ can reproduce the process, precisely
            - that machine is a _computer_

- Algorithms can be studied _independently_ of the _machine_ which executes them
    + e.g. to understand their _properties_, _limitations_, theoretical _costs_

---

## What is computer science essentially about

- Defining _algorithms_ as __recipes__ for processing _interesting problems_
    + requires clear representations for input / output / storage __data__

- Studying algorithms’ _time/memory requirements_, formally
    + as well as their _termination_

- Algorithms can be _combined_ to solve _more complex_ problems

---

## Example: sorting algorithm (Bubble sort)

{{<multicol>}}
{{%col%}}
![Bubble sort pseudo-code](./bubble-sort.png)
{{%/col%}}
{{%col%}}
- `Input`: array of _comparable_ items
    + several algorithms to _compare_ items
        * depending on items _type_

<br>

- `Output`: sorted array
    + according to comparison strategy

<br>

- Many algorithms with different properties
    + e.g. _bubble sort_
{{%/col%}}
{{</multicol>}}

---

## Let's recall the big picture (pt. 1)

> Why do people care about algorithms in the first place?

- Put it simply, most people don't really care about algorithms per se

- They care about __automating__ the _solutions_ to _problems_
    + most commonly quicker, more precise, less error-prone than humans
        * (when the problem is _repetitive_ and _structured_ enough)
    
- Hence, _computers_ are __enablers__ for _automation_
    + and algorithms are the strategies followed by computers to solve problems

- However, _not_ all problems are as _simple_ as ordering an array
    + most real-world problems are _complex_, _multi-faceted_, and _ambiguous_

- _Effort_ and _creativity_ is required to understand how to 
    1. __decompose__ real-world _problems_ into simpler ones
    2. __select__ the right _algorithms_ to solve them
    3. __combine__ _algorithms_ to solve the original problem
    4. __instruct__ a _computer_ to do all such stuff

---

## More nomenclature (pt. 1)

(from [IEEE Standard Glossary](https://ieeexplore.ieee.org/document/159342))

> __Software: computer _programs_, _procedures_, and possibly associated _documentation_ and data 
> pertaining to the operation of a computer system

- Software $\supset$ algorithms
    + all algorithms can be expressed in software
    + not all software is expressing algorithms
        * e.g. there are programs which are not meant to _terminate_ (OS, web servers, etc.)

---

## More nomenclature (pt. 2)

(from [IEEE Standard Glossary](https://ieeexplore.ieee.org/document/159342))

> __Software Engineering__ (SE) definition:
>
> (1) The application of a _systematic_, disciplined, quantifiable approach to the _development_, operation, 
> and maintenance of __software__; that is, the application of engineering to software. 
>
> (2) The study of approaches as in (1).

- Focus on the _development_ of a software _product_ ...
    + i.e. something which needs to _meet requirements_

- ... and on the _process_ of developing it
    + i.e. making the process _reproducible_, _sustainable_, and _maintainable_

---

## Let's recall the big picture (pt. 2)

- Demand is for _automation_ of _solutions_ to _problems_

- Supply is for _products_ which do that by means of
    + computers (__hardware__), as produced by _electronic engineering_ ...
    + running __software__, as produced by _software engineering_


- Computer engineering mostly focuses on creating __general-purpose__ computers
    + i.e. computers which can be instructed to solve _any_ problem
        * (given the right _software_)

- Software engineering mostly focuses on creating __specific-purpose__ software
    + i.e. software which solves a particular set of problems
        * (when run on a _general purpose_ computer)

---

## What is software engineering essentially about (pt. 1)

- Studying how to __realise__ software _products_ which meets _customers' requirements_
    + customers $\approx$ the _stakeholders_ seeking for automatic solutions to problems
    + requirements $\approx$ description about _what_ problems should be solved + constraints about _how_

- As the goal is a product...
    + ... _success_ is measured in terms of __requirements satisfaction__
        * i.e. whether the products is _effective_ / _efficient_ w.r.t. the requirements
    + ... a notion of product __lifecycle__ is inherently present
        * from requirements specification to implementation, _and beyond_
            <!-- ![Concept of software engineering phases](./se.png) -->
            - there including validation, and __maintenance__

{{<image width="25" src="./se.png">}}

---

## What is software engineering essentially about (pt. 2)

- As it is an engineering discipline, _optimization_ of the _development_ process is a key concern
    + mostly because _demand will evolve_ and _requirements will change_
        * and __nobody__ wants to _restart_ development from scratch
    + also because the product will need to be _maintained_ over time
        * and it is _boring_ and _costly_ to maintain the software
    + also because optimising development can, on __the long run__,
        1. _reduce_ the _cost_ of the product
        2. _increase_ the _quality_ of the product
        3. _reduce_ the _time_ to market of novel features / products

- Software development process should be _reproducible_, _sustainable_, _evolvable_, and _maintainable_
    + __reproducible__ $\approx$ repeatable, with _predictable_ outcomes
    + __sustainable__ $\approx$ it's possible to _timely_ satisfy requirements with _controllable_ costs and efforts
    + __evolvable__ $\approx$ it's possible to _adapt_ the product to _new_ requirements in a sustainable way
    + __maintainable__ $\approx$ it's possible to _fix_, _improve_, or just keep the product _alive_ in a sustainable way

---

## Why is software engineering relevant?

- _Software_ is _everywhere_
    + from _smartphones_ to _cars_, from _fridges_ to _toasters_, from _banks_ to _hospitals_, from _schools_ to _governments_, from _entertainment_ to _science_, from _industry_ to _agriculture_

- _Software_ is a strange sort of product
    + it's _intangible_, _invisible_, and _weightless_
    + __zero marginal cost__: the cost of producing more one product unit is negligible
    + most of the cost is in the _conception_, _development_ and _maintenance_ of the product

- Some software products may also come with:
    + _infrastructural_ costs (e.g. servers, networks, licenses, energy, cooling, etc.)
    + _operational_ costs (e.g. people operating the servers, networks, etc.)

- Most cost entries are (directly or indirectly) _personnel_ costs
    + personnel must be creative, knowledgeable, disciplined, motivated, and _coordinated_
        * performance is not really proportional to the amount of person-time spent  

- Misunderstanding these aspects can lead to __software crises__
    + cf. [A Collection of Well-Known Software Failures](https://www.cse.psu.edu/~gxt29/bug/softwarebug.html)
    + cf. [37 Epic Software Failures that Mandate the Need for Adequate Software Testing](https://www.cigniti.com/blog/37-software-failures-inadequate-software-testing/)

---

## About software crises

---

## Why is software engineering relevant for Digital Transformation?

---

## What are you expected to learn in this course

