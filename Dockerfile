FROM python:3.12-slim

WORKDIR /app
COPY src ./src
COPY examples ./examples
COPY prompts ./prompts

ENTRYPOINT ["python", "-m", "src.requirements_parser"]
CMD ["examples/meeting-notes.md"]
