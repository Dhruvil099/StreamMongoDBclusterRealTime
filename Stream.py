import pandas as pd
import urllib
from time import sleep
from IPython.display import clear_output
from pymongo import MongoClient

while(True):
    k=[]
    clear_output(wait=True)
    MONGODB_CONNECTION_STRING = "mongodb+srv://KDRM:"+urllib.parse.quote("pass@123")+"@cluster0.iffy9by.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(MONGODB_CONNECTION_STRING)
    db = client.symbolsDB
    symbol_list_from_DB = db.test.find({})
    source = pd.DataFrame(list(symbol_list_from_DB))
    no = db.test.count_documents({})  
    for i in range(no):
        # appennding timestamps according to the count of documents in a collection
        k.append(pd.Timestamp.now()) 
    # defining a column for Time for timestamps mapped to the documents    
    source['Time']= k
    # reinitiating the list as one could perform insert, delete operation and change the count of documents
    k=[] 
    display(source.set_index('Time'))
