class _PurrCompileException(Exception):

    """Generic exception for Purr compilation"""

    def __init__(self, message: str, line: int, col: int):
        message = f"[x] {message} | Line: {line} Col: {col}"
        super().__init__(message)


class PurrCompileInternalException(_PurrCompileException):

    """Exception likely due to a bug in compiler"""

    def __init__(self, message: str, line: int, col: int):
        message = f"PurrCompileInternalException: {message}"
        super().__init__(message, line, col)


class PurrCompileSyntaxException(_PurrCompileException):

    """Exception due to syntax error"""

    def __init__(self, message: str, line: int, col: int):
        message = f"PurrCompileSyntaxException: {message}"
        super().__init__(message, line, col)


class PurrCompileASTException(_PurrCompileException):

    """Exception due to error in AST"""

    def __init__(self, message: str, line: int, col: int):
        message = f"PurrCompileASTException: {message}"
        super().__init__(message, line, col)
