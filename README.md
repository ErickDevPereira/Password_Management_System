## Password Management System

This project empowers the user to store, delete and access usernames and passwords in a highly dinamic way. Moreover, it can generate secure passwords with 16 digits. Each user can create an account or log in an existing one, which gave its own dataset of passwords available to be accessed, deleted or incremented with the aid of a beautiful UI created with CustomTkinter library.

Furthermore, the account password for this developed software(not to be confused with the stored passwords) is nicely protected inside the database with SSH256 encryption, ensuring absolute security over user accounts.

The language used to buid this project was Python, with the libraries CustomTkinter as the GUI, hashlib for the cryptograph, mysql-connector-python to do the CRUD and random for the random logic. The database used here was MySQL. There are 5 scripts in total: the main_script is responsible for connecting all the other python modules and run the software itself; args is a module that has direct access to crucial arguments in the GUI allowing immediate access to widget positional arguments, window resolution size and much more; SQL_CRUD is responsible for the connection between Python and MySQL; pw_generator is the module that handles the logic behind the password generator; basic_structure.sql has the structure of the database.

This branch can be easily used to create a remote database.
