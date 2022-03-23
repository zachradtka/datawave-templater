FROM python:3

WORKDIR /app

COPY generate_templates.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Create a user with USER_ID and GROUP_ID for correct file permissions
ARG USER_ID
ARG GROUP_ID
RUN groupadd --gid ${GROUP_ID} user
RUN useradd --uid ${USER_ID} --gid ${GROUP_ID} user

RUN chown -R user:user /app

USER user

VOLUME [ "/data" ]

ENTRYPOINT ["python", "generate_templates.py"]
