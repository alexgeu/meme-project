# The ThreeSquareGag - MemeSite

## General

This project is being developed for the Information Systems Development course at the University of Liechtenstein

* Project start: 13.03.2020
* Project end: 04.06.2020 

The developers are Sasa Malesevic, Sophie Hartl and Alexander Geuze

## Project description
The target is to create a web app that allows users to browse memes and get away of their daily struggle for a couple of minutes.
Memes can be uploaded, liked and commented. The prerequisite to use the like and comment function is a registered user.

Following features are included:
* Uploading a meme
* Like a meme
* Comment a meme
* Category management
* Search function
* Quicklinks (sidebar)
* User management including profile
* Updating of profile
* Pagination
* Different templates
* Bootstrap styling

## Installation guide

This setup is going to guide you through the first time setup of this project.

Required dependencies are:

- Python 3.6

After installing python go to the directory where you want your project to be located and clone the github repository by opening your console in the desired folder and running the following command:

```
git clone https://github.com/alexgeu/meme-project.git
```

Now navigate your console into the newly created `meme-project` folder. The next step is to create a virtual environment. To do this, we will use the `venv` package. On Windows this package comes with the python installation. On Linux you might have to run

```
sudo apt install -y python3-venv
```

To create a virtual environment you run 

```python -m venv env```

For the name of the virtual environment we choose `env`. You just need to remember what it is because the next step is to activate the virtual environment. This step differs between Windows and UNIX systems:

WINDOWS
```
env\Scripts\activate.bat
```

UNIX
```
source env/bin/activate
```

After activating our virtual environment, the next step is to install all the required dependencies:

```
pip install -r requirements.txt
```

This commands gets all the packages that are saved in the `requirements.txt` file and installs the versions that are defined there. If at any point you add a package to the project you need to run `pip freeze > requirements.txt` to add the new dependency to the file.

Now that we have all the dependencies setup correctly you can go into the `memeProject` folder. This is the folder where our `manage.py` file is located.

In this folder we need to setup our database. To do so, we need to run two commands:

1) `python manage.py migrate`
2) `python manage.py createsuperuser`

The first command creates a database from all our files and the second command creates a user that allows us to navigate our own app

The last step of the initial setup is to check if everything worked correctly by running

```
python3 manage.py runserver
```

## Project structure

### Folder structure

meme-project (This folder is where our environment, our readme and our requirements.txt are located)

-> memeProject (This folder is where our manage.py file is located)
--> memeProject (This is where all comes together)
