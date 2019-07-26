FROM python:3.7-slim

WORKDIR /time-tracker
COPY . /time-tracker

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "timetracker.py"]
