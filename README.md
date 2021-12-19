# python-project-create

Simple project for command line python projects creation with preconfigured hierarchy

## Usage

```bash
usage: pyproject-create [-h] [--git-init] [dirs [dirs ...]]

Simple application for creating basic python project.

positional arguments:
  dirs        list of whitespace separated directories to be initialized

optional arguments:
  -h, --help  show this help message and exit
  --git-init  should git repository be initialized (default is False)
```

## Reasoning

Just to speed up creation of python project folders. With git initialization.

Structure created:

```bash
./project-dir:
  |__ .gitignore
  |__ main.py
  |__ README.md
  |__ modules/
      |__ __init__.py
  
```

Only ``` main.py ``` file is populated, with:
```python
if __name__ == "__main__":
    print("Hello World")
```

## Enjoy