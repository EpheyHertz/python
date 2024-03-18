#use of classes
class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Invalid name")
        if house not in("Nairobi","Perez","Embu"):
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    
    



def main():
    student=get_house()
    print(f"{student.name} from {student.house}")
    
    
def get_house():
    name=input("What is your name?")
    house=input("What is your house?")
    try:
           return Student(name,house)
    except Value:
     ...
     
     
    
    
    
    
    
if __name__=="__main__":
    main()