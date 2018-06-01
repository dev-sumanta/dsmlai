from sys import argv

script, user_name = argv
print(argv, len(argv))
prompt = '>'

print("Hi {0} I'm the {1} script".format(user_name, script))
print("I'd like to ask you a few questions")
print('Do you like me {}'.format(user_name))
likes = input(prompt)

print('Where do you live')
lives = input(prompt)

print('What kind of computer do you have')
computer = input(prompt)

print('So you live in {0}. I had hoped you would like me and your \
response to liking me was {1}. And you have a computer of type \
 {2}. Nice !'.format(lives, likes, computer))
