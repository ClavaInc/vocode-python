from typing import Generator, Optional
from vocode.streaming.agent.base_agent import BaseAgent
import logging


class CustomAgent(BaseAgent):
    def respond(
        self,
        human_input,
        is_interrupt: bool = False,
        conversation_id: Optional[str] = None,
    ) -> tuple[str, bool]:
        logger = logging.getLogger(__name__)
        logger.debug("PRINTING SELF")
        logger.debug(self)
        logger.debug("PRINTING SELF.RESPOND_FUNC")
        logger.debug(self.agent_config.respond_func)
        logger.debug("PRINTING SELF.RESPOND_FUNC(human_input)")
        logger.debug(self.agent_config.respond_func(human_input))
        response = "Hello, world!"
        return response, False

    def generate_response(
        self,
        human_input,
        is_interrupt: bool = False,
        conversation_id: Optional[str] = None,
    ) -> Generator:
        response = "Hello, world!"
        yield response

    def update_last_bot_message_on_cut_off(self, message: str):
        pass
