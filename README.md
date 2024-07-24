# MLOPS_Deep_Learning
A basic classification project to underscore the importance of production grade deployment lifecycle

- [Data link](https://drive.google.com/drive/folders/1lkG7hhcX_Hb07M6tIrz0nJ6cLu9PpTGi?usp=drive_link)

# Workflows
1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py which is the driver file
8. Update the dvc.yaml


# How to run?
```bash
conda create -n chest python=3.10 -y
```

```bash
conda activate chest
```

```bash
pip install -r requirements.txt
```

```bash
python3 app.py
```