users = [
	{ 'id': 0, 'name': 'Hero' },
	{ 'id': 1, 'name': 'Dunn' },
	{ 'id': 2, 'name': 'Sue' },
	{ 'id': 3, 'name': 'Chi' },
	{ 'id': 4, 'name': 'Thor' },
	{ 'id': 5, 'name': 'Clive' },
	{ 'id': 6, 'name': 'Hicks' },
	{ 'id': 7, 'name': 'Devin' },
	{ 'id': 8, 'name': 'Kate' },
	{ 'id': 9, 'name': 'Klein' }
]

friendships = [
	(0, 1),
	(0, 2),
	(1, 2),
	(1, 3),
	(2, 3),
	(3, 4),
	(4, 5),
	(5, 6),
	(5, 7),
	(6, 8), 
	(7, 8), 
	(8, 9), 
]

# add friends list to users
for user in users:
	user['friends'] = []

# add friends to all users friends list
for i, j in friendships:
	users[i]['friends'].append(j) # add i as a friend of j
	users[j]['friends'].append(i) # add j as a friend of i

# find the total number of friends someone has
def number_of_friends(user):
	""" How many friends does _user_ have? """
	return len(user['friends'])	# length of friend_ids list

# find the total number of connections in our network
total_connections = sum(number_of_friends(user) for user in users)


####################################################################
# NOTES ############################################################
####################################################################

# # return len(user(['friends'])) 	# length of friend_ids list
# 	# return len(users[0]['friends']) # length of friends list for users[0]
# 	return len(users[user_id]['friends']) # length of friends list
# 	print len(users[i]['friends'])
# 	return len(user(['friends'])) 	# length of friend_ids list

# for user in users:
# 	user_id = users['id']
# 	print number_of_friends(user_ie)

# total_connections = sum(number_of_friends(user) for user in users) #24
# print total_connections