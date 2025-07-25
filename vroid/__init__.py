from typing import Literal, NamedTuple

from vroid.client import VRoid
from vroid.oauth import VRoidOAuth


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info = VersionInfo(major=0, minor=1, micro=1, releaselevel="final", serial=0)

__version__ = f"{version_info.major}.{version_info.minor}.{version_info.micro}"

if version_info.releaselevel != "final":
    __version__ = f"{__version__}-{version_info.releaselevel}.{version_info.serial}"

__all__ = (
    "VRoid",
    "VRoidOAuth",
)
