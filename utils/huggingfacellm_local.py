
import os
from typing import Optional

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer


class HuggingFaceLLMLocal:
    def __init__(self, model_name: str, max_new_tokens: int = 256, local_load_path: Optional[str] = None):
        self.model_name = model_name
        self.max_new_tokens = max_new_tokens
        self.device = self._get_device()
        print(self.device)

        if local_load_path and os.path.exists(local_load_path):
            print(f"🔄 Loading model from local path: {local_load_path}")
            self.tokenizer = AutoTokenizer.from_pretrained(local_load_path, use_fast=True,trust_remote_code=True)
            self.model = AutoModelForCausalLM.from_pretrained(
                local_load_path,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                device_map="auto" if self.device != "cpu" else None,
                trust_remote_code=True
            )
        else:
            print(f"⬇️ Downloading model from Hugging Face Hub: {model_name}")
            self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                device_map="auto" if self.device != "cpu" else None,
            )
            self.save_model(local_load_path)

        self.streamer = TextStreamer(self.tokenizer)

    def get_llm_and_tokenizer(self):
        return self.model,self.tokenizer


    def _get_device(self) -> str:
        if torch.cuda.is_available():
            return "cuda"
        elif torch.backends.mps.is_available():
            return "mps"
        else:
            return "cpu"

    def save_model(self, save_path: str):
        """Save model and tokenizer to local directory."""
        os.makedirs(save_path, exist_ok=True)
        print(f"💾 Saving model and tokenizer to {save_path}...")
        self.model.save_pretrained(save_path)
        self.tokenizer.save_pretrained(save_path)
        print("✅ Save complete.")

if __name__ == "__main__":
    model_name = ""
    local_path = r"C:\Arnab's Projects\Python\model_loading_hf_poc\local_models\qwen"

    # # First-time load from Hugging Face and save locally
    # llm = HuggingFaceLLM(model_name=model_name)
    # llm.save_model(save_path=local_path)

    # Later: Load from local path without Internet

    llm_local = HuggingFaceLLMLocal(model_name=model_name, local_load_path=local_path)

    system_msg = "You're a helpful assistant"
    user_question = "What is the capital of India?"

    # response = llm_local.generate_assistant_response(system_msg, user_question)
    # print("\nAssistant:", response)
