
# Basic set of software examples how to use uFR Series readers API

Software example written for Python. Shows basic usage of uFR Series reader's API.

Three basic usage software examples formed by difficulty level : Simplest, Simple and Advanced.

## Getting Started
 
Download project and run examples or explore source code.

Appropriate ufr-lib dynamic library (ufCoder-...) is mandatory for this project, choose it depending on platform and architecture.

### Prerequisites

* uFR series reader

* Python v3.5

* PyQt5 framework v5.6

### Installing

No installation needed.

## Usage

Example provides basic functionality, formed by difficulty level :

1. Simplest - getting card serial number (UID), reading and writing data by Linear functions,

2. Simple - expanded set of functions, use of reader and card keys, authentication methods, reader UI signals

3. Advanced - more functions added, like Block manipulation etc.

  ## Dependencies
  This example relies on our uFCoder library, depending on your platform and Python distribution you should edit the following lines: 
  For the <b> Simplest </b> example, edit line  <b>37</b> in <b> uFSimplest.py  </b>  file, so it corresponds to your plaftorm/Python distribution.
 E.g if you have 64bit Python on Windows, the following should be used 
 self.mySO = windll.LoadLibrary(os.getcwd() + '\\\ufr-lib\\windows\\\x86_64\\\uFCoder-x86_64.dll')'
 
 This change should also be applied to the line <b> 120 </b> in <b> uFCoderSimple.py  </b> for the <b> Simple </b> example, and line <b> 69 </b> in <b> ufadvanced/Functions.py </b> for the <b> Advanced </b> example.
 Note: this method of loading our libraries is deprecated and will be updated in the following updates of this example.
## License 

This project is licensed under the ..... License - see the [LICENSE.md](LICENSE.md) file for details
  
## Acknowledgments

* Purpose of this software demo is to provide additional info about usage of uFR Series API specific features.

* It is specific to mentioned hardware ONLY and some other hardware might have different approach, please bear in mind that.