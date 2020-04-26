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

Key: name 
Conditions: john

Key: name
Conditions: like '%oh%'

Key: age
Conditions: < 45

Key: name
Conditions: != john

Key: name
Sort: asc
Key: age
Sort: asc

Key: name
Sort: desc


DISCLAIMER:

max 9 columns in a collection