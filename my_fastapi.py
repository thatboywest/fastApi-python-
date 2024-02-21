from fastapi import FastAPI

app = FastAPI()

inventory={
    1:{
        "name":"milk",
        "brand":"brookside",
        "price":60,

    }
}
@app.get("/get-item {item_id}")
def get_item (item_id:int):
    return inventory [item_id]