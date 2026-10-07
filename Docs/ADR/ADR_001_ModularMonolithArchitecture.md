# ADR 001 — Modular Monolith Architecture

## Status

Accepted

## Context

Enterprise AgentOS contains multiple logical components including:

- API
- authentication
- RBAC
- agent orchestration
- tools
- MCP
- memory
- workers
- approvals
- audit logging
- observability

Splitting these components into independent microservices at the beginning
would add operational complexity without providing meaningful benefits for
the initial project.

## Decision

AgentOS will initially use a modular monolith architecture.

The backend will contain clearly separated modules for:

- API
- agents
- tools
- security
- services
- memory
- MCP
- observability
- persistence

Long-running execution will use a separate worker process.

The MCP server will run as a separate process.

## Consequences

### Positive

- easier local development
- easier testing
- simpler deployment
- clear module boundaries
- lower infrastructure complexity
- easier debugging

### Negative

- less physical isolation between backend modules
- future scaling may require extracting selected components

The architecture will be designed so components can be extracted later
if real scaling requirements justify it.
