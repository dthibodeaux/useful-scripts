# This are steps to deploy the app using ArgoCD

# Create Dockerfile, build image, and deploy

#  vi Dockerfile
#  FROM python:3.7
#  
#  RUN mkdir /app 
#  WORKDIR /app
#  ADD . /app/
#  RUN pip install -r requirements.txt
#
#  EXPOSE 5000
#  CMD ["python", "/app/main.py"]
#

# docker build -f Dockerfile -t <repo/app_name:V1<version> .