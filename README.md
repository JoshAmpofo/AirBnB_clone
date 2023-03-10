![AirBnB logo](https://imgs.search.brave.com/SoaC2WQ8fFNaJ2c_SoMUQLTLyyfqg73IGwcEui9F1o4/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzL2VhLzM4/LzUwL2VhMzg1MGEw/ZTU3YWE5ZmY1ZDcw/MDdkYjBlYzBlNWM4/LmpwZw)

# The AirBnB Clone Project

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

| Folder | File | Description |
| :--- | :--- | :--- |
| tests |  | Contains test files for AirBnb Clone |
|  | console.py | Command line Interpreter for managing AirBnB objects |
| models | base_model.py | Defines all common attributes/methods for other classes |
|  | amenity.py | Creates class `amenity` |
|  | city.py | Creates class `city` |
|  | place.py | Creates class `place` |
|  | review.py | Creates class `review` |
|  | state.py | Creates class `state` |
|  | user.py | Creates class `user` |
| models/engine/ | file_storage.py | Serializes instances to a JSON file and deserializes JSON file to instances |
| More models to be updated soon |

### Pictorial Overview of Project

### Console side (backend server side)
![Storage Engines](https://imgs.search.brave.com/b1DFPRHyUwm2FEudVI2LIE7brnCaQ2KLGPdVQ7cEoyM/rs:fit:1200:669:1/g:ce/aHR0cHM6Ly91c2Vy/LWltYWdlcy5naXRo/dWJ1c2VyY29udGVu/dC5jb20vOTM3NzI3/NzUvMTgzMDMwMjAy/LTdmZTk4Y2VhLTIw/YTUtNGRhNi05MDIz/LTAxODc1MmJkYzQw/NS5wbmc)
