# build env
FROM node:21.7.1-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . ./
RUN npm run build
# Копируем файлы в общий том, указанный в docker-compose.yml
CMD cp -r build/* /static/