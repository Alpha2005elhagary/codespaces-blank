from abc import ABC, abstractmethod
class Quiz(ABC):
    def __init__(self, question, answer, score=0):  # Fixed spelling of score
        self.question = question
        self.answer = answer
        self.score = score
    @abstractmethod
    def perform_action(self):
        pass
class QuestionManager(Quiz):
    def __init__(self, question, answer, score=0):
        super().__init__(question, answer, score)
    def adding_and_updating(self):
        return f"Question added/updated: {self.question}"
class QuizManager(Quiz):
    def __init__(self, question, answer, score=0):
        super().__init__(question, answer, score)
    def quiz_run(self):
        print("The quiz has started")
        print("Answer the question:")
        print(f"Question: {self.question}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == self.answer.lower():
            print("Correct!")
            self.score = 1
        else:
            print(f"Wrong! The correct answer was: {self.answer}")
        return self.score
class ScoreManager(Quiz):
    def __init__(self, question, answer, score=0):
        super().__init__(question, answer, score)
    def calculate_score(self):
        return self.score
class MultipleChoiceQuestion(Quiz):
    def __init__(self, question, answer, options, score=0):
        super().__init__(question, answer, score)
        self.options = options
    def display_question(self):
        print(f"Question: {self.question}")
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")
    def perform_action(self):
        self.display_question()
        user_answer = input("Choose the correct option (1/2/3/4): ").strip()
        if user_answer == self.answer:
            print("Correct!")
            self.score = 1
        else:
            print("Wrong answer!")
        return self.score
class TrueFalseQuestion(Quiz):
    def __init__(self, question, answer, score=0):
        super().__init__(question, answer, score)
    def display_question(self):
        print(f"Question: {self.question} (True/False)")
    def perform_action(self):
        self.display_question()
        user_answer = input("Your answer (True/False): ").strip().lower()
        if user_answer == self.answer.lower():
            print("Correct!")
            self.score = 1
        else:
            print(f"Wrong! The correct answer was: {self.answer}")
        return self.score
class IQuestionRepository(Quiz):
    def __init__(self, question, answer, score=0):
        super().__init__(question, answer, score)
    def store_and_fetch(self):
        return self.question, self.answer
class IScoreCalculable(Quiz):
    def __init__(self, question, answer, score=0):
        super().__init__(question, answer, score)
    def calculations(self):
        if self.score == 0:
            return 0
        score_percentage = (self.score / 1) * 100  # Just an example calculation
        return round(score_percentage, 2)
question = "What is the capital of France?"
answer = "3"
options = ["London", "Berlin", "Paris", "Madrid"]
mcq = MultipleChoiceQuestion(question, answer, options)
mcq.perform_action()
tfq = TrueFalseQuestion("Is Python a programming language?", "True")
tfq.perform_action()