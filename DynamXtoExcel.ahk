/*
!!!SCRIPT IS WIP!!!
autohotkey script to automate dynamx to excel conversion, current dynamx application does not
support the exporting of data to excel for bimodal analysis


Prerequisites before starting: 
	- must have DynamX open with file of interest opened
	- DynamX window must be maximized
	- user must be present

Goal:
	- user click on sequence then presses hotkey 
		- hotkey automates clicking on -->views-->stacked spectral plot-->copy spectrum -->open excel
		-->paste spectrum
		- could possibly implement a excel data format option for bimodal analysis
			-same script or create a different script
				ie. powershell 
	- gradually automate user clicking process




ctrl M: starts the script 

For window spy for AHKv2:
-  window size=screen size
*/



#HotIf WinExist("ahk_class LVDChild")
^m::
{
/*
WinActivate "ahk_class LVDChild"
WinMaximize
*/

WinGetPos ,, &w, &h, "A"

Mousex := 
MsgBox "window height=" w " , " h
MsgBox "Success"
}


;turn off script option 
~Escape::ExitApp
