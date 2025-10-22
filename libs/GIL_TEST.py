from sysconfig import get_config_var


def gil_test() -> None:
    """
    A simple function to test the Global Interpreter Lock (GIL) behavior in Python.
    """

    gil_status = get_config_var("Py_GIL_DISABLED")

    if gil_status:
        print("GIL is disabled in this Python build.")
    else:
        print("GIL is enabled in this Python Environment.")


if __name__ == "__main__":
    gil_test()
