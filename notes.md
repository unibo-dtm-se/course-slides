# Introduction to the course

- Goal: understand phases, their motivation, their utility, and their cost

- Didactic material

# Introduction to SE

1. What is software
0. Computer science vs. software engineering
    - Goal of CS: studying algorithms
    - Goal of SE: producing working software products
0. What is software
0. Working SW = meeting the requirements
0. Focus on the process = making the process sustainable / maintainable
0. What sustainable means
0. What maintainable means 
0. Software crises
0. CMM levels
0. Overview on workflow phases
    1. Requirement gathering
    2. Requirement analisis
    3. Design
        a. Modelling
        b. Architecture
    4. Implementation
        c. design patterns
    5. Testing
    6. Deployment
    7. Release
    8. Maintenance
0. The role of methodologies

# Preleminaries

Anatomy of a Python project

Running example: the calculator

## Code and code organization

> Example of a Python script showing a calculator app

## Running the code via the Python interpreter

Interpreted vs. Compiled

Python caches

Differences among versions of the runtime (lunch the project with different interpreters)

## The runtime environment

The notion of dependencies

Where are dependencies taken from?

How to automatically restore dependencies?

## Model - View - Controller

The script presented so far can only serve one particular purpose (desktop GUI)

The day requirements change, the script will have to be rewritten from scratch

Core idea: minimize the effort to be spent on handling requirements changes

In practice, we need to split the code into three parts:
- Model: the logic of the application
- View: the way the application is presented to the user
- Controller: the junction among the two

> Example of the same application, but with a different organization

### Brief intuition about modelling

- Represeting input/output data structures

- Representing processing logic

### Different views

- Desktop GUI
- Command-line GUI
- Web GUI
- Mobile GUI

## The notion of interface

Any piece of software can be seen as a black box, exposing an interface towards its users

Which kind of users?
- other pieces of software
- human users (as mediated by some input/output device)

## Many sorts of software artifacts

- Libraries (used by other pieces of software)
- Command-line tools (used by human users or other pieces of software)
- Graphical user interfaces (used by human users via screen, keyboard, mouse, touchpad, etc.)
- Web applications (used by human users via web browsers)

## Component view

To minimize effort on the long run, and maximise reuse, a software project commonly consisting of several components:

Each component is a software artifact, with a clear purpose and interface, and its own development lifecycle

The system is attained by composing the components together

Design is essentially about deciding which and how many components to have, 
how each component should work, and how they should interact with each other

## Other advantages of components

- Division of labor

- Divide et impera approach to handle complexity

- Fine grained testability

### Testing

Core idea of automated testing: write code that checks the correctness of other code

Goals:
- ensure that the code works as expected
- ensure that the code keeps working as expected (after change)


## Deployment, packaging, and release

- Deployment: the process of making the software available to the users
    + may require further coding, e.g. to automate the installation process

- Packaging: the process of creating a distributable artifact (e.g. self-contained installer, or a package for a package manager)
    + may require further coding, e.g. to automate the packaging process

- Release: the process of making a version package publicly available
    + this may imply the availability of some web portal where packages are published
        * several versions of the same package may coexist on the portal
    + may require further coding, e.g. to automate the upload process

### Versioning

- The process of assigning a unique identifier to each release
- The identifier is used to refer to the release in the future
- In this way several variants of the same software can coexist
- Users may want to have access to previous versions of the software for several reasons

## Maintenance

Let's assume that the software development is over.
The result is bug-free, and meets all the requirements.
The users are happy, and the software is widely used.
The requirements are not going to change, and the software is not going to be extended.

Is it ok to not change the source code anymore?

No, it is not.

The runtime may still change, without developers being in control of that.
- e.g. novel version of Python will be released, until the current one is eventually too old
- e.g. novel version of the operating system will be released, until the current one is eventually too old
- etc.

Maintenance work is required just to keep the software alive.

Also consider that it's very unlikely that the software is bug-free, 
and that requirements never change.

## Cooperation among developers

- Code is meant to be read by humans, not computers

- Importance of keeping the code understandable
    * documentation
    * coding style
    * code review
    * linting
    * conventions
    * project structure

- Importance of automating all aspects of the development process
    * testing
    * deployment
    * packaging
    * release
    * maintenance

- Importance of (distributed) version control tools
    * to keep track of changes
    * to allow for parallel development
    * to allow for reverting changes
    * to allow for branching and merging
