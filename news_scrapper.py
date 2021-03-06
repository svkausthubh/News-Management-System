from webscrappingyahoo import NewsArcticlesYahoo
from webscrappingreutres import NewsArticlesReuter
from webscrappingTimesOfIndia import NewsArticlesTimes
from Output import outputdirectory
import pandas
import concurrent.futures
import fileinput
from flaskpart import app
import sys

argument_list=sys.argv
pickle=pandas.read_pickle('symbols.pickle')

# inputfile=input("Enter The Path Of The File:")
# # f=open(inputfile,"r")
# # if f.mode=="r":
# #     urls=f.readlines()
# # f.close()
    
if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(NewsArcticlesYahoo,pickle.symbol[:50])
        executor.map(NewsArticlesReuter,pickle.symbol[:50])
        executor.map(NewsArticlesTimes,pickle.symbol[:50])
    pass

outputdirectory(argument_list[1])

