# CSC478 Final Project Application Part 1
import os
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

# Some utility function
def cosSim(vecA,vecB):
    return np.dot(vecA, vecB) / ( np.linalg.norm(vecA) * np.linalg.norm(vecB) )

def cosDist(vecA,vecB):
    return 1 - np.dot(vecA, vecB) / ( np.linalg.norm(vecA) * np.linalg.norm(vecB) )

def userProfile(userId):
    # Get the movie ids of top 5 highest rating.
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

# kNN predict
def kNNPredict(data,k,userId,movieId,distMea=cosDist,weighted=False):
    dists = []
    index = []
    for i in range(len(users)):
        if i != userId and data[i,movieId] != 0:
            dists.append(distMea(data[userId,:],data[i,:]))
            index.append(i)

    topKIndex = np.argsort(dists)[:k]
    
    rating = 0    
    for i in topKIndex:
        rating += data[index[i],movieId]
    rating = int(round(rating/len(topKIndex)))
    return rating

def kNNErrStat(data,uList,mList,k):
    errCnt = 0
    totCnt = 0
    errRate = 0
    err = 0
    rsme = 0

    for i in uList:
        for j in mList:
            pred = kNNPredict(data,k,i,j)
            actl = int(data[i-1,j-1])
            if actl != 0:
                totCnt += 1
                if pred != actl:
                    errCnt += 1
                    err += (actl-pred)*(actl-pred)
            # print "user" + str(i) +"/" + movies.title[j] + " prediction : " + str(pred) + " vs actual: " + str(actl)
    rmse = np.sqrt(err/totCnt)
    errRate = errCnt/float(totCnt)
    print "the total error rate with k=%d is: %f, rmse is %f" % (k,errRate,rmse)
    return errRate,rmse

# Load movieLens data
if __name__ == "__main__":
    print "loading data..."
    os.chdir('/Users/Dachi/Dropbox/5_Career/DePaul/CSC478_ProgrammingDataMiningApp/Project')
    path = './Movielens'
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
        userId = int(userId)
        print "You have selected user " + str(userId)
        userProfile(userId)
        
        print "\nPlease enter a movie id to predict for: (1 to 1682)"
        movieId = raw_input()
        while not movieId.isdigit() or int(movieId) < 1 or int(movieId) > 1682:
            print "Please enter a movie id to predict for: (1 to 1682)"
        movieId = int(movieId)
        print "You have selected movie " + movies.title[movieId]
        
        rating = kNNPredict(rating_mat,46,userId,movieId)    
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

