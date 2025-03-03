import torch
from torchvision import transforms
from PIL import Image
import requests
from io import BytesIO


def upscale_image_with_esrgan(input_path, output_path):
    img = Image.open(input_path).convert('RGB')

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.unsqueeze(0))  
    ])

    img_tensor = transform(img)

    with torch.no_grad():

        upscaled_tensor = model(img_tensor)  

    upscaled_img = transforms.ToPILImage()(upscaled_tensor.squeeze(0))

    upscaled_img.save(output_path)
    print(f"Upscaled image saved at {output_path}")

