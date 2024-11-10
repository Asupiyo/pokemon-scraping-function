import subprocess
import boto3
import os

pwd = os.getcwd()
print(pwd)
zfile = rf"{pwd}\lambda_function.zip"
pfile = rf"{pwd}\pokemon_data_aws\lambda_function.py"
lfile = rf"{pwd}\venv\Lib\site-packages\*"


def create_zip():
    subprocess.run(['powershell', 'compress-archive', '-Path', lfile, ',', pfile, '-Update', '-DestinationPath', zfile])


def upload_zip(function_name, zip_file_path):
    lambda_client = boto3.client('lambda')

    with open(zip_file_path, 'rb') as zip_file:
        response = lambda_client.update_function_code(
            FunctionName=function_name,
            ZipFile=zip_file.read()
        )

    print(f"Lambda function '{function_name}' updated successfully.")


if __name__ == '__main__':
    create_zip()
    upload_zip('asupiyo-lambda', zfile)
