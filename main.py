#!/bin/python3
from pathlib import Path
from argparse import ArgumentParser as arg


class ArgParser:
    def __init__(self, 
                 desc: str="Simple application for creating basic python project."):
        self.__parser = arg(description=desc)
        self.__parser.add_argument("dirs", nargs="*", default=".", 
                                   help="list of whitespace separated directories to be initialized")
        self.__parser.add_argument("--git-init", type=bool, default=True, 
                                   help="should git repository be initialized (default is true)")
        self.__argv = self.__parser.parse_args()

    def parse_args(self):
        return self.__argv
    
    def get_dirs(self):
        return self.__argv.dirs
    
    def get_git_init(self):
        return self.__argv.git_init


class ProjectGenerator:
    def __init__(self, target: list):
        self.__project_path = self.__populate_path(target)    
        self.__generate_project_folder() 
        self.__generate_modules()   
        self.__generate_file("__init__.py", "modules")
        self.__generate_file(".gitignore")
        self.__generate_file('README.md')
        self.__generate_file("main.py")
    
    def __str__(self):
        return self.__project_path.__str__()
    
    def __generate_project_folder(self):
        for path in self.__project_path:
            if not path.exists() or not path.is_dir():
                path.mkdir()
    
    def __populate_path(self, l: list):
        tmp = []
        for p in l:
            i = Path(p).absolute()
            if i not in tmp:
                tmp.append(i)
        return tmp
    
    def __generate_modules(self):
        self.__modules = []
        for path in self.__project_path:
            self.__modules.append(path / "modules")
        
        for path in self.__modules:
            if not path.exists() or not path.is_dir():
                path.mkdir()
            else:
                print(path.absolute(), "already exists. Aborting.")

    def __generate_file(self, name: str, sub_dir: str=""):
        files = []
        for path in self.__project_path:
            files.append(path / sub_dir / name)
        
        for path in files:
            if not path.exists():
                path.touch()
                if name == "main.py":
                    path.write_text('if __name__ == "__main__":\n\tprint("Hello World")')
                elif name == ".gitignore":
                    path.write_text('/.idea/\n/.vscode/\n')
            else:
                print(path.absolute(), "already exists. Aborting")
                

if __name__ == "__main__":
    parser = ArgParser()
    generator = ProjectGenerator(parser.get_dirs())
