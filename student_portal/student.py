# student_class
class Student:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s

    def get_infos(self):
        return (self.name,
                self.age,
                self.score)

    def original_name(self):
        return self.name

    def original_score(self):
        return self.score

    def original_age(self):
        return self.age

    def get_score(self, scores):
        self.score = scores
        return self.score

    def get_write(self, file):
        file.write(self.name)
        file.write(',')
        file.write(str(self.age))
        file.write(',')
        file.write(str(self.score))
        file.write('\n')
