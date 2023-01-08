# ffAlive

Run FFMPEG commands with progress bars.

## Usage

```python
from ffAlive import ffAlive
ffAlive( 'input.mp4', 'output.mov' )
```

It's that simple! If you want to add additional options, add them as a list in the third paramater:

```python
from ffAlive import ffAlive
ffAlive( 'input.mp4', 'output.mov', [ '-c:v', 'prores_ks' ] )
```

And if you have something more complex, you can use `False` for the first two parameters, and put everything in the list.

```python
from ffAlive import ffAlive
ffAlive( False, False, [ 
    '-i', 'left.wav',
    '-i', 'right.wav',
    '-i', 'centre.wav',
    '-i', 'lfe.wav',
    '-i', 'ls.wav',
    '-i', 'rs.wav',
    '-filter_complex', '[0][1][2][3][4]amerge=inputs=5,channelmap=map=0|1|2|3|4|5:5.1',
    '5-1.wav',
    '-ac', '2',
    'stereo.wav'
] )
```

It also has a useful ffprobe tool, that outputs as a dictionary.

``` python
from ffAlive import ffprobe
print( ffprobe( 'input.mp4' ) )
```