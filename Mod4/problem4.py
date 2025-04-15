'''
#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, 
and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), 
or R (appropriate for over 18) rated movies.
'''

print("Hello. I would like to be able to tell you what type of movies you can see. (G, PG-13, or R)")
age = int(input("Could you please let me know your age? "))
if (age < 13):
  print("You can see G rated movies.")
elif (age >= 13 and age <= 17):
  print("You can see PG-13 rated movies.")
else:
  print("You can see R rated movies.")
