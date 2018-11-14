import applescript
from applescript.aecodecs import AEType
from pprint import pprint
script1 = '''tell application "iTunes"
  get name of tracks of playlist "ARR"
end tell
'''
script = '''tell app "iTunes" 
get every track of playlist "library" whose artist contains "Fiona Apple"
end tell
'''
scr = '''tell app "iTunes" 
set trk to track id 9716
get name of trk
end tell'''
s = '''tell app "iTunes"
play tracks of playlist "TUP"
end tell'''
out = applescript.AppleScript(script).run()
#pprint.pprint(applescript.AppleScript(script).run())
x = AEType(b'seld')
print(out[0][x])
for key in out[0]:
    print(key is x)