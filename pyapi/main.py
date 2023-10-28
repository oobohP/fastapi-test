from fastapi import FastAPI, HTTPException

app = FastAPI()

# Store todos in memory (replace with a database in a real application)
todos = []

class Todo:
    def __init__(self, id: int, body: str):
        self.id = id
        self.body = body

@app.get("/")
def index():
    return {"message": "Hello World"}

# GET all todos
@app.get("/todos")
def get_todos():
    return todos

# POST a new todo
@app.post("/todos")
def create_todo(body: str):
    new_todo = Todo(id=len(todos) + 1, body=body)
    todos.append(new_todo)
    return new_todo

# UPDATE a todo's body
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, body: str):
    if todo_id < 1 or todo_id > len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    todos[todo_id - 1].body = body
    return {"message": "Todo updated successfully"}

# DELETE a todo by its ID
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id < 1 or todo_id > len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    deleted_todo = todos.pop(todo_id - 1)
    return {"message": "Todo deleted successfully", "deleted_todo": deleted_todo}
