# Contributing to garrison-plugin-factorio

Thanks for your interest in contributing! This plugin follows the [Garrison Plugin API](https://github.com/ProfessorZ/garrison).

## Getting Started

1. **Fork** this repository
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/garrison-plugin-factorio`
3. Create a **feature branch**: `git checkout -b feature/my-improvement`
4. Make your changes
5. **Test** against a real Factorio server if possible
6. Open a **Pull Request** from your fork

> ⚠️ Direct pushes to `main` are not accepted. All changes must come via Pull Request from a fork.

## Plugin Structure

```
garrison-plugin-factorio/
  manifest.json    # Plugin metadata — update version on changes
  plugin.py        # GamePlugin implementation (get_players, get_status, kick/ban)
  schema.py        # RCON command definitions
  options.py       # Server options handler (/config get/set)
```

## What to Contribute

- **New RCON commands** — add to `schema.py` with accurate parameter definitions
- **Bug fixes** — especially RCON response parsing edge cases
- **New PZ versions** — update schema version compatibility
- **Options** — add missing server options with correct types and ranges

## Versioning

This project uses [Semantic Versioning](https://semver.org/):

- `PATCH` (1.0.x) — bug fixes, documentation updates
- `MINOR` (1.x.0) — new commands/options, backwards-compatible additions
- `MAJOR` (x.0.0) — breaking changes to plugin.py interface

Update `manifest.json` version on every release.

## Code Style

- Python 3.12+
- Type hints on all public methods
- Follow the existing `GamePlugin` interface contract
- No external dependencies beyond what Garrison core provides

## Reporting Issues

Open a GitHub issue with:
- Factorio server version (Version number)
- RCON command that failed
- Expected vs actual output
