# MOOD 

## Participants 

- Joanna Blaszka 
- Kamil Dutkiewicz 
- Paulina Jewulska (team leader)
- Dawid Justyna 
- Riza Yarar 

## Do you need more people: No 

## Short description of the idea 

MOOD is a simple web application that checks users' mood and choose adequate entertainment depending on their choices. Funny movie, good book or interesting podcast? Users only need to answer some questions about their feelings and time limitation and app quickly selects a lot of options that hopely satisfy user. 

## How to start 	

1. Create virtual environment: ```python -m venv mood-env```	
1. Activate virtual environment:	
    - on Linux: ```source mood-env/bin/activate```	
    - on Windows: ```.\mood-env\Scripts\activate```	
1. Install dependencies: ```pip install -r requirements.txt```	
1. Run application: ```python manage.py runserver```

# Technology stack: 

- Frontend: Django Templates, Bootstrap 
- Backend: Python, Django 
- Database: SQLite 

# Features 

- User registration

Whenever user want, can go back to previous results. 
- Adding a calendar to mark the mood 
   
MOOD will adapt the form of entertainment to the user for each day. 
- Adding preferences

The user can help the application in the selection of appropriate entertainment. 
- Matching movies with 'Netflix' and 'HBO' 

Using ML, we can match movies to the user,  so that he can see what he wants  
- Matching podcasts, books,  movies and series 

The user can also choose to entertain for a longer time and grade it later. 
- Information where find mental help if user often has a bad day  

The application will recommend other websites or applications that help, for example, in the treatment of depression. 
- Chat Bot for logged user  

Register user can talk to the bot and match the result more closely. 
- Statistics about preferences of users using  

time range, age range, Sex, Period of year(winter,spring,etc...) 

 

## User Stories: 

- as a user I would like to be able to log in with my personal account 
- as a user I would like to enter the password twice during registration so as not to make mistakes 
- as a user I would like to see the rating of the film I got 
- as a user I would like to see a list of movies in the database 
- as a user I would like to rate movies  
- as a user I would like to see the link or application name where to look for help 

## Project roadmap: 

### SPRINT 1: 
- Create trello board 
- Create github repository    

### SPRINT 2: 
- Learn Django and set up project 
- Create basic layout 
- Study datasets  
- Learn word2vec 

### SPRINT 3: 
- Brainstorm on questions 
- Add new implementations to layout 
- Collect data from user (not logged) 
- Preprocessing of dataset  
- Write some unit tests 

### SPRINT 4: 
- Classification of dataset 
- Get emotions from https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
- Get similar themes from that dataset 
- Use word2vec to find similar emotions and themes in that sample 
- Divide movies into emotions categories using previously mention sample 
- Divide movies into themes categories  

### SPRINT 5: 
- Implement of matching function 
- Display results to the user (not logged) 
- Add registration and login 
- Implement chat bot  
- Implement function for matching  data from chat bot  
- Write some tests 

### SPRINT 6: 
- Creation of statistics and displaying them 
- Add information about mental help to users with continuing bad mood 
- Write some tests 

### SPRINT 7: 
- Final corections and test
