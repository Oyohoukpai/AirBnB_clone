    AirBnB Clone - The Console


Air bnb clone.


   Table of Contents.

- Description

- Purpose

- Requirements

- File Structure

- Usage Examples

- Bugs

- Authors

- License

- Description.



   Purpose.

The purpose of this project is to understand how to:


- create a Python package.

- create a command interpreter using the cmd module.

- serialize and deserialize a Class.

- write and read a JSON file.

- manage datetime

- use *args and **kwargs

- handle named arguments in a function

- HTML and CSS concepts

Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!


Before developing a big and complex web application, we will build the front end step-by-step.


The first step is to “design” / “sketch” / “prototype” each element:


- Create simple HTML static pages

- Style guide

- Fake contents

- No Javascript

- No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

3Learning Objectives

- What is HTML

- How to create an HTML page

- What is a markup language

- What is the DOM

- What is an element / tag

- What is an attribute

- How does the browser load a webpage

- What is CSS

- How to add style to an element

- What is a class

- What is a selector

- How to compute CSS Specificity Value

- What are Box properties in CSS

     #Requirements

- PYTHON SCRIPT REQUIREMENTS

~ Allowed editors: vi, vim, emacs

~ the first line of all files should be exactly #!/usr/bin/python3

~ all code should use the PEP8 style (version 1.7.*)

~ all files must be executable

~ all files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)

#PYTHON TEST CASE REQUIREMENTS

~ all test files should be in the folder tests

~ all test files should be text files (extension: .txt)

~ all test files should be executed using the command python3 -m doctest ./tests/*

~ all modules should have documentation python3 -c 'print(__import__("my_module").__doc__)'

~ all functions (inside and outside of classes) should have documentation python3 -c 'print(__import__("my_module").my_funct\ ion.__doc__)'

#General

~ Allowed editors: vi, vim, emacs

~ All your files should end with a new line

~ A README.md file, at the root of the folder of the project, is mandatory

~ Your code should be W3C compliant and validate with W3C-Validator

~ All your CSS files should be in styles folder

~ All your images should be in images folder

~ You are not allowed to use !important and id (#... in the CSS file)

~ You are not allowed to use tags img, embed and iframe

~ You are not allowed to use Javascript

~ Current screenshots have been done on Chrome 56 or more.

~ No cross browsers

~ You have to follow all requirements but some margin/padding are missing - you should try to fit as much as you can to screenshots

~ Usage Examples for console

* Interactive Mode

* ~/me$ ./console.py

* (hbnb) help


Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
~/me$
Non-Interactive Mode
~/me$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)

~/me$ cat test_help
help
~/me$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
~/me$
Bugs
At this time, there are no known bugs.

License
AirBnB Clone is open source and free to download and use
