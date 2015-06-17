from __future__ import division

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

# find the total number of users in our network
num_users = len(users)

# find the average number of connections in our network
avg_connections = total_connections / num_users

# create a list of tuples (user_id, number_of_friends)
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

# sort num_friends_by_id by number of friends largest to smallest
sorted_number_of_friends = sorted(num_friends_by_id, key = lambda (user_id, number_of_friends): number_of_friends, reverse = True)

print sorted_number_of_friends
