# Use the official Python 3.13 slim image as the base image
# This provides a minimal Linux OS with Python pre-installed
FROM python:3.13.11-slim

# Copy the uv binary from the official uv image into this image
# This uses a multi-stage build to avoid installing uv via pip or curl
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set /code as the working directory inside the container
# All subsequent commands will be executed relative to this directory
WORKDIR /code

# Add the virtual environment's bin directory to the PATH
# This ensures the container uses the venv's Python and installed packages by default
ENV PATH="/code/.venv/bin:$PATH"

# Copy dependency definition and lock files into the container
# These files are copied first to take advantage of Docker layer caching
COPY pyproject.toml .python-version uv.lock ./

# Install project dependencies using uv
# --locked ensures exact versions from uv.lock are installed for reproducibility
RUN uv sync --locked

# Copy the application source code into the container
# This is done after dependency installation to avoid unnecessary rebuilds
COPY pipeline.py .

# Define the command that runs when the container starts
# This executes pipeline.py using the virtual environment's Python interpreter
ENTRYPOINT ["python", "pipeline.py"]
