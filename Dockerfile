FROM python:3.9.4
WORKDIR /home/app
#COPY requirements.txt .
#RUN pip install -r requirements.txt
COPY rabin_karp.py .
COPY inputs.txt .
ENTRYPOINT ["python3", "rabin_karp.py"]
