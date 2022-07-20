FROM python:3.10.4

ENV PYTHONUNBUFFERED=1
WORKDIR /blog_api/social_networks
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]