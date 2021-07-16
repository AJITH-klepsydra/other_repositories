# Image to ascii
## Opencv,Python 

#### Watch __[Youtube tutorial](https://www.youtube.com/watch?v=o50QiZeNFH8)__of this project

___
<img src="https://i9.ytimg.com/vi/o50QiZeNFH8/maxresdefault.jpg?time=1606501500000&sqp=CPyIhf4F&rs=AOn4CLCAf3bC4m8eJxgcqkZr5GodEoyGHw" >



## Code

Details about the __[Project](https://github.com/AJITH-klepsydra/Image_To_Ascii_Art/)__ ,

## Set-Up
```bash
import (os,time,pickle)
from main import ImageToAscii
```
```bash
$ pip install cv2 && pip install numpy
//make suitable changes to the runner file
$ python runner.py
```

Run the runner.py file
>convert image to ascii art with

```bash
obj = ImageToAscii("/home/klepsydra/Pictures/me/wedding_proposal.jpg", 4)

```
> Video to ascii art pickle file
```bash
obj = ImageToAscii("/home/klepsydra/Desktop/videoplayback.mp4", 5)
obj.video_ascii()

```
> Read a pickle file
```bash
def read():
	pickle_off = open ("output.txt", "rb")
	emp = pickle.load(pickle_off)
	for el in emp:
		print(el)
		time.sleep(0.02)
		os.system('clear')
read()
```
---

### image to ascii 

#### OpenCv,python
