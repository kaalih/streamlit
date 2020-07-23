FROM python:3.7.4-slim-stretch
COPY requirements.txt /
RUN  pip install -r requirements.txt

COPY . /

# starting point
CMD streamlit run app/app.py