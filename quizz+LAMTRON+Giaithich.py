dictnr = {
    "Quiz1": "A Learning in Tk? Name A Long ?",
    "Quiz2": "CC",
    "Choice": ["A.True", "B.False"],
    "Result": "False"
}
giai_thich_sai = [
    "sai vi long di som",
    "Sai vì Long tên Long chứ k phải tên là 'gì'.LOL!",
    "Sai vi Long đẹp trai mà ahihihihihihihi"
]
question_pack = [
    {
        "Question": "Co di muon k?",
        "Choice": ["A.Co", "B.Khong"],
        "result": "B"
    },
    {
        "Question": "Ten Long la gi?",
        "Choice": ["A.Co", "B.Khong"],
        "result": "A"
    },
    {
        "Question": "Long dep trai k?",
        "Choice": ["A.Co", "B.Khong"],
        "result": "A"
    }
]
c1 = False
correct = 0
c = question_pack
i = 0
while i < 3:
 choi = c[i]["Question"]
 print(choi, sep="\n")
 ur_choice = input("Your choice?").upper()
 if ur_choice == c[i]["result"]:
    print("Bingo")
    correct += 1
 else:
    print("Nah")
    print(giai_thich_sai[i])
    correct -=1
    if correct < 0:
         correct = 0
 i +=1
print("Ban tra loi dung:",round((correct/3) * 100,2),"%")