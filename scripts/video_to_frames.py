import cv2, os, time
import imagehash
import numpy as np
from alive_progress import alive_bar
from skimage.metrics import structural_similarity as ssim
print('''   



_|      _|                      _|        _|  
_|_|  _|_|    _|_|_|    _|_|_|  _|_|_|        
_|  _|  _|  _|    _|  _|        _|    _|  _|  
_|      _|  _|    _|  _|        _|    _|  _|  
_|      _|    _|_|_|    _|_|_|  _|    _|  _|  
''')

start_time = time.perf_counter()
def CaptureFrames(num):
  vidcap = cv2.VideoCapture(f'{num}.mp4')
  os.makedirs(f"./frames/{num}_frames", exist_ok = True)
  success,image = vidcap.read()
  count = 0
  last_img = None

  with alive_bar(title=f'processing {num}.mp4', spinner='triangles', bar='bubbles') as bar:
    while success:
      success,image = vidcap.read()
      croped = image[78:994,630:1347]

      cv2.imshow('video', croped)
      if cv2.waitKey(1) == 27:
        exit(0)
      smol_size = tuple(map(lambda x: int(x*0.05) , croped.shape))
      smol = cv2.resize(croped, (smol_size[0], smol_size[1]), interpolation = cv2.INTER_AREA)
      smol_gray = cv2.cvtColor(smol,cv2.COLOR_BGR2GRAY)
      # print('Read a new frame: ', success)
      if last_img is not None:
        # breakpoint()
        # this_hash = imagehash.average_hash(croped)
        # last_hash = imagehash.average_hash(last_img)
        
        
        s = ssim(smol_gray,last_img) 
        # difference =  cv2.subtract(croped, last_img)
        # result = not(np.bitwise_xor(croped,last_img).any())
        # result = not np.any(difference)
        # cv2.imshow('video', difference)
        # breakpoint()
        # print(s)
        # print(s)
        if s > 0.9 :
          continue
      last_img = smol_gray
      cv2.imwrite("frames/%d_frames/%d.jpg" %( num ,count), croped)     # save frame as JPEG file      
      count += 1
      bar()

# breakpoint()
# CaptureFrames(71)
# CaptureFrames(73)
# CaptureFrames(74)
# CaptureFrames(75)
# CaptureFrames(76)
# CaptureFrames(77)
# CaptureFrames(78)

for i in range(89,101):
  try:
    CaptureFrames(i)
  except:
    continue
print("")
print(f"\nProcess completed in {time.perf_counter()-start_time} seconds.")
input('\nPress ENTER to exit')