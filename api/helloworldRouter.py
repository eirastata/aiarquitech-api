from fastapi import APIRouter
from api.openai_service import perguntar_chatgpt

router = APIRouter()

@router.get("/api/chat")
async def chat(pergunta: str):

    resposta = perguntar_chatgpt(pergunta)

    return resposta
