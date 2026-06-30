from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import String

from datetime import datetime

from app.database.database import Base

class ScanHistory(Base):

    __tablename__ = "scan_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    scan_type = Column(
        String
    )

    status = Column(
        String
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )