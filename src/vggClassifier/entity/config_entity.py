from pathlib import Path
from dataclasses import dataclass # 

# dataclass is used to store data
# Type safety -> mention the datatypes
# frozen=True -> immutabilty throughout program's execution
@dataclass(frozen=True)
class DataIngestionConfig: # wraps the dict of config.yaml
    root_dir: Path
    source_url: str
    unzip_dir: Path
    local_data_file: Path