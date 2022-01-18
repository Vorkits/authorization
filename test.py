path='/Users/mac/Desktop/flash'
from pathlib import Path
Path(path+'/try again').mkdir(parents=True, exist_ok=True)
for i in range(50):
    Path(path+f'/try again{i}').mkdir(parents=True, exist_ok=True)
    for j in range(30):
        Path(path+f'/try again{i}'+f'/present here{j}').mkdir(parents=True, exist_ok=True)