#name : Pierre Andre El Boustany
#McGill ID : 26107411

import musicalbeeps
from note import Note

class Melody:
    
    def __init__(self, filename):
        '''
        >>> happy_birthday = Melody("birthday.txt")
        >>> len(happy_birthday.notes)
        25
        
        >>> print(happy_birthday.notes[5])
        1.0 F 4 sharp
        
        >>> fur_elise = Melody("fur_elise.txt")
        >>> len(fur_elise.notes)
        165
        
        >>> print(happy_birthday.notes[10])
        0.5 A 4 natural
        '''
        f = open(filename)
        
        i = 0
        rep_loc = 0
        n_list = []
        rep = []
        n = []
        
        for line in f:
            if i == 0:
                self.title = line[:-1]
                
            elif i == 1:
                self.author = line[:-1]
                
            else:
                n = line.split()  
                if n[1] != 'R':
                    n[0] = str(float(n[0]))
                    n[3] = n[3].lower()
               
                    
                    
                if n[-1] == 'true':
                    rep_loc += 1 
                n.pop(-1)
                if n[1] != 'R':
                    n_list.append(Note(float(n[0]), n[1], int(n[2]), n[3].lower()))
                else:
                    n_list.append(Note(float(n[0]), n[1]))
                    
                if rep_loc == 1 or rep_loc == 2:
                    if n[1] != 'R':
                        rep.append(Note(float(n[0]), n[1], int(n[2]), n[3].lower()))
                    else:
                        rep.append(Note(float(n[0]), n[1]))
                    
                
                    if rep_loc == 2 :
                        for elt in rep :
                            n_list.append(elt)
                        rep_loc = 0
                        rep = []
                    
            
            n = []
            i += 1
        self.notes = n_list
        
        
    def play(self, player):
        for line in self.notes:
            line.play(player)

    def get_total_duration(self):
        '''
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0
        
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> hot_cross_buns.get_total_duration()
        8.0
        '''
        total_dur = 0
        for line in self.notes:
            total_dur += line.duration
        return total_dur
         
     
    def lower_octave(self):
        '''
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        
        >>> happy_birthday.notes[3].octave
        3
        '''
        i = 0
        for line in self.notes:
            if line.pitch != 'R':
                
                if line.octave > Note.OCTAVE_MIN:
                    i += 1
            else:
                i += 1
        for line in self.notes:
            if i == len(self.notes):
                line.octave -=1
            else:
                return False
        return True
        
            
    def upper_octave(self):
        '''
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.upper_octave()
        True
        
        >>> happy_birthday.notes[3].octave
        5
        '''
        i = 0
        for line in self.notes:
            if line.pitch != 'R':
                
                if line.octave < Note.OCTAVE_MAX:
                    i += 1
            else:
                i += 1
        for line in self.notes:
            if i == len(self.notes):
                line.octave +=1
            else:
                return False
        return True
        
    def change_tempo(self, temp):
        '''
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_tempo(2.0)
        >>> happy_birthday.get_total_duration()
        26
        '''
        for line in self.notes:
            line.duration = line.duration * temp
            

