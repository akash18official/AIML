Project Overview

This project is a skeleton code for creating a simple Python application using:

1) UV – Environment and package manager
2) Uvicorn – ASGI web server for running FastAPI apps
3) Docker – For building images and running containers

The project structure is organized as follows:

1)mycode.py – Contains the application logic, implemented within classes
2)main.py – Creates objects from mycode.py and exposes endpoints via FastAPI


Clearing some of the common doubts:

FastAPI
# Akash - added on 27-01-2026

FastAPI is a Python framework for building APIs and web servers.
It allows you to handle HTTP requests, return JSON responses, and automatically generate API documentation.

Important: FastAPI itself is just a Python object. Creating an instance does not start a server or listen on any port.

Important: Why Uvicorn is Required
# Akash- added on 30-01-2026

Uvicorn is an ASGI server that runs the FastAPI app and listens for incoming HTTP requests.
When you create a FastAPI app object, nothing is exposed on a port.

Uvicorn bridges the gap by starting a server, binding to a port, and handling requests from browsers or clients.

In other words:
FastAPI = Defines the application logic and endpoints
Uvicorn = Makes the FastAPI app accessible over HTTP

This combination allows your app to serve requests reliably in development and production environments.


# Akash- added on 31-01-2026
Main commands used for uv:

uv init - creates dependency file, and creates a virtual environment
uv sync - After adding a new dependency to the file, run uv sync to install it

Imp: when creating the docker file, make sure that following uv commands are added if you are using uv for package and env management:

RUN pip install --no-cache-dir uv -- installs uv

COPY pyproject.toml uv.lock ./ -- copy dependency file to working directory in container

RUN uv sync --no-cache -- uv sync helps to install exact dependencies.


imp : ensure to give port mapping when running docker images on container.


