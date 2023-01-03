#!/bin/bash
#check and kill python + ffmpeg process
pyProcID=$(ps -ef | grep theMain.py | grep -v grep | awk '{print $2}')
#test pid
#echo $pyProcID
if [ -z $pyProcID ]
then
      echo "theMain(\$pyProcID) is not running"
else
      echo "theMain(\$pyProcID) is running (PID: $pyProcID)"
      echo "Stopping PID: $pyProcID"
      $(ps -ef | grep theMain.py | grep -v grep | awk '{print $2}' | xargs kill -9)
fi

#although python process died, ffmpeg process stayed alive
sleep 2

pyProcID=$(ps -ef | grep ffmpeg | grep -v grep | awk '{print $2}')
#test pid
#echo $pyProcID
if [ -z $pyProcID ]
then
      echo "ffmpeg(\$pyProcID) is not running"
else
      echo "ffmpeg(\$pyProcID) is running (PID: $pyProcID)"
      echo "Stopping PID: $pyProcID"
      $(ps -ef | grep ffmpeg | grep -v grep | awk '{print $2}' | xargs kill -9)
fi

#start process
echo "starting..."
nohup python theMain.py > recording.log 2>&1 &

pyProcID=$(ps -ef | grep theMain.py | grep -v grep | awk '{print $2}')
#test pid
#echo $pyProcID
if [ -z $pyProcID ]
then
      echo "theMain(\$pyProcID) is not running"
else
      echo "theMain(\$pyProcID) is running (PID: $pyProcID)"
fi

#although python process died, ffmpeg process stayed alive
sleep 5

pyProcID=$(ps -ef | grep ffmpeg | grep -v grep | awk '{print $2}')
#test pid
#echo $pyProcID
if [ -z $pyProcID ]
then
      echo "ffmpeg(\$pyProcID) is not running"
else
      echo "ffmpeg(\$pyProcID) is running (PID: $pyProcID)"
fi