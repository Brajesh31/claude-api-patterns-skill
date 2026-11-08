# API Patterns

## Overview

This repository contains a Claude skill for applying consistent API patterns across service design and implementation. It includes focused guidance for common API concerns and conventions.

## Topics

- API style and resource organization.
- Authentication and authorization.
- Documentation practices.
- GraphQL considerations.
- Rate limiting and response design.

## Repository Structure

```text
SKILL.md
api-style.md
auth.md
documentation.md
graphql.md
rate-limiting.md
response.md
LICENSE
```

## Getting Started

1. Review `SKILL.md` and the topic files relevant to your task.
2. Install the skill in the skills directory supported by your Claude environment.
3. Describe the API context, consumers, constraints, and desired outcome.
4. Apply the relevant patterns consistently.
5. Validate behavior, error handling, security, and compatibility against the actual service.

## Usage Notes

Choose patterns based on the API's requirements rather than applying every convention blindly. Keep behavior consistent across endpoints and document intentional exceptions.

## License

MIT. See [LICENSE](LICENSE).

## Supporting resources

Added the missing REST, tRPC, versioning, and API security-testing guides, plus `scripts/api_validator.py`. The validator performs a lightweight static inventory of route declarations. It does not prove that authentication, authorization, or runtime behavior is secure. Run it with `python scripts/api_validator.py <project_path>`.

## Additional files

- `rest.md`, `trpc.md`, `versioning.md`, and `security-testing.md`
- `scripts/api_validator.py`

The script inventories common route declarations from source files. It is a static helper, not a security scanner.
