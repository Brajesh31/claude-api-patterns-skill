# tRPC API Design

tRPC is useful when a TypeScript client and server share a codebase or can share types, and end-to-end compile-time inference materially improves developer experience.

## Good fit
- TypeScript-first applications with coordinated client/server releases.
- Internal product APIs where browser/mobile clients use a controlled toolchain.
- Teams that value inferred input/output types and procedure-level composition.

## Cautions
- It is not a universal public API contract for arbitrary third-party clients.
- Cross-language consumers need another contract boundary.
- Shared types do not replace runtime validation.
- Authorization must be enforced on the server for every protected procedure.

## Design practices
- Group procedures by domain router.
- Validate inputs with runtime schemas.
- Put authorization and business invariants in reusable server-side middleware/services.
- Keep procedures thin and delegate to application logic.
- Use explicit error codes and stable client error handling.
- Test unauthorized access, invalid input, and nested router behavior.

## Alternatives
Use REST or GraphQL when clients are heterogeneous, external integrations are central, or a language-neutral contract is required.
