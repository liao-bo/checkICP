#Install mongodb 3.4.7
##1.After installation, must manual create admin account
 \#mongod --port 27017 --dbpath /data/db   
 \#mongo       
 \>use admin    
 \>db.createUser(    
... {    
... user:"admin",    
... pwd:"123456",   
... roles:[{role:"userAdminAnyDatabase",db:"admin"}]   
... }   
... )   

##2. restart the mongodb
\#mongod --auth --port 27017 --dbpath /data/db

#Creat project DB
 \#mongo    
 \>use admin  
 \>db.auth("admin","123456")  
 \>use checkicp  
 \>db.createUser(  
... {  
... user:"checkicp",  
... pwd:"checkicp",  
... roles:[{role:"readWrite",db:"checkicp"}]  
... }  
... )