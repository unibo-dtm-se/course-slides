+++

title = "Distributed version control basics"
description = "Distributed version control systems, basics of Git"
outputs = ["Reveal"]

+++

# Distributed version control basics

{{% import path="reusable/header-dp.md" %}}

---

# Version control

---

## Tracking changes

Did you ever need to *roll back* some project or assignment to a previous version?

How did you track the *history* of the project?

### Classic way

1. find a naming convention for files/folders
2. make a copy every time there is some relevant progress
3. make a copy every time an ambitious but risky development begins

**Inefficient!**
* Consumes a lot of resources
* Requires time
* How to tell what was in some previous releases?
* How to cherry-pick some changes?

---

## Fostering collaborative workflows

Did you ever need to develop some project or assignment *as a team*?

How did you organize the work to *maximize the productivity*?

### Classic ways

* *One screen, many heads*
  * a.k.a. one works, the other ones sleep
* *Locks*: "please do not touch section 2, I'm working on that"
  * probability of arising conflicts close to 100%
* *Realtime-sharing* (like google docs or overleaf)
  * okay in many cases for text documents (but with a risk of frankestein-ization)
  * disruptive with code (inconsistencies are much less tolerable in formal languages)

---

## Version control systems

Tools meant to support the development of projects by:
* Tracking the project *history*
* Allowing *roll-backs*
* Collecting *meta-information* on the changes
  * Authors, dates, notes...
* *Merging* information produced at different stages
* (in some cases) *facilitate parallel workflows*
* Also called Source Content Management (SCM)

**Distributed**: *Every copy* of the repository contains
(i.e., every developer locally have)
*the entire history*.

**Centralized**: A *reference copy* of the repository contains the whole history;
developers work on a subset of such history


---

## Short history

* **Concurrent Versioning System (CVS)** (1986): client-server (*centralized* model, the truth is on the server), operates on single files or repository-level, history stored in a hidden directory, uses delta compression to save space.
* **Apache Subversion (SVN)** (2000): successor to CVS, still largely used (especially in businesses that struggle to renovate their processes). *Centralized* model (similar to CVS). Improved binary file management. Improved concurrency for the operation, still cumbersome for parallel workflows.
* **Mercurial** and **Git** (both April 2005): *decentralized* version control systems (DVCSs), no "special" copy of the repository, each client stores the whole history. Highly scalable. Foster parallel work by allowing easy branching and merging. Very similar conceptually (when two succesful tools emerge at the same time with a similar model independently, it is an indication that the underlying model is "the right one" for the context).

**Git** is now the dominant DVCS (although Mercurial is still in use, e.g., for Python, Java, Facebook).

---

## Google trends to today

<!-- write-here "shared-slides/git/git-trends.md" -->

<!-- end-write -->

---

## Intuition: the history of a project

1. Create a new project
```mermaid
%%{init: { 'gitGraph': { 'showBranches': false }} }%%
gitGraph
  commit id: "Initialize project"
```

---

2. Make some changes

```mermaid
%%{init: { 'gitGraph': { 'showBranches': false }} }%%
gitGraph
  commit id: "Initialize project"
  commit id: "Make some changes"
```

---

3. Then more and more, until the project is ready

```mermaid
%%{init: { 'gitGraph': { 'showBranches': false }} }%%
gitGraph
  commit id: "Initialize project"
  commit id: "Make some changes"
  commit id: "Make more changes"
  commit id: "It's finished!" type: HIGHLIGHT
```

At a first glance, the history of a project *looks like* a **line**.

---

## Except that, in the real world...

> Anything that can go wrong will go wrong
> <br><cite>$1^{st}$ Murphy's law</cite>

> If anything simply cannot go wrong, it will anyway
> <cite>$5^{th}$ Murphy's law</cite>

---

# ...things go wrong

```mermaid
%%{init: { 'gitGraph': { 'showBranches': false }} }%%
gitGraph
  commit id: "Initialize project"
  commit id: "Make some changes"
  commit id: "Make more changes"
  commit id: "It's *not* finished! :(" type: REVERSE tag: "fail"
```

---

## Rolling back changes

Go *back in time* to a previous state where things work

```mermaid
%%{init: { 'gitGraph': { 'showBranches': false }} }%%
gitGraph
  commit id: "init"
  commit id: "okay" type: HIGHLIGHT
  commit id: "error" type: REVERSE
  commit id: "reject" type: REVERSE
```

---

## Get the previous version and fix

Then fix the mistake

```mermaid
%%{init: { 'gitGraph': { 'mainBranchName': 'master' }} }%%
gitGraph
  commit id: "init"
  commit id: "okay"
  branch fix-issue
  checkout master
  commit id: "error" type: REVERSE
  commit id: "reject" type: REVERSE
  checkout fix-issue
  commit id: "improve"
  commit id: "finished" type: HIGHLIGHT
```

If you consider rollbacks, history is a **tree**!

---

# Collaboration: diverging

Alice and Bob work together for some time, then they go home and work separately, in parallel

They have a *diverging history*!

```mermaid
%%{init: { 'gitGraph': { 'mainBranchName': 'alice'}} }%%
gitGraph
  commit id: "together-1"
  commit id: "together-2"
  commit id: "together-3"
  branch bob
  commit id: "bob-4"
  checkout alice
  commit id: "alice-4"
  checkout bob
  commit id: "bob-5"
  checkout alice
  commit id: "alice-5"
  checkout bob
  commit id: "bob-6"
  checkout alice
  commit id: "alice-6"
```

---

# Collaboration: reconciling

```mermaid
%%{init: { 'gitGraph': { 'mainBranchName': 'alice'}} }%%
gitGraph
  commit id: "together-1"
  commit id: "together-2"
  commit id: "together-3"
  branch bob
  commit id: "bob-4"
  checkout alice
  commit id: "alice-4"
  checkout bob
  commit id: "bob-5"
  checkout alice
  commit id: "alice-5"
  checkout bob
  commit id: "bob-6"
  checkout alice
  commit id: "alice-6"
  merge bob tag: "reconciled!"
  commit id: "together-7"
```

If you have the possibility to *reconcile diverging developments*, the history becomes a **graph**!

Reconciling diverging developments is usually referred to as **merge**

---

## DVCS concepts and terminology: *Repository*

Project **meta-data**. Includes the whole project history
* information on how to *roll back* changes 
* *authors* of changes
* *dates*
* *differences* between different points in time
* and so on

Usually, stored in a hidden folder in the *root folder* of the project

---

## DVCS concepts and terminology: *Working Tree*

(or *worktree*, or *working directory*)

the collection of **files** (usually, inside a *root folder*) that constitute the project,
excluding the *meta-data*.

---

## DVCS concepts and terminology: *Commit*

A **saved status** of the project.
* Collects the *changes* required to transform the previous (*parent*) commit into the current (*differential tracking*)
* Creates a *snapshot* of the status of the worktree (snapshotting).
* Records metadata: *parent commit*, *author*, *date*, a *message* summarizing the changes, and a *unique identifier*.
* A commit with no parent is an *initial commit*.
* A commit with multiple parents is a *merge commit*.

```mermaid
%%{init: { 'gitGraph': { 'mainBranchName': 'alice'}} }%%
gitGraph
  commit tag: "initial"
  commit
  commit
  branch bob
  commit
  checkout alice
  commit
  checkout bob
  commit
  checkout alice
  commit
  checkout bob
  commit
  checkout alice
  commit
  merge bob tag: "merge"
  commit
```

---

## DVCS concepts and terminology: *Branch*

A **named sequence of commits**

```mermaid
%%{init: { 'gitGraph': { 'mainBranchName': 'default-branch'}} }%%
gitGraph
  commit
  commit
  commit
  branch branch2
  commit
  checkout default-branch
  commit
  checkout branch2
  branch branch3
  commit
  checkout default-branch
  branch branch4
  commit
  commit
  commit
  commit
  checkout branch3
  merge branch4
  commit
  commit
  commit
  checkout default-branch
  merge branch3
  checkout branch2
  commit
  commit
  merge default-branch
```

If no branch has been created at the first commit, a default name is used.

---

## DVCS concepts and terminology: *Commit references*

To be able to go *back in time* or *change branch*, we need to **refer to commits**
* Commit references are also referred to as `tree-ish`es
* Every commit has a **unique identifier**, which is a valid reference
* A **branch name** is a valid commit reference (points to the *last commit of that branch*)

```mermaid
  %%{init: { 'gitGraph': { 'mainBranchName': 'bname', 'showCommitLabel': true}} }%%
  gitGraph
    commit
    commit
    commit
    commit
    commit
    commit
    commit
    commit tag: "bname" type: HIGHLIGHT
  ```

---

## DVCS concepts and terminology: *the head reference* (pt. 1)

### A special commit name is  `HEAD`, which refers to the *current commit*

When _committing_, the `HEAD` moves *forward* to the new commit:

1. Before commit
  ```mermaid
  %%{init: { 'gitGraph': { 'mainBranchName': 'branch', 'showCommitLabel': true}} }%%
  gitGraph
    commit id: "1"
    commit id: "2"
    commit id: "3"
    commit id: "4"
    commit id: "5"
    commit id: "6"
    commit id: "7"
    commit id: "8"
    commit id: "9" tag: "HEAD"  type: HIGHLIGHT
  ```

2. After commit
  ```mermaid
  %%{init: { 'gitGraph': { 'mainBranchName': 'branch', 'showCommitLabel': true}} }%%
  gitGraph
    commit id: "1"
    commit id: "2"
    commit id: "3"
    commit id: "4"
    commit id: "5"
    commit id: "6"
    commit id: "7"
    commit id: "8"
    commit id: "9"
    commit id: "10" tag: "HEAD"  type: HIGHLIGHT
  ```

---

## DVCS concepts and terminology: *the head reference* (pt. 2)

### A special commit name is  `HEAD`, which refers to the *current commit*

When *checking out* some *previous* commit, the `HEAD` moves backward that commit:

1. After checking out commit `5`
  ```mermaid
  %%{init: { 'gitGraph': { 'mainBranchName': 'branch', 'showCommitLabel': true}} }%%
  gitGraph
    commit id: "1"
    commit id: "2"
    commit id: "3"
    commit id: "4"
    commit id: "5"  tag: "HEAD"  type: HIGHLIGHT
    commit id: "6"
    commit id: "7"
    commit id: "8"
    commit id: "9"
    commit id: "10" tag: "branch"
  ```

  + notice that the branch name keeps poiting to the *last* commit

---

## Absolute and relative references

Appending `~` and a number `i` to a valid tree-ish means "`i-th` parent of this tree-ish"

- this can be exploited w.r.t. the `HEAD` commit...

  ```mermaid
  %%{init: { 'gitGraph': { 'mainBranchName': 'branch', 'showCommitLabel': true}} }%%
  gitGraph
    commit id: "1" tag: "HEAD~7"
    commit id: "2" tag: "HEAD~6"
    commit id: "3" tag: "HEAD~5"
    commit id: "4" tag: "HEAD~4"
    commit id: "5" tag: "HEAD~3"
    commit id: "6" tag: "HEAD~2"
    commit id: "7" tag: "HEAD~1"
    commit id: "8" tag: "HEAD" type: HIGHLIGHT
    commit id: "9"
    commit id: "10"
  ```

- ... or w.r.t. any other reference commit

  ```mermaid
  %%{init: { 'gitGraph': { 'mainBranchName': 'branch', 'showCommitLabel': true}} }%%
  gitGraph
    commit id: "c1" tag: "c4~3"
    commit id: "c2" tag: "c4~2"
    commit id: "c3" tag: "c4~1"
    commit id: "c4" type: HIGHLIGHT
    commit id: "c5"
    commit id: "c6" tag: "c10~5"
    commit id: "c7" tag: "c10~3"
    commit id: "c8" tag: "c10~2"
    commit id: "c9" tag: "c10~1"
    commit id: "c10" type: HIGHLIGHT
  ```

---

## DVCS concepts and terminology: *Checkout*

The operation of **moving to another commit**
* Moving to *another branch*
* Moving *back in time*

Moves the `HEAD` to the specified *target tree-ish*

---

## Project evolution example

Let us try to see what happens when ve develop some project, step by step.

---

1. first commit

```mermaid
%%{init: { 'gitGraph': { 'mainBranchName': 'default-branch', 'showCommitLabel': true}} }%%
gitGraph
  commit id: "1" tag: "HEAD"
```

---

2. second commit

```mermaid
%%{init: { 'gitGraph': { 'mainBranchName': 'default-branch', 'showCommitLabel': true}} }%%
gitGraph
  commit id: "1"
  commit id: "2" tag: "HEAD"
```

---

![four commits later](./4commitslater.png)

---

```mermaid
%%{init: { 'gitGraph': { 'mainBranchName': 'default-branch', 'showCommitLabel': true}} }%%
gitGraph
  commit id: "1"
  commit id: "2"
  commit id: "3"
  commit id: "4" type: REVERSE
  commit id: "5"
  commit id: "6" tag: "HEAD"
```

Oh, no, there was a mistake in commit `4`! We need to roll back!

---

## *checkout of C4*

```mermaid
%%{init: { 'gitGraph': { 'mainBranchName': 'default-branch', 'showCommitLabel': true}} }%%
gitGraph
  commit id: "1"
  commit id: "2"
  commit id: "3"
  commit id: "4" tag: "HEAD" type: REVERSE
  commit id: "5"
  commit id: "6" tag: "default-branch"
```

* No information is lost, we can get back to `6` whenever we want to.
* what if we commit now?

---

## Branching!


```mermaid
%%{init: { 'gitGraph': { 'mainBranchName': 'default-branch', 'showCommitLabel': true}} }%%
gitGraph
  commit id: "1"
  commit id: "2"
  commit id: "3"
  commit id: "4" type: REVERSE
  branch new-branch
  checkout default-branch
  commit id: "5"
  commit id: "6" tag: "default-branch"
  checkout new-branch
  commit id: "7" tag: "HEAD"
```

* Okay, but there was useful stuff in `4`, I'd like to have it into `new-branch`

---

## Merging!

<!-- ```mermaid
%%{init: { 'gitGraph': { 'mainBranchName': 'default-branch', 'showCommitLabel': true}} }%%
gitGraph
  commit id: "1"
  commit id: "2"
  commit id: "3"
  commit id: "4" type: REVERSE
  branch new-branch
  checkout default-branch
  commit id: "5"
  checkout new-branch
  commit id: "7"
  merge default-branch id: "8" tag: "HEAD"
  checkout default-branch
  commit id: "6" tag: "default-branch"
  checkout new-branch
``` -->

{{<image width="80" src="https://mermaid.ink/svg/pako:eNqFkj1rwzAQhv_KcWC8uEO_i7a2Me3QdkigkxbFutiilmQUmRCM_3sl26Gpk9JNennu1QOnDgsrCRkmSaeM8gw6SEvlX5xoqnS4aaHMkxOmqD6EppClkjairf3FekjTDNJtZXfPVmvl38Sa6gB511LfQ58k3Bz6uAEoBgqUZMDxkuNJdnUmuz6T3XAEv2-IwTL_zJerPBKjERjaTXLDWEXFl209_PY-abydXjngs5Zj9H5ENbmSZrUT8RD1RBmPr_njYlb9j8ndz_CM_MsQMwwyYVUy7LKLEEdfkSaORy1xvA-oaL1d7U2BLK4pw7aRwtNCidIJjWwj6m1ISSpv3fv4P4Zv0n8D8j25-w">}}

**Notice that:**
* we have two branches
* `8` is a merge commit, as it has two parents: `7` and `5`
* the situation is the same regardless that is a *single developer going back on the development* or *multiple developers working in parallel*!
* this is possible because *every copy of the repository contains the entire history*!

---

## Reference DVCS: Git

De-facto reference distributed version control system

* *Distributed*
* Born in *2005* to replace BitKeeper as SCM for the Linux kernel
  * Performance was a major concern
  * Written in C
* Developed by Linus Torvalds
  * Now maintained by others
* *Unix-oriented*
  * Tracks Unix file permissions
* Very *fast*
  * At conception, 10 times faster than Mercurial¹, 100 times faster than Bazaar

¹ Less difference now, Facebook vastly improved Mercurial

---

## Funny historical introduction

{{< youtube id="4XpnKHJAok8" autoplay="false" title="Linus Torvalds introduces Git at Google" >}}

---

## Approach: terminal-first

**Git is a command line tool**

Although graphical interfaces exsist, it makes no sense to learn a GUI:
* they are more prone to future changes than the CLI
* they add a level of interposition between you and the tool
* unless they are incomplete, they expose *more complexity* than what we can deal with in this course
    * use them at your own risk
* learning the CLI first will give you a clear understaing of how *all* GUIs work

---

## Configuration

Configuration in Git happens at two level
* **global**: the default options, valid system-wide
* **repository**: the options specific to a repository. They have *precedence* over the global settings

### Strategy

Set up the global options reasonably,
then override them at the repository level, if needed.

### `git config`

The `config` subcommand sets the configuration options
* when operated with the `--global` option, configures the tool globally
* otherwise, it sets the option for the *current repository*
  * (there must be a valid repository)
* Usage: `git config [--global] category.option value`
  * sets `option` of `category` to `value`

---

## Configuration: main options

As said, `--global` can be omitted to override the global settings locally

### Username and email: `user.name` and `user.email`

A name and a contact are always saved as metadata, so they need to be set up

* `git config --global user.name "Your Real Name"`
* `git config --global user.email "your.email.address@your.provider"`

### Default editor

Some operations pop up a text editor.
It is convenient to set it to a tool that you know how to use
(to prevent, e.g., being "locked" inside `vi` or `vim`).
Any editor that you can invoke from the terminal works.

* `git config --global core.editor nano`

### Default branch name

How to name the default branch.
Two reasonable choices are `main` and `master`

* `git config --global init.defaultbranch master`

---

## Initializing a repository

### `git init`
* Initializes a new repository *inside the current directory*
* Reified in the `.git` folder
* The location of the `.git` folder marks the root of the repository
  * Do not nest repositories inside repositories, it is fragile
  * Nested projects are realized via *submodules* (not discussed in this course)
* **Beware of the place where you issue the command!**
  * First use `cd` to locate yourself inside the folder that contains (or will containe the project)
    * (possibly, first create the folder with `mkdir`)
  * **Then** issue `git init`
  * if something goes awry, you can delete the repository by deleting the `.git` folder.

---

## Staging

Git has the concept of *stage* (or *index*).
* Changes must be added to the stage to be committed.
* Commits save the *__changes__ included in the stage*
  * Files changed after being added to the stage neet to be re-staged
* `git add <files>` moves the current state of the files into the stage as *changes*
* `git reset <files>` removes currently staged *changes* of the files from stage
* `git commit` creates a new *changeset* with the contents of the stage

```mermaid
flowchart LR
workdir("working directory") --add--> stage("stage (or index)") --commit--> repository(repository)
stage --reset-->workdir
```

---

## Observing the repository status

It is extremely important to understand *clearly* what the current state of affairs is
* Which *branch* are we working on?
* Which *files* have been *modified*?
* Which *changes* are already *staged*?

`git status` prints the current state of the repository, example output:

```git
❯ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   content/_index.md
        new file:   content/dvcs-basics/_index.md
        new file:   content/dvcs-basics/staging.png

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   layouts/shortcodes/gravizo.html
        modified:   layouts/shortcodes/today.html
```

---

## Committing

* Requires an **author** and an **email**
  * They can be configured *globally* (at the *computer level*):
    * `git config --global user.name 'Your Real Name'`
    * `git config --global user.email 'your@email.com'`
  * The global settings can be *overridden* at the *repository level*
    * e.g., you want to commit with a different email between work and personal projects
    * `git config user.name 'Your Real Name'`
    * `git config user.email 'your@email.com'`
* Requires a **message**, using appropriate messages is **extremely important**
  * If unspecified, the commit does not get performed
  * it can be specified inline with `-m`, otherwise Git will pop up the *default editor*
    * `git commit -m 'my very clear and explanatory message'`
* The *date* is recorded automatically
* The *commit identifier* (a cryptographic hash) is generated automatically

---

## Default branch

At the first commit, there is no branch and no `HEAD`.

Depending on the version of Git, the following behavior may happen upon the first commit:
* Git creates a *new branch* named `master`
  * *legacy behavior*
  * the name is inherited from the default branch name in *Bitkeeper*
* Git creates a *new branch* named `master`, but warns that it is a deprecated behavior
  * although coming from the Latin "*magister*" (teacher) and not from the "master/slave" model of asymmetric communication control, many recently prefer `main` as seen as more inclusive
* Git refuses to commit until a default branch name is specified
  * *modern behavior*
  * Requires configuration: `git config --global init.defaultbranch default-branch-name`

---

## Ignoring files

In general, we do not want to track *all* the files in the repository folder:
* Some files could be *temporary* (e.g., created by the editor)
* Some files could be *regenerable* (e.g., compiled binaries and application archives)
* Some files could contain *private* information

Of course, we could just not `add` them, but the error is around the corner!

It would be much better to just tell Git to ignore some files.

This is achieved through a *special `.gitignore` file*.
  * the file must be named `.gitignore`, names like `foo.gitignore` or `gitignore.txt` won't work
    * A good way to create/append to this file is via `echo whatWeWantToIgnore >> .gitignore` (multiplatform command)
  * it is a list of paths that git will ignore (unless `git add` is called with the `--force` option)
  * it is possible to add exceptions

---

## `.gitignore` example

```ignore-list
# ignore the bin folder and all its contents
bin/
# ignore every pdf file
*.pdf
# rule exception (beginning with a !): pdf files named 'myImportantFile.pdf' should be tracked
!myImportantFile.pdf
```

---

<!-- write-here "shared-slides/git/newlines.md" -->

<!-- end-write -->

---

# Exercise (pt. 1)

## Let's recreate the [`modular-calculator`](https://github.com/unibo-dtm-se/modular-calculator) repository

1. Download the code as a ZIP and extract it somewhere

2. Create a new directory elsewhere, and make it a Git repository with `git init`

3. Ensure that your username and email are set up correctly, either globally or locally

4. Add the `.gitignore` and the `.gitattributes` files, and commit them
  + consider using [gitignore.io](https://www.toptal.com/developers/gitignore/)
  + consider using several commits

5. Add the files from the `modular-calculator` repository to the stage and commit them
  + consider using several commits

> What criterion to decide which and how many files to include per commit?

---

## Rule of thumb for commits

* **Atomicity**: a commit should be a *single* change
  * it should be possible to __describe__ it in a _single sentence_
  * it should be possible to __revert__ it without affecting other changes

* **Coherence**: a commit should contain *coherent* changes
  * it should move the repository from a *consistent* state to another *consistent* state

* **Frequency**: commits should be *small* and *frequent*
  * it is better to have *many* small commits than *few* large ones

> Commit toghether edits that are related to the same *conceptual* change

---

## Dealing with removal and renaming of files

* The removal of a file is a legit *change*
* As we discussed, `git add` adds a *change* to the stage
* **the change can be a removal!**

`git add someDeletedFile` is a correct command, that will stage the fact that `someDeletedFile` does not exist anymore, and its deletion must be registered at the next `commit`.

* File *renaming* is *equivalent to file deletion and file creation* where, incidentally, the new file has the same content of the deleted file
* To stage the rinomination of file `foo` into `bar`:
  * `git add foo bar`
  * it records that `foo` has been deleted and `bar` has been created
  * Git is smart enough to understand that it is a name change, and will deal with it *efficiently*

---

# Exercise (pt. 2)

## Make the `calculator.gui` module a package

6. Create a new directory `gui` inside the `calculator` directory

7. Move the `gui.py` file inside the `gui` directory, and rename it to `__init__.py`

8. Add all the files to the stage and look at the status

9. Commit the changes

---

## Visualizing the history

Of course, it is useful to visualize the history of commits.
Git provides a dedicated sub-command:

`git log`

* opens a *navigable interactive view* of the history from the `HEAD` commit (the current commit) backwards
  * Press <kbd>Q</kbd>
* *compact* visualization: `git log --oneline`
* visualization of *all branches*: `git log --all`
* visualization of a lateral *graph*: `git log --graph`
* compact visualization of all branches with a graph: `git log --oneline --all --graph`

---

### example output of `git log --oneline --all --graph`

```text
* d114802 (HEAD -> master, origin/master, origin/HEAD) moar contribution
| * edb658b (origin/renovate/gohugoio-hugo-0.94.x) ci(deps): update gohugoio/hugo action to v0.94.2
|/  
* 4ce3431 ci(deps): update gohugoio/hugo action to v0.94.1
* 9efa88a ci(deps): update gohugoio/hugo action to v0.93.3
* bf32a8b begin with build slides
* b803a65 lesson 1 looks ready
* 6a85f8f ci(deps): update gohugoio/hugo action to v0.93.2
* b474d2a write more on the introductory lesson
* 8a7105e ci(deps): update gohugoio/hugo action to v0.93.1
* 6e40642 begin writing the first lesson
```

---

## Referring to commits: `<tree-ish>`es

In git, a reference to a commit is called `<tree-ish>`. Valid `<tree-ish>`es are:
* Full *commit hashes*, such as `b82f7567961ba13b1794566dde97dda1e501cf88`.
* *Shortened commit hashes*, such as `b82f7567`.
* *Branch names*, in which case the reference is to the last commit of the branch.
* `HEAD`, a special name referring to the current commit (the head, indeed).
* *Tag names* (we will discuss what a tag is later on).

---

## Relative references

It is possible to build *relative references*, e.g., "get me the commit before this `<tree-ish>`",
by following the commit `<tree-ish>` with a tilde (`~`) and with the number of parents to get to:
* `<tree-ish>~STEPS` where `STEPS` is an integer number produces a reference to the `STEPS-th` parent of the provided `<tree-ish>`:
  * `b82f7567~1` references the *parent* of commit `b82f7567`.
  * `some_branch~2` refers to the *parent of the parent* of the last commit of branch `some_branch`.
  * `HEAD~3` refers to the *parent of the parent of the parent* of the current commit.

* In case of merge commits (with multiple parents), `~` selects the first one
* Selection of parents can be performed with caret in case of multiple parents (`^`)
  * We won't go in depth here, but:
    * The [`git rev-parse` reference on specifying revision](https://git-scm.com/docs/git-rev-parse#_specifying_revisions) is publicly available
    * A [much more readable explanation can be found on Stack overflow](https://stackoverflow.com/a/2222920/1916413)

---

## Visualizing the differences

We want to see which *differences* a commit introduced, or what we modified in some files of the work tree

Git provides support to visualize the changes in terms of *modified lines* through `git diff`:
* `git diff` shows the difference between the *stage* and the *working tree*
  * namely, what you would stage if you perform a `git add`
* `git diff --staged` shows the difference between `HEAD` and the *working tree*
* `git diff <tree-ish>` shows the difference between `<tree-ish>` and the *working tree* (*stage excluded*)
* `git diff --staged <tree-ish>` shows the difference between `<tree-ish>` and the *working tree*, *including staged changes*
* `git diff <from> <to>`, where `<from>` and `<to>` are `<tree-ish>`es, shows the differences between `<from>` and `<to>`

---

### `git diff` Example output:

```diff
diff --git a/.github/workflows/build-and-deploy.yml b/.github/workflows/build-and-deploy.yml
index b492a8c..28302ff 100644
--- a/.github/workflows/build-and-deploy.yml
+++ b/.github/workflows/build-and-deploy.yml
@@ -28,7 +28,7 @@ jobs:
           # Idea: the regex matcher of Renovate keeps this string up to date automatically
           # The version is extracted and used to access the correct version of the scripts
           USES=$(cat <<TRICK_RENOVATE
-          - uses: gohugoio/hugo@v0.94.1
+          - uses: gohugoio/hugo@v0.93.3
           TRICK_RENOVATE
           )
           echo "Scripts update line: \"$USES\""
```

The output is compatible with the Unix commands `diff` and `patch`

Still, *binary files are an issue*! Tracking the right files is paramount.

---

# Exercise (pt. 3)

## Visualize the differences among any two commits

10. Use `git log --oneline` to find the hashes of two commits

11. Use `git diff HEAD <to>` to visualize the differences between the last commit and any prior commit of your choice
  + try with both the tree-ish of the chosen commit and the `~` notation

---

## Navigating the history

Navigation of the history concretely means to move the head (in Git, `HEAD`) to arbitrary points of the history

In Git, this is performed with the `checkout` commit:
* `git checkout <tree-ish>`
  * Unless there are changes that could get lost, *moves* `HEAD` to the provided `<tree-ish>`
  * Updates all tracked files to their version at the provided `<tree-ish>`

The command can be used to selectively checkout a file from another revision:
* `git checkout <tree-ish> -- foo bar baz`
  * Restores the status of files `foo`, `bar`, and `baz` from commit `<tree-ish>`, and adds them to the stage (unless there are uncommitted changes that could be lost)
  * Note that `--` is surrounded by whitespaces, it is not a `--foo` option, it is just used as a separator between the `<tree-ish>` and the list of files
    * the files could be named as a `<tree-ish>` and we need disambiguation

---

# Exercise (pt. 4)

## Restore a file from the history

12. Use `git log --oneline` to find the hash of the last commit where the file `gui.py` was present

13. Use `git checkout <tree-ish> -- gui.py` to restore the file `gui.py` from the chosen commit

14. Use `git status` to check the status of the file

---

## Detached head

Git does **not** allow *multiple heads per branch*
(other DVCS do, in particular Mercurial):
for a commit to be valid, `HEAD` must be at the "end" of a branch (on its last commit), as follows:

```mermaid
flowchart RL
  HEAD{{"HEAD"}}
  b1(master)

  C10([10]) --> C9([9]) --> C8([8]) --> C7([7]) --> C6([6]) --> C5([5]) --> C4([4]) --> C3([3]) --> C2([2]) --> C1([1])
  b1 -.-> C10

  HEAD -.-> C10
  HEAD --"fas:fa-link"--o b1

  class HEAD head;
  class b1,b2 branch;
  class C1,C2,C3,C4,C5,C6,C7,C8,C9,C10 commit;
```

When an old commit is checked out this condition doesn't hold!

If we run `git checkout HEAD~4`:

```mermaid
flowchart RL
  HEAD{{"HEAD fas:fa-unlink"}}
  b1(master)

  C10([10]) --> C9([9]) --> C8([8]) --> C7([7]) --> C6([6]) --> C5([5]) --> C4([4]) --> C3([3]) --> C2([2]) --> C1([1])

  b1 -.-> C10

  HEAD -.-> C6

  class HEAD head;
  class b1,b2 branch;
  class C1,C2,C3,C4,C5,C6,C7,C8,C9,C10 commit;
```

The system enters a special workmode called *detached head*.

When **in detached head**, Git allows to make **commits**, but they **are lost**!

(Not really, but to retrieve them we need `git reflog` and `git cherry-pick`, that we won't discuss)

---

# Exercise (pt. 5)

## Enter the detached head state

15. Use `git log --oneline` to find the hash of some previous commit of choice

16. Use `git checkout <tree-ish>` to enter the detached head state

17. Try to edit some file and commit the changes

18. Check the current status with `git status`

19. Use `git checkout master` to return to the last commit of the `master` branch

20. Use `git log --oneline` to find the hash of the commit you made in the detached head state

---

# _Distributed_ version control

---

## How does Git support collaboration?

<!-- ![Real-world Decentralized VCS](./dvcs-sink.svg) -->
{{<image src="./dvcs-sink.svg" height="50">}}

<br>

1. One copy of the project history is stored in the *cloud*

2. Every developer has a *local copy* of the repository
    * The local copy is a *full copy* of whole history

3. Mechanisms and protocols are in place to *synchronize* the local copies with the cloud copy

---

## Git repository hosting

Several Web services allow the creation of *shared repositories on the cloud*.

They *enrich* the base git model with services built around the tool:

* **Forks**: copies of a repository associated to different users/organizations
* **Pull requests** (or **Merge requests**): formal requests to *pull* updates from *forks*
  * repositories do not allow pushes from everybody
  * what if we want to contribute to a project we cannot push to?
    * *fork* the repository (we *own* that copy)
    * write the contribution and push to our *fork*
    * ask the maintainers of the *original repository* to *pull from* our fork
* **Issue tracking**

---

## Most common services

* <i class="fa-brands fa-github"></i> **GitHub**
  * Replaced Sourceforge as the *de-facto standard* for open source projects hosting
  * *Academic plan*
* <i class="fa-brands fa-gitlab"></i> **GitLab**
  * Available for free as *self-hosted*
  * Userbase grew when Microsoft acquired GitHub
* <i class="fa-brands fa-bitbucket"></i> **Bitbucket**
  * From Atlassian
  * Well integrated with other products (e.g., Jira)


---

## <i class="fa-brands fa-github"></i> GitHub

* *Hosting* for git repositories
* *Free for open source*
* *Academic accounts*
* *De-facto standard* for open source projects
* One *static website* per-project, per-user, and per-organization
  * (a feature exploited by these slides)

---

## <i class="fa-brands fa-github"></i> repositories as remotes: authentication

<i class="fa-brands fa-github"></i> repositories are uniquely identified by an **owner** and a **repository name**
* `owner/repo` is a name unique to every repository

<i class="fa-brands fa-github"></i> supports two kind of authentications:
### **HTTPS** -- Requires authentication via token
* The <i class="fab fa-windows"></i> port of <i class="fa-brands fa-git"></i> should include a graphical authenticator, otherwise:
    * a token must be generated with `repo` access scope at https://github.com/settings/tokens/new
    * the URL `https://github.com/owner/repo.git` becomes: `https://token@github.com/owner/repo.git`
* Recommended to <i class="fab fa-windows"></i> users with no Unix shell

### **Secure Shell (SSH)** -- Requires authentication via public/private key pair
* Recommended to <i class="fab fa-linux"></i>/<i class="fab fa-apple"></i> users and to those with a working SSH installation
* The same protocol used to open remote terminals on other systems
* Tell Github your **public** key and use the **private** (and *secret*) key to authenticate

---

## Configuration of OpenSSH for <i class="fa-brands fa-github"></i>

**Disclaimer**: this is a "quick and dirty" way of generating and using SSH keys.
<!-- markdown-link-check-disable-next-line -->
You are warmly recommended to learn how it works and [the best security practices](https://archive.ph/3Pn0L).

1. If you don't already have one, generate a new key pair
    * `ssh-keygen`
    * You can confirm the default options
    * You can pick an empty password
        * <i class="fa-solid fa-arrow-up"></i> your private key will be stored *unencrypted* on your file system
        * please understand the associated security issues, if you don't, use a password.
2. Obtain your **public key**
    * `cat ~/.ssh/id_rsa.pub`
    * Looks something like:
    ```text
    ssh-rsa AAAAB3Nza<snip, a lot of seemingly random chars>PIl+qZfZ9+M= you@your_hostname
    ```
3. Create a new key at https://github.com/settings/ssh/new
    * Provide a title that allows you to identify the key
    * Paste your key

You are all set! Enjoy your secure authentication.

---

# Exercise (pt. 6)

## Publish your repository to <i class="fa-brands fa-github"></i>

21. Browse to <https://github.com>, log in with your credentials

22. Create a new __private__ repository, named `modular-calculator`

23. Create a new [personal access token](https://github.com/settings/tokens/new) with `repo` access scope
    + give it a name that allows you to remember about it (e.g., `my first token`)
    + give it an expiration date (the sooner the better)

24. Save the token in a safe place (from which it is easy to copy&paste it)
    + __do not share your token with anyone__
    + beware: after you close that page, __you won't be able to see the token again__

---

## Remotes

> Remotes are __local names__ for the *known copies* of a repository that exist somewhere on the Internet

* Each remote has a *name* and a *URL*
* When a repository is created via `init`, no remote is known.
* When a repository __cloned__ from the Internet, the remote source is called `origin` by default

<br>

The `remote` subcommand is used to inspect and manage remotes:
* `git remote -v` *lists* the known remotes

* `git remote add a-remote URL` *adds* a new remote named `a-remote` and pointing to `URL`
* `git remote show a-remote` displays *extended information* on `a-remote`
* `git remote remove a-remote` *removes* `a-remote` (it does not delete information on the remote, it *locally* forgets that it exits)

---

## Starting a repository

### Two ways to start a repository

1. **From scratch**: `git init` creates an empty repository
    + this is commonly the case for __novel__ projects
    + requires __publication__ of the repository to the cloud

2. **From a remote**: `git clone URL` creates a local copy of a remote repository (a *clone*)
    + this is commonly the case for __existing__ projects

---

## Publishing a repository (pt. 1)

1. Initialize a repository locally, and put some commits in it

2. Create a new repository on <i class="fa-brands fa-github"></i> (or any other service of choice)
    + let's say the URL of the repository is `https://somesite.com/repo.git`

3. Create a new remote in the local repository, let's call it `origin`
    + `git remote add origin https://somesite.com/repo.git`

4. Set the _upstream_ for the current branch
    + i.e. declare how the local branch will be named on the remote (better to use the same name)
    + e.g. if the current branch is `master`: 
        * `git branch --set-upstream-to=origin/master`

---

## Publishing a repository (pt. 2)

5. The situation will be as follows:

    ```mermaid
    flowchart RL

    subgraph somesite.com/repo.git
      direction RL
      HEAD{{"HEAD"}}
      master(master)

      C10([10]) --> C9([9]) --> C8([8]) --> C7([7]) --> C6([6]) --> C5([5]) --> C4([4]) --> C3([3]) --> C2([2]) --> C1([1])

      master -.-> C10

      HEAD -.-> C10
      HEAD --"fas:fa-link"--o master
    end

    subgraph local
      direction RL
      origin[(origin)]

      HEADL{{"HEAD"}}
      masterl(master)

      CL10([10]) --> CL9([9]) --> CL8([8]) --> CL7([7]) --> CL6([6]) --> CL5([5]) --> CL4([4]) --> CL3([3]) --> CL2([2]) --> CL1([1])

      masterl -.-> CL10
      masterl ==o master

      HEADL -.-> CL10
      HEADL --"fas:fa-link"--o masterl
    end

    origin ==o somesite.com/repo.git

    class local,somesite.com/repo.git repo;
    class origin remote;
    class HEAD,HEADL head;
    class master,masterl,bug22,serverless branch;
    class C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,CL1,CL2,CL3,CL4,CL5,CL6,CL7,CL8,CL9,CL10,CL11,CL12,CL13 commit;
    ```

    * locally, `git@somesite.com/repo.git` is saved as `origin`
    * the main branch (the branch where `HEAD` is attached, in our case `master`) on `origin` gets checked out locally with the same name
    * the local branch `master` is set up to track `origin/master` as upstream

6. From now on, local commits can be pushed to the remote with `git push`

---

# Exercise (pt. 7)

## Publish your repository to <i class="fa-brands fa-github"></i>

25. Add the remote `origin` to your local repository
    + `git remote add origin https://github.com/YOUR_USERNAME/modular-calculator.git`

26. Set the upstream for the `master` branch
    + `git branch --set-upstream-to=origin/master`

27. Push the local repository to the remote
    + `git push`
    + you may be asked to authenticate with your _username_ and the _personal access token_ (as password)

28. Check the status of the repository on <i class="fa-brands fa-github"></i> via your browser

29. Do some more commit locally and push them to the remote

---

## Cloning a repository (pt. 1)

* We can initialize an **emtpy** repository with `git init`
* But most of the time we want to start from a *local copy* of an **existing** repository

Git provides a `clone` subcommand that copies *the whole history* of a repository locally
* `git clone URL destination` creates the folder `destination` and clones the repository found at `URL`
  * If `destination` is not empty, fails
  * if `destination` is omitted, a folder with the same namen of the last segment of `URL` is created
  * `URL` can be remote or local, Git supports the `file://`, `https://`, and `ssh` protocols
      * `ssh` *recommended* when available
* The `clone` subcommand checks out the remote branch where the `HEAD` is attached (*default branch*)

---

## Cloning a repository (pt. 2)

### Examples

* `git clone /some/repository/on/my/file/system destination`
  * creates a local folder called `destination` and copies the repository from the local directory
* `git clone https://somewebsite.com/someRepository.git myfolder`
  * creates a local folder called `myfolder` and copies the repository located at the specified `URL`
* `git clone user@sshserver.com:SomePath/SomeRepo.git`
  * creates a local folder called `SomeRepo` and copies the repository located at the specified `URL`

--- 

## Cloning a repository (pt. 3)

### Situation after cloning

```mermaid
flowchart RL

subgraph somesite.com/repo.git
  direction RL
  HEAD{{"HEAD"}}
  master(master)
  serverless(feat/serverless)

  C10([10]) --> C9([9]) --> C8([8]) --> C7([7]) --> C6([6]) --> C5([5]) --> C4([4]) --> C3([3]) --> C2([2]) --> C1([1])
  C12([12]) --> C11([11]) --> C7

  master -.-> C10
  serverless -.-> C12

  HEAD -.-> C10
  HEAD --"fas:fa-link"--o master
end

subgraph local
  direction RL
  origin[(origin)]

  HEADL{{"HEAD"}}
  masterl(master)

  CL10([10]) --> CL9([9]) --> CL8([8]) --> CL7([7]) --> CL6([6]) --> CL5([5]) --> CL4([4]) --> CL3([3]) --> CL2([2]) --> CL1([1])

  masterl -.-> CL10
  masterl ==o master

  HEADL -.-> CL10
  HEADL --"fas:fa-link"--o masterl
end

origin ==o somesite.com/repo.git

class local,somesite.com/repo.git repo;
class origin remote;
class HEAD,HEADL head;
class master,masterl,bug22,serverless branch;
class C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,CL1,CL2,CL3,CL4,CL5,CL6,CL7,CL8,CL9,CL10,CL11,CL12,CL13 commit;
```

* `git@somesite.com/repo.git` is saved as `origin`
* The main branch (the branch where `HEAD` is attached, in our case `master`) on `origin` gets checked out locally with the same name
* The local branch `master` is set up to track `origin/master` as upstream
* Additional branches are *fetched* (they are known locally), but they are not checked out

---

# \[New\] Exercise (pt. 1)

## Clone somebody else's repository

1. Clone the following repository: <https://github.com/unibo-dtm-se/repository-example>
  - `git clone https://github.com/unibo-dtm-se/repository-example.git`

> Such repository is an instance of 
> [`template-project-work`](https://github.com/unibo-dtm-se/template-project-work), i.e. a template for 
> your final reports. It consists of static Web-site, based on the [Jekyll](https://jekyllrb.com/) technology.
> You write `.md` files, and Jekyll generates the HTML for you.
> The site is then hosted on GitHub pages, i.e. [here](https://unibo-dtm-se.github.io/template-project-work).

2. Wait for the _teacher_ to create and _push_ a few more commits
    + have a look to the commit history, on <i class="fa-brands fa-github"></i>

3. _Pull_ the commits from the remote
    + `git pull`

4. Ensure you have the teacher's commits locally
    + `git log --oneline`

---

# Exercise (pt. 2)

## Divergent histories

Let's now try to exemplify a potential situation of conflict

5. Let's select a few volunteers
    + we need your __GitHub usernames__ to give you _write rights_ on the repository

6. The _volunteer_ will be asked to _edit_ one file and _push_ the changes (say, file `sections/01-concept/index.md`)
    + try to _add_ some content to `.md` files, possibly, _deleting_ some prior content
    + _tell_ the teacher which files you edited

7. The _volunteer_ will be asked to _push_ their changes
    1. `git add <edited files here>` 2. `git commit -m "Description of the changes"` 3. `git push`

8. The _teacher_ will edit some __other__ file (_different_ from the one the volunteer edited) and then _commit_
    + let's pretend the teacher was not aware of the volunteer's changes
    + this is to simulate the scenario of __concurrent__ changes _to the different files_

9. The _teacher_ will attempt to _push_ their changes
    + `git push`

---

## Divergent histories (pt. 1)

### How to spot the situation, locally

Attempting to __push__ shall result in a _message_ like:

```text
To somesite.com/repo.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'somesite.com/repo.git'
hint: Updates were rejected because the remote contains work that you do
      not have locally. This is usually caused by another repository pushing
      to the same ref. You may want to first integrate the remote changes
      (e.g., 'git pull ...') before pushing again.
      See the 'Note about fast-forwards' in 'git push --help' for details.
```

* Why is this the case?
* How to solve?
  * (Git's `hint` explains it pretty well)

---

## Divergent histories (pt. 2)

### Understanding the issue

The situation is as follows:

```mermaid
flowchart RL

subgraph somesite.com/repo.git
  direction RL
  HEAD{{"HEAD"}}
  master(master)

  C10([10]) --> C9([9]) --> C8([8]) --> C7([7]) --> C6([6]) --> C5([5]) --> C4([4]) --> C3([3]) --> C2([2]) --> C1([1])

  master -.-> C10

  HEAD -.-> C10
  HEAD --"fas:fa-link"--o master
end

origin ==o somesite.com/repo.git

subgraph local
  direction RL
  origin[(origin)]

  masterl(master)
  HEADL{{"HEAD"}}

  CL11([11]) --> CL9([9]) --> CL8([8]) --> CL7([7]) --> CL6([6]) --> CL5([5]) --> CL4([4]) --> CL3([3]) --> CL2([2]) --> CL1([1])

  masterl -.-> CL11
  masterl ==o master

  HEADL -.-> CL11
  HEADL --"fas:fa-link"--o masterl
end

class local,somesite.com/repo.git repo;
class origin remote;
class HEAD,HEADL head;
class master,masterl,bug22,serverless,imported branch;
class C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,CL1,CL2,CL3,CL4,CL5,CL6,CL7,CL8,CL9,CL10,CL11,CL12,CL13 commit;
```

* The history is the __same__ for _local_ and _remote_, __up to__ commit `9`
* Then, the _remote_ history has a commit `10`, and the _local_ history has commit `9`

---

## Divergent histories (pt. 3)

### Solving the issue

⬇️ `git pull` ⬇️

```mermaid
flowchart RL

subgraph somesite.com/repo.git
  direction RL
  HEAD{{"HEAD"}}
  master(master)

  C10([10]) --> C9([9]) --> C8([8]) --> C7([7]) --> C6([6]) --> C5([5]) --> C4([4]) --> C3([3]) --> C2([2]) --> C1([1])

  master -.-> C10

  HEAD -.-> C10
  HEAD --"fas:fa-link"--o master
end

origin ==o somesite.com/repo.git

subgraph local
  direction RL
  origin[(origin)]

  masterl(master)
  HEADL{{"HEAD"}}

  CL12([12]) --> CL11([11]) --> CL9([9]) --> CL8([8]) --> CL7([7]) --> CL6([6]) --> CL5([5]) --> CL4([4]) --> CL3([3]) --> CL2([2]) --> CL1([1])
  CL12 --> CL10([10]) --> CL9

  masterl -.-> CL12
  masterl ==o master

  HEADL -.-> CL12
  HEADL --"fas:fa-link"--o masterl
end

class local,somesite.com/repo.git repo;
class origin remote;
class HEAD,HEADL head;
class master,masterl,bug22,serverless,imported branch;
class C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,CL1,CL2,CL3,CL4,CL5,CL6,CL7,CL8,CL9,CL10,CL11,CL12,CL13 commit;
```

* Now, the local history is a __superset__ of the remote history
    * i.e., it includes all the commits of the remote history, and some more

* A new __merge commit__ (`12`) is created in the _local_ history, which has `10` and `11` as parents

---

## Divergent histories (pt. 4)

### Solving the issue

> __Beware__: in general, when creating the _merging_ commits, 
>
> __conflicts__ might arise _if the same files were edited_

We'll discuss __conflict resolution__ in a few slides

---

## Divergent histories (pt. 5)

### Solving the issue

Assuming that you manage to create the merge commit with no issues...

⬇️ `git push` ⬇️

```mermaid
flowchart RL

subgraph somesite.com/repo.git
  direction RL
  HEAD{{"HEAD"}}
  master(master)

  C12([12]) --> C10([10]) --> C9([9]) --> C8([8]) --> C7([7]) --> C6([6]) --> C5([5]) --> C4([4]) --> C3([3]) --> C2([2]) --> C1([1])
  C12 --> C11([11]) --> C9

  master -.-> C12

  HEAD -.-> C12
  HEAD --"fas:fa-link"--o master
end

origin ==o somesite.com/repo.git

subgraph local
  direction RL
  origin[(origin)]

  masterl(master)
  HEADL{{"HEAD"}}

  CL12([12]) --> CL11([11]) --> CL9([9]) --> CL8([8]) --> CL7([7]) --> CL6([6]) --> CL5([5]) --> CL4([4]) --> CL3([3]) --> CL2([2]) --> CL1([1])
  CL12 --> CL10([10]) --> CL9

  masterl -.-> CL12
  masterl ==o master

  HEADL -.-> CL12
  HEADL --"fas:fa-link"--o masterl
end

class local,somesite.com/repo.git repo;
class origin remote;
class HEAD,HEADL head;
class master,masterl,bug22,serverless,imported branch;
class C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,CL1,CL2,CL3,CL4,CL5,CL6,CL7,CL8,CL9,CL10,CL11,CL12,CL13 commit;
```

The push succeeds now!

#### The local and remote histories are now __aligned__ 

(i.e., they are equal)

---

# Exercise (pt. 3)

## Divergent histories (continued)
 
10. The _teacher_ will __pull__ the changes from the remote
    + notice that a merge commit is created in the local history
        + `git log --oneline`

11. The _teacher_ will __push__ the changes to the remote, successfully
    + `git push`
    + have a look to the commit history, on <i class="fa-brands fa-github"></i>

12. The _volunteer_ will be asked to __pull__ the changes from the remote
    + this should work with no issues

---

# Exercise (pt. 4)

## Creating conflicts

13. The _volunteer_ will be asked to _edit_ some more file
    + try to _add_ some content to `.md` files, possibly, _deleting_ some prior content
        * say, to file `sections/02-requirements/index.md`
    + _tell_ the teacher which files you edited

14. The _volunteer_ will be asked to _push_ their changes

15. The _teacher_ will _edit_ the __same__ file (_the one the volunteer edited_) and then _commit_
    + let's pretend the teacher was not aware of the volunteer's changes
    + this is to simulate the scenario of __concurrent__ changes _to the same files_

16. The _teacher_ will attempt to _pull_ the volunteer's changes
    + `git pull`
    + Git will tell you that there are __merge conflicts__

> Merge conflicts cannot be resolved _automatically_ by Git, they require __human intervention__

---

## Merge conflicts

Git tries to resolve most conflicts by *itself*
* It's *pretty good* at it
* but things can still require *human intervention*

In case of conflict on one or more files, Git marks the subject files as *conflicted*, and modifies them adding *merge markers*:

```text
<<<<<<< Current changes
Changes made on the branch that is being merged into,
this is the branch currently checked out (HEAD).
=======
Changes made on the branch that is being merged in.
>>>>>>> Incoming changes
```

* (_VS Code_ may highlight the conflict markers with _colours_)
* The user should *change the conflicted files* so that they reflect the *final desired status*
* The (now fixed) files should get added to the stage with `git add`
* The merge operation can be concluded through `git commit`
  * In case of merge, the message is pre-filled in
  * If the message is okay, `git commit --no-edit` can be used to use it without editing

---

# Exercise (pt. 5)

## Resolving conflicts

17. The _teacher_ will _solve_ the conflicts __manually__ and then _commit_
    + `git commit --no-edit`
    + notice that there should be one more commit in the history, _whose message describes the conflict_
        * `git log`

18. The _teacher_ will attempt to _push_ the changes to the remote
    + `git push`
    + this should work with no issues
    + consider having a look to the commit history, on <i class="fa-brands fa-github"></i>

19. Students will be asked to _pull_ the changes from the remote
    + this should work with no issues

---

## Take-away 

### Simple protocol for cooperation

1. **Pull** before starting your working session

2. Make your __commits__ locally 

3. **Push** your changes to the remote, _as frequently as possible_
    + _before_ pushing:
        1. **pull** the changes from the remote
        2. __resolve__ conflicts, if any
        3. __commit__ the changes
        4. finally, _push_

4. Make sure to __push__ before your working session ends

--- 

# Branching

---

## Why branching?

* Most commonly, while _releasing_ version `N`, development teams are already working to version `N+1`

* Most commonly, the development team is working on _multiple_ __features__ at the same time

* To support many (different) development activities to occur _simultaneously_, developers exploit _branches_

> A __branch__ is a coherent _development line_

* technically, a branch is a __sequence of__ contiguous commits, with a __name__ 
    + the name acts as a __pointer__ to the last commit

---

## Example: the Git Flow (pt. 1)

(cf. <https://nvie.com/posts/a-successful-git-branching-model/>)

!["Git Flow representation as a graph"](gitflow-horizontal.png)

---

## Example: the Git Flow (pt. 2)

- `master` (or `main`) branch contains commits describing the _stable_ ($\approx$ publicly available & working) versions of the code
- `develop` branch contains commits where novel features under development are being integrated to create the next stable version
    + these commits are eventually propagated to the `master` branch
- `hotfix` branches (one per _hotfix_) are created whenever an urgent fix is needed on the stable version
    + these commits are later propagated to the `develop` branch too
- `feature` branches (one per _feature_) are created whenever a new feature is being developed
    + these commits are later propagated to the `develop` branch, and eventually to the `master` branch
+ `release` branches (one per _release_) are created whenever a new version is being prepared for release
    + these commits are later propagated to the `develop` and `master` branches

---

## Suggestion (pt. 1)

### This branching workflow could be used for writing your final report too!

1. `master` branch contains the _initial_ version of the report (which is equal to the template)

2. you create a `develop` branch

3. you create a `feature/section-N` branch for each section (`N` = 1, 2, ...`)  

4. as soon as a section is completed, the corresponding `feature/section-N` branch is merged into `develop`
    + the `feature/section-N` branch is deleted
    + further commits are performed on `develop` to better integrate the section with the rest

5. once satisfied with the _whole report_ you create a `release` branch, from `develop`
    + you perform the final adjustments on the `release` branch (e.g. date and version number in the front page)

6. once satisfied with the _whole report_ you merge the `release` branch into `master`
    + the `release` branch is deleted

7. if revisions are requested by the teacher, you may create a `hotfix` branch from `master`

8. ... and so on

---

## Suggestion (pt. 2)

### This branching workflow could be used for writing your final report too!

```mermaid
%%{init: { 'gitGraph': { 'mainBranchName': 'master'}} }%%
gitGraph
  commit tag: "initial" id: "use template"
  commit id: "write title"
  commit id: "write authors"
  branch develop
  commit id: "write abstract"
  commit id: "write concept"
  branch feature/02-requirements
  commit id: "write requirements"
  checkout develop
  merge feature/02-requirements
  commit id: "integrate requirements"
  branch feature/03-design
  commit id: "design class 1"
  branch feature/05-validation
  commit id: "test class 1"
  checkout feature/03-design
  commit id: "design class 2"
  checkout feature/05-validation
  merge feature/03-design
  commit id: "test class 2"
  branch feature/04-development
  commit id: "implement class 1"
  checkout develop
  merge feature/04-development
  commit id: "integrate sections"
  commit
  commit id: "..." type: HIGHLIGHT
  commit
  branch release
  commit id: "final adjustments"
  checkout master
  merge release
  commit id: "submittable" tag: "1.0"
```

<!-- --- -->

<!-- dont write-here "shared-slides/git/branching-merging.md" -->

<!-- end-write -->

<!-- --- -->

<!-- dont write-here "shared-slides/git/tagging-basics.md" -->

<!-- end-write -->

<!-- --- -->

<!-- dont write-here "shared-slides/git/branch-deletion.md" -->

<!-- dont end-write -->

<!-- ---

## Best practices

* The **CLI** is your *truth*
  * Beware of the GUIs
* Prepare an *ignore list* early
  * And *maintain it*
  * And maybe prepare it manually and don't copy/paste it
* When you have untracked files, *decide whether you want to track them or ignore them*
* Be very careful with *what* you track
* Prepare an *attribute file*
* *Pull* before pushing

--- -->

<!-- dont write-here "shared-slides/git/workflows-flow-fork.md" -->

<!-- end-write -->

---

# To be continued...