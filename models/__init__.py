from .postgres.enums import enum_models
from .postgres.schemas import schema_models

from .postgres.demo_tables import demo_models

models = {
    "postgres": {
        "test_db": {
            **enum_models,
            **schema_models,
            **demo_models
        }
    }
}