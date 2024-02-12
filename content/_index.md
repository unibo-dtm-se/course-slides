 +++

title = "Software Engineering Module 3: Intro"
description = "Introduction to the course"
outputs = ["Reveal"]
aliases = [
    "/intro/"
]

+++

# Software Engineering
### **(for Intelligent Distributed Systems)**
# Module 3: DevOps

## *Introduction to the module*

---

# Teacher

**[Danilo Pianini](https://www.unibo.it/sitoweb/danilo.pianini/en)**, Senior assistant professor (RTDB)

**email** [danilo.pianini@unibo.it](mailto:danilo.pianini@unibo.it)

**office hours** dynamic, send me an email for an appointment

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

* **2h** [introduction to agile and DevOps, a case from the literature, SCRUM](devops-intro)
* **3h+3h** [decentralized version control (with git) and team organization](dvcs-basics)
* **2h** [QA, testing, TDD, reproducibility and replicability (examples in Python)](qa-tdd)
* **3h** [software dependencies, build automation (examples with virtualenv / pyenv / pip)](build)
* **3h** [Continuous integration (examples with GitHub Actions)](ci)
* **2h** [versioning, semantic release](https://danysk.github.io/course-laboratory-of-software-systems/05-version-selection), [licenses](https://danysk.github.io/course-laboratory-of-software-systems/06-licenses) (if we got time)

---

## Exam

Each student can freely pick *one module* and take the exam on that.

For module 3, the exam requires the production of either an essay or an actionable tool part,
followed by a discussion with the teacher.

* **Option 1**: **Essay**. The student produces a *paper* discussing an investigation/in-depth analysis of some argument of the course
    * *$\LaTeX$ or Markdown* format (Word / Google Docs and other WYSIWYG formats are not accepted)
    * Particularly well-done work could be considered for the submission of a *scientific publication*
    * Work requiring a "practical" investigation can be performed in groups (ideally, couples)
* **Option 2**: **Project/Demonstrator**. The student produces a *software component* leveraging and/or related to the topics of the module
    * if the effort is consistent, larger groups will be allowed (up to 4 students)
    * `git` will be used to verify the actual contribution of each student

---

## Exam

Whichever is the choice, *contact the teacher for a pre-validation **before** beginning the work*!

The two options could be *combined*, e.g.,
a group produces a new tool,
and another exploits in the essay.

* Should the result be so good that the essay qualifies as a candidate scientific paper,
the authors of the sofware will most likely be included as co-authors.

**PROPOSALS FROM STUDENTS ARE WELCOME!**

* If you have an idea, propose it as exam theme!
* I might amend it or suggest changes/strategies or set requirements

<!--

---

## Example proposal

#### Systematic literature review: the experience with Scrum

* *Type*: essay
* *Group size*: 1

This activity consists in a search in the literature for experience reports on the application/migration to Scrum.
The research activity must be systematic
(namely, the search rules for the papers should be formalized).
The student should devise metrics to evaluate the impact of the methodology under study when comparin across different reports.
The goal is trying to estimate how successful has been Scrum so far.

*Notes*:
* A similar project could be done for other frameworks

---

## Example proposal

#### An analysis of the prominence of GitHub in science and its fragility

* *Type*: essay (possibly mixed)
* *Group size*: 2

This activity consists in a search in the literature for references to GitHub repositories.
The research activity must be systematic
(namely, the search rules for the papers should be formalized).
Papers should classified per year (and theme, possibly),
then be searched for references to artifacts stored on GitHub.
The goals are to:
1. Understand if and how GitHub penetrated into the scientific literature with time
2. Verify how many such repositories are still reachable and maintained

*Notes*:
* It is likely that the investigation requires a software tool to be performed in human time
* Other DVCS hosting providers could be analyzes as well (gitlab, bitbucket...)

---

## Example proposal

#### Infrastructure as a service: state of the art in industry

* *Type*: essay
* *Group size*: 1

This activity consists in an analysis of the existing techniques and tools for Infrastructure as a Service (IaaS).
Information must be searched in the literature and on other sources, too.

*Notes*:
* It might include a demo

---

## Example proposal

#### An analysis of developer distress on social media

* *Type*: mixed
* *Group size*: 2-4

This activity consists in the analysis (via scraping / API) of social media posts that indicate developers' distress,
and on a classification of their origin.
Sources may include Twitter, Reddit, Stack Overlow, etc.

*Notes*:
* It might benefit of pre-existing skills in sentiment analysis

---

## Example proposal

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

## Example proposal

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

## Example proposal

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

## Example proposal

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

-->

