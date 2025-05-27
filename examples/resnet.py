from torchvision import models, transforms
import torch
from PIL import Image

with open('./data/imagenet_classes.txt') as f:
    labels = [l.strip() for l in f.readlines()]

resnet = models.resnet101(weights=models.ResNet101_Weights.DEFAULT)
preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )])

img = Image.open('./data/cholo.png')
img_t = preprocess(img)
batch_t = torch.unsqueeze(img_t,0)
resnet.eval()
out = resnet(batch_t)
_, ix = torch.max(out,1)
ix_value = ix[0]
pct = torch.nn.functional.softmax(out,dim=1)[0]*100
print(labels[ix_value], pct[ix_value].item())