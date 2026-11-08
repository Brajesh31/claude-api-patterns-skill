# REST API Design

REST is a strong choice when resources are addressable, clients are heterogeneous, and HTTP caching and tooling are valuable.

## Resource modeling
- Use nouns for resource paths: `/users`, `/orders/{orderId}`.
- Use plural collection names consistently.
- Model relationships with nested paths only when the relationship is bounded and clear.
- Avoid deep nesting and action verbs in ordinary CRUD paths.
- Use query parameters for filtering, sorting, and pagination.

## HTTP methods
| Method | Typical intent | Idempotent |
|---|---|---|
| GET | Read a resource or collection | Yes |
| POST | Create or trigger a non-idempotent operation | No, unless designed otherwise |
| PUT | Replace a resource | Yes |
| PATCH | Partially update a resource | Depends on patch semantics |
| DELETE | Remove a resource | Yes |

## Status codes
Use 200 for successful reads/updates with a body, 201 for creation, 202 for accepted asynchronous work, 204 for success without a body, 400 for malformed input, 401 for unauthenticated, 403 for unauthorized, 404 for absent or intentionally concealed resources, 409 for state conflicts, 422 for semantically invalid input where adopted, 429 for throttling, and 5xx for server failures.

## Pagination and filtering
Use bounded page sizes. Choose cursor pagination for large or frequently changing collections. Define stable sorting and include continuation tokens rather than exposing database offsets where appropriate.

## Operational requirements
Set timeouts, request size limits, rate limits, correlation IDs, and consistent error bodies. Document idempotency keys for retryable create/payment operations.
