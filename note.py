#name : Pierre Andre El Boustany
#McGill ID : 26107411


import musicalbeeps


class Note:
    
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    
    def __init__(self, duration, pitch, octave = 1, accidental = 'natural'):
        '''
        >>> note = Note(2.0, "B", 4, "natural")
        >>> note.pitch
        'B'

        >>> note = Note(1.0, "C", 5, "sharp")
        >>> note.duration
        1.0
        
        >>> note = Note(0.25, "F", 3, "flat")
        >>> note.daccidental)
        "flat"
        '''
        pitch_values = ["A", "B", "C", "D", "E", "F", "G", "R"]
        octave_values = [1, 2, 3, 4, 5, 6, 7]
        accidental_values = ["natural", "flat", "sharp"]

        if pitch not in pitch_values or octave not in octave_values or accidental not in accidental_values or type(duration) != float:
            raise AssertionError ("One of your inputs is invalid")
        
        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental
        
    def __str__(self):
        '''
        >>> note = Note(2.0, "B", 4, "natural")
        >>> print(note)
        2.0 B 4 natural
        
        >>> note = Note(1.0, "C", 5, "sharp")
        >>> print(note)
        1.0 C 5 sharp
        '''
        return str(self.duration) + ' ' + self.pitch + ' ' + str(self.octave) + ' ' + self.accidental
        
    def play(self, player):

        if self.accidental == "natural":
            accidental = ""
        elif self.accidental == 'sharp':
            accidental = '#'
        elif self.accidental == 'flat':
            accidental = 'b'
        
        note_str = self.pitch + str(self.octave) + accidental
        if self.pitch == 'R':
            note_str = 'pause'
        player.play_note(note_str, self.duration)
        
        

        
        
        
        

    
