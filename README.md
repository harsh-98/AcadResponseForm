# IITR Response Form AutoComplete
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This script is for autocompletion of the response form for professor. Since it is a very long process and someone of us don't have time and just want to move to the Subject Registration Section.Through this script the review for the professor can be automatically filled, though for the Subject Registration you have to do that at the official website .

It works with python2 as the used `mechanize` package is only available for python2.

## Install 

`git clone https://github.com/harsh-98/AcadResponseForm.git`

## SetUp

    pip install -r requirements.txt
    python2 acadresponseform.py {username}

### Option

    For Full-automated Script : 1
	`under fully-automatic, options are randomly selected`
    For Semi-automated Script: 0
	`Under semi-automatic, you can select the individual ranking for the professor`
-    Random : 0
-    Strongly Agree : 1 
-    Agree : 2 
-    Neutral :3
-    Disagree : 4
-    Strongly Disagree :5


## License

This code is in the public domain (see [UNLICENSE](UNLICENSE) for more details). This means you can use, modify, and distribute it without any restriction. I appreciate, but don't require, acknowledgement in derivative works.
`
