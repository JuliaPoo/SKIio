class PurrCompileException(Exception):

    """Generic exception for Purr compilation"""

    def __init__(self, message: str, line: int, col: int):
        message = f"[x] {message} | Line: {line} Col: {col}"
        super().__init__(message)


class PurrCompileInternalException(PurrCompileException):

    """Exception likely due to a bug in compiler"""

    def __init__(self, message: str, line: int, col: int):
        message = f"PurrCompileInternalException: {message}"
        super().__init__(message, line, col)


class PurrCompileSyntaxException(PurrCompileException):

    """Exception due to syntax error"""

    def __init__(self, message: str, line: int, col: int):
        message = f"PurrCompileSyntaxException: {message}"
        super().__init__(message, line, col)


class PurrCompileASTException(PurrCompileException):

    """Exception due to error in AST"""

    def __init__(self, message: str, line: int, col: int):
        message = f"PurrCompileASTException: {message}"
        super().__init__(message, line, col)


class SKIioInternalException(Exception):
    """Generic exception happening within SKIio code"""

    def __init__(self, message: str):
        message = f"[x] SKIioInternalException: {message}"
        super().__init__(message)


class SKIioInterpreterException(Exception):
    """Generic exception happening while interpreting SKIio"""

    def __init__(self, message: str):
        message = f"[x] SKIioInterpreterException: {message}"
        super().__init__(message)
