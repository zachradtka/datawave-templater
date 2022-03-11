FROM python:3

WORKDIR /app

COPY generate_templates.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

VOLUME [ "/data" ]

ENTRYPOINT ["python", "generate_templates.py"]
