import torch
from huggingface_hub import login
from transformers import AutoProcessor, AutoModelForPreTraining

class ModelProvider:
    def __init__(self) -> None:
        pass

    def load_model(self):
        print("Logging into hugging face")
        login(token="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")
        print("Loading model...")
        model = AutoModelForPreTraining.from_pretrained("meta-llama/Llama-3.2-11B-Vision-Instruct", torch_dtype=torch.bfloat16, device_map="auto")
        model.save_pretrained("wsgi_runtime/model")
        # pipe = FluxPipeline.from_pretrained("models/lumina_model", torch_dtype=torch.bfloat16, device_map="balanced")        
        return model