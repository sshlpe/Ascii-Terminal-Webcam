# Ascii-Terminal-Webcam
A terminal-base webcam made with Opencv and AsciiMatics base and tasted only with Python 3.7 on mac base terminal.

![](https://github.com/sshlpe/Ascii-Terminal-Webcam/blob/main/assets/rezise_example.gif)


## Install
clone the repository and install dependencies.

```
git clone https://github.com/sshlpe/Ascii-Terminal-Webcam.git
cd Ascii-Terminal-Webcam
pip3 install -r requirements.txt
```

## Use
To use just run on terminal for normal use
```
python3 webcam.py
```
or if you want inverted brightness. You can also press 'r' on any time to invert the brightness.
```
python3 webcam.py -r 
```

## Notes

- The webcam with adjust to the terminal size, even when resizing it after the program start.
- Pressing 'q' on any point quits the program.
- Pressing 'r' on any point inverts the grays scale.
- Pressing 'c' saves a capture of the webcam on the "captures" folder, these will be overwrite when you run the program again, so if you want to keep them move them to another folder.
- The Fps depends on the size of the terminal.
