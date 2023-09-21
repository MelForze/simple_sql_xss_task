FROM python:3.11
WORKDIR /app
COPY . .

RUN python -m pip install flask
RUN python -m pip install mysql-connector-python 
RUN python -m pip install selenium
RUN python -m pip install webdriver-manager
RUN apt-get update && apt-get install -y firefox-esr

EXPOSE 5005
CMD ["sh", "-c", "sleep 20 && python /app/app.py"]