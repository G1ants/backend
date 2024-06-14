import logging

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

log = logging.getLogger(__name__)

router = APIRouter()

class MessageController:
    
    def __init__(self, service: MessageService):
        self.service = service