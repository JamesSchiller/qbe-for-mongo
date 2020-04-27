PURPOSE:

QBE for a mongo collection



PREREQUISIES:

* python 3.8
install python 3.8 comes with tcl 3.6 setup, which is not buggy
https://www.python.org/downloads/release/python-382/
warning for macos users, tcl 8.5 is buggy and brew install python links to tcl 8.5

* tcl
install tcl 8.6, 
https://www.activestate.com/products/tcl/downloads/



PROJECT CREATED FROM:

virtualenv --python $(which python3.8) venv

source venv/bin/activate

pip install -r requirements.txt 

python program.py



CONDITIONS LANGUAGE:

Collection: nameage
Key: name
Sort:
Show:  
Conditions: john
DML: 

Collection: nameage
Key: name
Sort: 
Show: 
Conditions: like '%oh%'
DML:

Collection: nameage
Key: age
Sort: 
Show:
Conditions: < 45
DML:

Collection: nameage
Key: name
Sort: 
Show:
Conditions: != john
DML: 

Collection: nameage  nameage
Key:        name     age
Sort:       asc      desc
Show:
Conditions:
DML:

Collection: nameage
Key: name
Sort: desc
Show: 
Conditions:
DML:

Collection:
Key:
Sort:
Show:
Conditions:
DML:


DISCLAIMER:

max 9 columns in a collection

DML is not implemented yet