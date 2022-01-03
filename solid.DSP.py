from enum import Enum
from abc import ABCMeta , abstractmethod

class teams(Enum):
    blue_team = 1
    Red_team = 2
    Green_team = 3

class TeamMembershipLookup():
    @abstractmethod
    def find_all_students_of_team(self,team):
        pass
class Student:
    def __init__(self,name):
        self.name = name
class TeamMemberships(TeamMembershipLookup):
    def __init__(self):
        self.team_memberships = []
    def add_team_memebrships(self,student,team):
        self.team_memberships.append((student,team))
    def find_all_students_of_team(self,team):
        for members in self.team_memberships:
            if members[1]==team:
                yield members[0].name
class Analysis():
    def __init__(self , team_membership_lookup):
        for student in team_membership_lookup.find_all_students_of_team(teams.Red_team):
            print(f'{student} is in RED TEAM')
student1=Student('Ravi')
student2=Student('Harry')
student3=Student('Zayn')

team_memberships = TeamMemberships()
team_memberships.add_team_memebrships(student1 , teams.blue_team)
team_memberships.add_team_memebrships(student2 , teams.Red_team)
team_memberships.add_team_memebrships(student3 , teams.Green_team)

Analysis(team_memberships)
