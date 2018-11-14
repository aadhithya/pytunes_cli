import argparse
from iTunesHandler import iTunes


def parse_args(itunes):
    parser = argparse.ArgumentParser()
    parser.add_argument('--play', '-p', help='Play main command.', action="store_true")
    parser.add_argument('-artist', '-ar', help='Plays the songs by the artist from library. Sub-command.', nargs='+')
    parser.add_argument('--song', '-sng', help='Plays the song. Sub-command.', nargs='+')
    parser.add_argument('--album', '-al', help='Plays the album from library. sub-command.', nargs = '+')
    parser.add_argument('--playlist', '-pl', help='Plays the playlist from library. Sub-command.', nargs = '+')
    parser.add_argument('--pause', '-ps', help='Pause',action="store_true")
    parser.add_argument('--stop', '-st', help='Stop',action="store_true")
    parser.add_argument('--resume', '-r', help='Resume',action="store_true")
    parser.add_argument('--play-pause', '-pp', help='Alternate between play and pause.',action="store_true")
    parser.add_argument('--search', '-s', help='Search. To be used with the one of the sub-commands.', action="store_true")

    args = parser.parse_args()

    if args.play:
        print('--play')
        if args.song:
            itunes.play(song=' '.join(args.song))
        elif args.artist:
            itunes.play(artist=' '.join(args.artist))
        elif args.album:
            itunes.play(album=' '.join(args.album))
        elif args.playlist:
            print(args.playlist)
            itunes.play(playlist=' '.join(args.playlist))
        else:
            itunes.play()
    elif args.pause:
        itunes.pause()
    elif args.stop:
        itunes.stop()
    elif args.play_pause:
        itunes.playpause()
    elif args.resume:
        itunes.resume()
    elif args.search:
        print('--search')
        if args.song:
            print(args.song)
        elif args.artist:
            print(args.artist)
        elif args.album:
            print(args.album)
        elif args.playlist:
            print(args.playlist)
        else:
            print('Error: Search needs a subcommand. sub-commands: --song, --artist, --playlist')
    else:
        itunes.play(song='bulti')



if __name__ == '__main__':
    itunes = iTunes()
    parse_args(itunes)