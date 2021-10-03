from graphene import ObjectType, Int, List, String, Field
import json


class Review(ObjectType):
    mark = Int(required=True)
    comment = String()
    likes = Int()


class User(ObjectType):
    id = String(required=True)
    name = String(required=True)
    phone = String(required=True)
    review = Field(Review)


class Query(ObjectType):
    user_list = None
    get_user = Field(List(User), id=String())

    async def resolve_get_user(self, info, id=None):
        with open("data.json") as users:
            user_list = json.load(users)

        if id is not None:
            for user in user_list:
                if user["id"] == id:
                    return [user]

        return user_list