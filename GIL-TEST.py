import sys
import sysconfig


def main() -> None:
    status = sysconfig.get_config_var("Py_GIL_DISABLED")

    print(f"Python version {sys.version}")

    if status is None:
        print(">>> GIL cannot disable")
    elif status == 0:
        print(">>> GIL is active")
    elif status == 1:
        print(">>> GIL is disabled")
    else:
        print(">>> Unknown status")


if __name__ == "__main__":
    main()
