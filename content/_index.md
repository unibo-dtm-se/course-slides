 +++

title = "Software Engineering, Module: 'Principles and Methods'"
description = "Introduction to the course"
outputs = ["Reveal"]
aliases = [
    "/intro/"
]

+++

{{% import path="reusable/header-course.md" %}}

---

# Teachers

## Module "Principles and Methods" 

**teacher:** {{<gc>}}, Junior assistant professor (RTD-A)

**email:** {{<gc-address>}}

<!-- **office hours** dynamic, send an email to the teacher for an appointment -->

## Module "Engineering of Distributed Systems and Enterprise Applications"

**teacher:** {{<ar>}}, Associate Professor

**email:** {{<ar-address>}}

## Remarks

**office hours** dynamic, send an email to the teachers for an appointment

Prof. {{<gc>}} is responsible for the course,
contact him for any aspect related to the course or the exam

---

## Virtuale

### {{<vle_url>}}  

Students _must_ enroll

- listen for announcements on the {{<forum_news>}}  
- ask for help or provide feeback on the {{<forum_general>}} 

---

## Organization

- __Tuesdays__ (_14:00-17:00_) in lab 4.2
    + you may use the PCs in the lab, or bring your laptops

- __Thursdays__ (_11:00-13:00_) in room 2.13
    + please, _bring your laptops_

- [Virtual room on Teams](https://teams.microsoft.com/l/meetup-join/19%3ameeting_MmM0ODExZDgtZGFjOS00YzU0LTk0MDQtMzdmZjU2Y2E0Nzg2%40thread.v2/0?context=%7b%22Tid%22%3a%22e99647dc-1b08-454a-bf8c-699181b389ab%22%2c%22Oid%22%3a%228bf5e0a6-9e33-4a87-9fa5-b9332620bedc%22%7d) is __just for the chat__
    + lectures will be held _in person_
    + __no__ blended lectures _by default_

> We will do our best follow the Italian convention "_quarto d'ora accademico_" 
> (i.e., starting 15 minutes after the scheduled time to allow people to accommodate)

+ please try to enter the room _on time_

---

## What is the course about? (pt. 1)

(Only insights here, there will be a [dedicated lecture](se-intro) on this topic)

- Put it simply, _software engineering_ is about __producing working software products__
    + not only writing code, but also 
        1. _understanding_ the _requirements_, 
        2. _designing_ the _product_, 
        3. _testing_ it, 
        4. _deploying_ it, 
        5. and _maintaining_ it

- In particular, nowadays, software engineering must also deal with:
    + __distribution__, i.e. multiple software components interconnected over the _Internet_
    + __artificial intelligence__, i.e. software components that may exhibit _human-like_ capabilities to some extent
        - e.g. understanding natural language, recognizing objects, making decisions, learning from data, etc. 

---

## What is the course about? (pt. 2)

- At the end of the course...
    + ... you shall have a clear understanding on the __whole process__ of software engineering
    + ... you should be able to _set up_ and _design_ a __software project__
    + ... you should be able to _reason_ about the __quality__ of a software project
    + ... you should have a clear understanding of brings __cost__ or __value__ in a software project
    + ... you will _not_ be required to be an __expert developer__

- To reach that goal, we shall follow a __learn-by-doing__ approach

---

## Exam (overview)

- The exam consists of a __project work__ to be _produced_ and _presented_ by students 

- The project work consists of 
    1. the _source code_ of a __software artifact__ and 
    2. a _textual report_ describing the __design__ and __development processes__ of the artifact itself

- The __report is more important than the source code__
    + the code could be a simple, pissibly incomplete, prototype or stub

- The project work can be done _individually_ or in _groups_ of __up to 4 students__
    + we _recommend_ doing it in _groups_, to practice with teamwork
    + individual contributions will be assessed via DVCS

- Students are encouraged to __propose__ project works themes/topics/concepts
    + we may help in refining initial proposals

- We incentivise students to _complete_ their project work __as soon as possible__ 
    + better if within _the next exam session_
    + possibly within _the same academic year_

---

## Exam (workflow)

1. **Proposal**: students _propose_ a project theme/topic/concept on {{<vle>}}
    - in case of group project, the group members should be _declared_ here

2. **Approval**: the teacher will provide feedback and possibly suggest changes/strategies or set requirements

3. **Repository creation**: students _create a GitHub repository_ and _share it_ with the teacher
    - granting _admin_ access to the teacher's GitHub account (username: [`gciatto`](https://github.com/gciatto))

4. **Development**: students _develop_ the software artifact and _write_ the report
    - the report should be written in [Markdown](https://www.markdownguide.org/) and stored in the repository (e.g. `README.md`)
    - the report should be written in _English_

5. **Submission**: students _submit_ the repository URL on {{<vle>}} and ask an _appointment_ for the discussion
    - submission is _not retractable_
    - appoitments may be scheduled in any moment of the academic year...
    - ... of course taking the teachers' availability into account

6. **Discussion**: students _present_ and _discuss_ their project work with the teacher
    - the discussion will be held _in English_
    - remote discussion may be possible via [Microsoft Teams](https://teams.microsoft.com/), in case of well-justified needs
    - the discussion will include _all the members_ of the group

---

## Exam (the software artifact)

> We don't really require you to be expert developers, nor to complete the development of a software artifact

- The software artifact can be a _simple_ prototype or stub, possibly _incomplete_
    + of course, completeness will be _rewarded_ 

- The software artifact can be developed in _any programming language_ of choice
    + we _recommend_ using __Python__

- The software arftifact is mostly aimed at demostrating students' _understanding_ of the many aspects of __software engineering__,
so that's what we will _mostly_ evaluate
    + e.g., analysing requirements, modelling a solution, designing interfaces, writing tests, managing dependencies, automating builds, tracking development, versioning, etc.

- Explotation of Git, GitHub, and version control is __important__ and will be evaluated

- Templates and guidelines for the source code will be provided on {{<vle>}}

---

## Exam (the report)

> The report is more important than the software artifact

- The report must be a document describing the __design__ and __development processes__ of the software artifact
    + possibly speculating on the aspects of development which have not been completed

- The report is the _entry point for evaluating_ the project work
    + it should detail _what has been done_ and _what has not been done_ (and _why_) ...
    + ... w.r.t. __all the aspects__ of __software engineering__ presented in the course

- Templates and guidelines for the report will be provided on {{<vle>}}

---

## Exam (the evaluation)

- Project work is _evaluated_ __once per group__
    1. an _overall mark_ is assigned to the project work, hence to the group
    2. _individual marks_ are then adjusted based on the __individual contributions__ to the project work

- Roughly speaking the evaluation of the project work will be based on the following aspects:
    + the _quality_ of the report and the presentation
    + the _precision_ of requirements elicitation and analysis
    + the _clarity_ of the design _documentation_
    + the _presence_ of tests and the _meaningfulness_ of the testing process
    + the _correct exploitation_ of 
        1. version control systems
        2. build automation systems
        3. continuous integration systems
    + the _adequate_ management of dependencies, versions, and licenses

- Extra points may be granted in case of (details on {{<vle>}}):
    + _early_ submission
    + _completeness_ of the software artifact
    + _quality_ of the software artifact

---

## Exam (examples of project works)

1. A web, mobile, or desktop __App__, possibly involving some _remote service_
    + e.g., a simple video game (involving online multiplayer) 
    + e.g., a calculator (involving a remote computation for advanced operations)
    + e.g., an instant messaging application
    + e.g., a note-taking, to-do list, calendar app (involving cloud storage)
    + e.g., a weather forecast (relying on pre-existing forecasting services)
    + e.g., a news aggregator (possibly scraping news from the web)
    <!-- + e.g., a social network client (possibily aggregating data from multiple sources) -->

2. A __startup__ _idea_, possibly involving some _remote service_
    + e.g., booking and managing appointments for professionals
    + e.g., general all-you-can-eat menus for restaurants
    + e.g., food delivery service
    + e.g., a platform for sharing and renting cars, bikes, rooms, etc.

3. A _toolkit_ supporting some (_data?_) __processing__ or __anlysis activity__ (with an _output_)
    + e.g., data analysis on social media, or GitHub
    + e.g., a tool for systematic literature reviews
    + e.g., a tool for automated document difference (possibly relying on third-party Web services)
    + e.g., a tool generating datasets via LLM

---

## Example proposal 1

#### An analysis of developer distress on social media 

* *Type*: mixed
* *Group size*: 2-4

This activity consists in the analysis (via scraping / API) of social media posts that indicate developers' distress,
and on a classification of their origin.
Sources may include Twitter, Reddit, Stack Overlow, etc.

*Notes*:
* It might benefit of pre-existing skills in sentiment analysis

---

## Example proposal 2

#### How are successful GitHub workflows organized?

* *Type*: mixed
* *Group size*: 2-4

This activity consists in the analysis (via API) of some interesting relationships that could be found on GitHub,
with the goal of investigating developer's habits and their evolution with time.

Some questions of interests may be:
* do the developer count relate to the branch count?
* do the presence of merge commits relate to the "success" of the project?

*Notes*:
* Identifying developers univocally may not be so easy
* More metrics could be devised
* Project success should be measured somehow but it is not trivial at all

---

## Example proposal 3

#### Private clouds with Kubernetes: a complete setup

* *Type*: project
* *Group size*: 1-2

This activity consists in the construction of a working private cloud based on Kubernetes.
Required features:
* Resilience to the loss of a master node (multi-master)
* Ability to run services (long-lived processes) or tasks (short-lived processes)
* Resource control and allocation via RBAC

*Notes*:
* Compute servers will be provided by the teacher
* Setup details should be collected into a guide
* Previous experience with Kubernetes and containerization is helpful

---

## Example proposal 4

#### Automated document difference

* *Type*: project
* *Group size*: 1-2

The goal of this project is to build a library leveraging the web API of [Draftable](https://draftable.com/)
to produce differential documents.
The software can be developed in any language of choice,
and must feature appropriate automation (build) and get published on official distribution channels.

The library should be exercised with a GitHub action.

*Notes*:
* The API key for the Draftable service will be provided by the teacher
* The language should be agreed with the teacher
    * Python, Java, Scala, Kotlin, Rust, and Ruby are all valid picks, other should be discussed

---

## Example proposal 5

#### A tool to support systematic literature reviews

* *Type*: project
* *Group size*: 1-2

The goal of this project is to build a software that queries multiple sources in the literature
(Google Scholar, Pubmed, Scopus, Web of Science, Arxiv...)
with a specific query, supporting the scientific investigation of existing results.
The software can be developed in any language of choice,
and must feature appropriate automation (build) and get published on official distribution channels.

*Notes*:
* The language should be agreed with the teacher
    * Python, Java, Scala, Kotlin, Rust, and Ruby are all valid picks, other should be discussed

---

## Techical Requirements

- An account on [GitHub](https://github.com) (create one if missing)
    + possibly, __based on your university email address__
        * if you already have a GitHub account, please add it as the secondary email address 
    + optionally, __with a profile picture__ showing your face or a recognizable avatar
    + possibly, with a __professional username__ (e.g., `john-doe` instead of `johnny-the-king`)

- A working installation of [Python](https://www.python.org/)
    + possibly version `3.11.x`

- A working installation of [Git](https://git-scm.com/)
    + if you need a GUI, you may choose 
        1. [GitHub Desktop](https://desktop.github.com/) 
        2. [SourceTree](https://www.sourcetreeapp.com/)
        3. [GitKraken](https://www.gitkraken.com/)

- A working installation of [Visual Studio Code](https://code.visualstudio.com/)

- \[Recommended\] A working installation of [PyCharm](https://www.jetbrains.com/pycharm/)
    + the community edition is free, and it's enough

--- 

# Module "Principles and Methods"

held by Prof. {{<gc>}}

### Remarks

- Lectures are recorded by default
    + recordings will be available on {{<vle>}}
    + access to recordings is by-request only (send an email to the teacher)

- Slides and other materials are available on {{<vle>}}
    + they are produced along the way, so they may not be available in advance
    + also, please re-download / re-load them before each class

---

# Module contents and action plan

<!--
2-3-3-2-3-3-2?
2022-04-05 - 2h intro
2022-04-06 - 3h git1
2022-04-20 - 3h git2
2022-05-03 - 2h tdd-qa
2022-05-04 - 3h build
2022-05-11 - 3h ci
2022-05-17 - 2h ?
2022-05-18 - 3h ?
-->
(order of lectures is __not final__)

1. [Introduction to software engineering](se-intro)
2. [Preliminary notions for Software Development](preliminaries)
0. [Decentralized version control (with git) and team organization](dvcs-basics)
0. [Object oriented programming (in Python)](oop)
0. [QA, testing, TDD, reproducibility and replicability (examples in Python)](qa-tdd)
0. [Build automation, packaging, and release (examples with Poetry)](build)
0. [Versioning, Conventional Commit](versioning)
0. [Continuous integration (examples with GitHub Actions)](ci)
0. [Licensing](https://unibo-spe.github.io/06-licenses/)

## Extras

- [Introduction to agile and DevOps, a case from the literature, SCRUM](devops-intro)