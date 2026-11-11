"""REST API versions this package speaks, and the generated package for each.

Keys are the version in the appliance's URL path (``/api/v{key}/...``), which is not
always the product version: Veeam Backup for Microsoft Azure 8.x serves ``/api/v8`` and
9.x serves ``/api/v9``.
"""

VERSION_TO_PACKAGE = {
    "8": "veeam_az.v8",
    "9": "veeam_az.v9",
}

# Other spellings accepted by VeeamClient, mapped to a key above. "8.1" was this
# package's only key before 0.3.0 even though no appliance serves /api/v8.1, so
# existing callers that pass it keep working and now reach /api/v8.
VERSION_ALIASES = {
    "8.0": "8",
    "8.1": "8",
    "9.0": "9",
}


def resolve_api_version(api_version: str) -> str:
    """Return the VERSION_TO_PACKAGE key for a version or alias ("v8.1" -> "8")."""
    version = str(api_version).strip().lstrip("vV")
    version = VERSION_ALIASES.get(version, version)
    if version not in VERSION_TO_PACKAGE:
        raise ValueError(f"Unsupported API version: {api_version}")
    return version
