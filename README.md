### Hexlet tests and linter status:
[![Actions Status](https://github.com/DyakonovVitaliy/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/DyakonovVitaliy/python-project-50/actions)

[![CI check](https://github.com/DyakonovVitaliy/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/DyakonovVitaliy/python-project-50/actions/workflows/main.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/91e160c526df83147845/maintainability)](https://codeclimate.com/github/DyakonovVitaliy/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/91e160c526df83147845/test_coverage)](https://codeclimate.com/github/DyakonovVitaliy/python-project-50/test_coverage)

# DESCRIPTION:

**Difference calculator**

Runs from the command line and calculates differences between two files with JSON and YAML extensions.

**Running help:**

`gendiff -h`

**Running the script with default settings:**

`gendiff <file_path1> <file_path2>`

**Comparing two flat JSON Files**

#### [![asciicast](https://asciinema.org/a/dHjq1kT79wh2Tufrx7gCbDzEf.svg)](https://asciinema.org/a/dHjq1kT79wh2Tufrx7gCbDzEf)

**Comparing two flat YAML Files**

#### [![asciicast](https://asciinema.org/a/XQAnI2I49PF0W5QlMWd26rMsA.svg)](https://asciinema.org/a/XQAnI2I49PF0W5QlMWd26rMsA)

**Recursive comparison two JSON or YAML files**

#### [![asciicast](https://asciinema.org/a/7DYlub1SUhsgC3WdlMHH8ZKrv.svg)](https://asciinema.org/a/7DYlub1SUhsgC3WdlMHH8ZKrv)

**Output of comparison results in flat format**

#### [![asciicast](https://asciinema.org/a/8rWBAhdkvKbQ72d25saMihbJH.svg)](https://asciinema.org/a/8rWBAhdkvKbQ72d25saMihbJH)

**Output of comparison results in JSON format**

#### [![asciicast](https://asciinema.org/a/vXFlf0l55HvQwKuYQraEgDI8p.svg)](https://asciinema.org/a/vXFlf0l55HvQwKuYQraEgDI8p)

### Installation requirements
- python = "^3.10"
- poetry = "^1.4.0"

### Installation
To install the project you need to use the following commands from Makefile:  

- __make install__: to install poetry packages.   
- __make build__: to build your packages inside your project.   
- __make publish__: It will let us execute the publish command.  
- __make package-install__: nstalls the built package from our OS, so we can start using simple shell commands. 