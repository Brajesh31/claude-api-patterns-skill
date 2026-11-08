# API Versioning

Version only when a change cannot be made compatibly. Prefer additive evolution and a published deprecation policy.

## Strategies
| Strategy | Example | Trade-off |
|---|---|---|
| URI | `/v1/orders` | Visible and easy to route, can multiply paths |
| Header | `Accept: application/vnd.example.v2+json` | Cleaner URLs, less discoverable |
| Query | `?version=2` | Simple but often awkward for caching and tooling |

## Compatibility
Usually compatible: adding optional fields, adding endpoints, adding enum values only when clients tolerate unknown values. Potentially breaking: removing/renaming fields, changing types, tightening validation, changing defaults, or changing authorization behavior.

## Lifecycle
1. Define supported versions and owners.
2. Publish migration guidance and a sunset date.
3. Measure usage by client/version.
4. Notify consumers before retirement.
5. Keep security fixes consistent across supported versions.
6. Remove a version only after the agreed deprecation window and usage review.

Never assume clients ignore unknown response fields or enum values unless the contract guarantees it.
