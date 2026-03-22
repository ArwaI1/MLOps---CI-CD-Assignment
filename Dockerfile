# Use python:3.10-slim as the base
FROM python:3.10-slim

# Accept an ARG RUN_ID
ARG RUN_ID

# Include a command to "download" the model using echo
RUN echo "Downloading model for Run ID: ${RUN_ID}"

# Keep container running for demonstration purposes
CMD ["echo", "Mock deployment container ready!"]