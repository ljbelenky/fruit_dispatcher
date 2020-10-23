FROM python

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install numpy flask pandas

EXPOSE 5000

ENTRYPOINT [ "python"]
 
CMD [ "fruit.py" ]