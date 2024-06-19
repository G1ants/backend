import json
import logging
import os
from dotenv import find_dotenv, load_dotenv
import httpx

from app.models.message import MessageRequest, MessageResponse, ProcessedMessageRequest

log = logging.getLogger(__name__)

load_dotenv(find_dotenv(filename=".env"))
ML_ENDPOINT_URL = os.environ.get("ML_ENDPOINT_URL")


class MessageService:

    def process(self, message_request: MessageRequest) -> ProcessedMessageRequest:
        # TODO: Implement logic to process the message request (if any)
        processed_message = ProcessedMessageRequest(
            message=message_request.message,
            chat_history=message_request.chat_history,
            agent=message_request.agent,
        )
        return processed_message

    ###
    ### API logic
    ###
    async def infer(self, input: ProcessedMessageRequest) -> MessageResponse:
        SERVICE_ENDPOINT = "inference"
        try:
            if not ML_ENDPOINT_URL:
                raise ValueError("ML_ENDPOINT_URL is not set in .env file.")

            url: str = f"{ML_ENDPOINT_URL}/{SERVICE_ENDPOINT}"

            data_dict = input.model_dump()

            async with httpx.AsyncClient(timeout=300.0) as client:
                response = await client.post(url, json=data_dict)
                message_response: MessageResponse = MessageResponse.model_validate(
                    response.json()
                )
                return message_response
        except json.JSONDecodeError as e:
            log.error(f"JSON decoding error: {e}")
            raise e
        except Exception as e:
            log.error(f"Unexpected error in infer: {e}")
            raise e
