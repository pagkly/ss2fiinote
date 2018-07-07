wsl sudo apt-get install -y python3 ^
python3-pip ^
idle3 ^
python3-xlib ^
python3-psutil &&^
REM wsl echo "" | sudo tee -a /etc/apt/sources.list
wsl sudo apt-get install -y xdotool ^
wmctrl ^
thunar ^
pdftoppm &&^
wsl sudo -H pip3 install pyscreenshot &&^
wsl pip3 install opencv-python imutils scipy numpy &&^
wsl pip install pillow &&^
REM echo "C:\Users\SP3\Documents\GitHub\FN35OCVbside" | awk '{gsub("C:","/mnt/c");gsub(/([\\])/,"/");print}'
wsl python3 /mnt/c/Users/SP3/Documents/GitHub/FN35OCVbside/libFN33and.py