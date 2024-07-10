from feliz_db.postgres_tools import PostgresModelHandler, PostgresField
from .enums import DemoStatusEnum

class ExampleTable(PostgresModelHandler):
    _id           = PostgresField(serial=True, primary_key=True)
    modified_time = PostgresField("TIMESTAMP")
    test_id       = PostgresField("TEXT", unique=True, index_type="BTREE")
    status        = PostgresField(enum_class=DemoStatusEnum)
    comments      = PostgresField("TEXT")

    meta = {
        "initialize": True,         # Optional - Default is False
        "init_index": True,         # Optional - Default is False
        # "conditional_init":False, # Optional - Default is False
        "init_type": "table",
        "schema_name": "demo",      # Type can be a list or a string
        "table_name": "example"     # Type can be a list or a string, but the length of the list must be 1
    }

demo_models = {
    "ExampleTable": ExampleTable
}