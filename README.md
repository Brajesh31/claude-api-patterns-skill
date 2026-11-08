# claude-api-patterns-skill

A Claude Code skill for selecting and applying consistent API design patterns across REST, GraphQL, and tRPC services.

## Overview

This skill helps teams make API design decisions based on consumers, use cases, infrastructure, and long-term compatibility. It covers resource organization, request and response conventions, authentication, versioning, pagination, rate limiting, documentation, and security testing.

The goal is consistency and predictable behavior, not applying every pattern to every API.

## Main Topics

### API Style Selection

Compare REST, GraphQL, and tRPC based on client needs, type-safety requirements, data access patterns, caching, and operational constraints.

### Resource and Route Design

- Resource naming and nesting.
- HTTP methods and status codes.
- Idempotency and safe retries.
- Filtering, sorting, and pagination.
- Consistent route conventions.

### Response and Error Design

- Stable response structures.
- Consistent error formats.
- Validation errors and field-level feedback.
- Pagination metadata.
- Compatibility across versions.

### Authentication and Authorization

- API keys and token-based authentication.
- OAuth and related authorization flows.
- Role and permission boundaries.
- Secure handling of credentials and sessions.

### Versioning and Rate Limiting

- API evolution strategies.
- Deprecation and migration planning.
- Rate-limit policies and response headers.
- Abuse prevention and resource protection.

### Documentation and Testing

- Clear endpoint contracts.
- Request and response examples.
- Validation of routes and schemas.
- Security testing considerations.

## Installation

```bash
git clone https://github.com/Brajesh31/claude-api-patterns-skill.git ~/.claude/skills/api-patterns
```

## Usage

Invoke the skill when designing a new API or reviewing an existing service:

```text
/api-patterns
```

Provide the API consumers, data model, authentication requirements, expected traffic, compatibility constraints, and framework.

## Reference Guide

| File | Purpose |
|---|---|
| `api-style.md` | Select an API style |
| `rest.md` | REST resource and method conventions |
| `response.md` | Response and error structure |
| `graphql.md` | GraphQL design considerations |
| `trpc.md` | Type-safe TypeScript API patterns |
| `versioning.md` | API evolution and versioning |
| `auth.md` | Authentication and authorization |
| `rate-limiting.md` | Traffic control and abuse prevention |
| `documentation.md` | API documentation practices |
| `security-testing.md` | API security test guidance |

## Validation Utility

The repository includes a lightweight route inventory script:

```bash
python scripts/api_validator.py <project_path>
```

This utility provides static inspection. It does not prove runtime correctness or establish that authentication and authorization are secure.

## API Design Checklist

- API style matches the consumers and use case.
- Resource and method names are consistent.
- Status codes reflect actual outcomes.
- Errors use a predictable structure.
- Pagination is bounded and stable.
- Authentication and authorization are enforced server-side.
- Rate limits protect expensive operations.
- Breaking changes have a migration plan.
- Contracts and examples are kept current.
- Tests cover success, validation, authorization, and failure paths.

## Repository Contents

- `SKILL.md`: Main API design workflow.
- `*.md`: Focused API design and implementation guides.
- `scripts/api_validator.py`: Lightweight route inspection utility.
- `README.md`: Overview and topic index.

## Practical Guidance

Choose conventions deliberately and apply them consistently. A small, coherent API is easier to maintain than a large set of patterns added without a clear consumer need.
