import logging

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.models.message import MessageRequest, MessageResponse, ProcessedMessageRequest
from app.services.message import MessageService

log = logging.getLogger(__name__)

router = APIRouter()


class MessageController:

    def __init__(self, service: MessageService):
        self.router = APIRouter()
        self.service = service
        self.setup_routes()

    def setup_routes(self):
        router = self.router

        @router.post("/")
        async def start(input: MessageRequest) -> JSONResponse:
            try:
                processed_input: ProcessedMessageRequest = self.service.process(
                    message_request=input
                )
                response: MessageResponse = await self.service.infer(
                    input=processed_input
                )
                return JSONResponse(status_code=200, content=response)
            except Exception as e:
                log.error(f"Unexpected error in essage controller: {e}")
                raise HTTPException(status_code=500, detail=str(e)) from e
