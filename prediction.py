import requests
import torch
from PIL import Image
# from transformers import MllamaForConditionalGeneration, AutoProcessor

def predict(model,processor,data):
    # Get the image URL and text from the input data
    image_url = data['image']
    text = data['text']
    print("Visia: Image URL :"+image_url)
    print("Visia: text :"+text)

    # model = MllamaForConditionalGeneration.from_pretrained(
    #     "hf_files/model",
    #     torch_dtype=torch.bfloat16,
    #     device_map="auto",
    # )
    # processor = AutoProcessor.from_pretrained("hf_files/processor")

    # url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/0052a70beed5bf71b92610a43a52df6d286cd5f3/diffusers/rabbit.jpg"
    url = image_url
    image = Image.open(requests.get(url, stream=True).raw)

    messages = [
        {"role": "user", "content": [
        {"type": "image"},
        {"type": "text", "text": text}
    ]}
    ]
    input_text = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(
        image,
        input_text,
        add_special_tokens=False,
        return_tensors="pt"
    ).to(model.device)

    output = model.generate(**inputs, max_new_tokens=4096)
    print(processor.decode(output[0]))
    return processor.decode(output[0])


