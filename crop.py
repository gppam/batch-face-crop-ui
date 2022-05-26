#!/usr/bin/python
import sys
import subprocess
import os
import PySimpleGUI as sg

def main():
	layout = [[sg.Text('Where are your photos found?')],
	         [sg.In(do_not_clear=True), sg.FolderBrowse()],
	         [sg.Text('Where do you want to save your cropped photos?')],
	         [sg.In(os.path.expanduser('~/Documents/cropped').replace("\\","/")), sg.FolderBrowse()],
	         [sg.Text('Set cropped dimensions (pixels)')],
	         [sg.Text('Width'), sg.Spin(values=[i for i in range(50, 1000)], initial_value=120, size=(6,1)),sg.Text('Height'), sg.Spin(values=[i for i in range(50, 1000)], initial_value=120, size=(6,1))],
	         [sg.Output(size=(60,15))],
	         [sg.Button('Start crop'), sg.Exit()]]

	window = sg.Window('Batch face crop', layout)

	while True:
		event, values = window.Read()
		if event in (None, 'Exit'):
			break

		loc = values[0].replace("\\","/")
		place = values[1]
		width = values[2]
		height = values[3]

		if event == 'Start crop':
			if not loc:
			    sg.Popup("Error", "No folder supplied.")

			elif not width:
				sg.Popup("Error", "Width is not entered.")

			elif not height:
				sg.Popup("Error", "Height is not entered.")

			else:
				if not type(width) == int or not type(height) == int:
					sg.Popup("Error", "Please enter a number.")

				width = str(width)
				height = str(height)
				stuff = ["autocrop", "-i", loc, "-o", place, "-w", width, "-H", height]
				runCommand(cmd=stuff, window=window)
				sg.Popup("Done", "Saved at ", place)

	window.Close()

def runCommand(cmd, timeout=None, window=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.Refresh() if window else None
    retval = p.wait(timeout)
    return (retval, output)


if __name__ == '__main__':
    main()