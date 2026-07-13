from fastapi import APIRouter, HTTPException, status

from schemas.quizSchema import QuizCreate, QuizResponse, QuizUpdate
from services import quizService

quizRouter = APIRouter(prefix="/quizzes", tags=["Quizzes"])


@quizRouter.post("/", response_model=QuizResponse, status_code=status.HTTP_201_CREATED)
def create_quiz(payload: QuizCreate) -> QuizResponse:
    return quizService.create_quiz(payload)


@quizRouter.get("/", response_model=list[QuizResponse])
def get_quizzes() -> list[QuizResponse]:
    return quizService.get_quizzes()


@quizRouter.get("/{quiz_id}", response_model=QuizResponse)
def get_quiz(quiz_id: str) -> QuizResponse:
    quiz = quizService.get_quiz(quiz_id)
    if quiz is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")
    return quiz


@quizRouter.put("/{quiz_id}", response_model=QuizResponse)
def update_quiz(quiz_id: str, payload: QuizUpdate) -> QuizResponse:
    quiz = quizService.update_quiz(quiz_id, payload)
    if quiz is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")
    return quiz


@quizRouter.delete("/{quiz_id}", status_code=status.HTTP_200_OK)
def delete_quiz(quiz_id: str) -> dict[str, str]:
    deleted = quizService.delete_quiz(quiz_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")
    return {"message": "Quiz deleted successfully"}