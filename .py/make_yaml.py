import yaml

data = {
    
    #train images(relative to 'path')
    'train' : './dataset/train/images',
    #val images(relative to 'path')
    'val' : './dataset/valid/images',
    #sfd
    'test' : './dataset/test/images',
    #sfdf
    'names' : 
    [
    'c_1',
    'c_2_01',
    'c_2_02',
    'c_3',
    'c_4_01_02',
    'c_4_02_01_02',
    'c_4_02_02_02',
    'c_4_02_03_02',
    'c_4_03',
    'c_5_02',
    'c_6',
    'c_7',
    ## 이 위에는 재활용
    ## 밑에는 일반쓰레기
    'c_1_01',
    'c_2_02_01',
    'c_3_01',
    'c_4_03_01',
    'c_5_01_01',
    'c_5_02_01',
    'c_6_01',
    'c_7_01',

    # 다중포장재
    'c_4_01_01',
    'c_4_02_01_01',
    'c_4_02_02_01',
    'c_4_02_03_01',
    'c_5_01',
    'c_8_01',
    'c_8_02',
    'c_8_01_01',
    'c_9'
    ],
    #rsfdf
    'nc' : 29
}
def save_yaml():
    #데이터 경로와 클래스 정보를 저장하고 있는 딕셔너리 객체 data를 YOLOv8 학습에 필요한 config.yaml에 저장
    with open('./config.yaml','w') as f:

        #yaml 파일 생성    
        yaml.dump(data,f)

    with open('./config.yaml','r') as f:
        config_yaml=yaml.safe_load(f)
    

