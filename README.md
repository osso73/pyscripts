# pyscripts
A collection of scripts written in python to do some day-to-day tasks. This is a number of scripts that can be used to automate some common tasks on the PC. I use them in Windows, so they are not really tested to work on linux. 

Some of the scripts have settings embedded in the script, such as folders where to store the information, etc. I may think about moving these settings outside, in `.ini` files or similar, so that they can be easily updated, and even used on linux.

I started creating a GUI using QT and PySide6. This is under folder `gui-qt`, and not finished yet. The idea is to offer a simple interface where all the command line options can be chosen through the graphical interface. Then, script is launched clicking a button "Go", that will call the script with the chosen options, and show the output in the window.

## Installation

You can install the scripts by creating a virtual environment, using the requirements file provided. This can be done using venv as follows:

```
python -m venv .venv 
.venv\Scripts\activate
pip install -r requirements.txt
```

If you are on linux, activate the environment using the following command:

```
source .venv\bin\activate 
```

## Usage

Once the environment is activated, you can run each script by using:

```
python scripts/<name>.py args
```

For each script, there is a `--help` argument that can be requested to provide a description of the arguments and options to be used.

To launch the graphical environment, use the following command:

```
python gui_qt/main.py
```

## Testing

Testing is not yet complete. But you can run all tests by running the command:

```
pytest
```

The config file `pytest.ini` contains the parameters to run the tests. If you want to see a coverage report, you can run:

```
coverage run
coverage html
```

And you get the html report to see the coverage of the programs.


## License

This project is using an MIT license.