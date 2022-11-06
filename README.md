<h1 align="center"> Practice-Python</h1>

Small programming practices in the python language, these programs are to familiarize myself with concepts and terms of the language

# Programs

|  Program  | Description                                                                 |
| :-------: | --------------------------------------------------------------------------- |
| ParImpar  | This code identifies given a number passed by the user if it is even or odd |
| BlackJack | Recreation of the card game black jack                                      |

# Steps to start

To begin, you must clone the repository in the folder where the program will work and enter its folder.

```sh
git clone https://github.com/EddyBel/Practice-Python.git
```

Enter its folder

```sh
cd Practice-Python
```

To start, you must start the python virtual environment with the :link:[virtualenv](https://virtualenv.pypa.io/en/latest/) dependency.

To create the virtual environment, the dependency must be executed with the name of the environment, by default the environment is called **"Dev"**.

```sh
python -m venv Dev
```

> ## Windows
>
> Raise the virtual environment in windows
>
> ```sh
> .\Dev\Scripts\activate
> ```

> ## Linux
>
> Raise the virtual environment in linux
>
> ```sh
> source Dev/bin/activate
> ```

Once inside the development environment, you must install all the dependencies found in the requirements.txt file.

```sh
pip install -r requeriments.txt
```

And finally you can execute the file **"main.py"** where all the scripts will be included.

```sh
python main.py
```

> ## Note
>
> To deactivate the environment, just execute the **"deactivate"** command.
>
> ```sh
> deactivate
> ```

# Proyect View

![preview](<./assets/doc/Preview%20(1).png>)

---

![preview2](<./assets/doc/Preview%20(2).png>)

# technologies

- Python
