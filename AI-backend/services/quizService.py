from datetime import datetime
from typing import Optional
from uuid import uuid4

from schemas.quizSchema import QuizCreate, QuizResponse, QuizUpdate

_quizzes: dict[str, QuizResponse] = {}


def create_quiz(payload: QuizCreate) -> QuizResponse:
    quiz_id = str(uuid4())
    now = datetime.utcnow()

    quiz = QuizResponse(
        id=quiz_id,
        **payload.model_dump(),
    )

    _quizzes[quiz_id] = quiz
    return quiz


def get_quizzes() -> list[QuizResponse]:
    return list(_quizzes.values())


def get_quiz(quiz_id: str) -> Optional[QuizResponse]:
    return _quizzes.get(quiz_id)


def update_quiz(quiz_id: str, payload: QuizUpdate) -> Optional[QuizResponse]:
    quiz = _quizzes.get(quiz_id)
    if quiz is None:
        return None

    update_data = payload.model_dump(exclude_unset=True)
    if not update_data:
        return quiz

    for field, value in update_data.items():
        setattr(quiz, field, value)

    quiz.updatedAt = datetime.utcnow()
    _quizzes[quiz_id] = quiz
    return quiz


def delete_quiz(quiz_id: str) -> bool:
    quiz = _quizzes.pop(quiz_id, None)
    return quiz is not None