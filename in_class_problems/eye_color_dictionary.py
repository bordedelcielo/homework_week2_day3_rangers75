def eye_color(d):
    for k,v in d.items():
        print(f'{k} has {v} eyes')


people = {
    'Max': 'blue',
    'Lilly': 'brown',
    'Barney': 'blue',
    'Larney': 'brown',
    'Ted': 'purple',
    'Sasuke Uchiha': 'Sharingan',
    'Firelord Zuko': 'yellow',
    'Darth Vader': 'yellow'
}

print(eye_color(people))