# OYTA Project Rules

## Never use Agents
Do not use the Agent tool in this project. Ever. It makes Karolina wait. Do the work directly.

## No dashes
Never use em dashes (—) or en dashes (–) in any file in this project. Karolina hates them. Use commas, full stops, or parentheses instead.

## Versioning
Every update to the framework file gets a version number. Bump it with each commit that changes the framework.

## Architecture sync (CODE ENFORCED)
Every change to AI-Terms.md or CLAUDE.md triggers a PostToolUse hook that injects a mandatory prompt: apply the same change to System Architecture.md. This is not a text rule. It is code. The agent cannot skip it. If the change is framework-only (e.g. Chapter 0), state why and move on.
