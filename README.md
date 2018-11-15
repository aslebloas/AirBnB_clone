# AirBnB clone
## Description of the project
This project is part of our training to become software engineers at
*Holberton School*.
This project is intended to be an Airbnb clone.

## Description of the command interpreter:
The command interpreter helps us to manage the objects of our project.

- Create a new object (ex: a new User or a new Place)

- Retrieve an object from a file, a database etc…

- Do operations on objects (count, compute stats, etc…)

- Update attributes of an object

- Destroy an object


### How to start it
To start the console:
```
$ cd AirBnB_clone
AirBnB$ ./console.py
```

### How to use it
All these objects classes are available:

- BaseModel (which is the parent class. All other classes inherit from it.)

- User

- Place

- State

- City

- Amenity

- Review

All these commands are available:

- `all / all <class name>` retrieve all instances of a class

- `show <class name> <object id>` retrieve an instance based on its ID

- `create <class name>`

- `update <class name> <object id> <attribute> <\"value\">`
update an instance based on his ID

- `destroy <class name> <object id>` destroy an instance based on his ID

- `quit` quit the console

- `help <command>` bring the documentation about a command

- `EOF` (which is Ctrl + D) quit the console

#### Alternatives

- `<class name>.all()` retrieve all instances of a class

- `<class name>.show(<id>)` retrieve an instance based on its ID

- `<class name>.count()` retrieve the number of instances of a class

- `<class name>.destroy(<id>)` destroy an instance based on his ID

- `<class name>.update(<id>, <attribute name>, <attribute value>)`
update an instance based on his ID

- `<class name>.update(<id>, <dictionary representation>)`
update an instance based on his ID with a dictionary


### Examples


```
~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
(hbnb)
(hbnb)
(hbnb) quit
~/AirBnB$
```

## Json file

You can use a json file to load objects from the start.
In this case it must comply with some rules.
The JSON file is a dictionary of dictionaries. The key are `<class name>.id`
Values are dictionaries with at least the following keys:
BaseModel:
__class__
created_at
id
Note: if an id is not present, a new one will be automatically created.

```
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "Holberton", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
```
