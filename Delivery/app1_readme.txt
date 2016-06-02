CSC478 Final Project Program Instruction

The paragraphs belows describe how to run the application part 1: movie recommendation system using collaborative filtering(user-based).

The path to load data is set as the current working directory, so if you want to run the python file(app1.py/app2.py) please run them at the root folder like the way below:

    python app1.py
    python app2.py

1.Program demonstration: app1.ipynb
You can open it using Jupyter notebook, the demonstration of the system and sample data run/evaluation results are presented in this file.

2.Interactive program: app1.py
You can run this python program in your python IDE or terminal, you can also pass the path to the data as a parameter when running this program, for example:
python xx.py /path/to/data

once the program starts running, it shows notification and instructions on how to run this program:
it will first load the data:

    loading data...
    loading data finished.

then it will ask user to input an user id (1 to 943) and display user's profile:

    Please enter an user id to predict: (1 to 943)
    1
    You have selected user 1
    
    User1's top 5 favorite movies are:
    Shall We Dance? (1996)
    Sense and Sensibility (1995)
    Star Wars (1977)
    L.A. Confidential (1997)
    Emma (1996)

then it will ask user to input a movie id (1 to 1682) and display the prediction/actual rating:
    
    Please enter a movie id to predict for: (1 to 1682)
    100
    You have selected movie Heavy Metal (1981)
    
    The predicted rating is 3.
    The user's acutal rating for this movie is 5.

it will ask whether the user want to continue, type Y or y to start over or quit the program:
    
    Print Y/y to continue or quit
    n
    Bye!

let us know in case of any questions or problems
