import os
import urllib3
from cfrgan.train import CFRTrain

if __name__=='__main__':
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
  os.environ["AWS_ACCESS_KEY_ID"] = ""
  os.environ["AWS_SECRET_ACCESS_KEY"] = ""
  os.environ["MLFLOW_S3_ENDPOINT_URL"] = ""
  os.environ["MLFLOW_S3_IGNORE_TLS"] = ""
  train = CFRTrain()
  train.main()

