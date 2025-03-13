from http import HTTPStatus


class NotFoundPostError(Exception):
    """Exception raised when an id doesn't return a post"""

    def __init__(
        self, message: str = 'Post not found', status_code=HTTPStatus.NOT_FOUND
    ):
        self.message = message
        self.status_code = status_code
