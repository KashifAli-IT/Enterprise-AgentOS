# ADR 002 — LangGraph for Agent Orchestration

## Status

Accepted

## Context

AgentOS requires multi-step, stateful agent workflows involving:

- multiple specialized agents
- tool calls
- conditional routing
- retries
- approvals
- execution state
- resumability

A simple request-response agent loop would make these workflows difficult
to control and observe.

## Decision

LangGraph will be used as the primary agent orchestration framework.

AgentOS will maintain explicit execution state and graph transitions.

The application will enforce:

- maximum iterations
- execution timeouts
- tool permissions
- approval policies
- persisted execution state

## Consequences

LangGraph provides explicit workflow structure and state management.

AgentOS remains responsible for authentication, authorization, tool
security, persistence, approvals, audit logging, and platform-level
policies.
