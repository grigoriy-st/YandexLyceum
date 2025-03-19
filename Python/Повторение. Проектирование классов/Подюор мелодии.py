N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция",
             "кварта", "квинта", "секста", "септима"]


class Note:
    notes = {
        'до': 'до-о',
        'ре': 'ре-э',
        'ми': 'ми-и',
        'фа': 'фа-а',
        'со': 'со-оль',
        'соль': 'со-оль',
        'ля': 'ля-а',
        'си': 'си-и',
    }

    def __init__(self, note, is_long=False):
        self.note = note
        self.is_long = is_long

    def play(self):
        print(self.note)

    def __str__(self) -> str:
        return self.notes[self.note] if self.is_long else self.note

    def __lt__(self, other):
        return PITCHES.index(self.note) < PITCHES.index(other.note)

    def __le__(self, other):
        return PITCHES.index(self.note) <= PITCHES.index(other.note)

    def __gt__(self, other):
        return PITCHES.index(self.note) > PITCHES.index(other.note)

    def __ge__(self, other):
        return PITCHES.index(self.note) >= PITCHES.index(other.note)

    def __eq__(self, other):
        return self.note == other.note

    def __rshift__(self, other):
        prev_index_pit = PITCHES.index(self.note) + other
        return Note(PITCHES[prev_index_pit % 7], self.is_long)

    def __lshift__(self, other):
        prev_index_pit = PITCHES.index(self.note) - other
        return Note(PITCHES[prev_index_pit % 7], self.is_long)

    def get_interval(self, other):
        dif_index = abs(PITCHES.index(self.note) - PITCHES.index(other.note))
        return INTERVALS[dif_index]


class Melody():
    def __init__(self, list_note=None):
        if list_note:
            self.list_note = [str(i) for i in list_note]
        else:
            self.list_note = []

    def __str__(self):
        string = ', '.join([str(i) for i in self.list_note])
        return string.capitalize()

    def append(self, new_note):
        self.list_note.append(new_note)

    def replace_last(self, new_note):
        self.list_note[-1] = new_note

    def remove_last(self):
        _ = self.list_note.pop()

    def clear(self):
        self.list_note = []

    def __len__(self):
        return len(self.list_note)

    def __rshift__(self, num):
        result = self.list_note[:]
        for note in range(len(self.list_note)):
            # проверка на длину ноты
            source = LONG_PITCHES if list(map(str, self.list_note))[note].__contains__('-') else PITCHES
            pit_index_note = source.index(self.list_note[note])
            if 0 <= pit_index_note + num < 7:
                # print(pit_index_note + num)
                result[note] = source[pit_index_note + num]
            else:
                return ', '.join(self.list_note[:]).capitalize()
        # self.list_note = result
        return Melody(result)

    def __lshift__(self, num):
        result = self.list_note[:]
        for note in range(len(self.list_note)):
            # проверка на длину ноты
            source = LONG_PITCHES if list(map(str, self.list_note))[note].__contains__('-') else PITCHES
            pit_index_note = source.index(self.list_note[note])
            if 0 <= pit_index_note - num < 7:
                result[note] = source[pit_index_note - num]
            else:
                return ', '.join(self.list_note[:]).capitalize()
        # self.list_note = result
        return Melody(result)



mel1 = Melody([Note('ре', True), Note('ми'), Note('до', True), Note('фа'), Note('ля'), Note('соль', True)])
m1 = mel1 >> 1
m2 = mel1 >> 3
print(m1)
print(m2)
print()

mel2 = Melody([Note('ре', True), Note('ми'), Note('до', True), Note('фа'), Note('ля'), Note('соль', True)])
m3 = mel2 << 2
m4 = mel2 << 2
print(m3)
print(m4)
print()

n1 = Note('фа', True)
n2 = Note('соль', True)
mel3 = Melody()
mel3.append(n1)
mel3.append(n2)
m5 = mel3 >> 1 >> 1
m6 = mel3 << 1 << 1
m7 = mel3 >> 3
m8 = mel3 << 3
print(m5)
print(m6)
print(m7)
print(m8)
print()

mel4 = Melody()
m9 = mel4 >> 3
m10 = mel4 << 3
print(m9)
print(m10)
print()

n3 = Note('ми', True)
n4 = Note('ми')
n5 = Note('фа')
mel5 = Melody([n5, n4, n3])
m11 = mel5 >> 2
m12 = mel5 << 2
m13 = mel5 >> 12
m14 = mel5 << 6
print(m11)
print(m12)
print(m13)
print(m14)


melody = Melody([Note('ре', True), Note('ми'), Note('до', True), Note('фа'), Note('ля'), Note('соль', True)])
print(melody)  # Ре, ми, до-о, фа, ля, со-оль
melody.replace_last(Note('си', True))
print(melody)  # Ре, ми, до-о, фа, ля, си-и
melody.remove_last()
print(melody)  # Ре, ми, до-о, фа, ля
melody.append(Note('соль', True))
melody.append(Note('соль', True))
print(melody)  # Ре, ми, до-о, фа, ля, со-оль, со-оль

melody = Melody([Note('ля'), Note('соль'), Note('ми'), Note('до', True)])
print(melody)
print(Melody() >> 2)
melody_up = melody >> 1
melody_down = melody << 1
melody.replace_last(Note('соль'))
print('>> 1:', melody_up)
print('<< 1:', melody_down)
print(melody)
