import logging

# import google.cloud.logging

# CLIENT = google.cloud.logging.Client()
# CLIENT.setup_logging()


def get_logger(name):
    return logging.getLogger(name)
