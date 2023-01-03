# import ffmpeg
# input_url = 'rtsp://id:pwd@192.168.0.253/nphMpeg4/nil-640x480'
# ffmpeg.input(input_url).filter('fps',5).output('test.mp4', **{'t':180}).run()

# import os
# dirname = os.path.dirname(__file__)
# filename = os.path.join(dirname, 'recordings/')
# print(dirname)
# print(filename)

import os
from dotenv import load_dotenv
load_dotenv()
USER_ID = os.getenv('USER_ID')
RECORDING_PATH = os.getenv('RECORDING_PATH')
print(USER_ID)
print(RECORDING_PATH)
print(type(RECORDING_PATH))
print(len(RECORDING_PATH))
