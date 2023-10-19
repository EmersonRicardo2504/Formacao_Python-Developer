import pprint
from datetime import datetime

import pymongo
import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://emersonricardo153:Neno1533@teste01.cubwoie.mongodb.net/")

db = client.test
collection = db.teste_collection
print(db.list_collection_names())

# definição de info para determinar o doc
post = {
    "author": "Mike",
    "text": "My first mongodb aplication based on python",
    "tags": ["mongo", "python3", "pymongo"],
    "date": datetime.utcnow(),
}


# preparando para submeter as infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)


print("\n")
print(db.posts.find_one())

print("\n")
pprint.pprint(db.posts.find_one())

#bulk inserts
new_posts = [{
        "author": "Mike",
        "text": "Another post",
        "tags": ["bulk", "post", "insert"],
        "date": datetime.utcnow()
         },
         {
        "author": "João",
        "text": "post from Joao. New post available",
        "title": "Mongo is fun",
        "date": datetime(2009, 11, 10, 10, 45)

}]

result = posts.insert_many(new_posts)
print(result.inserted_ids)

print("\nrecuperação final")
pprint.pprint(db.posts.find_one({"author": "Mike"}))

print("\n")
pprint.pprint(db.posts.find_one({"author": "João"}))

print(posts.find())

print('\n')
# recuperando estrutura de dados na coleção posts
print("Documentos dentro da coleção post ")
for post in posts.find():
    pprint.pprint(posts)

#operação pra contas os posts
print("\n")
print(posts.count_documents({}))

#pra recuparação pra determinado paramêtro
print(posts.count_documents({"author": "Mike"}))

pprint.pprint(posts.find({"tags": "insert"}))

# Definindo estrutura de recuperação post de maneira ordenada
print("Mostrando informações de forma ordenada")
print("\n")
for posts in posts.find({}).sort("date"):
    print(posts)

result = db.profiles.create_index([('author', pymongo.ASCENDING)],
                                  unique=True)

print(sorted(list(db.profiles.index_information())))


user_profile_user = [
    {"user": 123, 'name':"Emerson"},
    {"user": 567, 'name': "Teste_01"},

]

result = db.profile_user.insert_many(user_profile_user)

collections = db.list_collection_names()

print("Coleção armazenada no mongoDB\n")
for collection in collections:
    print(collection)


client.drop_database('test')
print(db.list_collection_names())
