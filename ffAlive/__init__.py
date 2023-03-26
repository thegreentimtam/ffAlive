import subprocess
import json
from alive_progress import alive_bar
from ffmpeg_progress_yield import FfmpegProgress

def ffprobe( file: str ) :
    ffprobe = subprocess.Popen([
        'ffprobe',
        '-print_format', 'json',
        '-show_streams',
        '-show_format',
        '-loglevel', 'quiet',
        '-hide_banner',
        file
    ], stdout=subprocess.PIPE ).stdout.read().strip().decode("utf-8")
    return json.loads( ffprobe )

def ffGetTotal( input ):
    metadata = ffprobe( str(input) )
    if 'streams' in metadata:
        for stream in metadata['streams']:
            if ( 'codec_type' in stream ) and ( stream['codec_type'] == 'video' ):
                if 'nb_frames' in stream:
                    return int( stream['nb_frames'] )
    if 'format' in metadata:
        if 'duration' in metadata['format']:
            return round( float( metadata['format']['duration'] ) )
    return 100

def ffCommand( input, output, options = [] ):
    command = [
            'ffmpeg',
            '-y',
    ]
    command = command + [ '-i', input ] if input else command
    command = command + options
    command.append( output ) if output else command
    return command

def ffAlive( input, output, options = [] ):
    with alive_bar( ffGetTotal( input ), manual=True ) as bar:
        ff_progress = FfmpegProgress( ffCommand( input, output, options ) )
        for progress in ff_progress.run_command_with_progress():
            bar( progress / 100 )