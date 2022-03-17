FROM nvcr.io/nvidia/pytorch:22.01-py3
USER root
ARG PYTHON_VERSION=3.9
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends --no-install-suggests \
          python${PYTHON_VERSION} \
          python3-pip \
        #   python${PYTHON_VERSION}-dev \
          build-essential\
        #   graphviz\
# Change default python
    && cd /usr/bin \
    && ln -sf python${PYTHON_VERSION}         python3 \
    && ln -sf python${PYTHON_VERSION}m        python3m \
    && ln -sf python${PYTHON_VERSION}-config  python3-config \
    && ln -sf python${PYTHON_VERSION}m-config python3m-config \
    && ln -sf python3                         /usr/bin/python \
# Update pip and add common packages
    && python -m pip install --upgrade pip \
    && python -m pip install --upgrade \
        setuptools \
        wheel \
        six \
# Cleanup
    && apt-get clean \
    && rm -rf $HOME/.cache/pip
RUN pip3 install --upgrade pip
RUN pip3 install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
WORKDIR /appli

