# Task Tracker - Backend API

RESTful API for the Task Tracker application, built with Flask.

## Features

- Complete CRUD operations for tasks
- Automatic timestamp recording (createdAt, completedAt)
- Manual time tracking support (timeSpent)
- CORS enabled for frontend integration

## Tech Stack

- Python 3
- Flask
- Flask-CORS

## API Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| GET | `/api/tasks` | Get all tasks | - |
| POST | `/api/tasks` | Create a new task | `{"text": "string"}` |
| PUT | `/api/tasks/{id}` | Update a task | `{"done": true}` or `{"timeSpent": 30}` or `{"text": "new text"}` |
| DELETE | `/api/tasks/{id}` | Delete a task | - |

## Data Structure

```json
{
  "id": 1,
  "text": "Learn Flask",
  "done": false,
  "createdAt": 1713600000000,
  "completedAt": null,
  "timeSpent": null
}
