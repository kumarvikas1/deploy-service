FROM python:3.8
WORKDIR /server
ENV version 0.1.3
#COPY ./requirements/login_predict-0.1.2-py2.py3-none-any.whl /server/login_predict-0.1.2-py2.py3-none-any.whl
#COPY ./requirements/login_predict-0.1.3-py2.py3-none-any.whl /server/login_predict-0.1.3-py2.py3-none-any.whl
COPY ./requirements/base.txt /server/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt
#RUN pip install login_predict-${version}-py2.py3-none-any.whl
COPY ./app /server/app
EXPOSE 8080
WORKDIR /server/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
