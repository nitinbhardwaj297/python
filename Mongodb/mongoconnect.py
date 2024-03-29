import pymongo

# Replace <password> with your actual password
uri = 'mongodb+srv://nitinbhardwaj:Nitin@123@demodb.ktiqfot.mongodb.net/'

client = pymongo.MongoClient(uri)

# Check if connection was successful
if client:
    print("Connected to MongoDB Atlas")
else:
    print("Failed to connect to MongoDB Atlas")