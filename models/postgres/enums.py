from feliz_db.postgres_tools import PostgresModelHandler, PostgresEnum

class DemoStatusEnum(PostgresModelHandler):
    ACTIVE   = PostgresEnum("ACTIVE")
    INACTIVE = PostgresEnum("INACTIVE")

    meta = {
        "initialize": True,
        "init_type": "enum",
        "enum_name": "demo_status"
    }

enum_models = {
    "DemoStatusEnum": DemoStatusEnum
}