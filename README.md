# The AirBnB Clone Project

![hbnb logo](https://user-images.githubusercontent.com/88311316/151070609-19608294-829e-408b-b2b3-5d1f2873f1e3.png)


This is the second major collaborative project in the ALX SE program. This project combines all the concepts that have been taught in Sprint 2: Higher Level Programming, specifically Python.


## Concepts Learned and Applied

- How to create a Python package
- How to create a command interpreter in Python using the `cmd` module
- Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage `datetime`
- What is a `UUID`
-What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function


# Scope

**AirBnB** is a *complete web application*, integrating database storage, a back-end API and a front-end interface.

The project is in four parts. Each part handles different aspects of Web development.
This first section deals with building the `console` that will act as a command line interpreter to manipulate data (no visual interface yet, perfect for development and debugging.

- The second section will be the front-end.
- The third section will be the database management system
- The last section will be the API.

## Description of Console and How to Use it

### Starting the Command Line Interpreter

The cmd interpreter can be started by executing the command `./console.py`.
- This console can `create`, `destroy`, `update` and `show` records of user details.
- The `help` function displays a list of commands and functions that can be used in the console

**Example (interactive mode)**
```bash
peabody@peabody-VirtualBox:~$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
=======================================
EOF all create help quit show update

(hbnb) help create

	Usage: <create classname>
	Creates new instance of BaseModel. Saves it and prints id

(hbnb) help quit
Quit command to exit the program
(hbnb) quit
peabody@peabody-VirtualBox:~$
```

**Example (non-interactive mode)**
```bash
peabody@peabody-VirtualBox:~$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
=======================================
EOF all create help quit show update

(hbnb)
peabody@peabody-VirtualBox:~$
peabody@peabody-VirtualBox:~$ cat test_help
help
peabody@peabody-VirtualBox:~$
peabody@peabody-VirtualBox:~$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
=======================================
EOF all create help quit show update

(hbnb)
peabody@peabody-VirtualBox:~$
```


### OBJECTS IMPLEMENTED
This repository contains the following files:

| **Folder** | **File** | **Description** |
| :--- | :--- | :--- |
| | \__init__.py | Treats directories as python modules |
| | [console.py](./console.py)  | Command line Interpreter for managing AirBnB objects |
| | [AUTHORS](./AUTHORS) | Contains info about project contributors |
| [tests](./tests/test_models) |  | Contains test files for AirBnb Clone |
| | [test_amenity](./tests/test_models/test_amenity.py) | Contains test cases for `Amenity` subclass |
| | [test_base_model](./tests/test_models/test_base_model) | Contains test cases for `BaseModel` parent class |
| | [test_city](./tests/test_models/test_city) | Contains test cases for `City` subclass |
| | [test_place](./tests/test_models/test_place) | Contains test cases for `Place` subclass |
| | [test_review](./tests/test_models/test_review) | Contains test cases for `Review` subclass |
| | [test_state](./tests/test_models/test_state) | Contains test cases for `State` subclass |
| | [test_user](./tests/test_models/test_user) | Contains test cases for `User` subclass |
| | [test_console](./tests/test_console.py) | Contains test cases for `console` |
| [Test_Engine](./tests/test_models/test_engine/) | [test_file_storage](./tests/test_models/test_engine/test_file_storage.py) | Contains test cases for JSON file storage module |
| [models](./models) | [base_model.py](./models/base_model.py) | Defines all common attributes/methods for other classes |
|  | [amenity.py](./models/amenity.py) | Defines subclass `amenity` |
|  | [city.py](./models/city.py) | Defines subclass `city` |
|  | [place.py](./models/place.py) | Defines subclass `place` |
|  | [review.py](./models/review.py) | Defines subclass `review` |
|  | [state.py](./models/state.py) | Defines subclass `state` |
|  | [user.py](./models/user.py) | Defines subclass `user` |
| [models/engine/](./models/engine) | [file_storage.py](./models/engine/file_storage.py) | Serializes instances to a JSON file and deserializes JSON file to instances |
| More models to be updated soon |

## Usage :wrench:
|  **Method**  |  **Description**  |
| ------------ | ----------------- |
| [create](./console.py) | Creates object of given class |
| [show](./console.py)   | Prints the string representation of an instance based on the class name and id |
| [all](./console.py)    | Prints all the string representation of all instances based or not on the class name |
| [update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute (saves changes to JSON file) |
| [destroy](./console.py) | Deletes an instance based on the class name and id (saves changes to JSON file) |
| [help](./console.py) | Print usage information and description about a specific command |
| [EOF](./console.py) | Cleanly terminate program using keyboard interrupt |
| [quit](./console.py) | Quit command to exit program |


### Console side (backend server side)
![Storage Engines](https://imgs.search.brave.com/b1DFPRHyUwm2FEudVI2LIE7brnCaQ2KLGPdVQ7cEoyM/rs:fit:1200:669:1/g:ce/aHR0cHM6Ly91c2Vy/LWltYWdlcy5naXRo/dWJ1c2VyY29udGVu/dC5jb20vOTM3NzI3/NzUvMTgzMDMwMjAy/LTdmZTk4Y2VhLTIw/YTUtNGRhNi05MDIz/LTAxODc1MmJkYzQw/NS5wbmc)
