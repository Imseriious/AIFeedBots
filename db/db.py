from pymongo import MongoClient
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://samserver:sam4321@aifeed.4vxtg.mongodb.net/dev?retryWrites=true&w=majority&appName=aifeed"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
   mydb = client["dev"]
   return mydb
   # Create the database for our example (we will use the same database throughout the tutorial
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()