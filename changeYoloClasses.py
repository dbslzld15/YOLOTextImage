fileName = "떡볶이_"  # 숫자를 제외한 파일의 이름
fileLocation = "C:/data/"  # annotation (텍스트) 파일 경로
originNum = 10  # 원래 텍스트 파일의 class 숫자
classNum = 1  # 바꿀 class 숫자

for i in range(0, 1200):
    try:
        num = 0
        fr = open(fileLocation + fileName + str(i) + '.txt', 'r')
        lines = fr.readlines()
        fr.close()
        for line in lines:
            line = line.replace(str(originNum), str(classNum), 1)
            if num == 0:
                fw = open(fileLocation + fileName + str(i) + '.txt', 'w+')
                fw.write(line)
                fw.close()
            else:
                fa = open(fileLocation + fileName + str(i) + '.txt', 'a')
                fa.write(line)
                fa.close()
            num += 1

        # print(txt)

    except:
        print("없는 파일 입니다")
