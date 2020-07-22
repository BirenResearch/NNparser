import utils.tftools as tt
# tested models
    # 1. keras pretrianed models: 
        # 'DenseNet121',  'DenseNet169',  'DenseNet201',
        # 'InceptionResNetV2',  'InceptionV3',
        # 'MobileNet',  'MobileNetV2',
        # 'NASNetLarge', 'NASNetMobile',
        # 'ResNet101', 'ResNet101V2', 'ResNet152', 'ResNet152V2', 'ResNet50', 'ResNet50V2',
        # 'VGG16',  'VGG19',
        # 'Xception',
    # 2 Reomendeation: din
    # 3 EfficientNet: EfficientNetB0 ~ EfficientNetB7
    # 4 NLP: bert

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-n","--nnname", help="Neural Networkto be parsed",
                    default='ResNet50')
parser.add_argument("-b","--batchsize", help="Batch Sized",
                    default=1, type=int)
parser.add_argument("-e","--BPE", help="Byte per element",
                    default=1, type=int)
args = parser.parse_args()

(model,isconv) = tt.GetModel(vars(args)) 

# Producing Parameter table of given Model 
paralist = tt.ListGen(model,isconv,vars(args)) 
    
# exproting tables to //outputs//tf
nnname = args.nnname
tt.tableExport(paralist,nnname)