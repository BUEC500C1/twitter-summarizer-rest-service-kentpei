#!/usr/bin/env python
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import tweetinfo
import re
import os
import subprocess
'''
img = Image.new('RGB', (100, 30), color=(0, 0, 0))
img = 
d = ImageDraw.Draw(img)
d.text((10, 10), "Hello World", fill=(0, 0, 0))
'''
#!/usr/bin/env python
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import tweetinfo
import re
import os
import subprocess
'''
img = Image.new('RGB', (100, 30), color=(0, 0, 0))
img = 
d = ImageDraw.Draw(img)
d.text((10, 10), "Hello World", fill=(0, 0, 0))
'''
def video(png,text,key):
    folder = os.path.exists('pictures')
    if not folder:
        os.makedirs('pictures')
    font = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    for i in range(len(text)):

        #image = Image.open(png)
        #draw = ImageDraw.Draw(image)
        #'/Library/Fonts/Arial.ttf'
        emoji_pattern = re.compile("["
                                    u"\U0001F600-\U0001F64F"  # emoticons
                                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                    "]+", flags=re.UNICODE)
        text[i] = emoji_pattern.sub(r'', text[i])
        img = Image.new('RGB', (600, 400), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        text_better = font.sub('--emoji--', text[i])
        text_better = text_better.encode('utf8')
        # font for windows user
        # font = ImageFont.truetype("arial.ttf", 28, encoding="unic")
        draw.text((0, 200),text_better, fill=(0, 0, 0))
        # save the image
        path = "./pictures/"
        #files = path + "*.png"
        #ffmpeg.input(files, pattern_type='glob', framerate=0.3 * self.num_threads).output('dailyfeed.mov').run()
        img.save(path+str(key)+'0'+ str(i+1) +'.png', optimize=True)
