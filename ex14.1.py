from sys import argv

script, user_name, age = argv
prompt = 'Please input here:\n'

print "Hi %s, you're %s years old, I'm the %s script." % (user_name, age, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name 
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What's your age?"
age = raw_input(prompt)

print '''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You're %r years old, maybe you don't have a girlfriend.
And you have a %r computer. Nice.
''' %(likes, lives, age, computer)
