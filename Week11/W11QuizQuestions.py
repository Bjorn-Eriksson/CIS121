#Created by Bjorn Eriksson

#Question 1: INCOMPLETE
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    
    def get_name(self):
        return self.name
    def get_major(self):
        return self.major
    def set_name(self, new_name):
        self.name = new_name
    def set_major(self, new_major):
        self.major = new_major
    
    def __str__(self):
        return f"Name: {self.name}, Major: {self.major}"

class Course:
    def __init__(self, course_name, course_num):
        self.course_name = course_name
        self.course_num = course_num
        self.students = []
    
    def get_number(self):
        return self.course_num
    def set_number(self, new_num):
        self.course_num = new_num
    
    def add_students(self, student):
        self.students.append(student)
    
    def show_student_enrollment(self):
        for student in self.students:
            return student
    def __str__(self):
        return f"Course name: {self.course_name}, Course number: {self.course_num}, Students: {self.students}"

student1 = Student("Bjorn", "Computer Science")
student2 = Student("Matt", "Teaching")

course1 = Course("Introduction to Comp Sci", 121)
'''
print(course1.add_students(student1))
print(course1.add_students(student2))
print(course1.show_student_enrollment())
'''




#Question 11 - complete
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def get_artist(self):
        return self.artist
    def set_artit(self, new_artist):
        self.artist = new_artist
    
    def play(self):
        return f"Playing {self.title} by {self.artist}"
    
    def __str__(self):
        return f"{self.title} by {self.artist}"

class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.songs = []
    
    def add_song(self, title):
        self.songs.append(title)
    
    def play_all(self):
        message = ''
        for song in self.songs:     #Study play_all in depth, I needed aid for it.
            message += song.play()
            message += '||| '
        return message
    
    def __str__(self):
        return f"Playlist: {self.playlist_name}, Number of songs: {len(self.songs)}"

playlist1 = Playlist("Groovy Beats!")
song1 = Song("505", "Arctic Monkeys")
song2 = Song("Arrabella", "Arctic Monkeys")
'''
print(playlist1)
playlist1.add_song(song1)
playlist1.add_song(song2)
print(playlist1)

print(playlist1.play_all())
'''

#Question 12 - complete
class TVShow:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
    
    def get_genre(self):
        return self.genre
    def set_genre(self, new_genre):
        self.genre = new_genre

    def preview(self):
        return f"Title: {self.title}, Genre: {self.genre}"
    
    def __str__(self):
        return f"Show title: {self.title}, Show Genre: {self.genre}"

class NetflixDashboard:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.shows = []
    
    def add_show(self, show):
        self.shows.append(show)
    
    def display_recommendations(self):
        print(f"Recommendations for {self.profile_name}:")
        for show in self.shows:
            print(show)
    
    def __str__(self):
        return f"NetflixDashboard for {self.profile_name} with {len(self.shows)} Shows."
'''
profile1 = NetflixDashboard("Bjorn's Profile")
show1 = TVShow("The Expanse", "Sci fi")
show2 = TVShow("Vikings", "Historical Drama")
print(profile1)
print(show1)
print(show2)
print("-----------")
profile1.add_show(show1)
profile1.add_show(show2)
print(profile1.display_recommendations())
'''









































