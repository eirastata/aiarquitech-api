# AIArquitech API

## Description

AI-powered REST API designed to handle chat interactions using OpenAI, built with scalable and maintainable architecture patterns using FastAPI.

---

## Overview

This project is a REST API developed with FastAPI that integrates with OpenAI to provide intelligent responses through a chat endpoint.

The project follows clean architecture principles, ensuring scalability, maintainability, and clear separation of responsibilities between layers.

This repository is part of my backend and AI engineering portfolio.

---

## Features

- REST API built with FastAPI
- Integration with OpenAI API
- Clean architecture structure
- Service layer implementation
- Modular and scalable design
- Interactive API documentation with Swagger

---

## Project Structure

```
AIArquitech/
│
├── api/
│   ├── helloworldRouter.py
│   └── openai_service.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/eirastata/aiarquitech-api.git
```

Enter the project folder

```
cd aiarquitech-api
```

Create virtual environment

```
python -m venv venv
```

Activate virtual environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Run the server

```
uvicorn main:app --reload
```

Access the documentation

```
http://127.0.0.1:8000/docs
```

---

## Endpoint Example

```
GET /api/chat?pergunta=Hello
```

Response example

```
{
  "resposta": "Hello. How can I assist you today?"
}
```

---

## Technologies Used

- Python
- FastAPI
- OpenAI API
- Uvicorn

---

## Architecture

This project follows a service-based architecture, separating:

- Routing layer
- Service layer
- Application entry point

This improves maintainability and scalability.

---

## Author

Tamine Eiras

LinkedIn  
https://linkedin.com/in/tamine-eiras

Project under active development for backend and AI engineering portfolio.
