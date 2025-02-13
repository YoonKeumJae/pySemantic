from typing import Annotated
from semantic_kernel.functions import kernel_function

class UsersPlugin:

    users = [
        {
            "id": 1,
            "name": "Alice",
            "age": 25,
            "email": "alice@example.com"
        },
        {
            "id": 2,
            "name": "Bob",
            "age": 30,
            "email": "bob@example.com"
        },
        {
            "id": 3,
            "name": "Charlie",
            "age": 28,
            "email": "charlie@example.com"
        },
        {
            "id": 4,
            "name": "David",
            "age": 35,
            "email": "david@example.com"
        },
        {
            "id": 5,
            "name": "Eve",
            "age": 22,
            "email": "eve@example.com"
        }
    ]
    @kernel_function(
        name="get_users_name",
        description="Gets a list of todo and their current state",
    )
    def get_users_name(
        self
    ) -> Annotated[str, "the output is a string"]:
        print("there are Alice, Bob, Charlie, David, and Eve")
        return None
    
    @kernel_function(
        name = "get_users",
        description="Get users info",
    )
    def get_users(
        self,
    ) -> Annotated[str, "the output is a string"]:
        return self.users