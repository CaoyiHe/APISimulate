# app/db/base.py

from sqlalchemy.ext.declarative import as_declarative, declared_attr

# 声明基本的数据库模型
@as_declarative()
class Base:
    id: int
    __name__: str

    # 自动生成表名
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
