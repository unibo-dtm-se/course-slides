
+++

title = "Continuous Integration"
description = "Make things work, keep them working, move fast"
outputs = ["Reveal"]

+++

# Continuous Integration

{{% import path="reusable/header-dp.md" %}}

---

# Continuous Integration

The practice of integrating code with a main development line **continuously**
<br>
_Verifying_ that the build remains intact
* Requires *build automation* to be in place
* Requires *testing* to be in place
* Pivot point of the *DevOps* practices
* Historically introduced by the extreme programming (XP) community
* Now widespread in the larger DevOps community

---

<!-- ## Microreleases and protoduction

* High frequency integration may lead to high frequency releases
    * Possibly, *one per commit*
    * Of course, *versioning* must be appropriate...

Traditionally, **protoduction** is jargon for a *prototype that ends up in production*

<table>
  <tbody>
    <tr>
      <td>
        <img src="protoduction.jpg" onerror="this.onerror=null; this.src='../../assets/protoduction.jpg'" width=90% />
      <td/>
      <td>

* Traditionally used with a *negative* meaning
    * It implied software
        * *unfinished*,
        * *unpolished*,
        * *badly designed*
    * Very common, unfortunately
* This is different in a continuously integrated environment
    * *Incrementality* is fostered
    * Partial features are *up to date* with the mainline

      <td/>
    </tr>
  </tbody> 
</table> -->

## What is integration in the first place?

1. Not just simply **merging** code from different *branches*/developers...

2. ... but actually also **building** the software, with all its *dependencies*...
    * restoring dependencies
    * compiling
    * linking
    * packaging

3. ... and **testing** the software
    * all sorts of *automated tests*: unit, integration, system, etc.
    * possibly, also *deployment* and *release* procedures 

4. for the sake of _checking_ that the software as a whole is still *working* despite the changes since the last release
  

5. possibly, doing further **adjustments** to the software *code* if necessary
    * e.g., if the component is _not working_ any more, or if the _tests are failing_, etc.
    * here code may also include *configuration* files or *build*, *test*, or *deployment* scripts

---

# The integration hell

* Traditional software development takes several months for *“integrating”* a couple of years of development
* The longer there is no integrated project, the higher the **risk**

<img src="integration-traditional.png" onerror="this.onerror=null; this.src='../../assets/integration-traditional.png'" width=40% />
$\Rightarrow$
<img src="integration-continuous.png" onerror="this.onerror=null; this.src='../../assets/integration-continuous.png'" width=40% />

---

## How to make the integration _continuous_?

1. __Repeat__ the integration process as _frequently as possible_
    * ideally, as frequently as _every commit_, in practice, as frequently as __every push__ to GitHub

2. This implies running _build_, _testing_, and _deployment_ processes __very frequently__ as well
    * which is only possible if the entire process is __automated__
      * which is only possible if __automatic tests_ are available, as well as _build automation_ scripts, and _automatic release/deployment_ scripts
    * of course, retrospective adjustments are _hard to automate_, and should be done _manually_

3. Do not rely on the assumption that developers will _always_ __remember__ to run these steps consistently before pushing
    * they will not, and they will forget to do it at some point
    * so we also need to _automate_ the __triggerig__ of the _build_, _testing_, and _deployment_ processes

4. Once the entire process is automated, there are __further benefits__:
    * integration _issues_ can be _spotted ASAP_
    * the process can be repeated on _different platforms_ (e.g. different OSs, and different versions of Python)
       - which is far more than what a developer can do on their own
    * emails and notifications can be sent upon _failures_ of the process

---

## Continous integration concept

* The build process should be *rich* (comprehensive), *fast*, and **automated**
* And run on _another machine_ (or VM) than the developer's one
    + this is to avoid the developer from being _unable to work_ while the build is running 
    + but also to ensure that the software runs _outside_ from the _developer's environment_
        - which increases the chances that the software will run on _other_ machines as well
    + to allow for testing the software onto many, _controlled environments_
        - which in turns allows for giving _compatibility guarantees_ to the customers/users

{{% multicol %}}
{{% col %}}
<img src="compiling.png" onerror="this.onerror=null; this.src='../../assets/compiling.png'" height=100% />
{{% /col %}}
{{% col %}}
{{<image src="./concept2.png" width="100%" alt="Continuous integration concept" >}}
{{% /col %}}
{{% /multicol %}}

---

## Continuous integration software

### Software that promotes CI practices should:

* Provide *clean environments* for compilation/testing
* Provide a *wide range* of environments
    * Matching the relevant specifications of the actual targets
* High degree of *configurability*
* Possibly, *declarative configuration*
* A *notification system* to alert about failures or issues
* Support for *authentication* and deployment to external services

---

## Continuous integration software

**Plenty** of technologies on the market

- [Circle CI](https://circleci.com/)
- [Travis CI](https://travis-ci.com/)
- [Werker](https://wercker.com/)
- [done.io](https://done.io/)
- [Codefresh](https://codefresh.io/)
- [Codeship](https://codeship.com/)
- [Bitbucket Pipelines](https://bitbucket.org/product/features/pipelines)
- [GitHub Actions](https://github.com/features/actions)
- [GitLab CI/CD Pipelines](https://docs.gitlab.com/ee/ci/pipelines/)
- [JetBrains TeamCity](https://www.jetbrains.com/teamcity)

> We will use __GitHub Actions__: GitHub integration, _free for FOSS_, multi-os OSs supported

---

# Core concepts

Naming and organization is variable across different technological, but *in general*:

* One or more **pipelines** can be associated to **events**
  * For instance, a *new commit*, an update to a *pull request*, or a *timeout*
* Every pipeline is composed of a **sequence** of **operations**
* Every **operation** could be composed of _sequential_ or _parallel_ **sub-operations**
* How many hierarchical levels are available depends on the specific platform
  * GitHub Actions: *workflow* $\Rightarrow$ *job* $\Rightarrow$ *step*
  * Travis CI: *build* $\Rightarrow$ *stage* $\Rightarrow$ *job*  $\Rightarrow$ *phase*
* Execution happens in a **fresh system** (virtual machine or container)
  * Often containers inside virtual machines
  * The specific point of the hierarchy at which the VM/container is spawned depends on the CI platform

---

## Pipeline design

In essence, designing a CI system is designing a software construction, verification, and delivery *pipeline*
with the abstractions provided by the selected provider.

1. **Think** of all the operations required starting from one or more *blank* VMs
    * OS configuration
    * Software installation
    * Project checkout
    * Compilation
    * Testing
    * Secrets configuration
    * Delivery
    * ...
2. **Organize** them in a dependency graph
3. **Model** the graph with the provided CI tooling

Configuration can grow complex, and is usually stored in a YAML file
<br>
(but there are exceptions, JetBrains TeamCity uses a Kotlin DSL).

---

## Pipeline design (abstract example)

![](./abstract-workflow.svg)

- Rectangles represent *operations*

---

## GitHub Actions (GHA): Structure

* **Workflows** are groups of one or many *jobs*
    - triggered by events such as: a developer _pushing_ on the repository, a _pull request_ being opened, a _timeout_, a _manual_ trigger, etc.
    - multiple workflows run in parallel, unless specified otherwise by whoever designed the workflows

* **Jobs** is a sequential list of logical *steps*
    * different jobs from the same workflow run in _parallel_, unless a _dependency_ among them is explicitly declared
       + in case of a dependency, the _dependent_ job will run _only after_ the dependency job is _completed successfully_
    * steps of the same job run in the _exact same order_ as they are defined in the job
    * each job runs inside a _fresh_ new __Virtual Machine__ (VM), with a _selectable OS_
        + most common development tools (e.g. Git, Python, Poetry, etc.) are pre-installed by default...
        + but further may be installed if needed (e.g. `MySQL`, `PostgreSQL`, etc.)
    * the VM is _destroyed_ after the job is completed
        + users can see the _logs_ of the job execution
        + any relevant data produced by the job must be explicitly saved _elsewhere_ (as part of the job), otherwise it will be lost
    * [IMPORTANT] jobs can be configured to run _multiple times_ with different OS/runtimes: this is the __matrix__ execution strategy

* **Steps** is just executing a _command_ in the _shell_ of the job's VM
    + e.g. cloning the repository via `git`
    + e.g. restoring Python dependencies via `poetry`
    + e.g. running the tests via `unittest`
    + e.g. releasing the software via `poetry`
    + e.g. doing some _automatic edit_ to the repository (such as updating the version number), then _committing_ and _pushing_ the change __automatically__


---

## GitHub Actions (practical example)

![](./actual-workflow.svg)

- Small rectangles represent *steps*
- Azure boxes represent *jobs*
- The whole is a *workflow*

---

## GitHub Actions: Configuration

- Workflows are configured in [YAML files](https://yaml.org/) located in the _default branch_ of the repository
  + in the `.github/workflows/` folder.

- One configuration file $\Rightarrow$ one workflow

- For security reasons,
workflows may need to get manually activated in the *Actions* tab of the GitHub web interface.
  + on a per-repository basis

---

## GitHub Actions: Runners

- Executors of GitHub actions are called *runners*
  + virtual machines (commonly hosted by GitHub)
    * with the GitHub Actions runner application installed.

> **Note**: the GitHub Actions application is open source and can be installed locally,
> creating "*self-hosted runners*". Self-hosted and GitHub-hosted runners can work together.

- Upon their creation, runners have a default environment
  + which depends on their *operating system*

- Documentation available at [https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#preinstalled-software](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#preinstalled-software)

---

## Convention over configuration

Several CI systems inherit the "*convention over configuration*" principle.

> GitHub actions **does not** adhere to the principle:
> if left unconfigured, the runner does nothing
> (it does not even clone the repository locally).

- __Probable reason__: Actions is an *all-round* repository automation system for GitHub,
  + not just a "plain" CI/CD pipeline
  + $\Rightarrow$ it can react to many different events, not just changes to the git repository history

---

## GHA: basic workflow structure

Minimal, simplified workflow structure:

```yaml
# Mandatory workflow name
name: Workflow Name
on: # Events that trigger the workflow
jobs: # Jobs composing the workflow, each one will run on a different runner
    Job-Name: # Every job must be named
        # The type of runner executing the job, usually the OS
        runs-on: runner-name
        steps: # A list of commands, or "actions"
            - # first step
            - # second step
    Another-Job: # This one runs in parallel with Job-Name
        runs-on: '...'
        steps: [ ... ]
```



---

## Workflow minimal example

```yaml
name: CI/CD
on: 
  push:
    branches: [ main ]
jobs:
  test:
    runs-on: ubuntu-latest
    name: Test on Linux
    timeout-minutes: 45
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Restore Python dependencies
        run: poetry install

      - name: Test
        shell: bash
        run: poetry run python -m unittest discover -v -s tests
```

[Consider `check.yml` file on the `calculator` repository](https://github.com/unibo-dtm-se/calculator/blob/master/.github/workflows/check.yml) for a more complete example

---

## GHA Steps: `run` vs `uses`

- `run`: run a command in the shell of the runner
  + e.g. `run: poetry install`
  + e.g. `run: python -m unittest discover -v -s tests`


- `uses`: run a *GitHub Actions' __action__*
  + e.g. [`actions/checkout@v4`](https://github.com/actions/checkout)
  + e.g. [`actions/setup-python@v5`](https://github.com/actions/setup-python)
  + e.g. [`actions/upload-artifact@v3`](https://github.com/actions/upload-artifact)
  + e.g. [`actions/download-artifact@v3`](https://github.com/actions/download-artifact)

### What is a GHA action?

- In the eyes of the GHA __user__: a _reusable_ and _parametric_ functionality which makes sense in the GHA ecosystem

- In the eyes of the GHA __developer__: a _GitHub repository_ the code to parametrise and reuse some functionality

---

## Checking out the repository

> By default, GitHub actions' *runners do **not** clone the repository*

(this is because actions may, sometimes, not need to access the code, e.g., when automating issues, projects, etc.)

### Cloning and checking out the repository is done via a dedicated action:

```yaml
name: Example workflow
on: 
  push:
    branches: [ main ]
jobs:
  permissions:
    contents: write # Give write (e.g. push) permissions to this Job (i.e. steps may perform changes to the repository it self)
  Explore-GitHub-Actions:
    - name: Check out repository code
      uses: actions/checkout@v4
      with:
        fetch-depth: 0 # Fetch all history for all branches and tags
        token: ${{ secrets.GITHUB_TOKEN }} # Use the GITHUB_TOKEN secret to clone, enabling future pushes in next steps
```

{{% fragment %}}

By default, only the last commit of the current branch is fetched by this action (*shallow cloning* has better *performance*)
* $\Rightarrow$ It may break operations that rely on the entire history!
    * e.g., computing the next version number depending on the last tag in the Git history
    * use `fetch-depth: 0` to fetch the entire history
* If you plan to be able to push changes to the repository, you need to 
    * provide a token with write permissions, e.g. `token: ${{ secrets.GITHUB_TOKEN }}`
      + secrets are explained a few slides later
    * if you use the `GITHUB_TOKEN` secret, you need to set the `permissions` field to `write` for the `contents` permission
      + this is because the default permission for the `GITHUB_TOKEN` secret are read-only

{{% /fragment %}}

---

## Writing outputs

Communication with the runner happens via *[workflow commands](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions)*
<br>
The simplest way to create outputs for actions is to print on standard output a message in the form:
<br>
`"{name}={value}"`
<br>
and redirect it to the end of the file stored in the `$GITHUB_OUTPUT` environment variable:
`echo "{name}={value}" >> $GITHUB_OUTPUT`

```yaml
name: Outputs
on: # ...
jobs:
  Build:
    runs-on: ubuntu-latest
    steps:
      - id: output-from-shell
        run: python -c 'import random; print(f"dice={random.randint(1, 6)}")' >> $GITHUB_OUTPUT

      - run: |
          echo "The dice roll resulted in number ${{ steps.output-from-shell.outputs.dice }}"
```

---

## Build matrix

Most software products are meant to be *portable*
* Across operating systems
* Across different frameworks and languages
* Across runtime configuration

A good continuous integration pipeline should test *all the supported combinations**
* or a sample, if the performance is otherwise unbearable

The solution is the adoption of a **build matrix**
* Build variables and their allowed values are specified
* The CI integrator generates the *cartesian product* of the variable values, and launches a build for each!
* Note: there is no built-in feature to exclude some combination
    * It must be done manually using `if` conditionals

---

## Build matrix in GHA

```yaml
name: Workflow with Matrix
on: # ...
jobs:
  test:
    strategy:
      fail-fast: false
      matrix:
        os:
          - ubuntu-latest
          - windows-latest
          - macos-latest
        python-version:
          - '3.10'
          - '3.11'
          - '3.12'
    runs-on: ${{ matrix.os }}
    name: Test on Python ${{ matrix.python-version }}, on ${{ matrix.os }}
    timeout-minutes: 45
    steps:
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install poetry
        run: pip install poetry
      
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Restore Python dependencies
        run: poetry install

      - name: Test
        shell: bash
        run: poetry run python -m unittest discover -v -s tests
```

---

## Private data and continuous integration

We would like the CI to be able to
* Sign our artifacts
* Delivery/Deploy our artifacts on remote targets

Both operations **require private information to be shared**

Of course, private data *can't be shared*
* Attackers may steal the identity
* Attackers may compromise deployments
* In case of open projects, attackers may exploit *pull requests*!
    * Fork your project (which has e.g. a secret environment variable)
    * Print the value of the secret (e.g. with `printenv`)

How to *share a secret* with the build environment?

---

## Secrets

Secrets can be stored in GitHub at the repository or organization level.

GitHub Actions can access these secrets from the context:
* Using the `secrets.<secret name>` context object
* Access is allowed only for workflows generated by local events
    * Namely, no secrets for pull requests

Secrets can be added from the web interface (for mice lovers), or via the GitHub CLI:

```bash
gh secret set TEST_PYPI_TOKEN -b "dhhfuidhfiudhfidnalnflkanjakl"
```

---

# Stale builds

1. Stuff *works*
2. *Nobody touches it* for months
3. Untouched stuff is now *borked*!

<br/>

* Connected to the issue of **build reproducibility**
    * The higher the build *reproducibility*, the higher its *robustness*
* The default runner configuration may change
* Some tools may become unavailable
* Some dependencies may get unavailable

**The sooner the issue is known, the better**

$\Rightarrow$ *Automatically run the build every some time* even if nobody touches the project
* How often? Depends on the project...
* **Warning**: GitHub Actions disables `cron` CI jobs if there is no action on the repository, which makes the mechanism less useful

---

## Additional checks and reportings

There exist a number of recommended services that provide additional QA and reports.

Non exhaustive list:
* [Codecov.io](https://codecov.io/)
    * Code coverage
    * Supports Jacoco XML reports
    * Nice data reporting system
* [Sonarcloud](https://sonarcloud.io/)
    * Multiple measures, covering reliability, security, maintainability, duplication, complexity...
* [Codacy](https://www.codacy.com/)
    * Automated software QA for several languages
* [Code Factor](https://www.codefactor.io/)
    * Automated software QA

---

## High quality FLOSS checklist

The [Linux Foundation](https://www.linuxfoundation.org/) [Core Infrastructure Initiative](https://www.coreinfrastructure.org/) created a checklist for high quality FLOSS.

**[CII Best Practices Badge Program https://bestpractices.coreinfrastructure.org/en](https://bestpractices.coreinfrastructure.org/en)**


* *Self-certification*: no need for bureaucracy
* Provides a nice *TODO list* for a high quality product
* Releases a *badge* that can be added e.g. to the project homepage

---

## Automated evolution

A full-fledged CI system allows reasonably safe *automated evolution of software*
<br>
At least, in terms of *dependency updates*

Assuming that you can *effectively intercept issues*,
here is a possible workflow for **automatic** dependency updates:

1. *Check* if there are new updates
2. *Apply* the update in a new branch
3. *Open* a pull request
4. *Verify* if changes break anything
    * If they do, manual intervention is required
5. *Merge*

---

## Automated evolution

**Bots** performing the aforementioned process for a variety of build systems exist.

They are usually integrated with the repository hosting provider

* Whitesource Renovate (Multiple)
    * Also updates github actions and Gradle Catalogs
* Dependabot (Multiple)
* Gemnasium (Ruby)
* Greenkeeper (NPM)

---

{{% import path="reusable/back.md" %}}