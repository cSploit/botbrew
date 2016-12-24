FROM debian:latest

MAINTAINER DeveloppSoft <developpsoft@gmail.com>

RUN apt update
RUN apt install --yes build-essential python python-yaml cmake bison flex git autoconf automake libtool antlr wget fakeroot ccache zip curl

RUN curl -sSL https://get.rvm.io | bash
RUN bash -l -c "rvm use 1.9.3-p125 --install"

RUN update-ca-certificates -f
RUN wget "http://dl.google.com/android/repository/android-ndk-r11c-linux-x86_64.zip" -O /tmp/ndk.zip
WORKDIR /root
RUN unzip /tmp/ndk.zip
RUN mv android-ndk-* .ndk

ADD ./ ./botbrew/

WORKDIR ./botbrew

RUN echo 'G_MAINTAINER="docker"\nG_NDKPATH="../.ndk"' > config.sh

RUN ./botbrew toolchain
RUN ./botbrew makefile > Makefile

RUN echo 'export PYTHONPATH="/usr/lib/python2.7/dist-packages"' > /start.sh
RUN echo '/bin/bash' >> /start.sh
RUN chmod +x /start.sh

CMD /start.sh
