# ADR 003 — MCP Integration

## Status

Accepted

## Context

AgentOS needs a standardized mechanism for exposing and consuming tools
and resources.

## Decision

Model Context Protocol (MCP) will be supported as an integration boundary.

AgentOS will provide:

1. An MCP server exposing selected enterprise tools and resources.
2. An MCP client capable of discovering approved MCP servers and tools.

MCP servers will not automatically receive unrestricted trust.

Each configured MCP server will have explicit:

- identity
- enabled state
- trust level
- allowed tools
- configuration

## Consequences

AgentOS can demonstrate both MCP provider and consumer capabilities while
retaining explicit control over tool execution.
