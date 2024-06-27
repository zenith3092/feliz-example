from feliz_db.postgres_tools import PostgresModelHandler, PostgresField

class ExampleTable(PostgresModelHandler):
    _id           = PostgresField(serial=True, primary_key=True)
    modified_time = PostgresField("TIMESTAMP")
    comments      = PostgresField("TEXT")

    meta = {
        "initialize": True,
        "conditional_init": False,
        "init_type": "table",
        "schema_name": ["demo"],
        "table_name": ["example"]
    }

demo_models = {
    "ExampleTable": ExampleTable
}