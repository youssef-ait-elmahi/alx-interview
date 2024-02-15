#!/usr/bin/node
const request = require('request');

const fetchCharacter = (url) => {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

const fetchFilm = (id) => {
  return new Promise((resolve, reject) => {
    const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).characters);
      }
    });
  });
};

const printCharacters = async () => {
  try {
    const id = process.argv[2];
    const charactersUrls = await fetchFilm(id);

    const characterNames = await Promise.all(charactersUrls.map(fetchCharacter));

    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error(error);
  }
};

printCharacters();
