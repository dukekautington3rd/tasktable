from prettytable import PrettyTable
from pymongo import MongoClient

def client_db():
    CONNECTION_STRING="mongodb://mongo:27017/"
    client = MongoClient(CONNECTION_STRING)
    return client


def get_data(db, col):
    myclient = client_db()
    # dblist = myclient.list_database_names()
    mydb = myclient[db]
    # collist = mydb.list_collection_names()
    mycol = mydb[col]
    header = list(mycol.find_one())
    header[0] = "Task"
    tasks = []
    for x in mycol.find():
        tasks.append(list(x.values()))
    return header, tasks

def gen_table(db, col):
    headers, tasks = get_data(db, col)
    table = PrettyTable(headers)
    table.preserve_internal_border = True
    table.add_rows(tasks)
    table.format = True
    table.align["Task"] = "l"
    return(table.get_html_string())

# print(gen_table("projects", "Lon"))