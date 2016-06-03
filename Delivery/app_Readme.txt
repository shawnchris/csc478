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



3.Program demonstration: app2.ipynb
You can open it using Jupyter notebook, the demonstration of the system and sample data run/evaluation results are presented in this file.

4.Interactive program: app2.py
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

then it will ask user to input a movie id (1 to 1682) to predict the rating and based on the movie id, it will recommend 5 similar movies for you

Please enter a movie id to predict for: (1 to 1682)
3

You have selected movie Get Shorty (1995)
Based on your selected Movie, we recommand the following movie to you:


Top 5 Recommended movies are :

['56' 'Pulp Fiction (1994)' '01-Jan-1994' ''
 'http://us.imdb.com/M/title-exact?Pulp%20Fiction%20(1994)']
_______________

['202' 'Groundhog Day (1993)' '01-Jan-1993' ''
 'http://us.imdb.com/M/title-exact?Groundhog%20Day%20(1993)']
_______________

['204' 'Back to the Future (1985)' '01-Jan-1985' ''
 'http://us.imdb.com/M/title-exact?Back%20to%20the%20Future%20(1985)']
_______________

['385' 'True Lies (1994)' '01-Jan-1994' ''
 'http://us.imdb.com/M/title-exact?True%20Lies%20(1994)']
_______________

['96' 'Terminator 2: Judgment Day (1991)' '01-Jan-1991' ''
 'http://us.imdb.com/M/title-exact?Terminator%202:%20Judgment%20Day%20(1991)']
_______________


next, it will ask you to choose a predict mothed:

Please enter method you want to use to predict for:
 1: cosSim
 2: pearsSim
 3: eculid Sim


and then display the prediction/actual rating:
    
   
    
    
    The predicted rating is 3.
    The user's acutal rating for this movie is 5.

it will ask whether the user want to continue, type Y or y to start over or quit the program:
    
    Print Y/y to continue or quit
    n
    Bye!











let us know in case of any questions or problems