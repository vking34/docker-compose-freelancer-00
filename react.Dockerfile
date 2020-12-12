FROM node:12.18
COPY . /app
WORKDIR /app/rsa-calculator/frontend
RUN npm install
RUN npm install -g react-scripts
RUN npm run build

EXPOSE 5000

CMD [ "npm", "start" ]


# build stage
FROM node:12.2.0-alpine as build
WORKDIR /app
COPY ./rsa-calculator/frontend/ /app
RUN npm i -g yarn

RUN yarn install --silent
RUN yarn global add react-scripts@3.0.1 --silent
RUN yarn run build

# deployment stage
FROM nginx:1.16.0-alpine
WORKDIR /
COPY --from=build /app/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY ./rsa-calculator/frontend/nginx/nginx.conf /etc/nginx/conf.d


EXPOSE 5000