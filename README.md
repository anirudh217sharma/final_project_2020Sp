# final_project
Each team creates a fork from this for their course project

Title : Monte Carlo simulation to address whether social distancing will help mitigate the spread of corona virus 

Assumptions : 

If a person comes within 6 metres of an infected person they will become infected 

No person in the population sample is immune to the virus 

Description : 

There is a population sample of 1000 people in which initially only a single person is infected which means the initial infection rate in the population sample is 0.1 %. The model will calculate the infection rate at the end of two months for two scenarios: 

1.) The people are moving freely around the area (150*150 square metre)  every day for which numpy.random.randit function was used to assign people random locations across the space.

2.) In the second scenario people are only leaving there house or living area for buying essential items such as grocery and leaving there house every four days.

Incubation period : Defined as the time when the person is contagious and can spread the virus to others - 5 days 

The age across the population comes from a normal distribution and the number of deaths per age group can be calculated by the respective probailities of death for each group

References : 

https://www.washingtonpost.com/graphics/2020/world/corona-simulator/
https://towardsdatascience.com/covid-19-social-distancing-simulation-f091a58732f9
https://github.com/o0oBluePhoenixo0o/COVID_19-Social-Dist-Simulation


