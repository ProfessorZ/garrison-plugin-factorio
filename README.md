# garrison-plugin-factorio

> Factorio RCON plugin for [Garrison](https://github.com/ProfessorZ/garrison) — the multi-game server management dashboard.

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/ProfessorZ/garrison-plugin-factorio/releases)
[![Garrison API](https://img.shields.io/badge/garrison--api-v1-green)](https://github.com/ProfessorZ/garrison)

## Features

- **Player management** — list online players, kick, ban, unban, promote/demote
- **Server status** — online/offline detection, version info
- **Server config** — live `/config get/set` support for all server settings
- **Full command schema** — all Factorio multiplayer commands with parameter definitions
- **Command autocomplete** — structured command definitions with parameter hints

## Requirements

- [Garrison](https://github.com/ProfessorZ/garrison) with Plugin API v1+
- Factorio dedicated server (1.1+ or 2.0+)
- RCON enabled on your Factorio server

## Installation

### Via Garrison Plugin Installer

```bash
garrison plugin install https://github.com/ProfessorZ/garrison-plugin-factorio
```

### Manual

Clone this repository into your Garrison plugins directory:

```bash
git clone https://github.com/ProfessorZ/garrison-plugin-factorio \
  ~/.garrison/plugins/garrison-plugin-factorio
```

Then restart Garrison.

## Enabling RCON on Factorio

Start the dedicated server with RCON flags:

```bash
factorio --start-server save.zip \
  --rcon-port 27015 \
  --rcon-password yourpassword
```

Or set in `server-settings.json`:

```json
{
  "admins": ["YourUsername"]
}
```

## Default Ports

| Type | Port |
|------|------|
| Game | 34197 (UDP) |
| RCON | 27015 (TCP, user-configured) |

## Command Categories

| Category | Commands |
|----------|----------|
| Player Management | /players, /kick, /ban, /unban, /bans |
| Admin | /admins, /promote, /demote, /admin |
| Server Config | /config get, /config set |
| Permissions | /permissions, group management |
| World | /evolution, /time, /seed, /version |
| Moderation | /ignore, /ignores, /whisper |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
