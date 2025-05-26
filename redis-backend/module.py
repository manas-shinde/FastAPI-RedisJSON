from pydantic import BaseModel
from typing import Optional
from redis_om import HashModel

from redisDb import redis_db


class TaskCreate(BaseModel):
    name: str
    complete: Optional[bool] = False


class Task(HashModel):
    name: str
    complete: Optional[bool] = False

    class Meta:
        database = redis_db
