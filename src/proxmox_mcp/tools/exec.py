"""Exec tools — run commands inside containers."""

from __future__ import annotations

from proxmox_mcp.server import mcp
from proxmox_mcp.tools import safety_checked, get_client
from proxmox_mcp.models import ProxmoxExecResponse


@mcp.tool()
@safety_checked
async def execute_lxc_command(node: str, vmid: int, command: str, confirmed: bool = False) -> dict:
    """Run a shell command inside an LXC container."""
    return await get_client().fetch_and_validate(
        f"/nodes/{node}/lxc/{vmid}/exec",
        ProxmoxExecResponse, method="POST",
        params={"command": command},
    )
