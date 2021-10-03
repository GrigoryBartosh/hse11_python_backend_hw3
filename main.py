from fastapi import FastAPI

from starlette.graphql import GraphQLApp
from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene import Schema
from schemas import Query


app = FastAPI()
app.add_route("/", GraphQLApp(
  schema=Schema(query=Query),
  executor_class=AsyncioExecutor)
)