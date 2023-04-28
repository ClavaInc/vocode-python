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
        response = self.agent_config.respond_func(human_input, conversation_id)
        return response, False

    def generate_response(
        self,
        human_input,
        is_interrupt: bool = False,
        conversation_id: Optional[str] = None,
    ) -> Generator:
        response = self.agent_config.respond_func(human_input, conversation_id)
        yield response

    def update_last_bot_message_on_cut_off(self, message: str):
        pass
