# RTSP client 

Gather RTSP stream from an IP camera and save recordings in mp4 format.

Tested with Panasonic BL-C131A to Raspberry PI 3B.



## Install

### Raspberry Pi OS
```
sudo apt update
sudo apt install -y ffmpeg
pip install -r requirements.txt
```

### OSX
```
brew install ffmpeg
pip install -r requirements.txt
```



## Execute
### Edit `.env` file
Rename `.env_temp` to `.env` and input necessary information as shown in the comments.

- Notes:
* For RTSP url(`RTSP_URL`), port is usually 554. There should be seperate RTSP port setting on the camera setting page.
* `IP_CAM_BASE_URL` is used to call REST APIs to camera(ex. Pan, Tilt). Leave it blank unless you know the API, and python script edit is required)

### Run/Stop/Status
```
./run.sh
```
`run.sh` first kills recording process and then starts recording again.
./stop.sh
`stop.sh` kills recording and ffmpeg processes.
./status.sh
`status.sh` shows status of recording

### Create Cronjob
Have `run.sh` shell script execute through cron
* edit `crontab`
```
crontab -e
```
* place the following line(if using `vim` type `i` before pasting in the line) to the file to make it run everyday at 23:59, and quit editing(type `:wq!`+enter or `^+x`)
```
59 23 * * * cd /path/to/folder/panasonic_ffmpeg_recording && ./run.sh
```



## Useful links
* [Homebrew installation](https://brew.sh/)
* [Panasonic REST APIs](https://camera-sdk.com/p_6705-how-to-connect-to-a-panasonic-camera.html)
