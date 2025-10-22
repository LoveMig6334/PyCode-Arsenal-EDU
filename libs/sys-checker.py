import os
import sys


def version_check() -> None:
    """
    A simple function to check and print the current Python version.
    """

    system_version = sys.version_info
    print(
        f"Current Python version: {system_version.major}.{system_version.minor}.{system_version.micro}"
    )


def os_details() -> None:
    """
    A simple function to check and print the current operating system details.
    """

    os_version = os.name
    os_platform = os.sys.platform

    print(f"Operating System: {os_version}, Platform: {os_platform}")


if __name__ == "__main__":
    version_check()
    os_details()
