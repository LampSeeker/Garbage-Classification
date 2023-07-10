import os
import json
from PIL import Image
# annotation 정보들을 YOLO의 darknet 프레임워크가 사용하는 label format으로 변경
'''
#추출해야할 딕셔너리 내 item 
    "class_name" 
    "annotation" : 
    {
        "coord":
            {
            "x": 851.1382318154939,
			"y": 0,
			"width": 174.76049674748663,
			"height": 137.71710526315792
            }
    }

'''
label_kr = {
    'c_1' :0, #'종이',
    'c_2_01': 1, #'종이팩',
    'c_2_02': 2, #'종이컵',
    'c_3': 3, #'캔류',
    'c_4_01_02': 4, #'재사용 유리(소주병 + 맥주병)',
    'c_4_02_01_02': 5, #'갈색 유리',
    'c_4_02_02_02': 6, #'녹색 유리',
    'c_4_02_03_02': 7, #'백색 유리',
    'c_4_03': 8, #'기타 유리',
    'c_5_02': 9, #'페트',
    'c_6': 10, #'플라스틱',
    'c_7': 11, #'비닐',
    ## 이 위에는 재활용
    ## 밑에는 일반쓰레기
    'c_1_01': 12, #'종이 + 이물질',
    'c_2_02_01': 13, #'종이컵 + 이물질',
    'c_3_01': 14, #'캔 + 이물질',
    'c_4_03_01': 15, #'기타 유리 + 이물질',
    'c_5_01_01': 16, #'페트 + 이물질 + 다중포장재',
    'c_5_02_01' : 17, #'페트+이물질',
    'c_6_01': 18, #'플라스틱 + 이물질',
    'c_7_01': 19, #'비닐 + 이물질',

    # 다중포장재
    'c_4_01_01': 20, #'재사용 유리(소주병+맥주병) + 다중 포장재',
    'c_4_02_01_01': 21, #'갈색 유리 + 다중포장재',
    'c_4_02_02_01': 22, #'녹색 유리 + 다중포장재',
    'c_4_02_03_01': 23, #'백색 유리 + 다중포장재',
    'c_5_01': 24, #'페트 + 다중포장재',
    'c_8_01': 25, #'흰색 스티로폼',
    'c_8_02': 26, #'컬러 스티로폼',
    'c_8_01_01': 27, #'스티로폼 + 이물질',
    'c_9': 28, #'건전지'
}


# 폴더 경로를 지정하기
json_folder_path = r'K:\데이터\307.생활폐기물 데이터 활용ㆍ환류\01.데이터\Training\02.라벨링데이터\TL_1.재활용선별장_A2_1'
img_folder_path = r'K:\데이터\307.생활폐기물 데이터 활용ㆍ환류\01.데이터\Training\01.원천데이터\TS_1.재활용선별장_A2 (2)'

def extract_annotation_yolov8(json_folder_path,img_folder_path):    
    
    # 폴더 내의 모든 파일을 가져옵니다.
    file_list = os.listdir(json_folder_path)
    # JSON 파일만 선택합니다.
    json_files = [file for file in file_list if file.endswith('.json')]
    image_size = [1847, 883] #match image의 size
    # 각 JSON 파일 열기
    for json_file in json_files:

        json_path = os.path.join(json_folder_path, json_file)
        #json 파일과 img 이름이 같으므로
        file_name = os.path.splitext(os.path.basename(json_file))[0]
        jpg_file = os.path.join(img_folder_path, file_name + ".jpg")
        
        if os.path.isfile(jpg_file):  # 해당 경로에 JPG 파일이 존재하는 경우    
            image = Image.open(jpg_file)                     
            image_size = list(image.size)
        else:
            continue
            
        with open(json_path, 'r',encoding="UTF-8") as file:
            data = json.load(file)

        # 딕셔너리 추출 및 "objects" 키의 값을 추출
        extracted_objects = []  # 추출한 "objects" 값들을 저장할 리스트

        # JSON 파일에서 "objects" 키의 값이 리스트인 경우 추출
        if "objects" in data and isinstance(data["objects"], list):
            for dictionary in data["objects"]:
                #리스트 내 딕셔너리 형식에서 해당 키값이 있을 경우에 추출                
                if "class_name" in dictionary and "annotation" in dictionary:                    
                    class_name = label_kr[dictionary["class_name"]]
                    
                    #class_name = dictionary["class_name"]                                  
                    box= dictionary["annotation"]["coord"]                    
                    #기존 box format을 yolo 포맷으로 변환
                    left, top, width, height = box['x'],box['y'],box['width'],box['height']

                    x_center = (left + width / 2) / image_size[0]
                    y_center = (top + height / 2) / image_size[1]
                    #정규화
                    box_width = width / image_size[0]
                    box_height = height / image_size[1]
                   
                    extracted_objects.append((class_name,x_center,y_center,box_width,box_height))   
                    
        # 추출한 값을 텍스트 파일로 저장
        text_file_name = os.path.splitext(json_file)[0] + '.txt'
        text_file_path = os.path.join(json_folder_path, text_file_name)
        with open(text_file_path, 'w',encoding='UTF-8') as file:
            for obj in extracted_objects:
                
                #한글 유니코드로 저장되는 현상 방지
                file.write(json.dumps(obj,ensure_ascii=False).replace('"','').replace(',','')[1:-1] + '\n')


extract_annotation_yolov8(json_folder_path,img_folder_path)



