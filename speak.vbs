For Each msg In WScript.Arguments
    CreateObject("sapi.spvoice").speak msg
next
