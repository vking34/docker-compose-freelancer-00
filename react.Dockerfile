FROM node:alpine
COPY . /app
WORKDIR /app/rsa-calculator/frontend
RUN npm install
RUN npm build

EXPOSE 5000

CMD [ "npm", "start" ]