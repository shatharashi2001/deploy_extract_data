import logging
import traceback


class FileNotFoundError(Exception):
    code = 400
    description = {"error message": "No file received."}


class FileNotAcceptedError(Exception):
    code = 400
    description = {
        "error message": "File type is not accepted. Accepted file types: .bmp, .jfif, .jpg, .jpeg, .pdf, .tiff."
    }


def handle_exception(custom_exc):
    exc_message = f"{custom_exc.code} {custom_exc.description['error message']}"
    logging.error(traceback.format_exc())
    logging.error(exc_message)
    return exc_message
