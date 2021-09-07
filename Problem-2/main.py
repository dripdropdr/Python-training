# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Student(object):
    def __init__(self, num, name, midterm, final, assignment):
        self.num = int(num)
        self.name = name
        self.midterm = int(midterm)
        self.final = int(final)
        self.assignment = int(assignment)
        self.totalscore = 0
        self.average = 0
        self.grade = ""

    def setAverage(self):

        self.totalscore = self.midterm+self.final+self.assignment
        self.average = float(format((self.totalscore)/3, ".2f"))

    def setGrade(self, idx, total):#바로 percentage 받거나 / 전체인원, 인덱스값(내 등수) 받기
        percentage = (idx+1)/total
        if percentage <=0.2:
            self.grade = 'A'
        elif 0.2<=percentage<=0.5:
            self.grade = 'B'
        elif 0.5<=percentage<=0.9:
            self.grade = 'C'
        else:
            self.grade = 'D'



def getStudentInfo():
    while True:
        try:
            filename = input("처리할 성적 파일 루트를 입력해주세요.")
            f = open_file(filename).split('\n')
            break

        except (FileNotFoundError, IOError, OSError):
            print("정확한 파일 경로를 입력해주세요. ex)C:\LabAssignment\\testfile.txt")
            pass

    studentList = []
    for idx, value in enumerate(f):
        num, name, midterm, final, assignment = value.split(' ')
        studentList.append(Student(num, name, midterm, final, assignment))
        studentList[idx].setAverage()


    return studentList


def orderStudent(studentList):
    # studentList.sort(key=studentList.average, reverse=True)
    studentList = sorted(studentList, key=lambda student: student.average, reverse=True)

    return studentList

def gradeStudent(studentList):
    for idx, val in enumerate(studentList):
        print(val.name,(idx+1)/len(studentList))
        val.setGrade(idx, len(studentList))


    return studentList


def output_result(studentList):
    studentList = sorted(studentList, key=lambda student: student.num)
    result = "학번 이름  중간 기말 과제 총점 평균  학점\n"
    for obj in studentList:
        obj_list=[obj.num, obj.name, obj.midterm, obj.final, obj.assignment, obj.totalscore, obj.average, obj.grade]
        obj_list = list(map(str, obj_list))

        result += "  ".join(obj_list) +"\n"

        # result += str(obj.num) + " " + obj.name + " " + str(obj.midterm) + " " + str(obj.final) + " " + str(obj.assignment) + " " + str(obj.totalscore) + " " + str(obj.average) + " " + obj.grade + "\n"

    print(result)

    while True:
        choice = input("결과를 파일로 저장하시겠습니까? [Y/N]").upper()
        if choice == 'Y':
            write_file(result)
            break
        elif choice == "N":
            print("결과를 저장하지 않습니다.")
            break
        else:
            print("올바른 값을 입력해주세요!")
            pass


def write_file(result):
    newFile = open("ResultScore.txt", 'w')
    newFile.write(result)
    newFile.close()
    print('결과가 파일로 출력되었습니다!')



def open_file(filename):
    lines = ""
    with open(filename, 'r', encoding='utf8') as fh:
        for line in fh:
            lines += line

        return lines


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    score_data = getStudentInfo()
    order_student = orderStudent(score_data)
    grade_student = gradeStudent(order_student)
    output_result(grade_student)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
