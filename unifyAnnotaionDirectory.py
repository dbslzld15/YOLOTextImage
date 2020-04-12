import os

fileName = "떡볶이__"  # 숫자를 제외한 파일의 이름
fileLocation = "C:/data/annotations/떡볶이/"  # 라벨링 한 annotation 파일 경로
jpgLocation = "C:/data/dataset/떡볶이/" # 라벨링했던 jpg가 저장되어 있는 경로 설정
trainTextLocation = "C:/data/"  # train.txt가 있는 경로

for i in range(0, 1000):
    try:
        fr = open(fileLocation + fileName + str(i) + '.txt', 'r')
        # print(txt)
        fw = open(trainTextLocation+'train.txt', 'a')
        fw.write(jpgLocation+fileName+str(i) + '.jpg\n')

        fr.close()
        fw.close()

    except:
        print("없는 파일 입니다")