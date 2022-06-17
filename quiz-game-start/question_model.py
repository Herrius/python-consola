from cgitb import text
from mimetypes import init


class Question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer
