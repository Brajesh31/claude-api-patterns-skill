# API Security Testing

Use this guide only for systems you own or are explicitly authorized to test. Prefer staging environments and non-destructive test accounts.

## Core checks
- Object-level authorization: users cannot read or modify another user's objects.
- Function-level authorization: privileged routes require the correct role.
- Authentication: session/token validation, expiration, audience, issuer, and key rotation.
- Property-level authorization: clients cannot mass-assign protected fields.
- Resource limits: pagination caps, payload limits, query depth, and timeouts.
- Rate limiting: per-user and per-IP controls on sensitive operations.
- Inventory: remove stale versions, debug routes, and undocumented endpoints.
- Configuration: TLS, CORS allowlists, security headers, and safe error responses.

## Test method
1. Define scope, allowed accounts, rate limits, and stop conditions.
2. Create at least two synthetic users with distinct ownership.
3. Capture normal authorized requests.
4. Repeat with the other test identity and verify access is denied.
5. Test malformed and oversized inputs within approved limits.
6. Record request, response, expected behavior, and remediation without collecting real user data.

## Reporting
Describe the affected endpoint, role, impact, evidence, severity rationale, and precise remediation. Redact tokens and personal information. Stop if testing risks availability or exposes production data.
