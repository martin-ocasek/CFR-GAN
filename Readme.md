
### Build .whl 
```shell
python setup.py bdist_wheel
```

### Train
##### Download models for training
```shell
cd /train_directory
wget -O saved_models/trained_weights_occ_3d.pth https://www.dropbox.com/s/c10xm4po7moxnnj/trained_weights_occ_3d.pth?dl=1
wget -O saved_models/face_res_50.pth https://www.dropbox.com/s/223ia6c9mtzgqgb/face_res_50.pth?dl=1

wget -O faceParsing/model_final_diss.pth https://www.dropbox.com/s/kjf01og7t15e30u/model_final_diss.pth?dl=1

wget -O mmRegressor/BFM/BFM_model_80.mat https://www.dropbox.com/s/xpvusyfjp0cau4b/BFM_model_80.mat?dl=1
wget -O mmRegressor/BFM/similarity_Lm3D_all.mat https://www.dropbox.com/s/j55cspuvqnvc0eq/similarity_Lm3D_all.mat?dl=1
```

##### Prepare test data
Normalized pictures for input dataset should be stored in `train_directory/test_imgs/input`

##### Generate pairs
 **`prepare.py`**
```python
from cfrgan import generate_pairs

if __name__=='main':
    generate_pairs.main()
```

```shell
python prepare.py 
```

##### Prepare valid and train lists
Prepare `train_files.txt` and `valid_files.txt` 

##### Run training
 **`train.py`**
```python
from cfrgan import train

if __name__=='__main__':
  train.main()
```

```shell
python train.py --img_path test_imgs/input --train_data_path test_imgs/output --valid_data_path test_imgs/output --train_data_list train_files.txt --valid_data_list valid_files.txt
```


