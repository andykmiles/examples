FROM python

WORKDIR /usr/src/app

RUN python -m pip install --no-cache-dir \
    pytest \
    pytest-cov \
    black \
    mypy \
    loguru
CMD bash
