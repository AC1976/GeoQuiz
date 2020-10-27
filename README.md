# Geo References 

This repository houses a basic geoquiz written in Python. From a list file with tuples for every capital, country, subregion on the planet, the quiz code picks a random tuple for posing the "what capital belongs to this country" question. The code then generates a tuple of four possible answers, including the correct one. These answers are based on the subregion of the country - so the alternative answers for say Netherlands (Amsterdam) would be Brussels, Berlin, London --- and not e.g. Bogota, Beijing, Brasilia. This to make it a little harder to figure out the proper answer. The four answers are then assigned to multiple choice items a, b, c and d -- which are shuffled at random to avoid the right answer being the same choice.

The code is then looped so that for every question answered correct, one gets a point. For every wrong answer, one loses a point. No points left means game over.

I'd like to develop this further into a free topography quiz / webapp for kids. Let me know if you want to team up, or feel free to use this code as you see fit for own purpose.
