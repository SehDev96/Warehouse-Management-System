# Warehouse-Management-System
This repo contains script and docker files to start up the application

## Description

This is a repository for warehouse management system web application. This warehouse management systems consists of three types of users which are Admin, Manager and Operator. Users will be able to use features like product management, warehouse management, user management and transaction management depending upon the role of the user. 

Backend Code: https://github.com/SehDev96/warehouse-backend.git
Frontend Code: https://github.com/SehDev96/warehouse-frontend.git

---

## Tech Stack 

Frontend: React 
Backend: Spring Boot
Database: Postgresql

## Prerequisite 

1. Python should be installed (if using python script to start docker) 
2. Docker should be installed (non-sudo access) 

--- 


## Steps to run application 

### Run application using python script: 
1. $ git clone https://github.com/SehDev96/Warehouse-Management-System.git
2. $ cd Warehouse-Management-System 
3. $ python3 runme.py 


### Run application using docker-compose: 
1. $ git clone https://github.com/SehDev96/Warehouse-Management-System.git
2. $ cd Warehouse-Management-System
3. $ git clone https://github.com/SehDev96/warehouse-frontend.git
4. $ git clone https://github.com/SehDev96/warehouse-backend.git
5. $ docker-compose up -d 
