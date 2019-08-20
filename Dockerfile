FROM python:3.6
LABEL maintainer="Kyle Galloway <kyle.galloway@cfdrc.com>"

ENV SRC_DIR /src
RUN mkdir $SRC_DIR
WORKDIR $SRC_DIR
VOLUME $SRC_DIR

# ADD . $SRC_DIR

CMD ["/bin/bash"]

