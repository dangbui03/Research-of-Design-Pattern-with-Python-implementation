import abc

class AbstractExpression(metaclass=abc.ABCMeta):
    """
    Declare an abstract Interpret operation that is common to all nodes
    in the abstract syntax tree.
    """
    @abc.abstractmethod
    def interpret(self):
        pass

class NoteExpression(AbstractExpression):
    """
    Implement an Interpret operation for note symbols in the music grammar.
    """
    def __init__(self, note):
        self.note = note

    def interpret(self):
        if self.note == "C":
            return "C là nốt đô - Một nốt nhạc căn bản"
        elif self.note == "D":
            return "D là nốt rê - Một nốt nhạc căn bản"
        elif self.note == "E":
            return "E là nốt mi - Một nốt nhạc căn bản"
        elif self.note == "F":
            return "F là nốt fa - Một nốt nhạc căn bản"
        elif self.note == "G":
            return "G là nốt sol - Một nốt nhạc căn bản"
        elif self.note == "A":
            return "A là nốt la - Một nốt nhạc căn bản"
        elif self.note == "B":
            return "B là nốt si - Một nốt nhạc căn bản"

class MusicInterpreter:
    """
    The client class that interprets musical expressions.
    """
    def __init__(self):
        self.expression = None

    def interpret(self, musical_expression):
        parts = musical_expression.split()
        for part in parts:
            if part.isalpha():
                self.expression = NoteExpression(part)
                print(self.expression.interpret())

def main():
    music_interpreter = MusicInterpreter()

    musical_expression = "C D E F G A B"
    music_interpreter.interpret(musical_expression)

if __name__ == "__main__":
    main()
