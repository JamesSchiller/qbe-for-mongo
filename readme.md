# Query By Example (QBE) for a mongo collection

![alt text here](https://github.com/JamesSchiller/images/blob/master/Screen%20Shot%202020-05-07%20at%2010.10.34%20PM.png?raw=true)

![alt text here](https://github.com/JamesSchiller/images/blob/master/Screen%20Shot%202020-05-07%20at%2010.11.29%20PM.png?raw=true)

![alt text here](https://github.com/JamesSchiller/images/blob/master/Screen%20Shot%202020-05-07%20at%2010.11.42%20PM.png?raw=true)

```
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

Collection: profiles profiles profiles profiles
Key:        _id      age      name     friends
Sort:      
Show:       x        x        x        x
Conditions:                            
DML:        insert   21       Jack     ["Bob", "Ken", "Karen"]     # Use double qoutes for each friend

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

Based on the <a href="http://pages.cs.wisc.edu/~dbbook/openAccess/thirdEdition/qbe.pdf">QBE Paper</a>