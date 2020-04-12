import os

fileName = "콩국수_"  # 숫자를 제외한 파일의 이름
annotationLocation = 'C:/data/annotations/'  # annotation 파일 경로(txt)
datasetLocation = 'C:/data/dataset/' # dataset 파일 경로(jpg)
changeName = "Kongguksu_"  # 바꿀 영어이름

for i in range(0, 1500):
    try:
        txtfile = annotationLocation + fileName + str(i) + '.txt'
        changetxtfile = annotationLocation + changeName + str(i) + '.txt'
        fr = open(txtfile, 'r')
        fr.close()
        os.rename(txtfile, changetxtfile)

    except Exception as e:
        print(e)

    try:
        jpgfile = datasetLocation + fileName + str(i) + '.jpg'
        changejpgfile = datasetLocation + changeName + str(i) + '.jpg'
        fjpg = open(jpgfile, 'r')
        fjpg.close()
        os.rename(jpgfile, changejpgfile)

    except Exception as e:
        print(e)


