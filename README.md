# Zuru_Task
The Project aims in portrying the basic understanding of Python libraries and coding practices.

#Installation - 
Install Pycharm and open the project Zuru_Task. 
The project contains a structure.json file which contains a list of directory y in nested structure.

The project structure is :
Zuru_Task/
├── pyls/
│   ├── __init__.py
│   └── pyls.py
└── structure.json

Task 1:
Run the Project by the following command in bash:
python -m pyls.pyls
o/p: LICENSE README.md ast go.mod lexer main.go parser token

Task 2:
mplement Command Line Arguments
Modify pyls.py to Accept Arguments:

Update pyls.py to handle command line arguments:
python pyls.py -A
o/p: .gitignore LICENSE README.md ast go.mod lexer main.go parser token

Task 3:
ls -l 
Implement the argument -l, that prints the results vertically with additional
information:
python -m pyls -l
o/p: 
drwxr-xr-x 1071 LICENSE
drwxr-xr-x 83 README.md
-rw-r--r-- 4096 ast
drwxr-xr-x 60 go.mod
drwxr-xr-x 4096 lexer
-rw-r--r-- 74 main.go
drwxr-xr-x 4096 parser
-rw-r--r-- 4096 token

Task 4:
Implement Additional Functionality
Add Reverse Order Functionality:

Update pyls.py to include the reverse order option:
python pyls.py -l -r
o/p:
token parser main.go lexer go.mod ast README.md LICENSE
-rw-r--r-- 4096 token
drwxr-xr-x 4096 parser
-rw-r--r-- 74 main.go
drwxr-xr-x 4096 lexer
drwxr-xr-x 60 go.mod
-rw-r--r-- 4096 ast
drwxr-xr-x 83 README.md
drwxr-xr-x 1071 LICENSE

Task 5:
Open Terminal and run the script with the sorting by time option:
bash

python -m pyls -A -l -r -t
-rw-r--r-- 4096 ast
drwxr-xr-x 4096 lexer
-rw-r--r-- 4096 token
-rw-r--r-- 74 main.go
drwxr-xr-x 60 go.mod
drwxr-xr-x 8911 .gitignore
drwxr-xr-x 1071 LICENSE

