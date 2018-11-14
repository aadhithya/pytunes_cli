# AppleScript commands for iTunes

1. Play a song [song]
`tell application "iTunes"
play "[song]"
end tell`
2. Stop
`Tell application "iTunes" to stop`
3. Pause
`Tell application "iTunes" to pause`
4. Play
`Tell application "iTunes" to play`
5. PlayPause
`Tell application "iTunes" to playpause`
6. Next Track
`Tell application "iTunes" to play next track`
7. Previous Track
`Tell application "iTunes" to play previous track`
8. Play Playlist
`tell app "iTunes" to play playlist "[playlist]"`
9. Play playlist[x]
`tell app "iTunes" to play track [x] of playlist "[playlist]"`
10. Track names of playlist
`tell app "iTunes" to get name of tracks of playlist "[playlist]"