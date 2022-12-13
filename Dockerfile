FROM colserra/light-encoder:libfdk-aac
WORKDIR /bot
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["bash","start.sh"]
