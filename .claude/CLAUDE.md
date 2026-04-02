# OYTA Project Rules

## Current State
- **Framework version:** v1.6 (2 April 2026)
- **Bill of Rights:** 5 sections, 14 rights
- **MVP:** 12 points (0 through 11) on download page
- **Website pages:** index, why, how, about, download, thankyou
- **Nav structure:** Why? | What you get | About | Call to Action (red) | [Get Your Terms →] with Community underneath
- **About page:** facts only (no personal story, no mission speech)
- **Call to Action section:** labelled "Truth" on homepage, contains the sofa text, three layers, moral over ethical line
- **Strategy:** OYTA Strategy.md in vault. Three enforcement layers: standard (framework), enforcement (audit AI), pressure (community)
- **Jobs To Be Done:** shareable list at Projects/OYTA/Jobs To Be Done.md in vault
- **TODO:** Projects/OYTA/TODO.md in vault. Keep this up to date every session

## Never use Agents
Do not use the Agent tool in this project. Ever. It makes Karolina wait. Do the work directly.

## No dashes
Never use em dashes (—) or en dashes (–) in any file in this project. Karolina hates them. Use commas, full stops, or parentheses instead.

## Versioning
Every update to the framework file gets a version number. Bump it with each commit that changes the framework. Update version on: AI-Terms.md (top and bottom), index.html, download.html (all instances).

## Architecture sync (CODE ENFORCED)
Every change to AI-Terms.md or CLAUDE.md triggers a PostToolUse hook that injects a mandatory prompt: apply the same change to System Architecture.md. This is not a text rule. It is code. The agent cannot skip it. If the change is framework-only (e.g. Chapter 0), state why and move on.

## TODO sync
At end of every OYTA session, update Projects/OYTA/TODO.md in the vault. Check off what was done. Add what emerged. This is not optional.

## Key files
- Framework: `AI-Terms.md` (the downloadable product)
- Strategy: `C:\Vaults\KarolinaVault\Projects\OYTA\OYTA Strategy.md`
- TODO: `C:\Vaults\KarolinaVault\Projects\OYTA\TODO.md`
- Jobs: `C:\Vaults\KarolinaVault\Projects\OYTA\Jobs To Be Done.md`
- Architecture: `C:\Vaults\KarolinaVault\System\System Architecture.md`
