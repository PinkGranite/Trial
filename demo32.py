class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)
            
    def change_some_words(self):
        self.lyrics[0] = 'hhahahahah'
        del self.lyrics[1]
            
happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bull_on_parade = Song(["They rally aroung the family",
"With pockets full of shells"])

happy_bday.sing_me_a_song()
bull_on_parade.sing_me_a_song()
happy_bday.change_some_words()
happy_bday.sing_me_a_song()