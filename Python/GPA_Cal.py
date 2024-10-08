import statistics
def DP():
    while True:
        x= input('What is your department? ').title().strip()
        if x.strip():
            return x
        else:
            print('Please enter your department')
DPT= DP()
def get_name():
    while True:
        y= input('What is your name- ').title().strip()
        if y.strip():
                return y
        else:
            print('Please enter your department')
name=get_name()

def no():
    while True:
        try:
            k= int(input(f'Hello {name} from Department of {DPT}\nhow many courses do you offer: '))
            if k==0:
                pass
            else:
                return k
        except ValueError:
            print('Enter number of scores as numeric value')   
k=no()
courses=[]
scores=[]

def get_course():
    for i in range(k):
            while True:
                name= input(f'Enter course no.{i+1}: ').upper().strip()
                if name.strip():
                    courses.append(name)
                    break
                else:
                    print('Please enter course code,',end="")

def get_score():
    for i in range(k):
        while True:
            try:
                scr=int(input(f'Enter score for {courses[i]}: '))
                if 0<=scr<=100:
                    scores.append(scr)
                if 0 <= scr <= 39:
                    scr= 'F'
                    Egrades.append(scr)
                    points.append(Grades[scr])
                    break
                elif 40 <=scr<= 44:
                    scr= 'E'
                    Egrades.append(scr)
                    points.append(Grades[scr])
                    break
                elif 45 <= scr <= 49:
                    scr= 'D'
                    Egrades.append(scr)
                    points.append(Grades[scr])
                    break
                elif 50<= scr<=  59:
                    scr= 'C'
                    Egrades.append(scr)
                    points.append(Grades[scr])
                    break
                elif 60<=scr<=69:
                    scr= 'B'
                    Egrades.append(scr)
                    points.append(Grades[scr])
                    break
                elif 70<=scr<=100:
                    scr='A'
                    Egrades.append(scr)
                    points.append(Grades[scr])
                    break
                else:
                    print('Invalid Score ',end="")
            except KeyError:
                print('Enter a real score-', end="")
            except ValueError:
                print('Check score and try again- ', end="")

def get_choice():
    while True:
        user_choice= input('Would you like to enter scores? Yes or No- ').capitalize()
        if user_choice== 'Yes' or user_choice=='No':
            if user_choice=='Yes':
                return True
            else:
                return False
        else:
            pass

Grades={'A':5,'B':4,'C':3,'D':2,'E':1,'F':0}
Egrades=[]
points=[]
credit_hour= []
def get_grade():
        for i in range(k):
            while True:
                try:
                    studgrade=input(f'Enter Grade for {courses[i]}: ').upper().strip()
                    if studgrade in Grades:
                        Egrades.append(studgrade)
                        points.append(Grades[studgrade])
                        break
                    else:
                        print('Check Grade and Retry ', end="")
                except ValueError:
                    pass

def run(): 
    get_course()         
    if get_choice():
        get_score()
    else:
        get_grade()

def check(v):
    if 25<=sum(v)<=30:
        print('Carry over detected ', end="")
        qst=input('Type Yes to continue or No to retry- ').capitalize().strip()
        if qst=='Yes' or qst=='No':
            if qst=='Yes':
                return True
            elif qst=='No':
                credit_hour.clear()
                return False
    elif sum(v)>30:
        print('Max Credit load exceeded ')
        credit_hour.pop()
        return False
    else:
        return True
    
def get_ch():
    for i in range(k):
        while True:
            try:
                chour= int(input(f'Enter Credit hour for {courses[i]}: '))
                credit_hour.append(chour)
                if check(credit_hour):
                    break
                else:
                    pass
            except ValueError:
                print('Check credit hour and retry')

def summary():
            print(f'\nDepartment of {DPT}\n{name}') 
            print('Courses\tScore\tGrade\tCredit hour ')
            for i in range(k):
                if scores:
                    print(f'{courses[i]}\t{scores[i]}\t{Egrades[i]}\t{credit_hour[i]}')
                else:
                    print(f'{courses[i]}\tN/A\t{Egrades[i]}\t{credit_hour[i]}')

def final_checks():
    while True:
        qst= input('Is this correct? type "OK" to proceed \n "Retry" to start over- ').upper()
        if qst== "OK":
            return True
        elif qst=="RETRY":
            return False
        else:
            pass

def GPA_Cal():
    GPA= statistics.fmean(points, credit_hour)
    finalGPA=round(GPA,2)
    print(f'Your GPA for this semester is {finalGPA}')
def reset():
    courses.clear()
    Egrades.clear()
    credit_hour.clear()
    points.clear()
   

def output():
    if final_checks():
        summary()
        GPA_Cal()
    else:
        reset()
        run()
        get_ch()
        summary()
        output()
        
def main():
    run()
    get_ch()
    summary()
    output()
if __name__ == "__main__":
	main()
