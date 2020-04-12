import os

fileName = "잔치국수__"  # 숫자를 제외한 파일의 이름
annotationLocation = "C:/data/annotations/"  # annotation 파일 경로
datasetLocation = "C:/data/dataset/"

for i in range(0, 1500):
    try:
        fr = open(annotationLocation + fileName + str(i) + '.txt', 'r')
        fr.close()

    except:
        jpgfile = datasetLocation + fileName + str(i) + '.jpg'
        if os.path.isfile(jpgfile):
            os.remove(jpgfile)
