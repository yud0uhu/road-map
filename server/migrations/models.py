from datetime import date
from time import time
from cv2 import detail_BlocksChannelsCompensator
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import INTEGER, TIMESTAMP

from sqlalchemy import (
    BOOLEAN,
    Column,
    INTEGER,
    TEXT,
    TIMESTAMP,
    VARCHAR,
)

from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.sql.functions import current_timestamp

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(
        INTEGER,
        primary_key=True,
        autoincrement=True,
    )

    created_at = Column(
        'created_at',
        TIMESTAMP(timezone=True),
        server_default=current_timestamp(),
        nullable=False,
        comment='登録日時',
    )

    updated_at = Column(
        'updated_at',
        TIMESTAMP(timezone=True),
        onupdate=current_timestamp(),
        comment='最終更新日時',
    )

    @declared_attr
    def __mapper_args__(cls):
        return {'order_by': 'id'}
        
class Item(BaseModel):
    __tablename__ = 'items'

    NO = Column(INTEGER, unique=True, nullable=False)
    PRIMARY_CATEGORY = Column(VARCHAR(100), nullable=False)
    SECONDARY_CATEGORY = Column(VARCHAR(100), nullable=False)
    TERTIARY_CATEGORY= Column(VARCHAR(100), nullable=False)
    IS_CHECKED = Column(BOOLEAN, nullable=False, default=True)

