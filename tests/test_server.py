from rhino_mcp import __version__
from rhino_mcp.server import get_version


def test_get_version_matches_package_version():
    assert get_version() == __version__
