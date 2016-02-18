<snippet>
  <content>
# Burrito
A Web Browser named Burrito that was built for the Raspbian OS on the Raspberry Pi.

## Installation
The simplest way to install this browser is as follows  
1. `sudo wget http://aaron-welsh.co.uk/Burrito.zip -P /home/$USER`  
2. `sudo unzip /home/$USER/Burrito.zip -d /home/$USER` (OR ANY OTHER UNZIP PROGRAM YOU HAVE INSTALLED - `sudo apt-get install unzip`)  
3. `sudo apt-get install python-webkit python-webkit-dev` (to install python programs that we need for the browser to work)
If you cannot find these packages to install, simply use `apt-cache search packagename`.  

To create a Desktop shortcut  
`sudo cp /home/$USER/Burrito/Burrito.desktop /home/$USER/Desktop  `
### Note:  
You will have to manually change the desktop shortcut location to your Burrito installation. This is simply done by right clicking on the shortcut, clicking on properties, desktop entry, and replacing "pi" with whatever your username is.  

To launch in the terminal
`python /home/pi/Burrito/burrito.py`

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b branch-name`
3. Add files to staging `git add .`
4. Commit your changes: `git commit -m 'Here are my changes'`
5. Push to the branch: `git push origin branch-name`
6. Submit a pull request and I will look at it ASAP.

## Disclaimer
Image by http://cliparts.co/clipart/2785349 and thanks to https://brobin.me/ for some nice Python articles/tutorials that helped with this project.

## Author
Aaron Welsh  
http://aaron-welsh.co.uk

## License
MIT
</content>
</snippet>
