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

https://theconversation.com/coronavirus-why-should-we-stay-1-5-metres-away-from-each-other-134029

https://www.samhealth.org/about-samaritan/news-search/2020/03/20/social-distancing

https://www.contagionlive.com/news/coronavirus-incubation-period-is-about-5-days-study-estimates
https://www.worldometers.info/coronavirus/coronavirus-age-sex-demographics/

Note : As a lot of interactive plots have been used in the notebook , github only displays the notebook as a static html page in order to view the notebook properl kindly download the final notebook - socail_distancing_covid19 or use this link : 

https://nbviewer.jupyter.org/ 

Please see the final analysis folder to view all the results and observations : Social_distacning_staticplots.ipynb 

All the function used are present in the final analysis folder : monte_carlo.py
