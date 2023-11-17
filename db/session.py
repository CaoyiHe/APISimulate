# app/db/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

# 创建数据库引擎
engine = create_engine(settings.database_url)

# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


