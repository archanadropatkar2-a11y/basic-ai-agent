# ADR 1: Selection of Tech Stack for Basic AI Agent

## Context

We are building a basic AI Agent as part of the AI-Augmented Workflow course.

The AI Agent will accept user input, send the request to an AI model, and return an appropriate response.

The project is designed for a beginner student, so the technology should be easy to learn, simple to implement, well documented, and compatible with AI-assisted coding tools such as GitHub Copilot.

The project should also be flexible enough to support future features such as memory, tools, databases, and web applications.

## Consequences

### Positive Consequences

- Python is beginner-friendly and widely used for AI development.
- The OpenAI API provides a simple way to connect the application to an AI model.
- Python has a large ecosystem of AI and automation libraries.
- GitHub Copilot can assist with Python code generation, explanation, debugging, and testing.
- Git and GitHub make it easy to track and demonstrate project development.
- The architecture can later be extended with tools, memory, databases, and RAG.
- Ollama provides a possible local/open-source alternative in the future.

### Negative Consequences

- The OpenAI API requires an internet connection.
- API usage may have limits or costs depending on the service and account.
- The API key must be kept secure and must not be uploaded to GitHub.
- Running AI models locally with Ollama may require more computer resources.
- AI coding assistants can generate incorrect code, so all AI-generated code must be reviewed and tested by the student.


## AI-Assisted Development

GitHub Copilot will be used as an AI-assisted coding tool during development.

It will be used to:

- Generate basic Python code.
- Explain unfamiliar code.
- Suggest corrections for errors.
- Help create test cases.
- Improve code structure.
- Generate documentation.

All AI-generated code will be reviewed, understood, tested, and modified by the student before being included in the project.

This approach supports the objective of the AI-Augmented Workflow course by combining human decision-making with AI-assisted software development.

## Alternatives Considered

### Java

Java could be used for developing the AI Agent, but Python was preferred because it is more commonly used for AI, Machine Learning, and automation projects.

### JavaScript / Node.js

Node.js is also suitable for AI-powered applications. However, Python was selected because of its beginner-friendly syntax and strong AI ecosystem.

### Ollama as the Primary Option

Ollama was considered because it supports running open-source AI models locally.

However, OpenAI API was selected for the initial implementation because it provides a simpler starting point for learning AI API integration.

Ollama can be explored later as an alternative.

## Security Considerations

The following security practices will be followed:

- The OpenAI API key will not be written directly in the Python source code.
- The API key will not be uploaded to GitHub.
- Environment variables will be used to store sensitive configuration.
- A `.env` file may be used for local development.
- The `.env` file will be added to `.gitignore`.
- AI-generated code will be reviewed and tested before use.
- Project dependencies will be documented.

 ## Future Improvements

The basic AI Agent can be extended in future with:

- Conversation memory.
- Tool and function calling.
- Web search capabilities.
- Database integration.
- Retrieval-Augmented Generation (RAG).
- A web-based user interface.
- Local AI models using Ollama.
- Automated testing.
- Logging and monitoring.
- Multi-step AI Agent workflows.

  ## Decision Summary

Python + OpenAI API + GitHub + GitHub Copilot has been selected as the initial technology stack because it provides a simple, flexible, and AI-friendly development environment suitable for a beginner-level AI Agent project.

Ollama will remain an alternative for future experimentation with locally hosted open-source AI models.

## Status Review

This ADR is currently **Proposed**.

The status can be changed to **Accepted** after the selected technology stack has been successfully installed, tested, and demonstrated in the basic AI Agent project.

