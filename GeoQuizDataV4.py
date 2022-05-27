import sqlite3
import random
from math import radians, cos, sin, asin, sqrt

## class GeoQuizData functions as a local API

class GeoQuizData:    
    def __init__(self, country_list=None):
        
        self.country_list = country_list
        self.quizquestion = self.QuizQuestion()
        self.allanswers = self.AllAnswers()
        self.topanswers = self.TopAnswers()
        self.api = self.API()

    def QuizQuestion(self):
    
        ## Query for a List of Capitals

        connection = sqlite3.connect('GeoQuizDataV3.db')
        c = connection.cursor()
        
        query_for_capitals = ("SELECT Land, Hoofdstad, point FROM Hoofdsteden")
        c.execute(query_for_capitals)
        all_capitals = c.fetchall()

        ## Make List of Capitals Not Yet Answered

        remaining_capitals = []
        
        for tuple in all_capitals:

            if tuple[0] not in self.country_list:
            
                remaining_capitals.append(tuple)
            
            else:       
            
                pass
        
        ## Pick a Randum Capital from the Remain List

        question = random.choice(remaining_capitals)

        ## GPS coords for the quiz question
        
        quiz_coords = question[2].split(',', 2)     ## split the point coordinates
        quiz_lat = float(quiz_coords[0].strip('('))     ## and make gps floats
        quiz_lon = float(quiz_coords[1].strip())        ## for lat and lon of quiz question
        
        ## construct clean output: 'Country, 'Capital', 'Lat', 'Lon', 'Qs left'

        quizquestion = [question[0], question[1], quiz_lat, quiz_lon, len(remaining_capitals)]

        return quizquestion

    def AllAnswers(self):

        ## Query for a List of Capitals + Cities

        connection = sqlite3.connect('GeoQuizDataV3.db')
        c = connection.cursor()
        
        query_for_capitals = ("SELECT Hoofdstad, point FROM Hoofdsteden")
        c.execute(query_for_capitals)
        capitals = c.fetchall()
        
        query_for_cities = ("SELECT Stad, point FROM Steden")
        c.execute(query_for_cities)
        cities = c.fetchall()
        
        ## Concat the Lists of Capitals + Cities

        answers = [*capitals, *cities]

        ## Polish the List for GPS coords

        clean_answers = []

        for tuple in answers:

            city = tuple[0]                            ## lock the city
            coords = tuple[1].split(',', 2)            ## split the point coordinates
            city_lat = float(coords[0].strip('('))     ## and make gps floats
            city_lon = float(coords[1].strip())        ## for lat and lon of quiz question
            item = [city, city_lat, city_lon]
            clean_answers.append(item)
        
        return clean_answers

    def TopAnswers(self):

        distance_matrix = []

        for tuple in self.allanswers:
            lat1 = self.quizquestion[2]
            lon1 = self.quizquestion[3]
            city = tuple[0]
            lat2 = tuple[1]
            lon2 = tuple[2]
        
            # haversine formula 
            R = 6372.8 # Earth radius in kilometers use 6372.8 km

            dLat = radians(lat2 - lat1)
            dLon = radians(lon2 - lon1)
            lat1 = radians(lat1)
            lat2 = radians(lat2)

            a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
            c = 2*asin(sqrt(a))
            
            distance = c * R
            items = [city, distance]
            distance_matrix.append(items)

        distance_matrix.sort(key=lambda x:x[1])
      
        top12 = [sublist for sublist in distance_matrix][1:13]

        top5 = random.sample(top12, k=5)   

        topanswers = [item[0] for item in top5]

        topanswers.append(self.quizquestion[1])

        random.shuffle(topanswers)

        return topanswers

    def API(self):

        ## parse the quiz data item by item for easy Flask consumption
        ## 'Country', 'City', 'Qs Remaining', 'Answers'

        response = [
            self.quizquestion[0],
            self.quizquestion[1],
            self.quizquestion[4],
            self.topanswers
        ]

        return response