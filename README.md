# Burrito
A very lightweight(4kb) Web Browser named Burrito that was built for the Raspbian OS on the Raspberry Pi.   
This was a very quick implementation due to browser lag (Chromium and FireFox) when I was testing my Pi. 

## Installation  
**Note: Previous installation no longer works. I have updated with how to install, but haven't tested it.**
1. `git clone git@github.com:aarogrammer/Burrito-Browser.git`  
2. `sudo apt-get install python-webkit python-webkit-dev` (to install python programs that we need for the browser to work)
If you cannot find these packages to install, simply use `apt-cache search packagename`.  

To create a Desktop shortcut  
`sudo cp /home/$USER/Burrito/Burrito.desktop /home/$USER/Desktop  `
### Note:  
You will have to manually change the desktop shortcut location to your Burrito installation. This is simply done by right clicking on the shortcut, clicking on properties, desktop entry, and replacing "pi" with whatever your username is.  

To launch in the terminal
`python /home/pi/Burrito/burrito.py`

## Credits
Image by http://cliparts.co/clipart/2785349 and thanks to https://brobin.me/ for some nice Python articles/tutorials that helped with this project.

## Author
Aaron Welsh  
http://aaron-welsh.co.uk

## License
MIT
