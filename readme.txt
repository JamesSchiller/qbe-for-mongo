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
Key:        _id      age    name     friends
Sort:      
Show:       x        x      x        x
Conditions:                            
DML:        insert   21     Jack     ["Bob", "Ken", "Karen"]     # Use double qoutes for each friend

Collection: profiles profiles profiles
Key:        _id      name     friends
Sort:      
Show:                x        
Conditions:                   ["Don", "Lynn"]      # Find names whose friends include Don and Lynn         
DML:           

Collection: profiles profiles
Key:        _id      name    
Sort:      
Show:                      
Conditions:          =           # Delete all docs where name is blank        
DML:        delete


DISCLAIMER:

max 9 columns in a collection

aggregation and complex conditions not implemented

refresh database and collection if you add new keys thru an insert