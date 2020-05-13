
### What is Project Euler?

Project Euler ([projecteuler.net](http://projecteuler.net)) is a series of challenging mathematical/computer programming problems that will require more than just mathematical insights to solve. Although mathematics will help you arrive at elegant and efficient methods, the use of a computer and programming skills will be required to solve most problems.

### What is projecteuler-solutions?

As the name suggests, projecteuler-solutions is a collection of solutions for site Project Euler. This site aims to provide complete and accurate solution listings for Project Euler.

### What is the purpose of this site?

After you struggle for hours or days on a difficult problem, you may eventually give up (after all, the world would be a strange place if people never gave up on a problem). At this point, you have two options:

* Without a solution, you leave feeling frustrated; you feel as if all your effort had been for nothing. With no way to check the right answer, you don't know how close you were to the solution or where you had gone wrong. If the solution required advanced techniques unfamiliar to you, you would have had no way of knowing. In the end, you have learned nothing, leaving without even the gratification of having figured out the problem.


* With a solution, you can compare your method with the correct solution, perhaps figure out what you did wrong. Alternatively, you can peek at the solution as a sort of 'hint' -- that is, knowing the solver's general approach, figure out the details of his solution, then code the solution yourself. Either way, you have gained from this problem -- as much as you would have gained had you solved the problem completely independently.

In the end, the purpose of Project Euler isn't to compete for rankings. The main purpose of the activity is to learn and improve yourself in a challenging and fun way. If you need to 'cheat' in order to learn from and enjoy the problems, so be it.

### Where are the solutions / How do I use this site?

Projecteuler-solutions provides merely a list of answers -- that is, it does not provide solutions or code for individual problems. The link to the list of answers can be found at the top of this page.

With the numerical answers, you have access to the official forums, in which you can access dozens of solutions in numerous different programming languages, often using several very different approaches. By unlocking this valuable resource for you, Projecteuler-solutions hopes that you will be able to get more out of Project Euler.


### What about cheating?

Of course, it is possible for one to mindlessly copy and paste solutions one by one into Project Euler to gain ranks. Obviously, this is quite pointless, as Project Euler ranks can gain you nothing in the real world. Your account is likely to get banned, and you are only cheating yourself of mathematical learning.

### An answer is missing / incorrect!

If you have the answer to a problem whose answer we do not yet have, or notice that an existing answer is incorrect, we would love to hear from you! Either create an issue on this repository, or email me at **arpitmishra0891@gmail.com**. I will verify the answer and update the solutions as soon as possible.


**New implementation** is welcome! For example, new solutions for a problem, different representations for a graph data structure or algorithm designs with different complexity.

**Improving comments** and **writing proper tests** are also highly welcome.

### Contribution

We appreciate any contribution, from fixing a grammar mistake in a comment to implementing complex algorithms. Please read this section if you are contributing your work.
Please help us keep our issue list small by adding fixes: #{$ISSUE_NO} to the commit message of pull requests that resolve open issues. GitHub will use this tag to auto close the issue when the PR is merged.

#### Coding Style

We want your work to be readable by others; therefore, we encourage you to note the following:

- Please write in Python 3.7+.  __print()__ is a function in Python 3 so __print "Hello"__ will _not_ work but __print("Hello")__ will.
- Please focus hard on naming of functions, classes, and variables.  Help your reader by using __descriptive names__ that can help you to remove redundant comments.
  - Single letter variable names are _old school_ so please avoid them unless their life only spans a few lines.
  - Expand acronyms because __gcd()__ is hard to understand but __greatest_common_divisor()__ is not.
  - Please follow the [Python Naming Conventions](https://pep8.org/#prescriptive-naming-conventions) so variable_names and function_names should be lower_case, CONSTANTS in UPPERCASE, ClassNames should be CamelCase, etc.



- We encourage the use of Python [f-strings](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python) where the make the code easier to read.



- Please consider running [__psf/black__](https://github.com/python/black) on your Python file(s) before submitting your pull request.  This is not yet a requirement but it does make your code more readable and automatically aligns it with much of [PEP 8](https://www.python.org/dev/peps/pep-0008/). There are other code formatters (autopep8, yapf) but the __black__ style is now the recommendation of the Python Core Team. To use it,

  ```bash
  pip3 install black  # only required the first time
  black .
  ```

- All submissions will need to pass the test __flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics__ before they will be accepted so if possible, try this test locally on your Python file(s) before submitting your pull request.

  ```bash
  pip3 install flake8  # only required the first time
  flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
  ```



- Original code submission require docstrings or comments to describe your work.

- More on docstrings and comments:

  If you are using a Wikipedia article or some other source material to create your algorithm, please add the URL in a docstring or comment to help your reader.

  The following are considered to be bad and may be requested to be improved:

  ```python
  x = x + 2	# increased by 2
  ```

  This is too trivial. Comments are expected to be explanatory. For comments, you can write them above, on or below a line of code, as long as you are consistent within the same piece of code.

  We encourage you to put docstrings inside your functions but please pay attention to indentation of docstrings. The following is acceptable in this case:

  ```python
  def sumab(a, b):
      """
      This function returns the sum of two integers a and b
  	  Return: a + b
      """
      return a + b
  ```

- Write tests (especially [__doctests__](https://docs.python.org/3/library/doctest.html)) to illustrate and verify your work.  We highly encourage the use of _doctests on all functions_.

  ```python
  def sumab(a, b):
      """
      This function returns the sum of two integers a and b
  	  Return: a + b
      >>> sumab(2, 2)
      4
      >>> sumab(-2, 3)
      1
      >>> sumab(4.9, 5.1)
      10.0
      """
      return a + b
  ```

  These doctests will be run by pytest as part of our automated testing so please try to run your doctests locally and make sure that they are found and pass:

  ```bash
  python3 -m doctest -v my_submission.py
  ```

  The use of the Python builtin __input()__ function is **not** encouraged:

  ```python
  input('Enter your input:')
  # Or even worse...
  input = eval(input("Enter your input: "))
  ```

  However, if your code uses __input()__ then we encourage you to gracefully deal with leading and trailing whitespace in user input by adding __.strip()__ as in:

  ```python
  starting_value = int(input("Please enter a starting value: ").strip())
  ```

  The use of [Python type hints](https://docs.python.org/3/library/typing.html) is encouraged for function parameters and return values.  Our automated testing will run [mypy](http://mypy-lang.org) so run that locally before making your submission.

  ```python
  def sumab(a: int, b: int) --> int:
    pass
  ```



- [__List comprehensions and generators__](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) are preferred over the use of `lambda`, `map`, `filter`, `reduce` but the important thing is to demonstrate the power of Python in code that is easy to read and maintain.



- Avoid importing external libraries for basic algorithms. Only use those libraries for complicated algorithms.
- If you need a third party module that is not in the file __requirements.txt__, please add it to that file as part of your submission.

#### Other Standard While Submitting Your Work

- File extension for code should be `.py`. Jupiter notebook files are acceptable in machine learning algorithms.
- Strictly use snake_case (underscore_separated) in your file_name, as it will be easy to parse in future using scripts.
- Please avoid creating new directories if at all possible. Try to fit your work into the existing directory structure.
- If possible, follow the standard *within* the folder you are submitting to.

