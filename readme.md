# Query By Example (QBE) for a mongo collection

![alt text here](https://github.com/JamesSchiller/images/blob/master/Screen%20Shot%202020-05-07%20at%2010.10.34%20PM.png?raw=true)

![alt text here](https://github.com/JamesSchiller/images/blob/master/Screen%20Shot%202020-05-07%20at%2010.11.29%20PM.png?raw=true)

![alt text here](https://github.com/JamesSchiller/images/blob/master/Screen%20Shot%202020-05-07%20at%2010.11.42%20PM.png?raw=true)

## QBE Language

```
Collection: profiles
Key:        name
Sort:
Show:       x
Conditions: john
DML: 

Collection: profiles
Key:        name
Sort: 
Show:       x
Conditions: like '%oh%'
DML:

Collection: profiles
Key:        age
Sort: 
Show:       x
Conditions: < 45
DML:

Collection: profiles
Key:        name
Sort: 
Show:       x
Conditions: != john
DML: 

Collection: profiles profiles
Key:        name     age
Sort:       asc      desc
Show:       x        x
Conditions:
DML:

Collection: profiles
Key:        name
Sort:       desc
Show:       x
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

Collection: profiles profiles profiles profiles
Key:        _id      age      name     friends
Sort:      
Show:       
Conditions:                            
DML:        insert   21       Jack     ["Bob", "Ken", "Karen"]     # Use double quotes for each friend

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
Conditions:          =           # Delete all profile docs where name is blank        
DML:        delete

Collection: profiles profiles
Key:        _id      name    
Sort:      
Show:                      
Conditions:          !=          # Delete all profile docs where name is NOT blank        
DML:        delete
```

## Prerequisites

```
* python 3.8
install python 3.8 comes with tcl 3.6 setup, which is not buggy
https://www.python.org/downloads/release/python-382/
warning for macos users, tcl 8.5 is buggy and brew install python links to tcl 8.5

* tcl
install tcl 8.6, 
https://www.activestate.com/products/tcl/downloads/
```

## Project Created From

```
PROJECT CREATED FROM:

virtualenv --python $(which python3.8) venv

source venv/bin/activate

pip install -r requirements.txt 

set environment variable at end of ~/.bashrc and source it so it sticks

~/.bashrc
--------------------------
...
export /Users/s13a/rsrch-25-mar-2020/tcl/qbe4
--------------------------

python program.py

change first line of qbe.py to venv

ln -s /Users/s13a/rsrch-25-mar-2020/tcl/qbe4/qbe.py /usr/local/bin/qbe

$ qbe
```

## References

Based on the <a href="http://pages.cs.wisc.edu/~dbbook/openAccess/thirdEdition/qbe.pdf">QBE Paper</a>

Microsoft Access QBE


## Limitations

max 9 columns in a collection

aggregation and complex conditions not implemented

refresh database and collection if you add new keys thru an insert

you can only insert integers not decimals for now