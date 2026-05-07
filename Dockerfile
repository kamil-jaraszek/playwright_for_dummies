FROM jenkins/jenkins:lts

USER root

# Install Python + pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Install Playwright + pytest
RUN pip3 install --upgrade pip && \
    pip3 install playwright pytest pytest-playwright && \
    playwright install

USER jenkins
