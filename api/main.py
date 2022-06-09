from enum import Enum
from typing import Union

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# FastApiのインスタンス
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name", "Baz"}]

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None], short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
    
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    # qに値が存在する場合
    # qはデフォルトで値が存在しない(None)ように設定しているため、URLにqの指定がなくてもエラーを出さないようにしている？
    # FastApiにおいてOptional[str] は」仕様できない
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/files/{file_path.path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# 引数の型をEnumを引数にとったClassにすることで、Class内で使われる変数しか表示されなくなる？
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}