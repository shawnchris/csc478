# CSC478 Final Project Application Part 1
import os
import sys
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

# Some utility function
def cosSim(vecA,vecB):
    return np.dot(vecA, vecB) / ( np.linalg.norm(vecA) * np.linalg.norm(vecB) )

def cosDist(vecA,vecB):
    return 1 - np.dot(vecA, vecB) / ( np.linalg.norm(vecA) * np.linalg.norm(vecB) )


def ecludSim(inA,inB):
    return 1.0 / (1.0 + la.norm(inA - inB))

def pearsSim(inA,inB):
    if len(inA) < 3 : return 1.0
    return 0.5 + 0.5 * corrcoef(inA, inB, rowvar = 0)[0][1]

def userProfile(userId):
    # Get the movie ids of top 5 highest rating.
    gender = "male" if users.gender[userId] == "M" else "female"
    print "User " + str(userId) + " is " + str(users.age[userId]) + " years old " + gender + \
    ", occupation: " + users.job[userId] + "."
    movieIds = np.argsort(rating_mat[userId,:])[-5:]
    
    # Print user's top 5 favorite movies
    print "\nUser" + str(userId) + "'s top 5 favorite movies are:"
    for i in movieIds:
        print movies.title[i] 
        
def unratedMovies(userId):
    unrated = []
    for i in range(len(movies)):
        if rating_mat[userId,i] == 0:
            unrated.append(i)
    return unrated

# rec_movie

def rec_most_similar_movies(dataMat, movie, querymovie, k, metric=pearsSim):
    mv = get_mv_text(movie, querymovie)
    print 'Selected Movie: \n'
    print mv[:5]
    
    simMovie = zeros(dataMat.shape[1])
    for i in range(dataMat.shape[1]):
        if i != querymovie:
            simMovie[i] = metric(dataMat[:,i], dataMat[:, querymovie])
    sortedVec = simMovie.argsort()[::-1]
    print '\nTop 5 Recommended movies are :\n'
    for i in range(k):
        print movie[sortedVec[i]][:5], '\n_______________\n'

# pridict rating
def PredictRateForUserMovie(dataMat, movie, userId,querymovie,metric=pearsSim):
    #mv = get_mv_text(movie, querymovie)
    #print 'Selected Movie: \n'
    #print mv[:5]
    
    unrated = unratedMovies(userId,movies,dataMat)
    simMovie = zeros(dataMat.shape[1])
    if querymovie not in unrated:
        print "User # %d has rated the movie, the rating is %d "%(userId,dataMat[userId][querymovie])
    else:   
        for i in range(dataMat.shape[1]):
            if i != querymovie:
                simMovie[i] = metric(dataMat[:,i], dataMat[:, querymovie])
        sortedVec = simMovie.argsort()[::-1]
        for j in sortedVec:
            if dataMat[userId][j] !=0:
                t = dataMat[userId][j]
                break
        print "Predict rating for user # %d, movie:  %s is: %d "%(userId,movie[querymovie][1],t)
    

# Load movieLens data
if __name__ == "__main__":
    print "loading data..."
    if len(sys.argv) <= 1:
        path = '/Users/Dachi/Dropbox/5_Career/DePaul/CSC478_ProgrammingDataMiningApp/Project/Movielens'
    else:
        path = sys.argv[1]
    os.chdir(path)
    users = pd.read_table('u.user',delimiter='|',header=None,names=["id","age","gender","job","zip code"])
    movies = pd.read_table('u.item',delimiter='|',header=None, names=["id","title","rl_date","vrl_date","url",
                                                                     "unknown","Action","Adventure","Animation",
                                                                     "Children's","Comedy","Crime","Documentary",
                                                                     "Drama","Fantasy","Film-Noir","Horror",
                                                                     "Musical","Mystery","Romance","Sci-Fi",
                                                                     "Thriller","War","Western"])
    ratings = pd.read_table('u.data',delimiter='\t',header=None,names=["user","movie","rating","timestamp"])
    genres = pd.read_table('u.genre',delimiter='|',header=None,names=["genre","id"])
    
    # Convert data to matrix
    rating_mat=np.zeros((len(users),len(movies)))
    for i in range(len(ratings)):
        user=int(ratings.user[i])-1
        movie=int(ratings.movie[i])-1
        rating=int(ratings.rating[i])
        rating_mat[user,movie]=rating

    print "loading data finished."

    # Interactive part
    cont = True
    while cont:
        print "\nPlease enter an user id to predict: (1 to 943)"
        userId = raw_input()
        while not userId.isdigit() or int(userId) < 1 or int(userId) > 943:
            print "Please enter an user id to predict: (1 to 943)"
            userId = raw_input()
        userId = int(userId)
        print "You have selected user " + str(userId)
        userProfile(userId)
        
        print "\nPlease enter a movie id to predict for: (1 to 1682)"
        movieId = raw_input()
        while not movieId.isdigit() or int(movieId) < 1 or int(movieId) > 1682:
            print "Please enter a movie id to predict for: (1 to 1682)"
            movieId = raw_input()
        movieId = int(movieId)
        print "You have selected movie " + movies.title[movieId]

        rec_most_similar_movies(rating_mat, movie,movieId, 5, metric=pearsSim)

        
        print "\nPlease enter method you want to use to predict for: \n 1: cosSim\n 2: pearsSim\n 3: eculid Sim"
        method = raw_input()
        while not method.isdigit() or int(method) < 1 or int(method) > 3:
            print "\nPlease enter method you want to use to predict for: \n 1: cosSim\n 2: pearsSim\n 3: eculid Sim"
            method = raw_input()
        if int(method) == 1:
            method ='cosSim'
        elif int(method) == 2:
            method ='pearsSim'
        else:
            method ='ecludSim'
        
            
        
        
        
        rating =PredictRateForUserMovie(rating_mat,movie,userId,movieId,method)
            
        print "\nThe predicted rating is %d." % (rating)
        if rating_mat[userId-1,movieId-1] == 0:
            print "The user does not rate this movie."
        else:
            print "The user's acutal rating for this movie is %d." % (rating_mat[userId-1,movieId-1])
        print "\nPrint Y/y to continue or quit"
        res = raw_input()
        if res.lower() != "y":
            cont = False
    print "Bye!"    



