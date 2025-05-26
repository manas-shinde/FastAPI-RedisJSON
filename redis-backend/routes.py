from fastapi import APIRouter, status
from starlette.requests import Request
from typing import List
from module import Task, TaskCreate


api_route = APIRouter()


@api_route.get("/", status_code=status.HTTP_200_OK)
async def get_all_task() -> List[str]:
    return [format_task(pk) for pk in Task.all_pks()]


def format_task(pk: str):
    task = Task.get(pk)
    return {
        'id': task.id,
        'name': task.name,
        'complete': task.complete
    }


@api_route.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_task(task: TaskCreate):
    new_task: Task = Task(name=task.name, complete=task.complete)
    return new_task.save()


@api_route.put("/{pk}")
async def update_task(pk: str, request: Request):
    task = Task.get(pk)
    body = await request.json()
    task.complete = int(body['complete'])
    return task.save()


@api_route.delete('/{pk}')
async def delete(pk: str):
    task = Task.get(pk)
    return task.delete()
