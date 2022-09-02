# This is a very simple AI (Artificial Intelligence) that can tell the difference between a circle and a rectangle.

from PIL import Image
import pyttsx3
engine = pyttsx3.init()

image = Image.open("ai_circle1.png")
cir1img = image.load()
circle1_data = []
for y in range(20):
  for x in range(20):
    circle1_data.append(cir1img[x,y])
image = Image.open("ai_circle2.png")
cir2img = image.load()
circle2_data = []
for y in range(20):
  for x in range(20):
    circle2_data.append(cir2img[x,y])
image = Image.open("ai_rect1.png")
rect1img = image.load()
rect1_data = []
for y in range(20):
  for x in range(20):
    rect1_data.append(rect1img[x,y])
image = Image.open("ai_rect2.png")
rect2img = image.load()
rect2_data = []
for y in range(20):
  for x in range(20):
    rect2_data.append(rect2img[x,y])

def check(data, bias, weights):
    to_output_neron = 0
    for i in range(len(data)):
        to_output_neron += data[i]*weights[i]
    if to_output_neron > bias:
        return True
    else:
        return False

def train():
    bias = 0

    weights =      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]            

    while True:
        circle1 = False
        circle2 = False
        rect1 = False
        rect2 = False
        bias += 1
        if check(circle1_data, bias, weights) == True:circle1 = True
        if check(circle2_data, bias, weights) == True:circle2 = True
        if check(rect1_data, bias, weights) == False:rect1 = True
        if check(rect2_data, bias, weights) == False:rect2 = True
        if circle1 == True and circle2 == True and rect1 == True and rect2 == True:return bias,weights
        else:
            if circle1 == False or circle2 == False:
                if circle1 == False:
                    for i in range(len(circle1_data)):
                        weights[i] += circle1_data[i]
                if circle2 == False:
                    for i in range(len(circle2_data)):
                        weights[i] += circle2_data[i]
                if rect1 == False:
                    for i in range(len(rect1_data)):
                        weights[i] += rect1_data[i]
                if rect2 == False:
                    for i in range(len(rect2_data)):
                        weights[i] += rect2_data[i]
            if rect1 == False or rect2 == False:
                if circle1 == False:
                    for i in range(len(circle1_data)):
                        weights[i] -= circle1_data[i]
                if circle2 == False:
                    for i in range(len(circle2_data)):
                        weights[i] -= circle2_data[i]
                if rect1 == False:
                    for i in range(len(rect1_data)):
                        weights[i] -= rect1_data[i]
                if rect2 == False:
                    for i in range(len(rect2_data)):
                        weights[i] -= rect2_data[i]

bias,weights = train()
print("Training Ended")
print(f"BIAS: {bias}")
print(f"Weights: {weights}")
