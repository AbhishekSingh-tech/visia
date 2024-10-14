import torch
from huggingface_hub import login
from transformers import AutoProcessor, AutoModelForPreTraining

class ProcessorProvider:
    def __init__(self) -> None:
        pass

    def load_processor(self):
        print("Logging into hugging face")
        login(token="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")
        print("Loading model...")
        processor = AutoProcessor.from_pretrained("meta-llama/Llama-3.2-11B-Vision-Instruct")
        processor.save_pretrained("wsgi_runtime/processor")
        # pipe = FluxPipeline.from_pretrained("models/lumina_model", torch_dtype=torch.bfloat16, device_map="balanced")        
        return processor