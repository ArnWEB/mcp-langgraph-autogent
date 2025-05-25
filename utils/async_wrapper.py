import asyncio
from typing import Any, List

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage


class AsyncChatModelWrapper(BaseChatModel):
    def __init__(self, chat_model: BaseChatModel):
        self.chat_model = chat_model

    @property
    def _llm_type(self) -> str:
        return "async_wrapper"

    def _generate(self, messages: List[BaseMessage], stop: Any = None) -> Any:
        # Required by BaseChatModel but not used because we override `ainvoke`
        raise NotImplementedError("Use `ainvoke` instead.")

    def _call_sync(self, input: Any) -> Any:
        return self.chat_model.invoke(input)

    async def ainvoke(self, input: Any, **kwargs: Any) -> Any:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._call_sync, input)
