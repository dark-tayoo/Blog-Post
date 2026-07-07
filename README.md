# Blog Post API

## Overview
This repository contains a backend RESTful API built with Django and Django REST Framework (DRF). It provides a foundational blog system allowing clients to create, read, update, and delete (CRUD) blog posts.

## Features
* **CRUD Operations:** Full support for managing blog posts.
* **Automated Timestamps:** Automatically tracks when a post is created (`created_at`) and last modified (`updated_at`).
* **RESTful Architecture:** Clean, standard API endpoints leveraging DRF serializers and views.

## Technologies Used
* Python
* Django
* Django REST Framework (DRF)

## API Endpoints

| HTTP Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/blogposts/` | Retrieve a list of all blog posts. |
| `POST` | `/blogposts/` | Create a new blog post. |
| `GET` | `/blogposts/<id>/` | Retrieve a specific blog post by ID. |
| `PUT/PATCH` | `/blogposts/<id>/` | Update a specific blog post. |
| `DELETE` | `/blogposts/<id>/` | Delete a specific blog post. |

## Data Models
### `BlogPost`
* `title`: String (max 100 characters)
* `content`: Text
* `created_at`: Datetime (auto-generated)
* `updated_at`: Datetime (auto-updated)

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dark-tayoo/Blog-Post.git
   cd Blog-Post
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install django djangorestframework
   # pip install -r requirements.txt (if available)
   ```

4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```
