import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import gradio as gr

# Define your classifier

class Classifier(nn.Module):
  def __init__(self, input_size, hidden_size, num_classes) -> None:
    super(Classifier, self).__init__()

    self.fc1 = nn.Linear(input_size, hidden_size)
    self.relu = nn.ReLU()
    self.fc2 = nn.Linear(hidden_size, num_classes)

  def forward(self, x):
    out = x.view(-1, 28*28)
    out = self.fc1(out)
    out = self.relu(out)
    out = self.fc2(out)
    return out

# Load model
model = Classifier(28*28, 512, 10)
model.load_state_dict(torch.load("/Users/sandhiya.cv/Downloads/Gradio/model.pth", map_location=torch.device('cpu')))
model.eval()

# Define preprocessing
transform = transforms.Compose([
    transforms.Grayscale(),     # ensure image is grayscale
    transforms.Resize((28, 28)),
    transforms.ToTensor()
])

# Inference function
def predict(image):
    img = transform(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        outputs = model(img)
        _, predicted = torch.max(outputs, 1)
    return f"Predicted Class: {predicted.item()}"

# Gradio interface
gr.Interface(fn=predict, inputs=gr.Image(type="pil"), outputs="text", title="Digit Classifier").launch()
