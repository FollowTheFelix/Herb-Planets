from django.shortcuts import render

planets = [
    {'name': 'Sun', 'herbs': 'Angelica, Ash, Bay, Calendula, Chamomile, Celandine, Eyebright, Frankincense, Juniper, Mistletoe, Rosemary, Saffron, Safflower, Saint-Johns Wort, Sunflower, Tormentilla, Walnuts', 'energies': 'Self-confidence, Success, Vitality, Courage, Authority, Dignity, Fame, Self Knowledge'},
    {'name': 'Moon', 'herbs': 'Almond, Anise Seed, Cabbage, Camphor, Cucumber, Fennel, Iris, Jasmine, Lettuce, Lily, Lotus, Moonwort, Mugwort, Pumpkin, Violet, Watercress, White Sandalwood', 'energies': 'Psychic Knowledge, Dreamworking, Childbirth, Fertility, Past Life Recall, Imagination, the Subconcious Mind'},
    {'name': 'Mars', 'herbs': 'Aloeswood, Asafoetida, Basil, Broom Tops, Briony, Cactus, Cayenne, Cumin, Dragons Blood Resin, Galangal, Garlic, Gentian, Ginger, Hawthorn, Horseraddish, Honeysuckle, Mustard, Nettle, Peppercorn, Red Sandalwood, Rue, Safflower, Sanicle, Tobacco, Wormwood', 'energies': 'Victory, Agression, Achievement, Energy, Action, Assertiveness, Strength, Sexual Desire'},
    {'name': 'Mercurcy', 'herbs': 'List Herbs', 'energies': 'List energies'},
    {'name': 'Jupiter', 'herbs': 'List Herbs', 'energies': 'List energies'},
    {'name': 'Venus', 'herbs': 'List Herbs', 'energies': 'List energies'},
    {'name': 'Saturn', 'herbs': 'List Herbs', 'energies': 'List energies'},
    {'name': 'Neptune', 'herbs': 'List Herbs', 'energies': 'List energies'},
    {'name': 'Uranus', 'herbs': 'List Herbs', 'energies': 'List energies'},
    {'name': 'Pluto', 'herbs': 'List Herbs', 'energies': 'List energies'},

]

# Create your views here.
def home(request):
    return render(request, 'home.html')
def planets_index(request):
    return render(request, 'planets/index.html', {'planets': planets})