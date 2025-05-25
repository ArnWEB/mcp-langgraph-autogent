# from transformers import AutoModelForCausalLM, AutoTokenizer
from abc import ABC
from typing import Any, List, Mapping, Optional

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers.pipelines import pipeline

from utils.huggingfacellm_local import HuggingFaceLLMLocal

# from utils.async_wrapper import AsyncChatModelWrapper



class QwenLLM:
    def __init__(self):
        model_name = "qwen"
        local_path = rf"C:\Arnab's Projects\Python\model_loading_hf_poc\local_models\{model_name}"
        model, tokenizer = HuggingFaceLLMLocal(
            model_name=model_name, local_load_path=local_path
        ).get_llm_and_tokenizer()

        pipe = pipeline(
            "text-generation", model=model, tokenizer=tokenizer, device_map="auto"
        )

        self.llm = HuggingFacePipeline(pipeline=pipe)

        self.chat_model = ChatHuggingFace(llm=self.llm, tokenizer=tokenizer)
        # self.async_chat_model = AsyncChatModelWrapper(self.chat_model)

    def get_chat_and_base_model(self):
        return self.chat_model, self.llm




if __name__ == "__main__":
    pass