+++

title = "QA, reproducibility, TDD"
description = "QA, reproducibility, TDD"
outputs = ["Reveal"]

+++

# QA, reproducibility, TDD

{{% import path="reusable/header-dp.md" %}}

---

## Quality assurance

As any engineered product, software should be *subject to quality assurance control*.

* Would you drive a car that has not been succefully passed its *quality control*?
* What does it mean that a car **passed** its *quality control checks*?
  * What does it mean for a bridge?
  * What does it mean for a chair?
  * What does it mean for a robot?
  * What does it mean for a medical software?

---

## Testing: criteria

Verify that the software meets quality criteria.

* **Functional** criteria:
  * Does *what* we expect it to do?
    * Does the software produce the expected results?
* **Non-functional** criteria:
  * Does it do it *how* we want it?
    * Is it secure?
    * Are performance acceptable?

---

## Automated vs. manual

Running an application manually is a form of testing: *exploratory testing*.
* Done **without a plan**

If there is a plan that can be followed step-by-step, then *there is a program that can do it for you*
* If a program can do it for you, the it *should* do it for you

---

## Testing scope

As any engineering product, software can be tested at different levels of abstraction.
* **Unit** testing: test *single software components*
  * Is this `class` behavior the expected one?
  * Is this *suspension spring* behavior the expected one?
  * Is this *steel rod* mechanical properties the expected ones?
* **Integration** testing: test *an entire subsystem*, with *multiple components*
  * Is this *OCR server* behavior the expected ones?
  * Is this *engine*  working as expected?
  * Is this *span of a bridge* working correctly?
* **End-to-end** (or **acceptance**) testing: test *an entire system*
  * Is this whole application functional?
  * Is the car lapping under 2 minutes?
  * Does the bridge work nominally with high traffic and strong wind?

A well-maintained engineering product must have tests at all granularity levels

---

## Reproducibility

**Reproducibility** is **central** for testing

(true for any engineering, but in particular for software)

* *Tests should always provide the same results*
  * Tests that work sometimets but sometimes not are called *flaky tests*
* Tests should be *self-contained* (they should not depend on the results of previous tests)
* *Random* events can be tested by *seeding* the random generators

Would you be comfortable with a car that passes the crash test 99.9% of time, but on the 0.1% of the cases fails unexplicably?

---

## Test plan

Testing should be *planned for in advance*.

A good test plan can guide the development, and should be ready *early* in the project.

When designing cars,
the crash testing procedure,
the engine test bench,
and so on are prepared well before the car prototype is ready!

---

## Test-Driven Development (TDD)

The practice of:
* converting *requirements to (executable) test* cases
* preparing tests *before* development
* define the *expected behavior* via test cases
* track all development by *always testing all cases*

---

## Development cycle in TDD

1. *Capture* a requirement into an executable *test*
2. Run the test suite, the _new test should **fail**_
3. Fix the code so that the new test passes
4. Re-run the whole test suite, all tests should pass
5. Improve the quality as needed (refactor, style, duplication...)

---

## Injecting tests into projects started without tests

Developing without testing is *unsustainable*

Yet many software projects have no or minimal tests, as:

> We do not have time (or money) for testing

Beware: **testing saves times in the long run**, not testing is a *cost*!
* Untested software components are likely sources of *technical debt*

---

## A much better quotation

> we never have the money to do it *right* but somehow we always have the fucking money to do it *twice*

$---$ UserInputSucks (@UserInputSucks) [May 27, 2019](https://twitter.com/UserInputSucks/status/1132904286415929345)

---

## Tackling bugs and regressions

When a new **bug** (or a **regression**, namely, a feature that was working and it is now compromised) is discovered,
*resist the temptation to "fix" the issue right away*

* A fix without a test could be *insufficient*
* The "fix" could break another feature (create a *regression*)

A more **robust approach**:
1. Reproduce the issue in a *minimal context*
2. Create a new *test case* that *correctly fails*
3. *Fix* the issue, and make sure that the test now *passes*

Writing the test *after* the fix is much less effective.

See this [example interaction](https://github.com/AlchemistSimulator/Alchemist/issues/1002) of a reasonable way to tackle bugs.

---

## Testing software before it is ready: boundaries

Problem: how is it possible to test code that *does not exist*?

More in general: how to design a testbed for an engineering product that is not prototypied yet?

**clean boundaries**: the component must have a well-defined interface with the rest of the world.
In software, it means that the component has a *well-defined Application Programming Interface* (API).
Our artifact must be **modularized** correctly
(this also helps with development, simplicity and maintenance)

**clear scope**: well engineered (software) components usually *do one thing well*.
Test plans are conceived to test that the one thing is performed correctly.

---

## Testing software before it is ready: missing components

We can now *design our tests*,
but how to **run** them if *the components surrounding the tested one are not ready*?

How to test a new suspension system if the "surrounding" car is not ready (not even fully designed) yet?

How to test that our new rocket engine works as expected with no rocket?

How to test that our multi-engine rocket works as expected without payload?

---

{{< youtube "QMcj58TbsyU" >}}

---

{{< youtube "kchq9AGXsyA" >}}

---

## Testing software before it is ready: test doubles

The trick: *simulate components that are not ready yet*!

When writing software, components required for the execution that are not ready yet can be simulated
**if their API has been clearly defined**

The simulated component are called *test doubles*

* *dummy*: a (usually unimplemented) placeholder (e.g., unused mandatory argument)
  * a weight put on the suspension
* *stub*: partly implemented dummy
  * a system applying variable weight to the suspension
* *spy*: a stub that tracks information of the way it is being used
  * a dynamometer recording the suspension behavior under different conditions
* *mock*: a spy that expects to be used in a certain way, and fails if the expectation is unmet
  * a smart dynamometer that interrupts testing if the suspension behavior is not nominal
* *fake*: a fully implemented version of the component unsuitable for production
  * a car prototype

---

## Test doubles and development cost

> Why should the team "waste" time creating doubles instead of just writing the thing?

doubles are **cheaper**: dedicated libraries make doubles *implementation extremely quick*
* In Python, [`unittest.mock`](https://docs.python.org/3/library/unittest.mock.html) is included in the distribution, and [Doubles](https://doubles.readthedocs.io/en/latest/) is a valid alternative.

doubles are **simpler**: only encode the behavior required to check some part of the behaviour. The probability of them being bugged is lower. *Debugging is easier*.

---

## Checking (**un**)tested components: coverage

*Code coverage* is a set of **metrics** that measure how much of the source code of a program has been executed when testing.

Common metrics:
* *function coverage*: did the flow control get through this function?
* *branch coverage*: did the flow control tried both branches of this condition?
* *line-of-code coverage*: did the flow control get through this line during tests?
  * *most common*, usually combined with *branch coverage*

[Example coverage report](https://app.codecov.io/gh/AlchemistSimulator/Alchemist)

{{% fragment %}}
**WARNING**

* the actual information coverage provides is which code is **partly tested** or **untested**!
* we *know nothing of the testing quality* on the covered part, but that control flow goes through.
* *Useful* metric, but it cannot be the *only* metric to evaluate testing
  * Dramatically high coverage requirements may induce *metric-chasing*!
{{% /fragment  %}}

---

## Quality Assurance

*"It works"* **is _not_ good enough**

(besides, the very notion of "it works" is debatable)

* Software quality should be *continuously assessed*
* The assessment should *automatic* whenever possible
* **QA should be integrated in the build system!**
  * It is fine to *fail the build* if quality criteria are not met

---

## Quality Assurance: levels

* *Style* and *coherence*
* *Flawed programming* patterns
* Violations of the *DRY* principle
* **Runtime Testing**

---

## Quality Assurance: static analysis

Code analysis without execution is called *static analysis*.

Static analysis tools are often referred to as *linters*
(especially those providing auto-formatting tools)

**Idiomatic** and **standardized** code:
* reduces *complexity*
* improves *understandandability*
* prevents *style-changing commits* with *unintelligible diffs*
* lowers the *maintenance* burden and related *costs*
* simplifies *code reviews*
* improves *security*

In *Python*:
* [Mypy](http://mypy-lang.org/): static analysis for bug detection (requires [annotations](https://www.python.org/dev/peps/pep-0484/))
* [Pyflakes](https://github.com/PyCQA/pyflakes): effective programming, excluding style
* [Pylint](https://pylint.org/): reverse engineering via [Pyreverse](https://www.logilab.org/blogentry/6883), style (enforces [PEP8](https://www.python.org/dev/peps/pep-0008/)), and effective programming
* [Bandit](https://github.com/PyCQA/bandit): security scanner
* [Prospector](https://prospector.landscape.io/en/master): tool collection. Includes Pylint and Pyflakes, adds [PEP27](https://www.python.org/dev/peps/pep-0257/)-compliance checks for comments, complexity, packaging (via [pyroma](https://github.com/regebro/pyroma)), secrets leaking (via [dodgy](https://github.com/landscapeio/dodgy)), and unused code (via [vulture](https://github.com/jendrikseipp/vulture)) checks.

---

## Quality Assurance: flawed programming patterns

Identification and reporting of *patterns* known to be *problematic*

* Early-interception of *potential bugs*
* Enforce *good programming principles*
* Improves *performance*
* Reduces *complexity*
* Reduces *maintenance cost*

---

## Quality Assurance: violations of the DRY principle

Code *replicated* rather than *reused*

* improves *understandandability*
* Reduces *maintenance cost*
* simplifies *code reviews*

General advice: **never copy/paste** your code
* If you need to copy something, you probably need to *refactor* something

Multi-language tool: [Copy/Paste Detector (CPD)](https://pmd.github.io/latest/pmd_userdocs_cpd.html) (part of PMD)

---

## Additional checks and reportings

There exist a number of recommended services that provide additional QA and reports.

Non-exhaustive list:
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

## Unit testing in Python

An example repository: [https://github.com/DanySK/python-testing-101/tree/master/example-py-unittest](https://github.com/DanySK/python-testing-101/tree/master/example-py-unittest)

Try the following:
1. Clone the repository
2. Move into `example-py-unittest` folder
3. Run the tests with `python -m unittest discover` (option `-m` runs a module as script, `discover` is an option that instructs `unittest` to find and run all tests), observe the results
4. Introduce a bug in `calc.py` and re-run the tests. Observe the behavior

---

### Do it yourself!
1. Based on the project structure of the examplar, prepare a `complex.py` implementing a complex number
2. The class should support methods for adding, subtracting, multiplying, and dividing complex numbers. Create the number and implement them with `pass`
3. Prepare the test cases to verify that the behaviour is the intended one
4. Implement the methods!

**Notes**:
* A complex number can be modelled as a couple of real numbers, one for the real part, one for the imaginary part.
* Try to emulate the behavior of a number via [operator overloading](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)!
