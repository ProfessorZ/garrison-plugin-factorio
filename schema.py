"""Factorio RCON command schema v2.0.0 — full real command list (32 commands)."""


def get_commands():
    """Return the list of CommandDef objects for Factorio."""
    from app.plugins.base import CommandDef, CommandParam

    return [
        # ── PLAYER_MGMT ─────────────────────────────────────────────
        CommandDef(
            name="/whisper",
            description="Send a private message to a player",
            category="PLAYER_MGMT",
            params=[
                CommandParam(name="player", type="string", description="Target player name"),
                CommandParam(name="message", type="string", description="Message to send"),
            ],
            example="/whisper <player> <message>",
        ),
        CommandDef(
            name="/shout",
            description="Send a message to all players",
            category="PLAYER_MGMT",
            params=[CommandParam(name="message", type="string", description="Message to shout")],
            example="/shout <message>",
        ),
        CommandDef(
            name="/reply",
            description="Reply to the last whisper received",
            category="PLAYER_MGMT",
            params=[CommandParam(name="message", type="string", description="Reply message")],
            example="/reply <message>",
        ),
        CommandDef(name="/players", description="List connected players", category="PLAYER_MGMT", example="/players"),
        CommandDef(
            name="/kick",
            description="Kick a player from the server",
            category="PLAYER_MGMT",
            params=[
                CommandParam(name="player", type="string", description="Player to kick"),
                CommandParam(name="reason", type="string", required=False, description="Kick reason"),
            ],
            example="/kick <player> <reason>",
        ),
        CommandDef(
            name="/ban",
            description="Ban a player from the server",
            category="PLAYER_MGMT",
            params=[
                CommandParam(name="player", type="string", description="Player to ban"),
                CommandParam(name="reason", type="string", required=False, description="Ban reason"),
            ],
            example="/ban <player> <reason>",
        ),
        CommandDef(name="/bans", description="List all banned players", category="PLAYER_MGMT", example="/bans"),
        CommandDef(
            name="/unban",
            description="Unban a player",
            category="PLAYER_MGMT",
            params=[CommandParam(name="player", type="string", description="Player to unban")],
            example="/unban <player>",
        ),
        CommandDef(name="/admins", description="List server admins", category="PLAYER_MGMT", example="/admins"),
        CommandDef(
            name="/promote",
            description="Promote a player to admin",
            category="PLAYER_MGMT",
            params=[CommandParam(name="player", type="string", description="Player to promote")],
            example="/promote <player>",
        ),
        CommandDef(
            name="/demote",
            description="Demote a player from admin",
            category="PLAYER_MGMT",
            params=[CommandParam(name="player", type="string", description="Player to demote")],
            example="/demote <player>",
        ),
        CommandDef(
            name="/color",
            description="Change a player's color",
            category="PLAYER_MGMT",
            params=[
                CommandParam(name="player", type="string", description="Player name"),
                CommandParam(name="color", type="string", description="Color value (e.g. red, #ff0000, or r g b a)"),
            ],
            example="/color <player> <color>",
        ),
        CommandDef(
            name="/mute",
            description="Mute a player",
            category="PLAYER_MGMT",
            params=[CommandParam(name="player", type="string", description="Player to mute")],
            example="/mute <player>",
        ),
        CommandDef(
            name="/unmute",
            description="Unmute a player",
            category="PLAYER_MGMT",
            params=[CommandParam(name="player", type="string", description="Player to unmute")],
            example="/unmute <player>",
        ),
        CommandDef(name="/mutes", description="List all muted players", category="PLAYER_MGMT", example="/mutes"),
        CommandDef(
            name="/ignore",
            description="Ignore a player's chat messages",
            category="PLAYER_MGMT",
            params=[CommandParam(name="player", type="string", description="Player to ignore")],
            example="/ignore <player>",
        ),
        CommandDef(
            name="/unignore",
            description="Stop ignoring a player",
            category="PLAYER_MGMT",
            params=[CommandParam(name="player", type="string", description="Player to unignore")],
            example="/unignore <player>",
        ),
        CommandDef(name="/ignores", description="List all ignored players", category="PLAYER_MGMT", example="/ignores"),
        CommandDef(
            name="/whitelist",
            description="Manage the server whitelist (add/remove/get/clear)",
            category="PLAYER_MGMT",
            params=[CommandParam(name="player", type="string", description="Player to add or remove")],
            example="/whitelist add <player>",
        ),
        CommandDef(name="/banlist", description="Show the ban list", category="PLAYER_MGMT", example="/banlist"),
        CommandDef(
            name="/permissions",
            description="Manage permission groups",
            category="PLAYER_MGMT",
            params=[
                CommandParam(name="group", type="string", required=False, description="Permission group name"),
            ],
            example="/permissions <group>",
        ),
        CommandDef(
            name="/swap-players",
            description="Swap two players' characters",
            category="PLAYER_MGMT",
            params=[
                CommandParam(name="player1", type="string", description="First player"),
                CommandParam(name="player2", type="string", description="Second player"),
            ],
            example="/swap-players <player1> <player2>",
        ),

        # ── SCRIPTING ────────────────────────────────────────────────
        CommandDef(
            name="/command",
            description="Execute a Lua command",
            category="SCRIPTING",
            params=[CommandParam(name="lua_code", type="string", description="Lua code to execute")],
            example="/command game.print('hello')",
        ),
        CommandDef(
            name="/measured-command",
            description="Execute a Lua command and report execution time",
            category="SCRIPTING",
            params=[CommandParam(name="lua_code", type="string", description="Lua code to execute")],
            example="/measured-command game.print('hello')",
        ),
        CommandDef(
            name="/silent-command",
            description="Execute a Lua command without printing output",
            category="SCRIPTING",
            params=[CommandParam(name="lua_code", type="string", description="Lua code to execute")],
            example="/silent-command game.speed = 2",
        ),

        # ── SERVER ───────────────────────────────────────────────────
        CommandDef(name="/version", description="Print the game version", category="SERVER", example="/version"),
        CommandDef(name="/time", description="Print the map age", category="SERVER", example="/time"),
        CommandDef(
            name="/server-save",
            description="Force a server autosave",
            category="SERVER",
            params=[CommandParam(name="name", type="string", required=False, description="Save file name")],
            example="/server-save <name>",
        ),
        CommandDef(name="/seed", description="Print the map seed", category="SERVER", example="/seed"),
        CommandDef(
            name="/config",
            description="Get or set server configuration values",
            category="SERVER",
            params=[CommandParam(name="option", type="string", required=False, description="Config option to get/set")],
            example="/config get afk-auto-kick",
        ),
        CommandDef(name="/evolution", description="Print the evolution factor", category="SERVER", example="/evolution"),
        CommandDef(
            name="/screenshot",
            description="Take a screenshot of the game",
            category="SERVER",
            params=[
                CommandParam(name="resolution", type="string", required=False, description="Screenshot resolution (e.g. 1920x1080)"),
            ],
            example="/screenshot <resolution>",
        ),
        CommandDef(
            name="/open",
            description="Open a player's inventory or map",
            category="SERVER",
            params=[CommandParam(name="target", type="string", required=False, description="What to open")],
            example="/open <target>",
        ),
        CommandDef(name="/alerts", description="Show active alerts", category="SERVER", example="/alerts"),
        CommandDef(
            name="/purge",
            description="Purge a player's chat messages",
            category="SERVER",
            params=[CommandParam(name="player", type="string", description="Player whose messages to purge")],
            example="/purge <player>",
        ),
        CommandDef(name="/clear", description="Clear the console log", category="SERVER", example="/clear"),
        CommandDef(
            name="/space-platform-delete-time",
            description="Set or get the time before idle space platforms are deleted",
            category="SERVER",
            params=[CommandParam(name="minutes", type="integer", required=False, description="Minutes before deletion")],
            example="/space-platform-delete-time <minutes>",
        ),
        CommandDef(name="/delete-blueprint-library", description="Delete your blueprint library", category="SERVER", example="/delete-blueprint-library"),
        CommandDef(name="/toggle-action-logging", description="Toggle logging of player actions", category="SERVER", example="/toggle-action-logging"),

        # ── PERFORMANCE ──────────────────────────────────────────────
        CommandDef(name="/toggle-heavy-mode", description="Toggle heavy mode (extra entity validation)", category="PERFORMANCE", example="/toggle-heavy-mode"),
        CommandDef(
            name="/perf-avg-frames",
            description="Set the number of frames for performance averaging",
            category="PERFORMANCE",
            params=[CommandParam(name="count", type="integer", description="Number of frames to average")],
            example="/perf-avg-frames <count>",
        ),

        # ── DEBUG ────────────────────────────────────────────────────
        CommandDef(name="/editor", description="Toggle the map editor", category="DEBUG", example="/editor"),
        CommandDef(name="/admin", description="Toggle admin status on yourself", category="DEBUG", example="/admin"),
        CommandDef(
            name="/cheat",
            description="Toggle cheat mode or run a cheat subcommand",
            category="DEBUG",
            params=[CommandParam(name="subcommand", type="string", required=False, description="Cheat subcommand (e.g. all)")],
            example="/cheat all",
        ),
        CommandDef(name="/unlock-shortcut-bar", description="Unlock all shortcut bar items", category="DEBUG", example="/unlock-shortcut-bar"),
        CommandDef(name="/unlock-tips", description="Unlock all tips and tricks", category="DEBUG", example="/unlock-tips"),
        CommandDef(name="/reset-tips", description="Reset tips and tricks to unread state", category="DEBUG", example="/reset-tips"),
        CommandDef(name="/large-blueprint-size", description="Toggle allowing larger blueprints", category="DEBUG", example="/large-blueprint-size"),
        CommandDef(name="/mute-programmable-speaker", description="Mute all programmable speakers", category="DEBUG", example="/mute-programmable-speaker"),
    ]
