import cv2


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def loading_displaying_saving():
    img = cv2.imread('images/8829199908894.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('tire', img)
    cv2.waitKey(0)
    cv2.imwrite('images/8829199908894_gray.jpg', img)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    loading_displaying_saving()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
