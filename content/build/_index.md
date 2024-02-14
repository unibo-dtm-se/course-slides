 +++

title = "Software dependencies, Build automation"
description = "Introduction to agile and DevOps, a case from the literature, SCRUM"
outputs = ["Reveal"]

+++

# Software dependencies, Build automation

{{% import path="reusable/header-dp.md" %}}

---

# The build "life cycle"
#### (Not to be confused with the system development life cycle (SDLC))

The process of creating *tested deployable software artifacts*
<br/>
from *source* code

May include, depending on the system specifics:
* *Source code manipulation* and generation
* Source code *quality assurance*
* *Dependency management*
* *Compilation*, linking
* *Binary manipulation*
* *Test execution*
* Test *quality assurance* (e.g., coverage)
* API *documentation*
* *Packaging*
* *Delivery*

---

# Lifecycle styles

* **Custom**: select some phases that the product needs and perform them.
    * *Flexible and configurable*: tailored on each project's needs
    * *Hard to adapt and port*

* **Standard**: run a sequence of pre-defined actions/phases.
    * *Portable and easy to understand*: replicated on every product
    * *Limited configuration options*

---

# Build automation

Automation of the build lifecycle

* In principle, the lifecycle could be executed manually
* In reality *time is precious* and *repetitivy is boring*

$\Rightarrow$ Create software that automates the building of some software!

* All those concerns that hold for sofware creation hold for build systems creation...

---

## Build automation: basics and styles

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
* *Configuration limited* by the provided options

---

## Hybrid automators

Create a *declarative infrastructure* upon an *imperative basis*, and
*allow easy access to the underlying machinery*

**Domain-Specific Languages** are helpful in this context: they can "hide" imperativity without ruling it out

Still, many challenges remain open:
* How to reuse the build logic?
    * within a project, and among projects

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

## A simple financial application

Build an application that performs a simple graphical MACD analysis of a financial product:

![app screenshot](app.png)

* How many Non-Comment Lines of Code (NCLoC)?

---

{{< mentimeter "12dc23978d6774050055d681b9cd72c9/ddac3c5150cf" >}}

---

## A possible solution

{{< github repo="python-finance-plot" path="macd.py" >}}

[about 45 NCLoC](https://github.com/DanySK/python-finance-plot)

---

## The trick: using a few libraries

* **yfinance**
    * Financial data from Yahoo! Finance
* **Pandas**
    * Data in tabular format
* **Pandas-TA**
    * Pandas technical analysis enhancement
* **PyQt5**
    * Graphical interface

---

## Actual dependency tree

```
matplotlib==3.5.1
  cycler==0.11.0
  fonttools==4.30.0
  kiwisolver==1.3.2
  numpy==1.22.3
  packaging==21.3
    pyparsing==3.0.7
  Pillow==9.0.1
  pyparsing==3.0.7
  python-dateutil==2.8.2
    six==1.16.0
pandas-ta==0.3.14b0
  pandas==1.4.1
    numpy==1.22.3
    python-dateutil==2.8.2
      six==1.16.0
    pytz==2021.3
PyQt5==5.15.6
  PyQt5-Qt5==5.15.2
  PyQt5-sip==12.9.1
yfinance==0.1.70
  lxml==4.8.0
  multitasking==0.0.10
  numpy==1.22.3
  pandas==1.4.1
    numpy==1.22.3
    python-dateutil==2.8.2
      six==1.16.0
    pytz==2021.3
  requests==2.27.1
    certifi==2021.10.8
    charset-normalizer==2.0.12
    idna==3.3
    urllib3==1.26.8
```

* 4 *direct* dependencies
* 21 *transitive* dependencies

In large projects, *transitive* dependencies often dominate

---


## Towards a **dependency hell**

* It's common for non-toy projects to get past 50 dependencies
* *Searching*, *downloading* and *verifying compatibility* by hand is unbearable
* **Version conflicts** arise soon
  * one of your direct dependencies uses library A at version 1
  * another uses library A at version 2
  * $\Rightarrow$  *transitive dependency conflict* on A
* **Upgrading** by hand requires, *time*, *effort* and *tons of testing*

---

## Dealing with dependencies

**Source import**

Duplication, more library code than business code, updates almost impossible, inconsistencies, unmaintainable

**Binary import**

Hard to update, [toxic for the Version Control System](https://bitbucket.org/danysk/exploded-repository-example)

**Desiderata**

* *Declarative* specification of libraries and versions
* *Automatic retrieval*
* Automatic *resolution of transitive dependencies*
* Dependency **scopes**
  * In general, you may need *compile-only*, *test-only*, and *runtime-only* dependencies
  * not specifically in Python and other interpreted languages
* Customizable software *sources*

---

## Reproducibility

We want that something that works *for us* works *for everyone*

We do not want to depend on the *system configuration*

We want to *declare* our requirements and have a **machine** figure out how to configure the system

We want everyone to be able to rebuild the *exact same environment*

---

## Python `pip`

[`pip`](https://pip.pypa.io/en/stable/) is the package installer for Python

By default, fetches packages on the [Python Package Index (PyPI)](https://pypi.org/)
* It is the *standard package repository for Python*

Pip is *shipped with most Python distributions*

---

## Using `pip`

* `pip install package_name`
    * Installs `package_name` *for the current user*
    * Running with `sudo` installs the packages *system-wide*
    * In any case, the installation is **global**
* `pip install -r requirements.txt`
    * Reads the contents of the provided *text file*
    * It flattens them and runs a normal `pip install`
    * The file name is arbitrary, but it is *customary* to use `requirements.txt`
        * (also helps with automation)

#### Example `requirements.txt`

{{< github repo="python-finance-plot" path="requirements.txt" >}}

---

## The problem with global installations

What if, for two different projects, you need *two different versions of the same library*?

* We need **isolated environments**!
* `pip` does not support them!

Workarounds, anyone?

---

## Virtualenv and venv

* Tell `pip` to *install* into a specific folder (e.g., `foo/bar`)
    * there exist an option in recent versions of `pip`: `--target=foo/bar`
* Tell `python` to *search* libraries in `foo/bar`
    * by default, the interpreter looks into the paths listed in the *environment variable* `PYTHONPATH`

**Cumbersome if done manually!**

`venv` and `virtualenv` deal with *isolation of multiple python library installations*

a.k.a. **virtual envelopes**

* `venv` is in the standard library
* `virtualenv` is not, but has some *additional features*
* They are *almost completely interchangeable*

---

## [`venv`](https://docs.python.org/3/library/venv.html)

* 1. Tell Python where to **initialize** the virtual environment:
  * `python3 -m venv /path/to/new/virtual/environment`
  * Commonly: `python3 -m venv .venv`
  * From Python 3.9, it can update `pip` with `--upgrade-deps`
  * inside the target folder, the script copies or symlinks the Python binaries

* 2. **Activate** the virtual environment
  * Bash/Zsh: `source .venv/bin/activate`
  * Powershell: `.venv\Scripts\Activate.ps1`
  * it [shims](https://stackoverflow.com/questions/2116142/what-is-a-shim) the terminal commands to run *inside the virtual envelop*

* 3. **Install** all your dependencies
  * `pip install -r requirements.txt`
* 4. Once done, **deactivate** the virtual environment
  * `deactivate`
  * The command is added upon activation and restores the "normal" shell behavior

---

## Exercise:

1. Create a new virtual environment, activate it, and deactivate it
2. From the `master` branch of the [finance-plot](https://github.com/DanySK/python-finance-plot) example,
run the application using the virtual environment, then deactivate it.

---

## Python's conflicting standards

![xkcd](https://imgs.xkcd.com/comics/python_environment.png)

Since there were no standard management systems originally,
multiple tools *proliferated*

* The Python Packaging Authority (PyPA) is inconsistent in its suggestions:
    * [Recommends `venv`](https://archive.ph/aNQGe)
    * Also [recommends Pipenv, which uses `virtualenv`](https://archive.ph/H2xeN)
    * Also [endorses Poetry](https://archive.ph/H2xeN)

---

## Interpreter as dependency

If you designed your software for Python 3.0, it might not work in Python 3.10
* indeed, it is very likely that if you designed it for Python 2.x it won't work in Python 3.x

In languages that require a runtime (Python, Javascript, Java...)
**the runtime is a dependency as well**!

And again: multiple projects may require *different versions*
* We need something to manage *multiple Python versions* on the *same system* at the *same time*
* How to port them across different installations?

---

## Pyenv

* Neither `venv` nor `virtualenv` deal perfectly with the interpreter isolation
* Ideally, we would like to write the interpreter version somewhere, and have it downloaded
* Additional tools exist for this scope, e.g., [`pyenv`](https://github.com/pyenv/pyenv)
    * Allows multiple installations of Python *per-user*
    * They are reused per-project
    * Controlled by a simple `.pythonversion` file in the project root

We still have consistency issues:
* `venv`/`virtualenv` do not isolate the *interpreter* versions
* `pyenv` does not create virtual envelopes *per-project*

We need these tools to communicate to achieve **per-project** *virtual envelopes with embedded python*
* A [plugin of pyenv](https://github.com/pyenv/pyenv-virtualenv) for using virtualenv exists
* ...but the situation is getting rather complicated...

---

## [Poetry](https://python-poetry.org/)

Integrated management of dependencies in Python
* Very *recent* (first release in 2018)
* *Declarative* configuration via [TOML](https://github.com/toml-lang/toml)
* Manages both the *interpreter* and the library *dependencies*
  * For the interpreter, it requires pyenv
* Simplifies *packaging*
* Relies on **convention over configuration**
  * Pre-configured overridable *sensible defaults*
  * or: if the project is *set up as expected*, then there is *almost no configuration* necessary

---

## Conventional directory structure

Library:

```
project-name
├── pyproject.toml
├── README.md
├── project_name
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_project_name.py
```

Module:

```
project-name
├── pyproject.toml
├── README.md
├── project_name.py
└── tests
    ├── __init__.py
    └── test_project_name.py
```

---

## Dependency ranges and locking

* A project can depend on a specific version of a library or on a *range* of versions
* We want to be able to specify ranges, but *retain the ability to use an exact version*

> This software is compatible with `library` version 2.x. For our examples, we used version 2.6.87

Expressing something like this is done via **dependency locking**:
* Configure the build file with the range of supported versions
* Use the build tool to *lock* the dependencies (pinpoint their version)
  * In practice, create a lock file where the exact version is explicit
* Locking usually also locks the **transitive dependencies**!
  * Once locked, we have a snapshot of a working environment

[Poetry allows range specifications and locks automatically](https://python-poetry.org/docs/dependency-specification/)

---

## Example configuration file

{{< github repo="python-finance-plot" path="pyproject.toml" branch="poetry" >}}

---

### Poetry: initialization

Poetry provides a built-in tool to initialize a repository
* `poetry new project-name`
  * Initializes the directory structure
  * Creates a stub TOML configuration
  * Alternatively, for existing projects, a `poetry init` interactive process is available for migration

---

### Poetry: virtual environments

Similar to `venv`, Poetry creates virtual environments (embedding the interpreter, too)
* `poetry shell`
  * activates the environment
  * the environment can be deactivated with `exit`
* `poetry env info`
  * prints information about the currently activated virtual environment
* `poetry env list`
  * lists all the virtual environments associated with the current project
* `poetry use` is the subcommand to determine which enviroment to use
  * `poetry use system` picks the python version from the `PATH`
  * `poetry use /path/to/python` selects an *existing* version of python

---

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
  * PyEnv can be used to let multiple Python versions live together
