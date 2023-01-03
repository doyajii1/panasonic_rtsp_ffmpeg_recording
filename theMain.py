from datetime import datetime
import time
import os
from dotenv import load_dotenv
from fileOperation import fileOperatorClass
import ffmpeg

load_dotenv()

# read in basic config info from .env file
USER_ID=os.getenv('USER_ID')
USER_PWD=os.getenv('USER_PWD')
RTSP_URL=os.getenv('RTSP_URL')
FFMPEG_FPS=os.getenv('FFMPEG_FPS')
IP_CAM_BASE_URL=os.getenv('IP_CAM_BASE_URL')
FFMPEG_RECORDING_LEN=os.getenv('FFMPEG_RECORDING_LEN')
RECORDING_PATH = os.getenv('RECORDING_PATH')


#if path is empty in .env file, use recordings folder within project folder
if(len(RECORDING_PATH)==0):
    RECORDING_PATH = os.path.join(os.path.dirname(__file__), 'recordings')


recording_file_suffix = ".mp4"
# http://id:pwd@ip_cam_base_url
url_base = "http://"+USER_ID+":"+USER_PWD+"@"+IP_CAM_BASE_URL


while True:
    #delete early file before start recording
    fileOp = fileOperatorClass()
    if(fileOp.get_first_added_file(RECORDING_PATH) != None):
        fileOp.delete_file()


    #get time for file name
    dt_string = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    print("date and time =", dt_string)


    #adjust pan/tilt specific to panasonic camera(Panasonic BL-C131A)
    if(len(IP_CAM_BASE_URL)>0):
        import requests
        url = url_base+"/nphControlCamera"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        body_center = {"Direction":"HomePosition",
                        "Data":0,
                        "Resolution":"640x480",
                        "Quality":"Standard",
                        "RPeriod":65535,
                        "Size":"STD",
                        "PresetOperation":"Move",
                        "Language":0,
                        "Type":"HomePosition"}

        body_darker = {"Direction":"Darker",
                        "Resolution":"640x480",
                        "Quality":"Standard",
                        "Mode":"MPEG-4",
                        "RPeriod":0,
                        "Size":"STD",
                        "PresetOperation":"Move",
                        "Language":0}

        body_brightSTD = {"Direction":"DefaultBrightness",
                            "Resolution":"640x480",
                            "Quality":"Standard",
                            "Mode":"MPEG-4",
                            "RPeriod":0,
                            "Size":"STD",
                            "PresetOperation":"Move",
                            "Language":0}

        # center camera for panasonic camera
        response = requests.post(url, body_center, headers)
        print("Center Camera - Status Code: ", response.status_code)

        # darken image for panasonic camera
        for x in range(0, 4):
            time.sleep(0.2)
            requests.post(url, body_darker, headers)
            print("Darken Image - Status Code: ", response.status_code)


    # start ffmpeg recording for FFMPEG_RECORDING_LEN seconds
    # rtsp://id:pwd@rtsp_url/nphMpeg4/nil-320x240
    input_url = 'rtsp://'+USER_ID+":"+USER_PWD+"@"+RTSP_URL 
    file_name = RECORDING_PATH+"/"+dt_string+recording_file_suffix
    ffmpeg.input(input_url).filter('fps',FFMPEG_FPS).output(file_name, **{'t':FFMPEG_RECORDING_LEN}).run()