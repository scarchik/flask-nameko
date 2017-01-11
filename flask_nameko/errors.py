class FlaskNamekoException(Exception):
    pass


class BadConfigurationError(FlaskNamekoException):
    pass


class ClientUnavailableError(FlaskNamekoException):
    pass


class ClusterNotConfiguredError(FlaskNamekoException):
    pass
