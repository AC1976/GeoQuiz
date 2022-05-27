# GeoQuiz
Python / Flask based Quiz Geo Game 

GeoQuiz is a Python application to support kids in learning the capitals of the 198 countries of the world. The application consists of two main components. The first component is a Python class -- GeoQuizData -- that encapsulates all functionality required for generating random quiz questions and answers.

GeoQuizData:

* Retrieves from a sqlite database file all capital and key cities of the planet;
* Picks a random capital / country combination;
* Generates x-alternative answers, based on a distance map for the relevant country;
* Shuffles and picks 5 out of the x-alternative answers, for 'wrong' multiple choice options;
* Exports, API-style, a response consisting of (i) country, (ii) capital, (iii) list of 5 wrong answers

The second component is a Flask app, styled with Buma CSS, which is mostly UI to show the multiple choice quiz game and take input. The game logic (remaining questions, remaining lifes) is embedded in the Flask app and routes, which works, but seems clunky (to me).

