from sqlalchemy import Integer, String, DateTime, func, Text

from RSSFeed.database import PkModel, Column


class Post(PkModel):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    short_description = Column(String(255), nullable=True)
    content = Column(Text, nullable=False)
