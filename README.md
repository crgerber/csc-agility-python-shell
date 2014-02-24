## Synopsis

The Agility Shell is a CLI for Agility in the form of an interactive shell

It provides a scripting interface that feels natural for developers and system administrators


## Code Example

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Motivation

Providing API SDK on top of any comprehensive, fine grained API increases adoption and encourages automation of repetitive tasks, specially if the SDK is available in a high level language like Python

The Shell has a pluggable architecture, for example via the ssh plugin, it provides a method to execute shell scripts on compute instances, selectively, using the credentials from the Agility DB

The reporting feature provides a way to preserve the meta-state of an environment, before a major change for the purpose of generating diff reports

Building on top of the Agility Shell, it's straight forward to develop field test suites to verify system integrity for example through and after an upgrade

Last but not least, the shell is an interactive tool to learn the Agility REST API's, other than curl. One that would allow navigation and  full manipulation of the XML results

## Installation

Configure your agility instance in the agilityshell.cfg file and drop it on the shell root dir

Dependencies are: Python2.7, python-lxml, and python-dateutil which you can install using python pip.

## API Reference


## Tests


## Contributors


## License