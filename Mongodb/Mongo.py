import pymongo
from urllib.parse import quote_plus

# Replace <your-cluster-uri> with your MongoDB Atlas cluster URI
username = quote_plus('nitinbhardwaj')
password = quote_plus('Nitin@123')
cluster = 'demodb.ktiqfot.mongodb.net/'


uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '?retryWrites=true&w=majority'

# client = MongoClient(uri, server_api=ServerApi('1'))


client = pymongo.MongoClient(uri)

db = client['DEMODB']
collection = db["products"]

data = [
    {
        "name": "Laptop",
        "brand": "Dell",
        "price": 1200.50,
        "description": "15.6-inch laptop with Intel Core i5 processor, 8GB RAM, and 512GB SSD.",
        "category": "Electronics"
    },
    {
        "name": "Smartphone",
        "brand": "Samsung",
        "price": 899.99,
        "description": "6.7-inch smartphone with AMOLED display, 128GB storage, and triple-camera setup.",
        "category": "Electronics"
    },
    {
        "name": "Headphones",
        "brand": "Sony",
        "price": 149.99,
        "description": "Wireless headphones with noise-canceling technology and 30-hour battery life.",
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "brand": "Nike",
        "price": 99.99,
        "description": "Men's running shoes with responsive cushioning and breathable mesh upper.",
        "category": "Footwear"
    }
]

result = collection.insert_many(data)
print("Inserted document IDs:", result.inserted_ids)
