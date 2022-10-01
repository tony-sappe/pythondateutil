# Python Date Utilities

Code originally found on [SourceForge](https://sourceforge.net/projects/pythondateutil/) and all credit goes to [Phil Schwartz](https://sourceforge.net/u/phil_schwartz/profile/)


Archived site linked to the code: [arch:holidays.mailzilla.net](https://web.archive.org/web/20120906015624/http://holidays.mailzilla.net/)

## Why
After using the library it became apparent that discrepancies existed. Somewhere there was a bug or a miscalculation. It was initially observed when converting between Julian and Hebrew. The first step for fixing the code was improving the format so it could be parsed by linters. Further inspection led to a rounding issue in `hebrew_delay_1()` which lead to incorrect dates. In the spirit of Free Software the code is now re-shared on Github to hopefully disseminate Phil's code to a wider audience for years to come.


[Original project README](ORIG_README.md)
