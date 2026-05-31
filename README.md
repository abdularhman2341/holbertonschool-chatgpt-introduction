# Holberton School - ChatGPT Introduction

## Description
This repository contains the tasks for the **ChatGPT Introduction** project. The main objective of this project is to learn how to effectively use ChatGPT as a tool to identify, debug, and fix errors in existing code samples, as well as to document code properly and implement error handling.

## Learning Objectives
* How to use AI to find bugs in code (Logic errors, infinite loops, typos).
* How to add missing features or conditions to existing code.
* How to properly document Python functions.
* How to implement error handling to prevent programs from crashing.

## Requirements
* All Python scripts are written to be executed on Ubuntu 20.04 LTS using Python3 (version 3.8.5).
* All Python scripts must be executable (`chmod +x`).
* The first line of all Python files should be exactly `#!/usr/bin/python3`.
* Code must follow the standard style guidelines.

## Project Files (Directory: `debugging`)

| File Name | Description |
| :--- | :--- |
| `factorial.py` | A Python script that calculates the factorial of a number. Fixed an infinite loop issue by properly decrementing the variable. |
| `print_arguments.py` | A Python script that prints arguments passed to it. Fixed to print only the arguments without the script name. |
| `change_background.html` | An HTML/JS file that changes the background color upon a button click. Fixed a typo in the button ID that prevented the script from working. |
| `mines.py` | A Python implementation of Minesweeper. Added a mechanism to detect when all non-mine cells have been revealed, thus winning the game. |
| `factorial_recursive.py` | A recursive factorial Python script. Added standard function documentation (description, parameters, and return values). |
| `checkbook.py` | A Python script simulating a checkbook. Implemented error handling (`try-except`) to prevent crashes when a user inputs non-numeric values. |
| `tic.py` | A Python implementation of Tic-Tac-Toe. Fixed logical bugs regarding winner declaration and added robust input validation to prevent crashes. |

## Author
Abdularhman asiri 
* Prepared for the Holberton School curriculum.
