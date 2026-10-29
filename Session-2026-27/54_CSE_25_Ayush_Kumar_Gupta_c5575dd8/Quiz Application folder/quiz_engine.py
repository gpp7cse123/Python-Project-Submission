"""
Quiz Engine Module - Handles data loading, business logic, and scoring.
Diploma Computer Science Engineering - Micro Project
Demonstrates:
  - Classes and Object-Oriented Programming (OOP)
  - File Handling (reading and parsing JSON files)
  - Exception Handling (try-except blocks for file errors)
  - Data Structures: Lists, Dictionaries, and Primitive Data Types
  - Conditional Logic and Iteration (Loops)
"""

import json
import os


class Question:
    """
    Represents an individual multiple-choice question.
    Demonstrates OOP encapsulation: bundling question data and behavior together.
    """

    def __init__(self, q_id, question_text, options, correct_answer, explanation=""):
        # Variables and Data Types:
        # q_id: int
        # question_text: str
        # options: list of strings
        # correct_answer: str
        # explanation: str
        # user_answer: str (stores user's selected option, None if unattempted)
        self.q_id = q_id
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation
        self.user_answer = None  # None indicates question hasn't been answered yet

    def is_attempted(self):
        """Returns True if the user selected an answer, False otherwise."""
        return self.user_answer is not None and self.user_answer.strip() != ""

    def is_correct(self):
        """
        Demonstrates conditional statement:
        Compares the user's selected answer with the verified correct answer.
        """
        if not self.is_attempted():
            return False
        return self.user_answer.strip().lower() == self.correct_answer.strip().lower()

    def set_user_answer(self, answer):
        """Sets or updates the user's answer."""
        self.user_answer = answer

    def clear_user_answer(self):
        """Clears user's selection."""
        self.user_answer = None


class QuizManager:
    """
    Manages quiz state, loading questions from JSON, navigating questions,
    and calculating final results and performance remarks.
    """

    def __init__(self, json_file_path="quiz_data.json"):
        self.json_file_path = json_file_path
        self.raw_data = {}  # Dictionary to hold parsed JSON data
        self.student_name = ""
        self.current_category = ""
        self.questions = []  # List of Question objects for current session
        self.current_index = 0  # Zero-based index of the currently displayed question

        # Load questions on initialization
        self.load_data()

    def load_data(self):
        """
        Demonstrates:
        1. File Handling: Using open() to read files
        2. JSON Processing: json.load()
        3. Exception Handling: Handling FileNotFoundError, json.JSONDecodeError,
           and generic Exceptions gracefully with fallback data.
        """
        try:
            if not os.path.exists(self.json_file_path):
                # Try finding alternative question files in the same directory
                alt_path = os.path.join(os.path.dirname(self.json_file_path), "question.json")
                if os.path.exists(alt_path):
                    self.json_file_path = alt_path
                else:
                    raise FileNotFoundError(f"File not found: '{self.json_file_path}'")

            with open(self.json_file_path, "r", encoding="utf-8") as file:
                self.raw_data = json.load(file)

            # Universal schema support: handles both {"quiz_database": ...} and {"categories": ...}
            if "quiz_database" in self.raw_data and isinstance(self.raw_data["quiz_database"], dict):
                converted = {}
                for key, val in self.raw_data["quiz_database"].items():
                    topic_name = val.get("topic", key.replace("_", " ").title())
                    converted[topic_name] = val.get("questions", [])
                self.raw_data = {"categories": converted}

            # Validate basic JSON structure
            if "categories" not in self.raw_data or not isinstance(self.raw_data["categories"], dict):
                raise ValueError("JSON file is missing the 'categories' dictionary.")

        except FileNotFoundError as fnf_err:
            print(f"[Warning] {fnf_err}. Loading fallback built-in quiz data.")
            self._load_fallback_data()

        except json.JSONDecodeError as json_err:
            print(f"[Warning] Invalid JSON syntax: {json_err}. Loading fallback data.")
            self._load_fallback_data()

        except Exception as gen_err:
            print(f"[Warning] Unexpected error loading quiz data: {gen_err}. Loading fallback data.")
            self._load_fallback_data()

    def _load_fallback_data(self):
        """
        Provides emergency fallback data so the application never crashes during a demo,
        even if the external JSON file is missing or corrupted.
        """
        self.raw_data = {
            "categories": {
                "Python Programming": [
                    {
                        "id": 1,
                        "question": "What is the correct file extension for Python files?",
                        "options": [".pt", ".py", ".pyt", ".python"],
                        "answer": ".py",
                        "explanation": ".py is standard for Python scripts."
                    },
                    {
                        "id": 2,
                        "question": "Which keyword is used to define a function in Python?",
                        "options": ["func", "define", "def", "function"],
                        "answer": "def",
                        "explanation": "'def' defines functions in Python."
                    }
                ],
                "Computer Fundamentals": [
                    {
                        "id": 1,
                        "question": "What does CPU stand for?",
                        "options": [
                            "Central Process Unit",
                            "Central Processing Unit",
                            "Computer Processing Utility",
                            "Central Processor Universal"
                        ],
                        "answer": "Central Processing Unit",
                        "explanation": "CPU executes computer instructions."
                    }
                ],
                "General Knowledge": [
                    {
                        "id": 1,
                        "question": "Who is known as the father of modern computers?",
                        "options": ["Alan Turing", "Charles Babbage", "Bill Gates", "Ada Lovelace"],
                        "answer": "Charles Babbage",
                        "explanation": "Charles Babbage conceptualized mechanical computers."
                    }
                ]
            }
        }

    def get_categories(self):
        """
        Returns a list of available quiz categories.
        Demonstrates dictionary keys retrieval and list conversion.
        """
        if "categories" in self.raw_data:
            return list(self.raw_data["categories"].keys())
        return []

    def start_quiz(self, student_name, category):
        """
        Initializes a new quiz session for a student and category.
        Demonstrates loops, conditionals, and object instantiation.
        """
        # Validate inputs
        name_clean = student_name.strip()
        if not name_clean:
            raise ValueError("Student name cannot be empty.")

        if category not in self.raw_data.get("categories", {}):
            raise ValueError(f"Category '{category}' does not exist.")

        self.student_name = name_clean
        self.current_category = category
        self.current_index = 0
        self.questions = []

        # Iterate over raw question dictionaries and build Question objects (Demonstrates Loop)
        raw_questions = self.raw_data["categories"][category]
        for item in raw_questions:
            q = Question(
                q_id=item.get("id", len(self.questions) + 1),
                question_text=item.get("question", ""),
                options=item.get("options", []),
                correct_answer=item.get("answer", ""),
                explanation=item.get("explanation", "")
            )
            self.questions.append(q)

        if not self.questions:
            raise ValueError(f"No questions found under category '{category}'.")

    def get_total_questions(self):
        """Returns the total number of questions in current quiz."""
        return len(self.questions)

    def get_current_question(self):
        """Returns the current Question object based on current_index."""
        if 0 <= self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def set_current_answer(self, option_text):
        """Records the user's selected answer for the current question."""
        curr_q = self.get_current_question()
        if curr_q:
            curr_q.set_user_answer(option_text)

    def clear_current_answer(self):
        """Clears the user's selected answer for the current question."""
        curr_q = self.get_current_question()
        if curr_q:
            curr_q.clear_user_answer()

    def next_question(self):
        """Advances to the next question if available."""
        if self.has_next():
            self.current_index += 1
            return True
        return False

    def prev_question(self):
        """Goes back to the previous question if available."""
        if self.has_prev():
            self.current_index -= 1
            return True
        return False

    def has_next(self):
        """Returns True if there is a subsequent question."""
        return self.current_index < len(self.questions) - 1

    def has_prev(self):
        """Returns True if there is a preceding question."""
        return self.current_index > 0

    def get_unanswered_count(self):
        """Returns how many questions remain unanswered."""
        unanswered = 0
        for q in self.questions:
            if not q.is_attempted():
                unanswered += 1
        return unanswered

    def calculate_results(self):
        """
        Calculates final score, percentage, counts, and performance remarks.
        Demonstrates loops, counters, mathematical operations, and conditionals.
        Returns a dictionary containing full summary and review data.
        """
        total = len(self.questions)
        correct_count = 0
        incorrect_count = 0
        skipped_count = 0
        detailed_review = []

        # Loop through all questions to tally results
        for idx, q in enumerate(self.questions, start=1):
            is_att = q.is_attempted()
            is_corr = q.is_correct()

            if not is_att:
                skipped_count += 1
                status = "Skipped"
            elif is_corr:
                correct_count += 1
                status = "Correct"
            else:
                incorrect_count += 1
                status = "Incorrect"

            detailed_review.append({
                "number": idx,
                "question": q.question_text,
                "user_answer": q.user_answer if is_att else "Not Attempted",
                "correct_answer": q.correct_answer,
                "status": status,
                "explanation": q.explanation
            })

        # Calculate percentage (Demonstrates arithmetic and rounding)
        percentage = (correct_count / total * 100.0) if total > 0 else 0.0
        percentage = round(percentage, 2)

        # Performance remarks evaluation (Demonstrates if-elif-else hierarchy)
        if percentage >= 90.0:
            remarks = "Outstanding! Exceptional mastery of the subject."
            grade = "A+"
            badge_color = "#10B981"  # Emerald Green
        elif percentage >= 75.0:
            remarks = "Excellent Work! Solid understanding and great performance."
            grade = "A"
            badge_color = "#3B82F6"  # Blue
        elif percentage >= 60.0:
            remarks = "Good Effort! You have a decent grasp, keep practicing."
            grade = "B"
            badge_color = "#F59E0B"  # Amber
        elif percentage >= 40.0:
            remarks = "Average! Re-read key concepts to improve your fundamentals."
            grade = "C"
            badge_color = "#F97316"  # Orange
        else:
            remarks = "Needs Improvement. Review the topics and try again!"
            grade = "D"
            badge_color = "#EF4444"  # Red

        # Return comprehensive results dictionary
        return {
            "student_name": self.student_name,
            "category": self.current_category,
            "total_questions": total,
            "correct": correct_count,
            "incorrect": incorrect_count,
            "skipped": skipped_count,
            "score": correct_count,
            "percentage": percentage,
            "grade": grade,
            "remarks": remarks,
            "badge_color": badge_color,
            "review": detailed_review
        }

    def reset_quiz(self):
        """Resets current quiz questions and index."""
        self.current_index = 0
        for q in self.questions:
            q.clear_user_answer()


# If quiz_engine.py is executed directly, launch the main GUI application
if __name__ == "__main__":
    print("Launching Python Quiz Application...")
    from main import QuizApp
    app = QuizApp()
    app.mainloop()

