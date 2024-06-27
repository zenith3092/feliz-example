from flask import Blueprint

from feliz.api_tools import handler, TrueResponse, FalseResponse
from feliz_db.postgres_tools import PostgresHandler

testApi = Blueprint("test", __name__)

@handler("/example/<uid>", testApi, methods=["GET"])
def example(uid, DB, input_request, **params):
    start_time = input_request.get("start_time", "")
    end_time   = input_request.get("end_time", "")

    DH: PostgresHandler = DB["postgres"]["test_db"]

    conditions = []
    if start_time != "":
        conditions.append(("modified_time >=", start_time))
    if end_time != "":
        conditions.append(("modified_time <=", end_time))
    
    get_res = DH.get_data(table="demo.example", conditional_rule_list=conditions)
    if not get_res["indicator"]:
        return FalseResponse(get_res["message"])

    return TrueResponse("Success", get_res["formatted_data"])