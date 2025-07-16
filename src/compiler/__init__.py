"""
Compilador Pascal em Python
"""

__version__ = "1.0.0"
__author__ = "Lucas Guimarães Borges (lcsgborges)"
__email__ = "lcsgborges@gmail.com"

from .lexer import Lexer, Token, TokenType
from .parser import Parser, ParseError
from .interpreter import Interpreter, RuntimeError
from .ast_nodes import *

__all__ = [
    'Lexer', 'Token', 'TokenType',
    'Parser', 'ParseError', 
    'Interpreter', 'RuntimeError',
    'ASTNode', 'Expression', 'Statement', 'Program'
]
