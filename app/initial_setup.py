from entities.notification import Notification
from database.database_config import engine, Base
Base.metadata.create_all(engine)