import numpy as np
import cv2 as cv



def mean_linear_smoothong(min, max, len1):
    for i in range(min, len(image) - min):
        print(str(round(((i - min) * 100) / len(image) - min)) + "%")
        for j in range(min, len(image[i]) - min):
            sum = 0

            for k in range(-min, max):
                for l in range(-min, max):
                    sum = sum + image[i + k][j + l]

            imagecopy[i][j] = int(sum / len1)

    cv.imshow("clh", imagecopy)
    cv.waitKey()
    cv.destroyAllWindows()


def median_linear_smoothong(min, last):
    imagecopy = image.copy()
    arr = []
    for i in range(min, len(image) - min):
        print(str(round(((i - min) * 100) / len(image) - min)) + "%")
        for j in range(min, len(image[i]) - min):

            for k in range(-min, last):
                for l in range(-min, last):
                    arr.append(image[i + k][j + l])

            imagecopy[i][j] = int(np.median(arr))
            arr.clear()

    cv.imshow("clh", imagecopy)
    cv.waitKey()
    cv.destroyAllWindows()


def min_linear_smoothong(min, last):
    imagecopy = image.copy()
    arr = []
    for i in range(min, len(image) - min):
        print(str(round(((i - min) * 100) / len(image) - min)) + "%")
        for j in range(min, len(image[i]) - min):

            for k in range(-min, last):
                for l in range(-min, last):
                    arr.append(image[i + k][j + l])

            imagecopy[i][j] = int(np.min(arr))
            arr.clear()

    cv.imshow("clh", imagecopy)
    cv.waitKey()
    cv.destroyAllWindows()


def max_linear_smoothong(min, last):
    imagecopy = image.copy()
    arr = []
    for i in range(min, len(image) - min):
        print(str(round(((i - min) * 100) / len(image) - min)) + "%")
        for j in range(min, len(image[i]) - min):

            for k in range(-min, last):
                for l in range(-min, last):
                    arr.append(image[i + k][j + l])

            imagecopy[i][j] = int(np.max(arr))
            arr.clear()

    cv.imshow("clh", imagecopy)
    cv.waitKey()
    cv.destroyAllWindows()


def Adaptive_local_histogram_processing():
    img = cv.imread("The-original-image-of-Cameraman.png", 1)
    lab_im = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    l, a, b = cv.split(lab_im)
    equ = cv.equalizeHist(l)
    update_lab = cv.merge((equ, a, b))
    his_img = cv.cvtColor(update_lab, cv.COLOR_LAB2BGR)
    clahe = cv.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    clahe_img = clahe.apply(l)
    update_lab2 = cv.merge((clahe_img, a, b))
    clahe_img2 = cv.cvtColor(update_lab2, cv.COLOR_LAB2BGR)
    # cv.imshow("hist", clahe_img2)
    cv.imshow("clh", clahe_img2)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    print("کدوم برنامه اجرا شود ؟")
    print("1:smooth nonlinear filter smooth linear filter")
    print("2:Adaptive local histogram processing")
    select = int(input())
    if (select == 1):
        image = cv.imread("original.jpg", cv.IMREAD_GRAYSCALE)
        imagecopy = image.copy()
        print("چه نوع فیلتری  برای میانگین گیری که جز خطی می باشد اعمال می شود ؟")
        print("1:   3*3 ")
        print("2: 7*7 ")
        print("3:  11*11 ")
        select = int(input())
        if (select == 1):
            mean_linear_smoothong(1, 2, 9)
        elif (select == 2):
            mean_linear_smoothong(3, 4, 49)
        elif (select == 3):
            mean_linear_smoothong(5, 6, 121)
        else:
            print("opps,")

        print("چه نوع فیلتری  برای میانه گیری که جز غیر خطی است اعمال می شود ؟")
        print("1:   3*3 ")
        print("2: 7*7 ")
        print("3:  11*11 ")
        select = int(input())
        if (select == 1):
            median_linear_smoothong(1, 2)
        elif (select == 2):
            median_linear_smoothong(3, 4)
        elif (select == 3):
            median_linear_smoothong(5, 6)
        else:
            print("opps,")

        print("چه نوع فیلتری  برای حالت (مین )که جز غیر خطی است اعمال می شود ؟")
        print("1:   3*3 ")
        print("2: 7*7 ")
        print("3:  11*11 ")
        select = int(input())
        if (select == 1):
            min_linear_smoothong(1, 2)
        elif (select == 2):
            min_linear_smoothong(3, 4)
        elif (select == 3):
            min_linear_smoothong(5, 6)
        else:
            print("opps,")

        print("چه نوع فیلتری  برای حالت (ماکس) که جز غیر خطی است اعمال می شود ؟")
        print("1:   3*3 ")
        print("2: 7*7 ")
        print("3:  11*11 ")
        select = int(input())
        if (select == 1):
            max_linear_smoothong(1, 2)
        elif (select == 2):
            max_linear_smoothong(3, 4)
        elif (select == 3):
            max_linear_smoothong(5, 6)
        else:
            print("opps,")
    else:
        Adaptive_local_histogram_processing()
