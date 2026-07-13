from datetime import datetime

from pydantic import BaseModel, ConfigDict

from models.quizModel import Quiz, Question


class QuizCreate(Quiz):
    """Schema used for creating a quiz."""
    pass


class QuizUpdate(BaseModel):
    title: str | None = None
    difficulty: str | None = None
    totalQuestions: int | None = None
    questions: list[Question] | None = None


class QuizResponse(Quiz):
    id: str
    createdAt: datetime
    updatedAt: datetime

    model_config = ConfigDict(from_attributes=True)