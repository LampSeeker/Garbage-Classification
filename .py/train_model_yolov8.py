from ultralytics import YOLO
import make_yaml
import torch

print(torch.cuda.is_available())

def train_model():

    make_yaml.save_yaml()
    model = YOLO('yolov8n.pt')
    #print(type(model.names),len(model.names))
    #print(model.names)
    #https://github.com/ultralytics/ultralytics/issues/2039
    #model �μ� ���� : https://docs.ultralytics.com/modes/train/#resuming-interrupted-trainings
    result=model.train(data='./config.yaml',epochs=10,device='0')
   # model.to('cuda')

    result=model.val()

    success = model.export(format='onnx')

