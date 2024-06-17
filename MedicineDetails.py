from paddleocr import PaddleOCR


def RecognizeMedicineInfo(image):
    
    # imagepath = r"D:\Graduation Project\RealVersionOfModel version Six (Last Update)\TestImages\All-Vent\huawei p30 418.jpg"
    # image = cv2.imread(image_path)

    pipline = PaddleOCR(rec_algorithm='CRNN',use_angle_cls=True)


    ocr = pipline
    result = ocr.ocr(image, cls=True)
    words = [row[1][0] for row in result[0]]
    return words


# def RecognizeMedicineInfo():
#     return "fuuuuck"

# if __name__ == "__main__":
#     image_path = sys.argv[1]
#     x =RecognizeMedicineInfo(image_path)
#     print(x)
    









# import sys
# from paddleocr import PaddleOCR

# def perform_ocr(image_path):
#     ocr = PaddleOCR(use_angle_cls=True, lang='en')
#     result = ocr.ocr(image_path, cls=True)
#     return result

# if __name__ == "__main__":
#     image_path = sys.argv[1]
#     result = perform_ocr(image_path)
#     for line in result:
#         print(line)
