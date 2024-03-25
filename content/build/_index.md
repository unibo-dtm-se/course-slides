 +++

title = "Software dependencies, Build automation"
description = "Introduction to agile and DevOps, a case from the literature, SCRUM"
outputs = ["Reveal"]

+++

# Software dependencies, Build automation

{{% import path="reusable/header-dp.md" %}}

---

# The build "life cycle"

(Not to be confused with the system development life cycle (SDLC))

> The process of creating *tested deployable software artifacts*
> <br/>
> from *source* code

May include, depending on the system specifics:
1. *Source code manipulation* and generation
1. Source code *quality assurance*
1. __Dependency management__
1. *Compilation*, linking
1. *Binary manipulation*
1. *Test execution*
1. Test *quality assurance* (e.g., coverage)
1. API *documentation*
1. __Packaging__
1. __Delivery__

<!-- ---

# Lifecycle styles

* **Custom**: select some phases that the product needs and perform them.
    * *Flexible and configurable*: tailored on each project's needs
    * *Hard to adapt and port*

* **Standard**: run a sequence of pre-defined actions/phases.
    * *Portable and easy to understand*: replicated on every product
    * *Limited configuration options* -->

---

# Build automation

Automation of the build lifecycle

* In principle, the lifecycle could be executed manually
* In reality *time is precious* and *repetitivy is boring* (and __error-prone__)

> $\Rightarrow$ Create software that automates the building of some software!

* All those concerns that hold for software creation hold for build systems creation...

---

<!-- ## Build automation: basics and styles

Different lifecycle types generate different build automation **styles**

**Imperative**: write a script that tells the system what to do to get
from code to artifacts
* *Examples*: make, cmake, Apache Ant
* *Abstraction gap*: verbose, repetitive
* Configuration (*declarative*) and actionable (*imperative*) logics *mixed* together
* Highly *configurable*

**Declarative**: adhere to some convention, customizing some settings
* *Examples*: Apache Maven
* Separation between *what* to do and *how* to do it
  * The build system decides how to do the stuff
* *Configuration limited* by the provided options -->

## __Declarative__ build automation systems

Modern build automation systems are __declarative__

> __Declarative__ software $\approx$ the program describes *what* to do, not *how* to do it
> <br>
> (as opposed to _imperative_ software $\approx$ the program describes *how* to do it, 
> <br>
> e.g. Python)

In other words:
- they rely on *conventions* and *defaults*
- as long as developers follow them, the configuration is _minimal_
- good look if you try to deviate from conventions :)

<!-- ---

## Hybrid automators

Create a *declarative infrastructure* upon an *imperative basis*, and
*allow easy access to the underlying machinery*

**Domain-Specific Languages** are helpful in this context: they can "hide" imperativity without ruling it out

Still, many challenges remain open:
* How to reuse the build logic?
    * within a project, and among projects -->

---

Many modern languages (such as Rust) come with a *build automator* as *part of their distribution*.

## In Python

Python is an *interpreted* language
* An arguably old one, too (1991)
* Initially used mainly for scripting
* No need to compile (as far as the project is pure Python)
* Build systems were a less pressing concerns than with other platforms...

The need for build systems in Python emerged with more complex use cases
* Since there were none, now there are several tools that do build-related jobs:

|  |   |   |   |
|---|---|---|---|
| [Anaconda](https://www.anaconda.com/)  | [Conda](https://docs.conda.io/en/latest/index.html) | [Miniconda](https://docs.conda.io/en/latest/miniconda.html) | [pip](https://pypi.org/project/pip/) |
| [Poetry](https://python-poetry.org/) | [PyBuilder](https://pybuilder.io/) | [PyEnv](https://github.com/pyenv/pyenv) | [virtualenv](https://virtualenv.pypa.io/en/latest/#) |
|  |   |   |   |

* The feature set varies wildly
* They are meant to solve different problems!

---

## Python's conflicting standards

![xkcd](https://imgs.xkcd.com/comics/python_environment.png)

Since there were no standard management systems originally,
multiple tools *proliferated*

* The Python Packaging Authority (PyPA) is inconsistent in its suggestions:
    * Recommends [`venv`](https://docs.python.org/3/library/venv.html)
    * Also recommends [Pipenv](https://pipenv.pypa.io/en/latest/) , which uses [`virtualenv`](https://virtualenv.pypa.io/en/latest/)
    * Also endorses [Poetry](https://python-poetry.org/)

* Many Python developers also exploit [PyEnv](https://github.com/pyenv/pyenv)

* Many data scientists use [Anaconda](https://www.anaconda.com/)

---

{{% section %}}

## What are all these tools? (pt. 1)

1. By default, Python is installed _system-wide_
    + i.e. there should be _one_ (and __only__ one) Python interpreter on the system

2. All Python installations come with `pip`, the _package installer_ for Python

3. So, one may __install__ Python packages _system-wide_ with `pip install PACKAGE_NAME`

> __One problem, many implications__: the same package can be installed _only once_ on the same Python installation
> + __(a)__ what if two projects on the same system require _different versions_ of the _same package_ as dependencies?
>     - say, __project A__ requires `Kivy==2.3` and __project B__ requires `Kivy==1.4`
> + __(b)__ what if two projects on the same system require _different versions of Python_?
>     - say, __project A__ requires Python `3.8` and __project B__ requires Python `3.10`

---

## What are all these tools? (pt. 2)

(consider reading this page for further details <https://stackoverflow.com/a/41573588>)

4. `virtualenv` and `venv` are tools to create _virtual_ Python installations _on the same system_
    + `virtualenv` is a _third-party_ tool, `venv` is _built-in_ in Python 3.3 and later
    + let's say you have Python `v. XXX` installed on your system... 
        - ... these tools let you create other _lightweight_ __copies__ of Python `v. XXX` in other folders
            * the copies are __fresh__, i.e. they _no package_ installed
            * but one may install _different_ packages in _each_ copy, via `pip`
    + now you can solve problem __(a)__

5. `PyEnv` is a tool to manage _multiple_ Python __installations__ _on the same system_
    + each installation may use a _different version_ of Python
    + now you can solve problem __(b)__


> __New problem__: many Python installations on the same system, 
> <br> each one with a different version of Python, and different packages installed 

recall all the issues we had in previous lectures?

--- 

## What are all these tools? (pt. 3)

6. Smart and adequate __convention__ to work with Python projects: __1-project-1-Python-env__
    + each Python project has its _own_ Python environment ...
        - be it virtual or not, as far as it uses the _same_ Python version required by that project
    + ... the environment _only_ contains the packages required by that project

7. Achieving this requires developers to be _disciplined_ and _meticulous_
    + other than being proficient with the tools above

8. `Poetry` is a tool that aims to _automate_ this process

{{% /section %}}

---

## From now on, let's use Poetry

> Poetry is a _declarative_ tool for __dependency management__, __packaging__, and __release__ in Python

- It handles both *dependencies* and *dev-dependencies* 
    * _replacing_ `requirements.txt` and `requirements-dev.txt`

- It _automates_ the __1-project-1-Python-env__ convention

- It simplifies the _packaging_ process for the project

- It simplifies the _publication_ process on PyPI (or other software repositories)

---

## Poetry's canonical project structure

```bash
root-directory/
├── main_package/
│   ├── __init__.py
│   ├── sub_module.py
│   └── sub_package/ 
│       ├── __init__.py 
│       └── sub_sub_module.py 
├── test/
│   ├── test_something.py
│   └── test_something_else.py/ 
├── pyproject.toml              # File where project configuration (metadata, dependencies, etc.) is stored
├── poetry.toml                 # File where Poetry configuration is stored
├── poetry.lock                 # File where Poetry locks the dependencies
└── README.md
```

Notice that, w.r.t. the canonical project structure we have been using so far:
  - the files `requirements.txt` and `requirements-dev.txt` are __not__ present any more
  - the files `pyproject.toml`, `poetry.toml`, and `poetry.lock` are __new entries__
  - the `poetry.lock` file is generated _automatically_ by Poetry, and you should not edit it

---

# Example (pt. 1)

## The [`calculator` repository](https://github.com/unibo-dtm-se/calculator)

1. Look at the [`pyproject.toml` file](https://github.com/unibo-dtm-se/calculator/blob/master/pyproject.toml)
    ```toml
    [tool.poetry]
    # name of the package to be published
    name = "unibo-dtm-se-calculator"

    # files to included for publication
    packages = [
        { include = "calculator" },
    ]

    # various metadata for publication
    version = "0.1.1"
    description = "A simple calculator toolkit written in Python, with several UIs. It is part of the Software Engineering course at the University of Bologna."
    authors = ["Giovanni Ciatto <giovanni.ciatto@unibo.it>"]
    license = "Apache 2.0"
    readme = "README.md"

    # dependencies (notice that Python is considered a dependency)
    [tool.poetry.dependencies]
    python = "^3.10.0"
    Kivy = "^2.3.0"

    # development dependencies
    [tool.poetry.group.dev.dependencies]
    poetry = "^1.7.0"
    pytest = "^8.1.0"
    coverage = "^7.4.0"
    mypy = "^1.9.0"

    # executable commands that will be created then installing this package
    [tool.poetry.scripts]
    calculator-gui = "calculator.ui.gui:start_app"
    calculator = "calculator.ui.cli:start_app"

    # where to download the dependencies from
    [[tool.poetry.source]]
    name = "PyPI"
    priority = "primary"

    # packaging dependencies
    [build-system]
    requires = ["poetry-core"]
    build-backend = "poetry.core.masonry.api"

    # mypy configuration
    [tool.mypy]
    ignore_missing_imports = true
    ```

    * learn how to specify dependencies here <https://python-poetry.org/docs/dependency-specification/>

---

# Example (pt. 2)

## The [`calculator` repository](https://github.com/unibo-dtm-se/calculator)

2. Look at the [`poetry.toml` file](https://github.com/unibo-dtm-se/calculator/blob/master/poetry.toml)

    ```toml
    # the project-specific environment will be created in the local .venv folder
    [virtualenvs]
    in-project = true 

    # packages produced by poetry may be published on the pypi-test repository
    [repositories.pypi-test]
    url = "https://test.pypi.org/legacy/"

    # another implicit repository is always available, namely PyPI
    # at https://pypi.org/
    ```

---

# Exercise (pt. 1)

## The [`calculator` repository](https://github.com/unibo-dtm-se/calculator)

1. Ensure you have Poetry installed on your system
    + <https://python-poetry.org/docs/#installing-with-the-official-installer>
    + run `poetry --version` to check

2. _Fork_ the repository  

3. _Clone_ the repository on your system
    + `git clone https://github.com/unibo-dtm-se/calculator.git`
    + then, open the `calculator` folder into VS code

4. Run `poetry install` in the terminal. This shall:
    - create a _virtual environment_ in the `.venv` directory
        + please ensure that a `.venv` directory __exists__ in your project directory, after running this command
    - _install_ the _dependencies_ declared in the `pyproject.toml` file
    - _lock_ the dependencies in the `poetry.lock` file

---

## Dependency ranges and locking

* A project can depend on a specific version of a library or on a *range* of versions
* We want to be able to specify ranges, but *retain the ability to use an exact version*

> This software is compatible with `library` version 2.3. For our examples, we used version 2.3._10_

Expressing something like this is done via **dependency locking**:
* Configure the build file with the range of supported versions
* Use the build tool to *lock* the dependencies (pinpoint their version)
  * In practice, create a lock file where the exact version is explicit
* Locking usually also locks the **transitive dependencies**!
  * Once locked, we have a snapshot of a working environment

[Poetry allows range specifications and locks automatically](https://python-poetry.org/docs/dependency-specification/)

---

# Exercise (pt. 2)

## The [`calculator` repository](https://github.com/unibo-dtm-se/calculator)

5. Let's use a shell in the virtual environment created by Poetry
    + run `poetry shell`
    + if this operation was fine, you should be able to run the command `calculator 1+1` to produce `2` as output
        + if you get an error, please let us know

6. Make sure that _VS Code_ is using the _same_ environment as the one created by Poetry.
    - Open the Command Palette (on <i class="fab fa-linux"></i>/<i class="fab fa-windows"></i> press <kbd>Ctrl</kbd>+<kbd>⇧</kbd>+<kbd>P</kbd>, use <kbd>⌘</kbd> instead of <kbd>Ctrl</kbd> on <i class="fab fa-apple"></i> )
    - Type `Python: Select Interpreter`
    - Choose the local environment, i.e. the one having path `./.venv/bin/python` 

7. This is an ordinary project, where you can operate _as usual_
    - run `python -m unittest discover -v -s tests` in the terminal
    - try to run tests in the UI, too

---

## Useful hints

1. So many Python environments in the shell... how to avoid mistakes?

    > If you want to be 100% you're running commands in the _right_ environment, you can prefix them with `poetry run`:
    > ```bash
    > poetry run python -m unittest discover -v -s tests
    > ```


2. Ok but what about VS Code's environments?
    
    > Get the habit of configuring the VS Code environment _manually_ when working with Python projects
---

# What's the value added of Poetry?

It supports publishing.

> Consider the following Web Page:
> <br> <https://pypi.org/project/unibo-dtm-se-calculator>

- This is the _PyPI_ page of the `unibo-dtm-se-calculator` package
    + which we published by means of Poetry

- After the project is made available on PyPI, it can be installed by anyone 
    + by running `pip install unibo-dtm-se-calculator`

---

# Exercise

## Installing a published package in a virgin environment

Let's first create a new Python environment, and then install the `unibo-dtm-se-calculator` package in it

1. Create a new Python environment (to simulate the _initially empty_ environment of a _new_ developer/user)
    1. open a fresh new terminal
    2. create the fresh new environment `python -m venv virgin-env`
    3. activate the environment 
      - on on <i class="fab fa-linux"></i>/<i class="fab fa-apple"></i> run `source virgin-env/bin/activate` 
      - on <i class="fab fa-windows"></i> use `.\virgin-env\Scripts\Activate`
    3. if you run commands `calculator` or `calculator-gui` they _should fail_

2. Install the `unibo-dtm-se-calculator` package `pip install unibo-dtm-se-calculator`

3. Try now to run the calculator in the shell
    + `calculator 1+1` should produce `2` as output
    + `calculao-gui` should open a GUI calculator

---

## How to publish Python packages on PyPI

### Prerequisites

- Have an account on [PyPI](https://pypi.org/)
     + generate an [API token](https://pypi.org/manage/account/) for your account

- Have an account on [Test-PyPI](https://test.pypi.org/)
    + generate an [API token](https://test.pypi.org/manage/account/) for your account

### Conceptual steps  

1. Publish on Test-Pypi, to ensure the procedure works

2. Publish on PyPI

3. Profit

---

## How to publish Python packages on Test-PyPI with Poetry

1. Build the project, i.e. produce *installable package* __(only do this after all Q/A checks pass)__
    * `poetry build`
    * this will create a `.whl` file and a `.tar.gz` file in the `dist/` directory

2. Upload installable packages on Test-PyPI
    * `poetry publish --repository pypi-test --username __token__ --password TEST_PYPI_API_TOKEN`
        + [the username is _literally_ `__token__`](https://pypi.org/help/#apitoken)
        + the password is the API token you generated on Test-PyPI
    * this will upload the package to Test-PyPI

3. That's it!
    * visit the page of your package on Test-PyPI
    * try to install it in a virgin environment via `pip install -i https://test.pypi.org/simple/ unibo-dtm-se-calculator`

---

## Problems that you may encounter

- Building may fail if your `pyproject.toml` is not properly configured, or missing data

- Upload may fail:
    + if your credentials are wrong, for some reason
    + if the package name is already taken
    + if the package version is already taken

- Installation may fail:
    + because your package has a dependency that is not available on Test-PyPI

---

## How to publish Python packages on PyPI with Poetry

1. Build the project, i.e. produce *installable package* __(only do this after all Q/A checks pass)__
    * `poetry build`
    * this will create a `.whl` file and a `.tar.gz` file in the `dist/` directory

2. Upload installable packages on PyPI
    * `poetry publish --repository pypi-test --username __token__ --password PYPI_API_TOKEN`
        + [the username is _literally_ `__token__`](https://pypi.org/help/#apitoken)
        + the password is the API token you generated on PyPI
    * this will upload the package to PyPI

3. That's it!
    * visit the page of your package on PyPI
    * try to install it in a virgin environment via `pip install unibo-dtm-se-calculator`

---

## Problems that you may encounter

- Building may fail if your `pyproject.toml` is not properly configured, or missing data
    + but you should already have fixed this when publishing on Test-PyPI

- Upload may fail:
    + if your credentials are wrong, for some reason
    + if the package name is already taken
    + if the package version is already taken

- Installation may fail, but in this case there must be an issue in the package itself

<!-- --- -->

<!-- ---

# Lessons learned

* Building a piece of software is not just writing code
* Software requires dependencies
* Dependency management is difficult
* All components of a runtime are part of the dependencies
  * Including interpreters
* Build Reproducibility is paramount
* Automatic configuration is desirable
* The Python build ecosystem is fragmented
  * Poetry is a modern take on Python dependency management and packaging
  * PyEnv can be used to let multiple Python versions live together -->
