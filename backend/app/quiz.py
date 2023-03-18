import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import get_db

router = APIRouter()


@router.get('/')
def get_quizzes(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    quizzes = db.query(models.Quiz).filter(
        models.Quiz.title.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(quizzes), 'quizzes': quizzes}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_quiz(payload: schemas.QuizBaseSchema, db: Session = Depends(get_db)):
    new_quiz = models.Quiz(**payload.dict())
    db.add(new_quiz)
    db.commit()
    db.refresh(new_quiz)
    return {"status": "success", "quiz": new_quiz}


@router.patch('/{quizId}')
def update_quiz(quizId: str, payload: schemas.QuizBaseSchema, db: Session = Depends(get_db)):
    quiz_query = db.query(models.Quiz).filter(models.Quiz.id == quizId)
    db_quiz = quiz_query.first()

    if not db_quiz:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No quiz with this id: {quizId} found')
    update_data = payload.dict(exclude_unset=True)
    quiz_query.filter(models.Quiz.id == quizId).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    db.refresh(db_quiz)
    return {"status": "success", "quiz": db_quiz}


@router.get('/{quizId}')
def get_post(quizId: str, db: Session = Depends(get_db)):
    quiz = db.query(models.Quiz).filter(models.Quiz.id == quizId).first()
    if not quiz:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No quiz with this id: {id} found")
    return {"status": "success", "quiz": quiz}


@router.delete('/{quizId}')
def delete_post(quizId: str, db: Session = Depends(get_db)):
    quiz_query = db.query(models.Quiz).filter(models.Quiz.id == quizId)
    quiz = quiz_query.first()
    if not quiz:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No quiz with this id: {id} found')
    quiz_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)