import torch
from PIL import Image
import torchvision.transforms as transforms
from torchvision.models.segmentation import deeplabv3_resnet50

# Load a pretrained DeepLabV3 model from torchvision
model = deeplabv3_resnet50(pretrained=True)
model.eval()  # Set the model to evaluation mode

# Helper function to preprocess the image for the model
def preprocess_image(image_path):
    img = Image.open(image_path)
    preprocess = transforms.Compose([
        transforms.Resize((768, 768)),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ])
    img_tensor = preprocess(img).unsqueeze(0)
    return img_tensor

# Load the source and initial images
source_image = preprocess_image("/home/orion/orion/analyzing-qr-code-generation-in-python/local/version1-0/qrcode_orioninsist.org.png")
init_image = preprocess_image("/home/orion/orion/analyzing-qr-code-generation-in-python/local/version1-0/qrcode_orioninsist.org.png")

# Perform image-to-image translation using the model
with torch.no_grad():
    output = model(source_image)['out']

# Post-process the output image (optional)
output_image = transforms.ToPILImage()(output.squeeze(0))

# Save the output image or do further processing as needed
output_image.save("output_qrcode.png")