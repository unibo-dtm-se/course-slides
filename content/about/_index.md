 +++

title = "About the course: 'Software Engineering'"
description = "Introduction to the course"
outputs = ["Reveal"]
aliases = [
    "/about/"
]

+++

# About the course

{{% import path="reusable/header.md" %}}

---

## Teacher

- **teacher:** {{<gc>}}, Junior assistant professor (RTD-A)

- **email:** {{<gc-address>}}

- **home page**: https://www.unibo.it/sitoweb/giovanni.ciatto/en

- **office hours:** dynamic, send an email to the teacher for an appointment

---

## Virtuale

### {{<vle_url>}}  

Students _must_ enroll

- listen for announcements on the {{<forum_news>}}  
- ask for help or provide feeback on the {{<forum_general>}} 

---

## Organization

- __Tuesdays__ (_14:30-17:30_) in lab 4.2
    + you may use the PCs in the lab, or bring your laptops

- __Thursdays__ (_11:00-13:00_) in lab 3.1
    + you may use the PCs in the lab, or bring your laptops

- {{< virtual_room >}} is __just for the chat__
    + lectures will be held _in person_
    + __no__ blended lectures _by default_

> I will do my best follow the Italian convention "_quarto d'ora accademico_" 
> <br> (i.e., starting _15 minutes after_ the scheduled time to allow people to accommodate)

+ please try to enter the room _on time_

---

## What is the course about? (pt. 1)

(Only insights here, there will be a [dedicated lecture](../se-intro) on this topic)

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

- The exam consists of: __written test__ and a (_optionally_) a __project work__
    + the written test is _mandatory_ and the maximum score is `27/30`
    + the project work is _optional_ and the maximum score is `6/30`
        * students can choose to _skip_ this part, but they will _not_ be able to reach the maximum score (`30/30`)
    + the final score is the __sum__ of the two scores, __capped to `30/30`__

- The rationale is as follows:
    1. the written test is aimed at _assessing_ the __theoretical__ knowledge of the student
    2. the project work is aimed at _assessing_ the __practical__ knowledge of the student

- The __written test__ consists of a _closed-book_ exam with _open-ended_ questions
    + exam is _in presence_, with _no internet connection_, and with a _time limit_
    + there will be _6 opportunities_ to take the exam along the year, roughly _4 in the summer_ session and _2 in the winter_ session
    
- The __project work__ consists of an _individual_ or _group_ effort where
    1. the student(s) develop a _software artifact_ and write a _report_ on the development process
    2. and finally they will _present_ and _discuss_ the project work with the teacher in an _oral_ discussion
        * the _oral_ discussion will be held _upon appointment_ with the teacher, possibly _remotely_

<!-- - In the project work __report is more important than the source code__
    + the code could be a simple, pissibly incomplete, prototype or stub

- The project work can be done _individually_ or in _groups_ of __up to 4 students__
    + we _recommend_ doing it in _groups_, to practice with teamwork
    + individual contributions will be assessed via DVCS

- Students are encouraged to __propose__ project works themes/topics/concepts
    + we may help in refining initial proposals

- We incentivise students to _complete_ their project work __as soon as possible__ 
    + better if within _the next exam session_
    + possibly within _the same academic year_ -->

---

## Details about the __written test__ (pt. 1)

- There will be __6 calls__ for the written tests along the academic year
    + roughly in June, July, August, September, January, and February

- The exact _dates_ and _locations_ of the exams will be made available on [AlmaEsami](https://almaesami.unibo.it), where you will be able to _register_ for exam calls
    + registration is _strictly necessary_ for participation (no registration, no exam)
    + dates are __not negotiable__, so please plan your presence accordingly
    + the amount of seats for each exam call is __limited__ (by the capacity of the room)
        * so, please register to the exam call _only if_ you are _sure_ you will attend

- The written test will be _in presence_, __no exception__
    + if you are not available for one of the exam calls, you will have to wait for the next one

- The written test should be conducted on the University's __computers__, but may fall back on __paper__ in case of technical issues
    + the day of the exam you __must__ bring:
        1. your __ID card__ or __passport__ to prove your identity
        2. a __pen__ (possibly black or blue)

---

## Details about the __written test__ (pt. 2)

- The written test is _closed-book_, with _open-ended_ questions
    + any attempt to cheat will result in the __immediate failure__ of the exam

- The teacher will provide the list of _possible questions_ in advance
    + the exam will consist of a _random selection_ of them
    + expect 1-2 potential questions _for each topic_ of the course

- During the exam, you will be subject to the following __restrictions__:
    * no _communication_ with other people, no _internet_ connection, no _phone_ usage, no access to _notes_ or _books_
    * no _leaving_ the room before the end of the exam
    * you can __renounce__ to the exam at any time (implies that your test will _not_ be evaluated)

- Results will be available on [AlmaEsami](https://almaesami.unibo.it) within a _few days_ from the exam
    + in case of _failure_ or _unsatisfying results_, you will be able to __retry__ in the next call
    + _concluding_ the test _without renouncing_ implies that any prior exam result will be __overwritten__

- Students should _inform_ the teacher of any __provable__ _special needs_ or _disabilities_ that may require _special arrangements_ for the exam
    + please don't do this at the last moment

- Upon reaching a successful result ($\geq$ `18/30`), it is up the student to:
    1. _inform_ the teacher that they intend to _skip_ the project work and _accept_ the result, hence __finalizing__ the exam
    2. or just _keep working_ on the project work, hence __postponing__ the finalization of the exam

---

## Details about the __project work__

- The project work is _optional_, but it is _strongly recommended_
    + it is a _great opportunity_ to _apply_ the concepts learned during the course
    + it is a _great opportunity_ to _practice_ with _teamwork_

- The project work can be done either _individually_ or in _groups_ of __up to 3 students__
    + groups shall be _declared_ on {{<vle>}} by the students _before_ starting the project work
    + the groups shall be _stable_ and _unchangeable_ during the project work
        + group member __cannot__ be _added/removed_ after the group's project idea has been _approved_
    + the members of the group shall present their project work _together_

- The evaluation of the project work will focus _not only_ on the _outcome_ (the software artifact) but also on the _process_ (the report)
    + the software artifact can be small and simple...
    + ... yet the report should describe _all the aspects_ of the _software engineering_ process presented in the course
    + the report should be written in _English_

---

## Project work's activity flow

(Starting after passing the written test is _recommended_ by not _mandatory_)

1. **Proposal**: students _propose_ a project theme/topic/concept on the {{<forum_projects>}}
    - in case of group project, the group members should be _declared_ here (names + __emails__)

2. **Approval**: the teacher may provide feedback, suggest changes/strategies, or set requirements, and eventually _approve_ the proposal

3. **Repositories creation**: students _create a GitHub organization_ and _grant the teacher access_ to it
    - granting _admin_ access to the teacher's GitHub account (username: [`gciatto`](https://github.com/gciatto))
    - the organization should be named `unibo-dtm-se-2425-YOUR_PROJECT_NAME`
    - the organization should contain (at least) _one repository_ for the software artifact and _another_ for the report

4. **Development**: students _develop_ the software artifact and _write_ the report
    - the report should be written in [Markdown](https://www.markdownguide.org/) and match [this template](https://github.com/unibo-dtm-se/template-project-work)
    - the report should be written in _English_

5. **Submission**: students _submit_ their GitHub organization URL on the {{<forum_projects>}} and ask an _appointment_ for the discussion
    - submission is _not retractable_
    - appointments may be scheduled in any moment of the academic year...
    - ... of course taking the teachers' availability into account

6. **Discussion**: students _present_ and _discuss_ their project work with the teacher
    - the discussion will be held _in English_
    - remote discussion may be possible via [Microsoft Teams](https://teams.microsoft.com/), in case of well-justified needs
    - the discussion will include _all the members_ of the group

---

## Details about the __software artifact__

> If you decide to do the project work, you will have to _develop_ a _software artifact_ to prove your capability to carry out a software project

- The software to be developed can range from _simple_ to _complex_, depending on your familiarity with development
    + proposing an idea that you're able to _complete_ is part of the game
        * so do not over-promise!

- Simple or complex, the point of the software artifact is to _demonstrate_ your _understanding_ of the _software engineering_ process
    + so, you should _encompass_ and _document_ all the _phases_ of the _software development_ process
        * e.g. the _requirements analysis_, the _design_, the _implementation_, the _testing_, the _deployment_, and the _maintenance_ of the software artifact

- The software artifact can be developed in _any programming language_ of choice
    + we _recommend_ using __Python__

- Exploitation of _Git_, _GitHub_, and version control is __important__ and will be evaluated

- Templates and guidelines for the source code will be provided on the [GitHub organization](https://github.com/unibo-dtm-se) of the course

---

## Details about the software artifact's __report__ (pt. 1)

> The _report_ (documenting the process) is _as important as_ the code it describes (the outcome)

- The report must be a document describing the __design__ and __development processes__ of the software artifact
    + possibly speculating on the aspects of development which have not been completed

- The report is the _entry point for evaluating_ the project work
    + it should detail _what has been done_ and _what has not been done_ (and _why_) ...
    + ... w.r.t. __all the aspects__ of __software engineering__ presented in the course

- Technically speaking, the report should be written in _Markdown_ and should match [this template](https://github.com/unibo-dtm-se/template-project-work)
    + so that it can be rendered as a static Web page, via [GitHub Pages](https://pages.github.com/) (example [here](https://unibo-dtm-se.github.io/template-project-work/))

---

## Details about the software artifact's __report__ (pt. 2)

### Recommended Table of Contents

0. __Title__ + __Authors List__ + __Abstract__
0. [opt] __Disclaimers__ (e.g., conflicts of interests, usage of AI, etc.)
0. __Concept__: short description of the idea behind the software being developed
0. __Requirements__: requirements + user stories + use cases + acceptance criteria
0. __Design__: overall architecture, structure, interaction, behaviour, etc.
0. __Development__: conventions on the usage of DVCS, other relevant implementation details
0. __Validation__: description of the testing activities, including unit tests, integration tests, etc.
0. __Release__: how to build, package, and release the software + details about licenses
0. __Deployment__: how to deploy the software and/or how to install and run it
0. __CI/CD__: description of the CI/CD pipelines, if any
0. __User guide__: how to use the software
0. __Developer guide__: how to contribute to the software
0. __Self-evaluation__: what went well, what went wrong, what could be improved (_1 section per group member_)
0. __Future works__: what could be done in the future to improve the software 

---

## Scoring and Grading

- The _written test_ is _evaluated_ __numerically__, after the written test is over:
    * each question is assigned a _maximum score_
    * each student's answers is given a score from `0` to the maximum
    * the _resulting score_ is the _sum_ of the scores of all the answers, __normalized to `27`__

- Project work is _evaluated_ __once per group__
    1. an _overall score_ is assigned to the project work, hence to the group
    2. _individual score_ are then adjusted based on the __individual contributions__ to the project work
    3. each _individual score_ is then __normalized to `6`__

- Assessing a __software project__ is _not trivial_, and _subjectivity_ is _unavoidable_
    + the teacher will do his best to be _fair_ and _consistent_
    + the teacher will provide _feedback_ on the project work, and _justify_ the assigned score
    + to make the process as _fair and transparent_ as possible, here's a [check-list of technical aspects the teacher will consider](https://github.com/unibo-dtm-se/resources/blob/main/project-work-checklist.md)

- The _final score_ is the __sum__ of the _normalized_ scores of the _written test_ and the _project work_
    + as the _maximum_ final score is `33/30`, the _final mark_ is _capped_ to `30/30`
    + if _no_ project work is done, and the _maximum final mark_ is `27/30`
    + if the project work is _perfect_ (i.e., `6/6`), _any_ written test score $\geq$ `24/30` will result in a _final mark_ of `30/30`
    + the final mark `30L` (_cum laude_) is assigned when the _final mark_ (before capping) is __above__ `30/30`

---

## Technical Requirements

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

- \[Useful\] A working installation of [PyCharm](https://www.jetbrains.com/pycharm/)
    + the community edition is free, and it's enough

--- 

## About recordings

- Lectures are __recorded by default__
    + recordings will be available on {{<vle>}}, in the __Panopto__ section

- During the course, access to __recordings__ is by-request only (send an email to the teacher)
    + only _well motivated_ requests will be accepted (health issues, family issues, transport issues, etc.)

- At the _end of the course_, the recordings will be __made available to all students__

- Recordings are _not_ a _substitute_ for _attending_ the _lectures_
    + they are a _complementary_ tool to _support_ the _learning_ process

- Recordings will be made following a __best-effort__ approach 
    + technical issues may arise, and some lectures may not be recorded
    + recordings may be incomplete, or contain defects

---

## About the slides

- Slides and other materials are available on {{<vle>}} and [GitHub]({{< slides-url >}})
    + they are produced along the way, so they may not be available in advance, or change abruptly overnight
    + also, please re-download / re-load them before each class

- The [online version of the slides]({{< slides-url >}}) is _updated automatically_
    + you will always see the latest version when you load the page

- If you need to _print_ the slides, please use the _printable version_ of the slides, which is commonly available in the _first slide_ of each lecture
    + pre-cooked PDFs are available on at <https://github.com/unibo-dtm-se/course-slides/releases/latest>

---

## About the exploitation of Generative AI in the course

- If you use __Generative AI__ tool (e.g. ChatGPT, Copilot, etc.) in writing your _code_ or _report_, this is __fine__ 
    * notice that as UniBo students, you may request a _free_ license to GitHub Pro, which includes GitHub Copilot, at <https://education.github.com/pack>

- But you __must__ be _transparent_ about _what_ AI tool you used and _why_ 
    * you _must_ declare that by means of a __disclaimer__ at the beginning of your report, e.g.:

        ```text
        “During the preparation of this work the author(s) used [NAME TOOL / SERVICE] in order to [REASON]. 
        After using this tool/service, 
        the author(s) reviewed and edited the content as needed 
        and take(s) full responsibility for the content of the final report/artifact.” 
        ```

- If the disclaimer is _not present_ in your report, this will be interpreted as __"no Generative AI was used at all"__

> If I have the impression that some student has _blindly copy-pasted_ content (from either AI chat, or the slides, or some book) _without understanding it_, I will set up an _oral examination_ and ask _further questions_ to investigate whether the student has actually understood what they wrote or not

---

{{% import path="reusable/back.md" %}}