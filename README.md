
# Directory manager script

## What the script does:

The script provides four commands: *create*, *move*, *delete* directories and 
*list* to see contents of directory.

## How to use the script:

### Installation

```console
$ # Create a virtual environment
$ python3 -m venv .venv
$ # Activate it
$ source .venv/bin/activate
$ # Install dependencies
$ pip install -r requirements.txt
```

### Script input

The script will read commands line by line from **instructions.txt**

### To run the script
```console
$ python src/main.py
```

### To run tests:
```console
$ pytest --cov --cov-report term-missing .
```