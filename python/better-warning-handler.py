import warnings
import traceback


# Custom function to display warning with a call stack
def custom_warning_handler(message, category, filename, lineno, file=None, line=None):
    print(f"{filename}:{lineno}: {category.__name__}: {message}")

    print("Call stack:")
    print("".join(traceback.format_stack()))
