from app.database.database import engine
from app.models.scan_history import Base
from app.models.user import User
from app.models.scan_history import ScanHistory

Base.metadata.create_all(bind=engine)

