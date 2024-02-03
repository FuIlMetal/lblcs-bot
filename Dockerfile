FROM python:3.10-alpine

ENV PYTHONBUFFERED 1

# Set workdir
WORKDIR /app
# Copy source files
COPY . .
# Create virtual environment
RUN python3 -m venv .venv
ENV PATH="/app/.venv/bin:$PATH"

# Install poetry and force poetry to use local env
RUN pip3 install poetry 
RUN python3 -m poetry config virtualenvs.create false 
RUN python3 -m poetry install --no-interaction --no-ansi

CMD ["python3", "app.py"]
