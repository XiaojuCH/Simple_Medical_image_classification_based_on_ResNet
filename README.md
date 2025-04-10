# Simple_Medical_image_classification_based_on_ResNet
__基于resnet的简单医学图像分类__
## 参数配置
需要在 Pycharm -> 工具 -> 运行配置 -> train -> 脚本形参内输入   
```--data_name pathmnist --input_root ./medmnist --output_root ./output --download True```  

## 修改内容
```
1. 创建resnet.py解决  
   from medmnist.models import ResNet18, ResNet50中  
   Cannot find reference 'models' in '__init__.py'的报错问题

2. train.py中,将  
   with open(INFO, 'r') as f:  
   info = json.load(f)  
修改为  
   info = INFO  
  
3.train.py中,将
  warnings.DeprecationWarning("... some warning message ...")  
修改为
  warnings.warn("... some warning message ...", DeprecationWarning)  
    
4.evaluator.py中,将  
  df.append(df_insert, ignore_index=True)  
修改为  
  df = pd.concat([df, df_insert], ignore_index=True)  
    
5. evaluator.py中,将  
   df = df.append(df_insert, ignore_index=True)  
修改为  
   df = pd.concat([df, df_insert], ignore_index=True)  
```
