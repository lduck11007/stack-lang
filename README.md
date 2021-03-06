<img align="left" src="icon.ico">

# MontiLang

An imperative stack-based programming language developed in python.

# About
Monti is a stack-based language revolving around imperative commands to manipulate the stack. 

# Current State
Some of the features that are currently implemented are as follows:

* Multiple Data types and type conversion
* Common operators (`+`, `-`, `*`, `%`, `/`, etc.)
* Multi line comments
* Nested loops and statements (`FOR`, `WHILE`, `IF`)
* Stack manipulation commands (`SWAP`, `ROT`, `NIP`, `POP`, `DUP`, `TRIM`)
* Equality, inequality and other operators (`==`, `>`, `<=`, etc.)
* User input
* Integer and string manipulation
* User defined commands
* And/Or/Not statements 
* Preprocessor statements and C++ style constants with `&DEFINE` commands
* Support for Multiple files with `&INCLUDE` commands
* Arrays

The following will be coming soon:

* Additional data types and operators

# Installation

The simplest way to use MontiLang is to download the binaries from the [Releases](https://github.com/lduck11007/MontiLang/releases) page. Alternatively, you can download and build from the source code with the instructions below. 

The easiest way to compile and use Monti is through the python package 'Pyinstaller'. Install Pyinstaller from PyPi and download the MontiLang source code.

Note: It is recomended that you build from source, as it is very easy, and gives full access to newer features that have not been added to release yet.

**On windows:**  

install [mysysgit](https://gitforwindows.org/), or download source files directly. 

    python -m pip install pyinstaller
    git clone https://github.com/lduck11007/MontiLang.git
    cd MontiLang/src
    pyinstaller --icon=../icon.ico main.py -n monti
    SETX /M path "%path%;C:\[path_to_directory]\MontiLang\src\dist\monti"

**On Linux:** 

use `pip`, or the built-in package manager for your distro to install pyinstaller. If this does not work, install from the [Pyinstaller releases](https://github.com/pyinstaller/pyinstaller/releases) and run `setup.py`, or run straight from the source code from `pyinstaller.py`. 

    git clone https://github.com/lduck11007/MontiLang.git
    cd /MontiLang/src
    pyinstaller icon=../icon.ico main.py -n monti
    PATH=/path/to/location:$PATH


# Usage:
To interpret a Monti file, use 

    monti [file] <optional flags>

If no file is specified, Monti will launch into an interactive shell

Including the the `-c` flag will cause the program to not run, but will preprocess and print the source code as it is read by the interpreter

# Examples

Example program that takes an input as a number, and prints that far into the Fibonacci sequence.

        /# Test Fibonacci program #/
        |Enter length of sequence: | INPUT NIP VAR loop .

        0 VAR a .
        1 VAR b .

        FOR loop
            a b + VAR c .
            a PRINT .
            b VAR a .
            c VAR b .
        ENDFOR

FizzBuzz: Program that loops through numbers 1-100, prints 'fizz' if it is a multiple of 3, 'buzz' if a multiple of 5, and 'fizzbuzz' if both.

        &DEFINE LOOP 100&
        1 VAR i .

        FOR LOOP
            || VAR ln .
            i 5 % 0 == 
            IF : .
                ln |Buzz| + VAR ln .
            ENDIF
            i 3 % 0 ==
            IF : .
                ln |Fizz| + VAR ln .
            ENDIF
            ln || ==
            IF : .
                i PRINT .
            ENDIF
            ln || !=
            IF : .
                ln PRINT .
            ENDIF
        i 1 + VAR i .
        ENDFOR
See the `Documentation.mt` file in `/examples` for a more detailed explanation of language features.

Help contribute to MontiLang, add examples on rosettacode at https://rosettacode.org/wiki/Category:MontiLang


### Extras

#### Why MontiLang is better than Python

##### Better floating point accuracy

**Python:**
```python
>>>0.1 + 0.2
0.30000000000000004
```

**MontiLang:**
```nginx
>>>0.1 0.2 + PRINT .
0.3
```

##### Easier use of system commands

**Python:**
```python
from os import system
command = raw_input()
system(command)
```

**MontiLang:**
```nginx
INPUT CMD
```

##### Automatic int/float conversion

**Python:**
```python
>>>print 1 / 2
0
# Or:
>>>from __future__ import division
>>>print 1 / 2
0.5
```

**MontiLang:**
```nginx
>>>1 2 / PRINT .
0.5
```
