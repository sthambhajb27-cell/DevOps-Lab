# Assignment 3: VisualCraft / Docker LLM

This assignment involves fine-tuning and deploying a Large Language Model (LLM) or a Stable Diffusion application using Docker.

## Setup
Due to the hardware requirements (GPU) for LLMs, ensure your Docker setup has NVIDIA Container Toolkit installed if running locally with GPU support.

## Dockerfile for LLM Inference (Example)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "serve_model.py"]
```

## Running the application
```bash
docker build -t llm-app .
docker run -p 8080:8080 llm-app
```
*(Please refer to the specific Assignment 3 PDF for exact model parameters and dependencies required by your instructor.)*
