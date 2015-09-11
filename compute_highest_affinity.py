#! /usr/bin/python

# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):		  
		site_set = set(site_list)
		#print site_set

		#build a site dictionary, key is site, val is a list of visiting users
		site_dict = dict()

		for i in range(0, len(site_list)):
				if	site_list[i] in site_dict:
						site_dict[site_list[i]].append(user_list[i])
				else:
						site_dict[site_list[i]] = [user_list[i]]
		#print site_dict
		
		#bulid a list with each pair of sites
		pair_list = [(x, y) for x in site_set for y in site_set if x < y]
		#print pair_list

		#count user num for each pair site
		record = dict()
		for pair in pair_list:
				record[pair] = 0
		
		for pair in pair_list:
				site1 = pair[0]
				site2 = pair[1]
				for site1_user in site_dict[site1]:
						if site1_user in site_dict[site2]:
								record[pair] = record[pair] + 1

		#print record
		max_num = 0
		for pair in pair_list:
				if(record[pair] >= max_num):
						max_num = record[pair]
						max_pair = pair

		return max_pair
