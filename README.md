# Mike Tyson's Punch-Out!! (1987) Automatic In-Game Timer

https://github.com/Igyeom/MTPO-Timer/assets/61957594/192f2fe2-c0ef-44c2-9045-f044726fe790
https://youtu.be/WIxp5R69MB4


## Quickstart

### Prerequisites
- OBS Studio
- Python 3.x (Required on non-Windows machines)
- A Capture Card (Required on NES Console, unless on emulator)
- Knowledge that the software is in a very skeleton form.

### Installation
- Go to the [Releases](https://github.com/Igyeom/MTPO-Timer/releases) tab
- Download the **.zip** file (it should be something like **v0.1.0-indev.zip**)
- Extract the ZIP file.
- Run the Batch file named **RUN_ME.bat**
- Open OBS Studio (if on NES console) and right-click the capture card output, then press "Windowed Projector (Source)"
- Press "Start Capture" on the newly opened window (not the projector, the timer program), then "Get Latest Screenshot", then immediately "Pause Capture" as you see the screen capture.
- Input the RGB colour of the blue background shown in the winning screen via the textbox below.
- Win a fight, adjust the green box as shown using the textbox below the screenshot and the "Preview" button.
![image](https://github.com/Igyeom/MTPO-Timer/assets/61957594/63b262ee-b7dc-44c2-a209-748b2b6770ed)
- Press "Confirm" to start capturing AND start fetching the text on the win screen.
- If it shows the correct time, you're good to go!


## Potential Enhancements
- Better UI Design and Timer (Saving PB's and Comparisons)
- More Intuitive Capture System (it only captures your primary monitor that you set in Settings for now)
- Hasn't been tested in a full run yet
- Tyson fight COULD be automated using the top-right timer, but for right now it's manual
- Fixing Don Flamenco's image being so **loooooong**
