FROM pytorch/pytorch

WORKDIR /app

COPY ../lesson34/requirements.txt requirements.txt
COPY ../lesson34/lesson34_hometask.py lesson34_hometask.py

RUN pip install accelerate
RUN pip install -r requirements.txt

CMD ["python", "-u", "lesson34_hometask.py"]


