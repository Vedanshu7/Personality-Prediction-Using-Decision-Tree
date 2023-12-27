from django.http import HttpResponse
from django.shortcuts import render
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def index(request):
    uri = "mongodb+srv://vedanshu:vedanshu@cluster0.bgoqd.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["Expert_System"]
    col = db["Questions"]
    x = col.find()
    for data in x:
        print(data)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return render(request, 'index.html')
