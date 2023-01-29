import uuid
from flask import Flask,request
from flask_smorest import abort
from db import items,stores

app = Flask(__name__)


@app.get("/store")
def get_store():
    return {"stores":stores}

@app.post("/create")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {**store_data,"id":store_id}
    stores[store_id] = new_store
    return stores,201

@app.post("/item")
def create_item():
    item_data = request.get_json()
    print(stores)
    if item_data['store_id'] not in stores:
        abort(400, message="store not found")
    item_id = uuid.uuid4().hex
    print(item_id)
    item = {**item_data,"id":item_id}
    print(item)
    items[item_id] = item
    return item, 200


@app.get("/store/<string:store_id>")
def get_items(store_id):
    try:
        print(items)
        return items[store_id]
    except KeyError:
        return {"error":"Item not founds"},404

@app.get("/item")
def get_all_item():
    return {"items": list(items.values())}

@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        print(items)
        del items[item_id]
        return {"message":"item deleted"}
    except KeyError:
        abort(404,message="Item not found")








