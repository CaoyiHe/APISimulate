# app/core/config.py

from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    # 例如：数据库连接字符串
    database_url: str = "sqlite:///./test.db"
    secret_key: str = "your_secret_key"


# 实例化配置对象
settings = Settings()
