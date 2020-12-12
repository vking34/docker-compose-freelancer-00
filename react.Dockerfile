FROM node:12.18
ENV NODE_ENV production
ENV PORT=5000
WORKDIR /app/rsa-calculator/frontend

COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
COPY . /app
RUN npm install
RUN npm install -g react-scripts
RUN npm build

EXPOSE 5000

CMD [ "npm", "start" ]