#!/bin/bash
while read line
do
    app=$line
    echo "Load for app: $app" 
    python manage.py loaddata dump/$app.json
done < $1
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
