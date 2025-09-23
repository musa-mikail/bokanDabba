from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.langgraph.core import process_input

router = APIRouter()

class InputRequest(BaseModel):
    prompt: str

class OutputResponse(BaseModel):
    result: str

@router.post("/process", response_model=OutputResponse)
def process(request: InputRequest):
    try:
        result = process_input(request.prompt)
        return OutputResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))