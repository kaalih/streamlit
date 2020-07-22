FROM python:3.7.4-slim-stretch
COPY . /

RUN  pip install -r requirements.txt

#CMD echo "test"
#CMD  streamlit run app/app.py

CMD streamlit run app/app.py