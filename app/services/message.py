import logging
from dotenv import find_dotenv, load_dotenv

log = logging.getLogger(__name__)

load_dotenv(find_dotenv(filename=".env"))

class MessageService:
    
    ###
    ### Main pipeline logic
    ###
    async def start(self, input):
        pass
    
    ###
    ### API logic
    ###
    async def infer(self, input):
        pass
