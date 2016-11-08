# Warp Speed

Challenge consisted of the following image:
![Challenge](files/forensics-150-warp_speed/warp_speed.5978d1405660e365872cf72dddc7515603f657f12526bd61e56feacf332cccad.jpg)

```
$ exiftool warp_speed.5978d1405660e365872cf72dddc7515603f657f12526bd61e56feacf332cccad.jpg | grep "Image Size"
Image Size                      : 1000x250
```

We need to rearrange the picture to the (almost) square. Having a matrix with the following composition

```
aaaabbb
aaaabbb
bccccdd
bccccdd
ddeeeef
ddeeeef
```

our goal is to create several lines, joining each `n`-th line `modulo` number of lines

```
aaaabbbccccddddeeeeff
aaaabbbccccddddeeeeff
```

.. finally we group the pixels by first `m` pixels from the arrays and iterate to the next position.

```python
#!/usr/bin/env python

import numpy as np
from PIL import Image
from collections import defaultdict

tmp = defaultdict(list)
data = np.zeros((504, 504, 3), dtype=np.uint8)

img = Image.open('warp_speed.5978d1405660e365872cf72dddc7515603f657f12526bd61e56feacf332cccad.jpg')
img = img.convert("RGB")

pix = img.load()
x_size, y_size = img.size[0], img.size[1]

# Each y % 8 line forms a long list of pixels in our dictionary
def parse_pixels():
  for y in range(y_size):
    for x in range(x_size):
      tmp[y % 8].append(pix[x, y])

# Take the 504 pixels from every list, then iterate to the next 504 pixels
def rearrange():
  for i in range((250000 / 504 / 8) - 1):
    for n in range(8):
      data[i*8 + n] = tmp[n][i*504:i*504+504]

parse_pixels()
rearrange()

img = Image.fromarray(data, 'RGB')
img.show()
```

![Solution](forensics-150-warp_speed.png)
