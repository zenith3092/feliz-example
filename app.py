from flask import Flask, request

from feliz.initialware_tools import InitialwareSystem, ImportGlobals, CorsInitialware, PostgresInitialware, JsonifyInitialware
from feliz.middleware_tools import MiddlewareSystem, JsonifyResponse
from feliz.api_tools import error_handler, api_route_register
from feliz.global_tools import get_configs
from feliz_db.postgres_tools import PostgresHandler

from utils.jsonify_rules import customized_jsonify
from models import models 
from apis import api_list

app = Flask(__name__)

iws = InitialwareSystem()
iws.use(ImportGlobals())
iws.use(CorsInitialware())
iws.use(PostgresInitialware(PostgresHandler, models["postgres"]))
iws.use(JsonifyInitialware(customized_jsonify))
iws.execute(app)

@app.before_request
def before_request():
    mws = MiddlewareSystem()
    mws.process_request(request)

@app.after_request
def after_request(response):
    mws = MiddlewareSystem()
    mws.use(JsonifyResponse())
    mws.process_response(response)
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    return error_handler(e)

for api in api_list:
    api_route_register(app, api)

if __name__ == "__main__":
    SERVER_CONFIG = get_configs("SERVER")
    app.run(host=SERVER_CONFIG["HOST"], port=SERVER_CONFIG["PORT"], debug=SERVER_CONFIG["DEBUG"])