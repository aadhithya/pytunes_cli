import applescript

""" 
def __run_script(source):
    if source is not None:
        try:
            res = applescript.AppleScript(source).run()
            return res
        except Exception as ex:
            print(ex)
            return None
    else:
        return None """



class iTunes:


    def __init__(self):
        print('Hello from itunes!')
    
    def play(self,song=None, playlist=None, artist=None, album=None):
        if song is not None:
            print('Playing Song {0}'.format(song))
            source = '''tell app "iTunes"
            play track "{0}"
            end tell'''.format(song)
            res = self.__run_script(source)
            return self.__handle_res(res)
        elif playlist is not None:
            print('Playing Playlist {0}'.format(playlist))
            source = '''tell app "iTunes"
            play tracks of playlist "{0}"
            end tell'''.format(playlist)
            res = self.__run_script(source)
            return self.__handle_res(res)
        elif artist is not None:
            print('Playing Artist {0}'.format(artist))
            source = '''tell app "iTunes"
            play tracks of artist "{0}"
            end tell'''.format(artist)
            res = self.__run_script(source)
            return self.__handle_res(res)
        elif album is not None:
            print('Playing Album {0}'.format(album))
            source = '''tell app "iTunes"
            play album "{0}"
            end tell'''.format(album)
            res = self.__run_script(source)
            return self.__handle_res(res)
        else:
            pass
        return
    
    def pause(self):
        source = 'tell app "iTunes" to pause'
        res = __run_script(source)
        return __handle_res(res)
    
    def stop(self):
        source = 'tell app "iTunes" to stop'
        res = self.__run_script(source)
        return self.__handle_res(res)
    
    def resume(self):
        source = 'tell app "iTunes" to resume'
        res = self.__run_script(source)
        return self.__handle_res(res)
    
    def playpause(self):
        source = 'tell app "iTunes" to playpause'
        res = self.__run_script(source)
        return self.__handle_res(res)

    def __run_script(self, source):
        if source is not None:
            try:
                res = applescript.AppleScript(source).run()
                return res
            except Exception as ex:
                print('iTunesHandlerError: {0}'.format(ex))
                return None
        else:
            return None

    def __handle_res(self,res):
        if res is not None:
            return True
        else:
            return False
            
    
