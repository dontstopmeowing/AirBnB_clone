<h1 align="center">
  <br>
  <a href="https://github.com/dontstopmeowing/AirBnB_clone"><img src="https://raw.githubusercontent.com/dontstopmeowing/AirBnB_clone/main/assets/logobyDnny.png" alt="AirBnB logo By me!"></a>
  <br>AirBnB_clone ✈️ <br>
</h1>

| 🥴 ** Menu ** 👉                                                                                                                                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🔍[Description](https://github.com/dontstopmeowing/AirBnB_clone#description- "Description]") - Description. 🔍                                                        |
| 📃 [Functionalities](https://github.com/dontstopmeowing/AirBnB_clone#functionalities-of-this-command-interpreter "Functionalities]") - Functionalities. 📃            |
| 📢 [Environment](https://github.com/dontstopmeowing/AirBnB_clone#Environment- "Environment]") - Environment. 📢                                                       |
| 🐺 [File descriptor](https://github.com/dontstopmeowing/AirBnB_clone#file-descriptor- "file descriptor]") - File descriptor. 🐺                                       |
| 🐔 [Flow chart](https://github.com/dontstopmeowing/AirBnB_clone#flowchart- "Flow chart]") - Flow chart. 🐔                                                            |
| 🔨 [Installation](https://github.com/dontstopmeowing/AirBnB_clone#installation- "Installation]") - Installation. 🔨                                                   |
| ✨ [Examples](https://github.com/dontstopmeowing/AirBnB_clone#examples- "Examples]") - Examples. ✨                                                                   |
| 🐭 [Bugs](https://github.com/dontstopmeowing/AirBnB_clone#bugs- "#bugs-]") - Known bugs. 🐭                                                                           |
| 📋 [Disclaimer & Credits](https://github.com/dontstopmeowing/AirBnB_clone/blob/main/README.md#disclaimer--credits- "Disclaimer & Credits]") - Disclaimer & Credits 📋 |
|                                                                                                                                                                       |

---

### Description 🔍

This is a Holberton school project which its goal is to do the first steps towards building our first full web application, the AirBnB clone!

### Functionalities of this command interpreter📃

- Create a new object (as in: a new user, place, city. review...)
- Retrieve an object from a file, a database as to see its information.
- Update an object as to add more records to that specific user or just change info.
- Destroy an object in order to delete an user from the database.

---

# Environment 📢

This project was interpreted and tested on Ubuntu 20.04 LTS using python3 (version 3.8.5). However, we are still confident that it shall run on any other version.

---

## File descriptor 🐺

| **File**          | **Brief description**                                                                                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AUTHORS`         | [AUTHORS](https://github.com/dontstopmeowing/AirBnB_clone/blob/main/AUTHORS "AUTHORS") - List that contents the contributors to this project                                                                    |
| `file_storage.py` | [file_storage.py](https://github.com/dontstopmeowing/AirBnB_clone/blob/main/models/engine/file_storage.py "file_storage.py]") - Contains the File Storage class that handles serialization and deserialization. |
| `base_model.py`   | [base_model.py](https://github.com/dontstopmeowing/AirBnB_clone/blob/main/models/base_model.py "base_model.py]") - Defines all common methods that other classes will inherit from                              |
| `amenity.py`      | [amenity.py](https://github.com/dontstopmeowing/AirBnB_clone/blob/main/models/amenity.py "amenity.py]") - Class that inherites from Base Model.                                                                 |
| `city.py`         | [amenity.py](https://github.com/dontstopmeowing/AirBnB_clone/blob/main/models/city.py "city.py]") - Class that inherites from Base Model.                                                                       |
| `place.py`        | [place.py](https://github.com/dontstopmeowing/AirBnB_clone/blob/main/models/place.py "place.py]") - Class that inherites from Base Model.                                                                       |
| `review.py`       | [review.py](https://github.com/dontstopmeowing/AirBnB_clone/blob/main/models/review.py "review.py]") - Class that inherites from Base Model.                                                                    |
| `user.py`         | [user.py](https://github.com/dontstopmeowing/AirBnB_clone/blob/main/models/user.py "user.py]") - Class that inherites from Base Model.                                                                          |
| `console.py`      | [console.py](https://github.com/dontstopmeowing/AirBnB_clone/blob/main/console.py "console.py]") - Contains the entry point of the command interpreter.                                                         |
|                   |

[🔼](https://github.com/dontstopmeowing/AirBnB_clone#------airbnb_clone-%EF%B8%8F- "Back to the top") - [Back to the top](https://github.com/dontstopmeowing/AirBnB_clone#------airbnb_clone-%EF%B8%8F- "Back to the top]") - Go back to the top. [🔼](https://github.com/dontstopmeowing/AirBnB_clone#------airbnb_clone-%EF%B8%8F- "Back to the top")

---

# Flowchart 🐔

-This is what we have achieved so far, not quite impressive (yet).

<a href="https://github.com/dontstopmeowing/AirBnB_clone#flowchart"><img src="https://raw.githubusercontent.com/dontstopmeowing/AirBnB_clone/main/assets/flowcharbyDnny.png" alt="Flowchart By me!"></a>

---

# Installation 🔨

1.  Clone this repository in your personal computer or machine with the following command:
    `git clone https://github.com/dontstopmeowing/AirBnB_clone.git`

2.  Go to the project s folder using the following command:
    `cd AirBnB_clone`

3.  Run the console interactively:
    `./console.py`

4.  Run the console in non interactively mode
    `echo "<command>" | ./console.py`

---

# Examples ✨

## Interactive mode

###### If everything worked as supposed to, you should be able to use and see the program s command prompt as shown below:

```bash
$ ./console.py
```

```bash
(hbnb)help

Documented commands (type help <topic>):

(hbnb)help author

Program written by Carlos Galeano.

(hbnb)help all

Prints all string representation of
all instances based or not on the class name

(hbnb)help create

Creates an instance of a defined class.

(hbnb)destroy
** class name missing **

(hbnb)create BaseModel
17e3e759-2f88-4555-825c-d2a1866772f9

(hbnb)show BaseModel 17e3e759-2f88-4555-825c-d2a1866772f9
[BaseModel] (17e3e759-2f88-4555-825c-d2a1866772f9) {'id': '17e3e759-2f88-4555-825c-d2a1866772f9', 'created_at': datetime.datetime(2021, 7, 1, 2, 48, 30, 971047), 'updated_at': datetime.datetime(2021, 7, 1, 2, 48, 30, 971310)}


update BaseModel 17e3e759-2f88-4555-825c-d2a1866772f9 first_name "Carlos Galeano"
(hbnb)

(hbnb)show BaseModel 17e3e759-2f88-4555-825c-d2a1866772f9
[BaseModel] (17e3e759-2f88-4555-825c-d2a1866772f9) {'id': '17e3e759-2f88-4555-825c-d2a1866772f9', 'created_at': datetime.datetime(2021, 7, 1, 2, 48, 30, 971047), 'updated_at': datetime.datetime(2021, 7, 1, 2, 48, 30, 971310), 'first_name': 'Carlos Galeano'}
```

## Non-interactive mod

```bash
$ echo "command" | ./console.py
```

```bash
echo "help" | ./console.py

Documented commands (type help <topic>):
========================================
EOF  all  author  create  destroy  help  quit  show  update

echo "help author" | ./console.py
Program Written by Carlos Galeano.

echo "help quit" | ./console.py
(hbnb)Quit command is used to exit the program.

echo "create BaseModel" | ./console.py
(hbnb)30de1643-d9f0-47fb-aa74-93e52859a8a6

echo "show BaseModel 30de1643-d9f0-47fb-aa74-93e52859a8a6" | ./console.py
(hbnb)[BaseModel] (30de1643-d9f0-47fb-aa74-93e52859a8a6) {'id': '30de1643-d9f0-47fb-aa74-93e52859a8a6', 'created_at': datetime.datetime(2021, 7, 1, 3, 5, 45, 966638), 'updated_at': datetime.datetime(2021, 7, 1, 3, 5, 45, 967401)}

echo "show BaseModel 17e3e759-2f88-4555-825c-d2a1866772f9" | ./console.py
(hbnb)[BaseModel] (17e3e759-2f88-4555-825c-d2a1866772f9) {'id': '17e3e759-2f88-4555-825c-d2a1866772f9', 'created_at': datetime.datetime(2021, 7, 1, 2, 48, 30, 971047), 'updated_at': datetime.datetime(2021, 7, 1, 2, 48, 30, 971310), 'first_name': 'Carlos Galeano'}
```

---

# Bugs 🐭

- No known bugs at release time (June 30, 2021). However, if you do find any; please report it to us!

---

# Code Contributors 💩

- Carlos Galeano [Twitter](https://twitter.com/CarlosG19285722) | [Email](carlos.galeano@outlook.it)

---

# Disclaimer & Credits 📋

- All the characters you see in the images above were designed by [Oversimplified](https://www.youtube.com/user/Webzwithaz).
- Huge thanks to [Juan Carabali](https://www.github.com/srDri/), I wouldn't have achieved this without your great help.

---

[🔼](https://github.com/dontstopmeowing/AirBnB_clone#------airbnb_clone-%EF%B8%8F- "Back to the top") - [Back to the top](https://github.com/dontstopmeowing/AirBnB_clone#------airbnb_clone-%EF%B8%8F- "Back to the top]") - Go back to the top. [🔼](https://github.com/dontstopmeowing/AirBnB_clone#------airbnb_clone-%EF%B8%8F- "Back to the top")
