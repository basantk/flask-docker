FROM python:3.7.16
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
#RUN pip install flask
COPY . .
CMD ["flask","run","--host","0.0.0.0"]