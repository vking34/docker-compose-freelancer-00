FROM node:alpine

WORKDIR /app/rsa-calculator/frontend

RUN npm install

COPY . /app

RUN npm build

EXPOSE 5000

CMD [ "npm", "start" ]