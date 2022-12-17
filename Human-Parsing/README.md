# Human Parsing model
We propose a simple yet effective multiple human parsing framework based on [Detectron2](https://github.com/facebookresearch/detectron2).

### Requirements
Please see attached requirement list.

Download the pretrained model from [detectron2_maskrcnn_cihp_finetune.pth](https://drive.google.com/file/d/1T797HPC9V1mmw0cDoVOPSF1F_rrTcGPG/view?usp=sharing) and put them under `pretrain_model/`

### Run method
Save your picture under `data/crop_pic` and name it as `demo.jpg`
```
python human_parsing.py
```
