import tensorflow as tf
from PIL import Image

TOTAL = 1000
filenames = []
for i in range(1,TOTAL+1):
    for type in ['COVID','Normal', 'Viral Pneumonia']:
        filenames.append(f'./dataset/{type}/images_with_mask/{type}-{i}.png')
for i in filenames:
  img=Image.open(i)
  a=img.convert("L", palette=Image.ADAPTIVE, colors=8)
  a.save(i)
