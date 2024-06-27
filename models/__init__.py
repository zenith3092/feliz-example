from .postgres.schemas import schema_models

from .postgres.demo_tables import demo_models

models = {
    "postgres": {
        "test_db": {
            **schema_models,
            **demo_models
        }
    }
}