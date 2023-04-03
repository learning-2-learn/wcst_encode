FROM ghcr.io/walkerlab/pytorch-jupyter:cuda-11.8.0-pytorch-1.13.0-torchvision-0.14.0-torchaudio-0.13.0-ubuntu-22.04

RUN git clone https://github.com/learning-2-learn/lfp_tools /src/lfp_tools &&\
        pip3 install -e /src/lfp_tools

RUN git clone https://github.com/learning-2-learn/spike_tools.git /src/spike_tools &&\
        pip3 install -e /src/spike_tools

RUN pip3 install --upgrade s3fs

COPY . /src/wcst_encode
RUN pip3 install -e /src/wcst_encode
