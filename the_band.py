class Person:
    def __init___(self):
        self.First_name = str()
        self.Second_name = str()
        self.Day = int()
        self.Month = int()
        self.Year = int()

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


john = Person()
paul = Person()
george = Person()
ringo = Person()

john.set_name("John", "Lennon")
paul.set_name("Paul", "McCartney")
george.set_name("George", "Harrison")
ringo.set_name("Ringo", "Starr")

john.set_dob(8, 10, 1940)
paul.set_dob(18, 6, 1942)
george.set_dob(25, 2, 1943)
ringo.set_dob(7, 7, 1940)

print(f"""{john.get_name()}
{john.get_dob()}

{paul.get_name()}
{paul.get_dob()}

{george.get_name()}
{george.get_dob()}

{ringo.get_name()}
{ringo.get_dob()}
""")