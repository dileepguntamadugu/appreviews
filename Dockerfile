FROM python
COPY requirements.txt requirements.txt
COPY analysis.py analysis.py
COPY datacleanse.py datacleanse.py
RUN pip install -r requirements.txt
RUN python datacleanse.py
#RUN python analysis.py