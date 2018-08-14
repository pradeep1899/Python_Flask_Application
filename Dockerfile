FROM python:alpine3.7
COPY . /Python_Flask_app
WORKDIR /Python_Flask_app
RUN pip install -r requirement.txt
#RUN pip install pipenv
#RUN export FLASK_APP=./employee/index.py
#RUN source $(pipenv --venv)/bin/activate
#RUN flask run -h 0.0.0.0
EXPOSE 4000
#CMD python ./index.py
ENTRYPOINT ["python"]
CMD ["./employee/index.py"]
