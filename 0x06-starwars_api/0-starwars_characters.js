#!/usr/bin/node

// import the fetch module
const http = require('node:http');

// Get the Movie ID
const movieID = process.argv[2];

if (!movieID) {
	console.error('Please provide a movie ID as a command-line argument.');
	process.exit(1);
}

// Base URL for the Star Wars API
const apiURL = 'https://swapi-api.alx-tools.com/api/films/${moviesID}/';

// fetch all movies
fetch(apiURL)
	.then((response) => {
		if (!response.ok) {
			throw new Error('Failed to fetch movie details. Status Code: ${response.status}');
		}
		return response.json();
	})
	.then((data) => {
		const films = data.results;

		// validate the movieID
		if (movieID < 1 || movieID > films.length) {
			console.error('Invalid Movie ID. Please use valid ID', films.length);
			return;
		}
		// get the selected movie by ID
		const selectedMovie = films[movieID - 1];
		console.log('Movie: ${selectedMovie.title}');

		// extract the characters list
		const characters = selectedMovie.characters;

		if(!characters || characters.length === 0) {
			console.log('No characters found');
			return;
		}
		// fetch and print characters
		characters.forEach((characterURL) => {
			fetch(characterURL)
			.then((charResponse) => {
				if (!charResponse.ok) {
					throw new Error('Failed. Staus Code ${charResponse.status}');
				}
				return charResponse.json();
			})
			.catch((error) => {
				console.error('Error fetching character:', error);
			});
		});
	})
	.catch((error) => {
		console.error('Error fetching movie data:', error);
	});
