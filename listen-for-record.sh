#! /bin/bash
### BEGIN INIT INFO
# Provides:          listen-for-record.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# If you want a command to always run, put it here
#./startenv.sh
source /home/pi/miniconda3/bin/activate dashcam

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting listen-for-record.py"
    /usr/local/bin/listen-for-record.py &
    ;;
  stop)
    echo "Stopping listen-for-record.py"
    pkill -f /usr/local/bin/listen-for-record.py
    ;;
  *)
    echo "Usage: /etc/init.d/listen-for-record.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
