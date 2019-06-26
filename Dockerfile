FROM python:3
ADD . /code
WORKDIR /code
RUN pip3 install Flask
RUN pip3 install -U textblob
RUN python3 -m textblob.download_corpora
CMD python3 Twitter_sentimentAnalysis.py
