# Python Date Utilities

This source code was originally found on [SourceForge](https://sourceforge.net/projects/pythondateutil/) and all credit goes to [Phil Schwartz](https://sourceforge.net/u/phil_schwartz/profile/)


Archived site linked to the code: [arch:holidays.mailzilla.net](https://web.archive.org/web/20120906015624/http://holidays.mailzilla.net/)


## Why
Research for a calendar project lead to http://www.fourmilab.ch/documents/calendar/ which is a very useful and well done project.
There was a desire to find comparable Python code. When searching for existing Python libraries a number of good projects were found.
However, Phil Schwartz's Python Date Utilities is a solid reproduction of the JavaScript code.


The code was written for Python2. It was trivial to make the minor edits to convert to Python3. (print statements -> print functions)


After using the library it became apparent that discrepancies existed. Somewhere there was a bug or a miscalculation.
It was initially observed when converting between Julian and Hebrew.
Combing through the code surfaced a rounding issue in `hebrew_delay_1()` which created incorrect dates.


The code is now re-shared on Github to hopefully disseminate Phil's code to a wider audience for years to come.
This is Free Software: please use, modify, and share.


[Original project README](ORIG_README.md)
