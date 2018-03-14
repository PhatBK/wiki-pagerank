# -*- coding: utf-8 -*-
rankings_file = "ranks.txt"
titles_file = "titles.txt"
output_file = "final_sorted_ranking.txt"
rankings = []
titles = {}
print('ranks file....')
with open(rankings_file, 'r') as f:
	for line in f:
		pair = line.split(' ')
		# print pair
		rankings.append((float(pair[2]), int(pair[0])))
print rankings
print('titles file...')
with open(titles_file, 'r') as f:
	for line in f:
		pair = line.split("\t")
		print pair
		title = pair[1]
		title = title[0:-1]
		# title = title.replace('_', ' ')
		titles[int(pair[0])] = title

print titles
rankings.sort()
rankings.reverse()

# ghi ra file:
with open(output_file, 'w+') as f:
	for pagerank, pageid in rankings:
		# print pagerank,"	",pageid
		f.write(str(pagerank) + '\t' + titles[pageid] + '\n')

print('Done')