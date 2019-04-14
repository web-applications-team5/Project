from werkzeug.exceptions import BadRequest, NotFound, MethodNotAllowed, UnsupportedMediaType, NotAcceptable, \
    InternalServerError

from app import app
from app.api.exception.Exceptions import NotFoundError
from app.model.result_schemas import ServiceExceptionSchema
from app.model.service_excpetions import ServiceException


def get_service_exception(msg, status_code, details):
    serviceExceptionSchema = ServiceExceptionSchema()
    serviceException = ServiceException(message=msg, code=status_code, details=details)
    response = serviceExceptionSchema.jsonify(serviceException)
    response.status_code = status_code
    return response


@app.errorhandler(NotFoundError)
def handle_invalid_usage(error):
    return get_service_exception(error.message, error.status_code, error.payload)


@app.errorhandler(Exception)
def handle_unexpected_error(error):
    print(error)
    return get_service_exception('An unexpected error has occurred.', 500, '')


@app.errorhandler(InternalServerError)
def handle_unexpected_error(exception):
    return get_service_exception(exception.name, exception.code, exception.description)


@app.errorhandler(BadRequest)
def handle_unexpected_error(exception):
    return get_service_exception(exception.name, 500, exception.description)


@app.errorhandler(NotFound)
def handle_unexpected_error(exception):
    return get_service_exception(exception.name, exception.code, exception.description)


@app.errorhandler(MethodNotAllowed)
def handle_unexpected_error(exception):
    return get_service_exception(exception.name, exception.code, exception.description)


@app.errorhandler(NotAcceptable)
def handle_unexpected_error(exception):
    return get_service_exception(exception.name, exception.code, exception.description)


@app.errorhandler(UnsupportedMediaType)
def handle_unexpected_error(exception):
    return get_service_exception(exception.name, exception.code, exception.description)