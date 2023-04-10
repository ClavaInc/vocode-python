from typing import Generator, Optional
from vocode.streaming.agent.base_agent import BaseAgent


class CustomAgent(BaseAgent):
    def respond(
        self,
        human_input,
        is_interrupt: bool = False,
        conversation_id: Optional[str] = None,
    ) -> tuple[str, bool]:
        print('PRINTING SELF')
        print(self)
        print('PRINTING SELF.RESPOND_FUNC')
        print(self.agent_config.respond_func)
        print('PRINTING SELF.RESPOND_FUNC(human_input)')
        print(self.agent_config.respond_func(human_input))
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
