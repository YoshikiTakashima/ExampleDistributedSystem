FROM ubuntu:19.10

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    	 python3 \
	 python3-pip && \
    pip3 install pyzmq

ADD . .

CMD [ "python3", "./recv.py" ]