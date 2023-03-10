![AirBnB clone](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230310%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230310T123132Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3711c3c4d1d58c7c5078d6c7094d782cfe5d19e695f913bbfff0f1eac0272754)
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
| models | amenity.py | Creates class `amenity` |
| models | city.py | Creates class `city` |
| models | place.py | Creates class `place` |
| models | review.py | Creates class `review` |
| models | state.py | Creates class `state` |
| models | user.py | Creates class `user` |
| models/engine/ | file_storage.py | Serializes instances to a JSON file and deserializes JSON file to instances |
| More models to be updated soon |

### Pictorial Overview of Project

### Console side (backend server side)
![Storage Engines](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230310%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230310T123132Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2d74812c65f9538a2647ba98e58f1c14dcf8b17ba5f15fedc01d669e230068e8)

