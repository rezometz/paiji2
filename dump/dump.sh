#!/bin/bash
while read line
do
    app=$line
    echo "Dump for app: $app" 
    python ../manage.py dumpdata $app > $app.json
done < $1
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
