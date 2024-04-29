/*
!!!SCRIPT IS WIP!!!
autohotkey script to automate dynamx to excel conversion, current dynamx application does not
support the exporting of data to excel for bimodal analysis


Prerequisites before starting: 
	- must have DynamX open with file of interest opened


ctrl M: starts the script 


*/



#HotIf WinExist("ahk_class LVDChild")
^m::
{
WinActivate "ahk_class LVDChild"
WinMaximize
MsgBox "Success"
}


;turn off script option 
~Escape::ExitApp
