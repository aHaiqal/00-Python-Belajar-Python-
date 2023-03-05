# Copy dictionary
teman_teman = {
    "cup":"ucup cup",
    "tong":"gentong",
    "dung":"dudung",
}

friends = teman_teman

print(f'friends = {friends} \n')
print(f'teman-teman = {teman_teman}\n')

teman_teman["dung"] = 'dduung'
print(f'friends = {friends} \n')
print(f'teman-teman = {teman_teman}\n')

# pop dictionary
dataDung = friends.pop('dung')
print(f'data dung = {dataDung}\n')
print(f'friend = {friends}')
