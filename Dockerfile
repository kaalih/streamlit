FROM python:3.7.4-slim-stretch

COPY . /
RUN  pip install -r requirements.txt

CMD streamlit run app/app.py