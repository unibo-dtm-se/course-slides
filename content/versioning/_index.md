 
+++

title = "Picking version numbers"
description = "Assigning meaning to revisions"
outputs = ["Reveal"]

+++

# Versioning, Conventional Commit 

{{% import path="reusable/header-dp.md" %}}

---

# Software versioning

> __Versioning__: the process of assigning a **unique identifier** to a **unique state** of some software
* Used to *distinguish* different software states
* Used to *refer* to different states of the same software
* The identifier is normally a sequence of alfanumeric characters spaced by dots, slashes, and dashes
* Assigning IDs in a *predictable* way could help gathering *information* on the software itself

---

# Versioning levels

Versioning can happen at different levels, for instance:

* *Code (DVCS)*
    * Fine grained
    * Automatic
    * Non-progressive
    * Non-linear (i.e., versions can't be sorted)
* *Subproject / feature version*
    * Often leveraging __code-naming__ 
    * Non-linear
    * e.g., Java JSRs, Kotlin KEEPs, [Python Enhancement Proposals (PEPs)](https://peps.python.org/).
* *Software release*
    * Usually manual
    * Usually linear

---

# Versioning scopes

W.r.t. the administrative boundaries (e.g. the organization, the department, the team) versioning can be:

* **Internal**
    * Identifies a point in development
    * Changes do not impact the "outer world"
* **External**
    * A publicly visible release of the software
    * Changes are disruptive

Often for *open source* projects, internal and external versioning *coincide*

---

# Versioning approaches
## Code naming

> The version is represented by a (usually pronounceable) *word*, *short phrase* or *acronym*

Examples: macOS __Sierra__, Windows __Vista__, Ubuntu __Bionic Beaver__

* With few exceptions, *does not provide any direct information on the project* (often by purpose)
* Very frequently used internally to refer to new _feature sets_
* Often used to "protect" the corporation from information leaking
* Often *changed to purposely create confusion*
* Used to separate pre-release versions from final releases
    * e.g., [Project Longhorn only became Windows Vista at release time](https://en.wikipedia.org/wiki/Development_of_Windows_Vista)
* Often associated for *commercial reasons* to other version numbers
    * e.g. Ubuntu `18.04` *Bionic Beaver* or MacOS X `10.13.5` *Sierra*
* Reasons for code-names are often *political and commercial* rather than technical

---

# Versioning approaches
## Date based versioning

> The version is represented by **a string representing the release date**

Example: Ubuntu `18.04`, Windows `2000`, Office `2007`, Visual Studio `2022`

* Dates *don’t always match development rate*
    * A project may change more in a week than in a year

* Useful for projects that are *fast-paced* (multiple releases per week)

* Useful as a *companion* for other versioning schemes

* Useful at the *commercial level* for clearly indicating the novelty (and the age) of a project
    * e.g. Windows 98, Office 2003

---

# Versioning approaches
## Unary numbering

> The version is represented by a **string whose length grows at each version**

Example: $\TeX$ `3.1`, `3.14`, `3.141`, ..., $\pi$

* Only useful for project that reached *maturity*

* Extremely *unlikely* in today’s software world

* May lead to *version length explosion*

---

# Versioning approaches
## Degree of retro compatibility

> The version is represented one or more _numbers_, separately incremented, that
> <br>
> **reflect incrementally widespread changes in the product**

Example: `1.0.1`, `1.1.0`, `2.0.0`

* Often used *in conjunction with other techniques*
* Often used *badly* (see the Linux kernel)
* *Formal methodologies* for applying it exist
* Sometimes instead of indicating API-level changes, the version may indicate user-level perceivable changes
    * Very much depends on who are the clients/customers

---

# Versioning in the real world
## [Microsoft Windows versioning](https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions)

Combination of all the techniques:
* *Dates* (Windows 9x, 2001)

* *Codenames* (NT, Vista, XP, Millenium Edition)

* Pre-release code-names (Longhorn)

* Dates for internal builds

* Incremental versions on *multiple levels*
    * e.g., Windows 95 is also MS-DOS 7.0 and Windows 4.00

* *Separation* between “commercial” versions and “actual” “versions”
    * e.g., Windows 7 is actually Windows 6.1, and Windows 10 is actually Windows 6.4
    * One future Windows may actually become Windows 7.0, clashing with the “commercial” version of an older product

<br>

**Proliferation of methodologies and inconsistencies leads to issues**
* [Ever wondered why there is no Windows 9?](https://medium.com/@omogidavis/the-curious-case-of-windows-9-why-did-microsoft-skip-a-number-1430ef606ae3)

---

# Versioning in the real world
## [Macintosh versioning](https://en.wikipedia.org/wiki/List_of_Apple_operating_systems#Macintosh_computers)

- Different versioning styles over time

- Version `1` to `9`: commercial names were linear

- Version `X` (`10` in Roman numerals) become part the commercial name

- __Mac OS X__ was a series of products, distinguished by a number of *big cats names* and *sub-numbers*
    * e.g. Mac OS X `10.0` (code name __Cheetah__) ... Mac OS X `10.8` (code name __Mountain Lion__)

- Product name become simply __macOS__ since version `10.12` (__Sierra__) 

- Version `11` (__Big Sur__) is the first version of macOS to be numbered `11`

- Current version is `14` (__Sonoma__)

- The __Darwin__ (i.e. macOS's Kernel) versioning schema is completely different from the commercial version number
    - last version is `23.4.0`

---

{{% section %}}

# Versioning in the real world
## Canonical Ubuntu versioning

Association of a *date in format* `YY.MM` and a *two word code-name* in form of `Adjective AnimalName`. Both the words of the code-name begin with the
same letter.

* Version number *does not track changes*
    * The development is arguably linear
    * But actually new versions may bring in substantial novelties, e.g. entirely new desktop environments

* "LTS" can be optionally appended to identify *“Long Term Support”* versions

* Two versions of Ubuntu can be compared by date but also by the first letter of their codename
    * “Zesty Zapus” is newer than “Utopic Unicorn”
    * Unfortunately, since there are a limited number of letters, “Bionic Beaver” is newer than “Xenial Xerus” and “Zesty Zapus”

---

# "Support" of software products (pt. 1)

What happens to a software product after a __new version__ is released?

1. Let's say product `X` is released under code name `Abstract Alfred` with version `1.0.0`

2. Developers keep working on the product, and release a new version `1.1.0` under code name `Boring Beatrix`

3. Some severe security issue is found in version `1.1.0` and a patch `1.1.1` is released
    + version `1.1.1` is now released under `Boring Beatrix v2` code name

4. The bug is still affecting `Abstract Alfred`, which still has a lot of active users
    + a patch `1.0.1` is released for `Abstract Alfred`, containing the same fix of `1.1.1`, but _not_ all the features of `1.1.0`
    + the patch is released under code name `Abstract Alfred v2`

> __Takeaways__:
> - one version does not stop to exist when the next one is released
> - bug fixes are often back-ported to older versions

---

# "Support" of software products (pt. 2)

- Big software companies often provide __support__ for their products, for a given amount of time
    - this is to give time to users/customers to migrate to newer versions  

- When releasing a new version of a product, the company shall keep spending money to maintain the old one
    - e.g. keep fixing bugs, keep providing security patches
    - e.g. providing guides for how to migrate to the new versions

- The __end of support__ is the date after which the company will not provide any more support for the product
    - no more updates will be released
    - no more help for users on how to migrate to newer versions

- Most commonly, the end of support is announced well _in advance_
    - _upon release_, the company will announce the end of support date

- On the user side, it is important to know _when_ the end of support is to __plan the migration__ to newer versions
    - most commonly, updates are very critical situations for development teams
    - they may want to _assess_ the new version before migrating to it, and _adjust issues_ after migration

---

# Support vs. Long-Term Support (LTS)

- Most commonly when release is __periodic__ the default support time window is _relatively short_

- Examples:
    + _Canonical_ releases one new version of _Ubuntu_ every __6 months__
    + _OpenJDK_ releases a new version of _Java_ every __6 months__

- Once every few years, a version is released with __Long-Term Support__ (LTS)
    - LTS versions are supported for a _much longer_ period of time
    - LTS versions are often preferred by _user_ companies, as they provide a _stable_ platform for a _longer time_

{{% /section %}}

---

# Versioning in the real world
## Wine versioning

Formerly a *pure date*, in ISO format without hyphens, e.g. `20040505`.

The project *switched to a classic versioning* in form of `major.minor`
* The change may give some headaches to dependency managers, since `20040505` is bigger than `3.9` and other subsequent versions.
* A `0.Date` format for initial development releases would have been advisable with hindsight

---

# Versioning in the real world
## $\TeX$ versioning

*Purely unary numbering* converging to $\pi{}$

* Current version (released in February 2021) is `3.141592653`
* Every time a new version is produced, a number from $\pi{}$ is added to the version string
* Sustainable just because $\TeX$ is now extremely stable, and development is almost frozen

> At the time of my death, it is my intention that the then-current versions of $\TeX$ [...] be forever left unchanged,
except that the final version numbers to be reported in the “banner” lines of the programs should become:
__TeX, Version $\pi $__ [...].
From that moment on, all “bugs” will be permanent “features”.
**<div style="text-align: right"> Donald E. Knuth</span>**

---

# Versioning in the real world
## Python Enhancement Proposal 440 ([PEP440](https://www.python.org/dev/peps/pep-0440/))

It is *the* way Python software should be versioned
* Flexible but complicated
* Order of release segments is mandated

Format: `[N!]N(.N)*[{a|b|rc}N][.postN][.devN]`
1. Optional _epoch segment_: an integer number `N` followed by exclamation mark (e.g. `1!`)
1. __Mandatory__ _release segment_: as many integer numbers `N1`, `N2`, ..., separated by `.` (e.g. `1.2.3.4.5`)
1. Optional _pre-release segment_: one of `a`, `b`, `rc` followed by an integer number `N` (e.g. `a1`, `b2`, `rc3`)
1. Optional _post-release segment_: one `.` followed by `post` and an integer number `N` (e.g. `.post1`)
1. Optional _development release segment_: one `.` followed by `dev` and an integer number `N` (e.g. `.dev1`)

---

# Versioning in the real world
## [Semantic Versioning (SemVer)](https://semver.org/)

Encodes version numbers and their change to *convey meaning about the underlying code* and what has been modified from one version to the next.
* Written in RFC-style
* No-retract
* Versioned using Semantic versioning
* Format `X.Y.Z[-P][+B]` 
    * `X` $\Rightarrow$ __mandatory__ Major (integer number)
    * `Y` $\Rightarrow$ __mandatory__ Minor (integer number)
    * `Z` $\Rightarrow$ __mandatory__ Patch (integer number)
    * `P` $\Rightarrow$ _optional_ Pre-release (alphanumeric string, prepended by `-`)
    * `B` $\Rightarrow$ _optional_ Build metadata (alphanumeric string, prepended by `+`)

---

# Versioning in the real world
## [Semantic Versioning (SemVer)](https://semver.org/) overivew

* Software using Semantic Versioning **MUST** *declare a public API*.
This API could be declared in the code itself or exist strictly in documentation.
However it is done, it *should be precise and comprehensive*.
* Once a versioned package has been released, the contents of that version **MUST NOT** *be modified*.
Any modifications **MUST** *be released as a new version*.
* A normal version number MUST take the form `X.Y.Z` where `X`, `Y`, and `Z` are *non-negative integers*, and **MUST NOT** *contain leading zeroes*.
* `X` is the major version, `Y` is the minor version, and `Z` is the patch version.
Each element **MUST** *increase numerically*.

---

# Versioning in the real world
## [Semantic Versioning (SemVer)](https://semver.org/) criteria

* Patch version `Z` **MUST** be *incremented if only backwards compatible bug fixes are introduced*.
A bug fix is defined as an internal change that fixes incorrect behavior.
* Minor version `Y` **MUST** be incremented if *new, backwards compatible functionality is introduced* to the public API.
    * It **MUST** be incremented if *any public API functionality is marked as deprecated*.
    * It **MAY** be incremented if *substantial new functionality* or improvements are introduced within the private code.
    * It **MAY** include patch level changes.
    * Patch version **MUST** *be reset to 0* when minor version is incremented.
* Major version `X` **MUST** be incremented if any *backwards incompatible changes* are introduced to the *public API*.
    * It `MAY` *include minor and patch level changes*.
    * Patch and minor version **MUST** *be reset to 0* when major version is incremented.

---

# Versioning in the real world
## [Semantic Versioning (SemVer)](https://semver.org/) details

* Version number `0.1.0` is the __minimum__ (i.e. first) one

* Major version zero (`0.y.z`) is for *initial development*: __anything may change at any time__
    * the public API should _not_ be considered stable

* Version `1.0.0` __defines the public API__ (or at least its first version)
    * the way in which the version number is incremented after this release is dependent on how the public API changes

* A *pre-release* version **MAY** be denoted by *appending a hyphen and a series of dot separated identifiers* immediately following the patch version
    * identifiers **MUST** comprise *only ASCII alphanumerics* and *hyphen* `[0-9A-Za-z-]`.
    * this may be used to mark _alpha_ releases, _beta_ releases, or _release candidates_

* *Build metadata* **MAY** be denoted by *appending a plus sign* and a series of dot separated identifiers immediately following the patch or pre-release version
    * identifiers **MUST** comprise *only ASCII alphanumerics and hyphen* `[0-9A-Za-z-]`.
    * this may be used to keep track of from which commit the version was built

---

# Versioning in the real world

- E.g. [NumPy](https://pypi.org/project/numpy/#history)
    - notice Git tags: <https://github.com/numpy/numpy/tags>

- E.g. [Kivy](https://pypi.org/project/Kivy/#history)
    - notice Git tags: <https://github.com/kivy/kivy/tags>

---

## The importance of a versioning methodology

**Think** *before* choosing a versioning schema, and then **be consistent**

* *Semantic versioning is warmly recommended*
    * Can be *integrated with the DVCS*!
    * Dates can be added (e.g. in the pre-release or build-metadata sections)

* *Codenames* can be used informally
    * For internal subprojects
    * As part of product promotion or for commercial activities 

* *Dates* may make sense for projects with fast and steady development
    * Possibly as part of a Semantic Versioned project
    * Dates are useful as part of a *better versioned* system

---

## DVCS-based versioning

* The underlying state of the *DVCS* can be used to assign version numbers to the software

* The practice can change, but consider for instance a case in which:
    * Manually added **tags** *identify versions*
        * And are in `X.Y.Z` format
    * An automated system searches for the _closest_ past tag `T`
        * if no tag is found, then `T=0.1.0`
        * If the current commit is tagged, then the version is `T`
        * Otherwise, if C is the count of intermediate commits and `H` the current hash, it is `T-C+H`
    * *Automatically generates a SemVer compatible version!*

---

## Commit message-based versioning

What do we need commit messages for?

{{% fragment %}}
Identify what is *different between changes*
{{% /fragment %}}

{{% fragment %}}
But isn't this essentially what _DVCS_ is about?
{{% /fragment %}}

{{% fragment %}}
### Idea

find a way to write *conventional* commit messages such that some _automatic tool_ can understand whether a new version should be released
{{% /fragment %}}

{{% fragment %}}
Put humans and sentiments out of the loop
{{% /fragment %}}

---

## Conventional commits

One of the possible ways to write standardized commits -- <https://www.conventionalcommits.org/>

Heavily inspired by *the Angular convention*: https://bit.ly/3VnAp4T

Format (optional parts in `[`square brackets`]`):

```text
type[(scope)][!]: description

[body]

[BREAKING CHANGE: <breaking change description>]
```

* `type`: *what the commit introduces*
    * Can differ among projects
    * `fix` (bug fix, no API change) and `feat` (new feature) always present
    * common optional types: `build`, `chore`, `ci`, `docs`, `style`, `refactor`, `perf`, `test`
* Optionally, the `scope` identifies the *module* of the software that was changed
* **Breaking changes** are identified by a `!` before the `:` and/or by a description in the footer of the commit after `BREAKING CHANGE: `

---

## Semantic release

### Idea

Assuming a conventional way to commit, use the information to understand *when* and *how* to release

### Practice

1. Decide *which branch* should be looked at for triggering releases
2. Define which *kind of release should be associated with which kind of commit*
    * Rules can be custom per-project, as far as they are consistent
    * e.g., `fix` and `docs` are `PATCH`, `feat` are `MINOR`, **Breaking changes** are `MAJOR`
    * Usually the commit *type* is relied upon, but the *scope* may be used as well
3. Scan all commits from the *last tag*, searching for the "largest" version change
4. If *at least one* version change was found, and this is still the *last commit* on the branch triggering releases,
create a release tag and perform the release procedure

---

## Automatic Semantic Release with `semantic-release`

An implementation of Semantic release: <https://github.com/semantic-release/semantic-release>

* Automatically __computes__ the _version number_ after commit & push
* Automatically __generates__ commit-based _release notes_
* Automatically __runs__ the _publishing commands_

### Example of projects using `semantic-release`

* [Alchemist](https://github.com/AlchemistSimulator/Alchemist)
* [2P-Kt](https://github.com/tuProlog/2p-kt)

---

{{% section %}}

## Check your understanding (pt. 1)

- In the context of SE, what is versioning?
- At what levels can version occur?
- What are the admissible scopes for software versioning?
- In the context of software versioning, what is code naming? What's its purpose?
- What are the versioning approaches you are aware of?
- Provide an overview of date-based versioning: purpose, functioning, pros, and cons
- Provide an overview of unary numbering (in the context of software versioning): purpose, functioning, pros, and cons
- Provide an overview of semantic versioning: purpose, functioning, pros, and cons
- How can one tie semantic versioning to DVCS commits?

---

## Check your understanding (pt. 2)

- In the context of DVCS, what are conventional commits? What's their purpose?
- In the context of conventional commits, what is a `breaking change`?
- In the context of conventional commits, what is a `feat`?
- In the context of conventional commits, what is a `fix`?
- In the context of conventional commits, what is a `chore`?

---

## Check your understanding (pt. 3)

- In the context of semantic versioning, what is the difference among a major, minor, or patch change?
- What is the idea behind semantic release?
- How are semantic versioning, conventional commits, and semantic release related?
- Suppose that, in your Python project, you add one more public method to a class or module. 
    + Is this a major, minor, or patch change?
- Suppose that, in your Python project, you add one more private method to a class or module and you use it inside another public function of that class or module. 
    + Is this a major, minor, or patch change?
- Suppose that, in your Python project, you rename (all occurrences of) a public function. 
    + Is this a major, minor, or patch change? 
- Suppose that, in your Python project, you rename (all occurrences of) a private function. 
    + Is this a major, minor, or patch change? 
- Suppose that, in your Python project, you rename (all usages of) a public function's parameter name. 
    + Is this a major, minor, or patch change? 
- Suppose that, in your Python project, you rename (all usages of) a private function's parameter name. 
    + Is this a major, minor, or patch change? 
- Suppose that, in your Python project, you rename (all occurrences of) a public class. 
    + Is this a major, minor, or patch change? 
- Suppose that, in your Python project, you rename (all usages of) a public class's constructor's parameter name. 
    + Is this a major, minor, or patch change? 

---

## Check your understanding (pt. 4)

- Suppose that, in your Python project, there's function f which is slow. After some edits to its body, you manage to make it much faster. 
    + Is this a major, minor, or patch change? 
- Suppose that, in your Python project, you add one more public method to a class or module. You commit the changes using conventional commit. 
    + What type would you use for the commit?
- Suppose that, in your Python project, you add one more private method to a class or module and you use it inside another public function of that class or module. You commit the changes using conventional commit. 
    + What type tag would you use for the commit?
- Suppose that, in your Python project, you rename (all occurrences of) a public function. You commit the changes using conventional commit.
    +  What type would you use for the commit? 
- Suppose that, in your Python project, you rename (all occurrences of) a private function. You commit the changes using conventional commit. 
    + What type would you use for the commit? 
- Suppose that, in your Python project, you rename (all usages of) a public function's parameter name. You commit the changes using conventional commit. 
    + What type would you use for the commit? 
- Suppose that, in your Python project, you rename (all usages of) a private function's parameter name. You commit the changes using conventional commit. 
    + What type would you use for the commit? 

---

## Check your understanding (pt. 5)

- Suppose that, in your Python project, you rename (all occurrences of) a public class. You commit the changes using conventional commit. 
    + What type would you use for the commit? 
- Suppose that, in your Python project, you rename (all usages of) a public class's constructor's parameter name. You commit the changes using conventional commit. 
    + What type would you use for the commit? 
- Suppose that, in your Python project, there's function f which is slow. After some edits to its body, you manage to make it much faster. You commit the changes using conventional commit. 
    + What type would you use for the commit? 
- Suppose your Python project is currently at version `1.2.3`. You add one more public method to a class or module. 
    + What should be the next version number if this change is going to be released immediately?
- Suppose your Python project is currently at version `1.2.3`. You add one more private method to a class or module and you use it inside another public function of that class or module. 
    + What should be the next version number if this change is going to be released immediately?
- Suppose your Python project is currently at version `1.2.3`. You rename (all occurrences of) a public function. 
    + What should be the next version number if this change is going to be released immediately?
- Suppose your Python project is currently at version `1.2.3`. You rename (all occurrences of) a private function. 
    + What should be the next version number if this change is going to be released immediately?
- Suppose your Python project is currently at version `1.2.3`. You rename (all usages of) a public function's parameter name. 
    + What should be the next version number if this change is going to be released immediately?
- Suppose your Python project is currently at version `1.2.3`. You rename (all usages of) a private function's parameter name. 
    + What should be the next version number if this change is going to be released immediately?

---

## Check your understanding (pt. 6)

- Suppose your Python project is currently at version `1.2.3`. You rename (all occurrences of) a public class. 
    + What should be the next version number if this change is going to be released immediately?
- Suppose your Python project is currently at version `1.2.3`. You rename (all usages of) a public class's constructor's parameter name. 
    + What should be the next version number if this change is going to be released immediately?
- Suppose your Python project is currently at version `1.2.3`. There's function f which is slow. After some edits to its body, you manage to make it much faster. 
    + What should be the next version number if this change is going to be released immediately?
- Since the last release (`1.2.3`), your semantic-versioned project's main branch contains the following commit types: `fix`, `fix`, `fix`. 
    + Should you release now, what's the next version number?
- Since the last release (`1.2.3`), your semantic-versioned project's main branch contains the following commit types: `fix`, `feat`, `feat`.  
    + Should you release now, what's the next version number?
- Since the last release (`1.2.3`), your semantic-versioned project's main branch contains the following commit types: `feat`, `feat`, `feat`.  
    + Should you release now, what's the next version number?
- Since the last release (`1.2.3`), your semantic-versioned project's main branch contains the following commit types: `chore`, `feat!`, `fix`.  
    + Should you release now, what's the next version number?
- Since the last release (`1.2.3`), your semantic-versioned project's main branch contains the following commit types: `fix`, `feat!`, `feat`.  
    + Should you release now, what's the next version number?

{{% /section %}}

---

{{% import path="reusable/back.md" %}}