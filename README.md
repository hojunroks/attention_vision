# Attention_Vision_Pytorch
I'm planning to use this repository to establish a baseline for applying attention and self-attention naturally to computer vision.


## Requirements

I highly recommend using Conda.
To install requirements:

```setup
conda create -n att_vis python=3.8
conda activate att_vis
pip install -r requirements.txt
```

## Training

To train the model, run this command:

```train
python train.py --input-data <path_to_data> --alpha 10 --beta 20
```


