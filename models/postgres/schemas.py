from feliz_db.postgres_tools import PostgresModelHandler

class DemoSchema(PostgresModelHandler):

    meta = {
        "initialize": True,            # Optional - Default is False
        # "conditional_init":False,    # Optional - Default is False
        "init_type":"schema", 
        "schema_name":"demo",          # Type can be a list or a string, but the length of the list must be 1
        # "authorization": "postgres"  # Optional - If not provided and using Initialware,
                                       #            it will default to the user provided in config file
    }

schema_models = {
    "DemoSchema": DemoSchema
}