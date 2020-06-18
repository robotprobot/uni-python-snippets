class Person:
    def __init___(self):
        self.First_name = str()
        self.Second_name = str()
        self.Day = int()
        self.Month = int()
        self.Year = int()
        self.Height = int()

    def set_name(self, forename, surname):
        self._first_name = forename
        self._last_name = surname

    def get_name(self):
        return self._first_name + " " + self._last_name

    def set_dob(self, d, m, y):
        if self._is_valid_date(d, m):
            self._day = int(d)
            self._month = int(m)
            self._year = int(y)
        else:
            return "Invalid date entered."

    def get_dob(self):
        return "{0}-{1}-{2}".format(self._day, self._month, self._year)

    def set_height(self, h):
        self._height = int(h)

    def get_height(self):
        return "{0}".format(self._height)

    def get_age_at(self, d, m, y):
        age = -1
        if self._is_valid_date(d, m) and self._is_after_dob(d, m, y):
            age = y - self._year
            if (m < self._month) or (m == self._month and d < self._year):
                age -= 1
        return age

    def get_details(self):
        return "{0}, {1}".format(self.get_name(), self._get_dob())

    def _is_valid_date(self, d, m):
        return 0 < d <= 31 and 0 < m <= 12

    def _is_after_dob(self, d, m, y):
        return (y > self._year) or \
               (y == self._year and m > self._month) or \
               (y == self._year and m == self._month and d > self._day)

def print_person(selectedperson):
    print(selectedperson.get_name())
    print(selectedperson.get_dob())
    print("Age on 7th November 2012: " + str(selectedperson.get_age_at(7, 11, 2012)))
    print("Height in inches: " + str(selectedperson.get_height()))
    print()

mum = Person()
dad = Person()
son = Person()
daughter = Person()

mum.set_name("Juliet", "Capulet")
dad.set_name("Romeo", "Montague")
son.set_name("Triolus", "Montague")
daughter.set_name("Cressida", "Montague")

mum.set_dob(7, 11, 1987)
dad.set_dob(21, 2, 1983)
son.set_dob(12, 4, 2009)
daughter.set_dob(13, 10, 2007)

mum.set_height(68)
dad.set_height(73)
son.set_height(33)
daughter.set_height(40)

print_person(mum)
print_person(dad)
print_person(son)
print_person(daughter)