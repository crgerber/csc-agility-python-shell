## Synopsis

CSC-AgilityShell is a Python REST API client. The REST method stubs are generated from the WADL file, but why stop there, the Python classes mapping the Agility Object Model are also generated using the html javadoc at https://<HOST>:8443/javadoc/scripting/allclasses-frame.html.

Used in a standalone application, AgilityShell is an interactive shell, built on top of IPython, leveraging IPython's autocomplete, interactive debugger, and interactive development features. Webservice endpoints are pre-loaded in memory as an object graph, with the agility (also aliased 'a') object as the root of the graph. Under each endpoint, all methods are listed with comprehensive documentation about the HTTP method (GET, POST, etc.), parameter names, and parameter types where applicable. The more documentation and metadata included in the WADL, the better AgilityShell method documentation gets.

Alternatively, AgilityShell can be imported by Python scripts and 3rd party applications as a python library, featuring a full REST client for Agility Platform. Including method stubs, object model and XML parser that unmarshals XML response into Python objects, and vice versa.


## Code Example


## Motivation

Providing API SDK on top of any comprehensive, fine grained API increases adoption and encourages automation of repetitive tasks, specially if the SDK is available in a high level language like Python

The Shell has a pluggable architecture, for example via the ssh plugin, it provides a method to execute shell scripts on compute instances, selectively, using the credentials from the Agility DB

The reporting feature provides a way to preserve the meta-state of an environment, before a major change for the purpose of generating diff reports

Building on top of the Agility Shell, it's straight forward to develop field test suites to verify system integrity for example through and after an upgrade

Last but not least, the shell is an interactive tool to learn the Agility REST API's, other than curl. One that would allow navigation and  full manipulation of the XML results

## Installation

AgilityShell depends on a couple of python libraries for XML parsing and handling iso-formatted dates in REST responses. Also one of the core dependencies of the interactive shell is IPython.

For convenience, a setup.py file is included in the root folder of the git repo. The setup.py files uses python setuptools to download dependencies via PyPi (Python Packaging Index). Don’t worry if you don’t have setuptools installed on your system, since the helper file ez_setup.py (also included in the repo) will install it for your platform.

That said, the only prerequisite is Python2.7 or later.

Clone the repo from github:

git clone https://github.com/csc/agility-python-shell.git

```sudo python setup.py install```
After successful installation of all dependencies, from the agility-python-shell root directory run:

```python agilityshell.py [-p path_to_configuration_file]```
If you don’t specify an alternative configuration file using the –p flag, the shell will look for the default configuration file with the name agilityshell.cfg in the current directory and use it to connect to the Agility Platform.

Dependencies are: Python2.7, python-lxml, and python-dateutil which you can install using python pip.

## API Reference


## Tests


## Contributors


## License
