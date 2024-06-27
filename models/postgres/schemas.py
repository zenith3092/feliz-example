from feliz_db.postgres_tools import PostgresModelHandler

class DemoSchema(PostgresModelHandler):

    meta = {
        "initialize": True,
        "conditional_init":False,
        "init_type":"schema",
        "schema_name":["demo"],
        "authorization": "postgres"
    }

schema_models = {
    "DemoSchema": DemoSchema
}