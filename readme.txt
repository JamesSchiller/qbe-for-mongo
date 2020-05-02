PURPOSE:

QBE for a mongo collection




PREREQUISITES:

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




TO MAKE EXECUTABLE:

#! ./venv/bin/python (first line of program.py points to your virtualenv)

change program.py to program.sh

sudo chmod +x program.sh

./program.sh




QBE LANGUAGE:

Collection: profiles
Key:        name
Sort:
Show:  
Conditions: john
DML: 

Collection: profiles
Key:        name
Sort: 
Show: 
Conditions: like '%oh%'
DML:

Collection: profiles
Key:        age
Sort: 
Show:
Conditions: < 45
DML:

Collection: profiles
Key:        name
Sort: 
Show:
Conditions: != john
DML: 

Collection: profiles profiles
Key:        name     age
Sort:       asc      desc
Show:
Conditions:
DML:

Collection: profiles
Key:        name
Sort:       desc
Show: 
Conditions:
DML:

Collection: profiles profiles profiles
Key:        _id      name     age
Sort:
Show:
Conditions:
DML:        insert   Baylee   22

Collection: profiles profiles
Key:        _id      name     
Sort:
Show:
Conditions:          Baylee
DML:        update   Bay

Collection: profiles profiles
Key:        _id      name     
Sort:
Show:
Conditions:          Bay
DML:        delete   

Collection: profiles profiles profiles
Key:        _id      name     friends
Sort:      
Show:                x        
Conditions:                   ["Don", "Lynn"]      # Find names whose friends include Don and Lynn         
DML:           




DISCLAIMER:

max 9 columns in a collection

aggregation and complex conditions not implemented

you cannot not add new keys thru an insert