# %%
import os
import sys
import glob
import shutil
import random

# %%
if not os.path.isdir("eye-data/train"):
    os.makedirs("eye-data/train/closed")
    os.makedirs("eye-data/train/open")
    os.makedirs("eye-data/valid/closed")
    os.makedirs("eye-data/valid/open")
    os.makedirs("eye-data/test/closed")
    os.makedirs("eye-data/test/open")

for img in random.sample(os.listdir("eye-data/closed"), 700):
    img = os.path.join("eye-data/closed", img)
    shutil.copy(img, "eye-data/train/closed")
for img in random.sample(os.listdir("eye-data/open"), 700):
    img = os.path.join("eye-data/open", img)
    shutil.copy(img, "eye-data/train/open")
for img in random.sample(os.listdir("eye-data/closed"), 350):
    img = os.path.join("eye-data/closed", img)
    shutil.copy(img, "eye-data/valid/closed")
for img in random.sample(os.listdir("eye-data/open"), 350):
    img = os.path.join("eye-data/open", img)
    shutil.copy(img, "eye-data/valid/open")
for img in random.sample(os.listdir("eye-data/closed"), 175):
    img = os.path.join("eye-data/closed", img)
    shutil.copy(img, "eye-data/test/closed")
for img in random.sample(os.listdir("eye-data/open"), 175):
    img = os.path.join("eye-data/open", img)
    shutil.copy(img, "eye-data/test/open")

# %%
if not os.path.isdir("yawn-data/train"):
    os.makedirs("yawn-data/train/no_yawn")
    os.makedirs("yawn-data/train/yawn")
    os.makedirs("yawn-data/valid/no_yawn")
    os.makedirs("yawn-data/valid/yawn")
    os.makedirs("yawn-data/test/no_yawn")
    os.makedirs("yawn-data/test/yawn")

for img in random.sample(os.listdir("yawn-data/no_yawn"), 700):
    img = os.path.join("yawn-data/no_yawn", img)
    shutil.copy(img, "yawn-data/train/no_yawn")
for img in random.sample(os.listdir("yawn-data/yawn"), 700):
    img = os.path.join("yawn-data/yawn", img)
    shutil.copy(img, "yawn-data/train/yawn")
for img in random.sample(os.listdir("yawn-data/no_yawn"), 350):
    img = os.path.join("yawn-data/no_yawn", img)
    shutil.copy(img, "yawn-data/valid/no_yawn")
for img in random.sample(os.listdir("yawn-data/yawn"), 350):
    img = os.path.join("yawn-data/yawn", img)
    shutil.copy(img, "yawn-data/valid/yawn")
for img in random.sample(os.listdir("yawn-data/no_yawn"), 175):
    img = os.path.join("yawn-data/no_yawn", img)
    shutil.copy(img, "yawn-data/test/no_yawn")
for img in random.sample(os.listdir("yawn-data/yawn"), 175):
    img = os.path.join("yawn-data/yawn", img)
    shutil.copy(img, "yawn-data/test/yawn")
# %%
