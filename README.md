# FastAPI Test

This is a quick and simple CRUD API built using FastAPI. The endpoints are designed to perform basic CRUD operations on an array that is stored in memory, as we are too lazy to connect a database or driver.

## Usage

### Get all todos

Simply navigating to /todos will show you all todos i.e in this case the array todos

### Create a new todo

To create a new todo, send a POST request to `/todos` with a `body` parameter in the query string. For example:

### Update a todo

To update the body of an existing todo, send a PUT request to `/todos/{todo_id}` with a `body` parameter in the query string. For example:

### Delete a todo

To delete an existing todo, send a DELETE request to `/todos/{todo_id}`. For example:
Note that the `todo_id` parameter should be replaced with the ID of the todo you wish to update or delete.