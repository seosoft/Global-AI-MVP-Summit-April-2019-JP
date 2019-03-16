RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential gcc g++ python-dev unixodbc unixodbc-dev
