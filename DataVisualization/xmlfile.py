from collections import Counter
import re
import pandas as pd
from pathlib import Path

def find_url(path_para):
    xml_str = Path(path_para).read_text(encoding="UTF-8")
    result=re.findall(r'(https?://[^\s"]+)',xml_str)
    return result

if __name__ == "__main__":
    result=find_url(r'c:/Users/Kevin/Desktop/PythonProject/DataVisualization/Untitled-4.xml')
    temp=pd.Series(result).value_counts()
    pd.Series(result).value_counts().to_csv('resultOfPandas.csv')
