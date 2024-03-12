from django.shortcuts import render

planets = [
    {'name': 'Sun', 'herbs': 'Angelica, Ash, Bay, Calendula, Chamomile, Celandine, Eyebright, Frankincense, Juniper, Mistletoe, Rosemary, Saffron, Safflower, Saint-Johns Wort, Sunflower, Tormentilla, Walnuts', 'energies': 'Self-confidence, Success, Vitality, Courage, Authority, Dignity, Fame, Self Knowledge'},
    {'name': 'Moon', 'herbs': 'Almond, Anise Seed, Cabbage, Camphor, Cucumber, Fennel, Iris, Jasmine, Lettuce, Lily, Lotus, Moonwort, Mugwort, Pumpkin, Violet, Watercress, White Sandalwood', 'energies': 'Psychic Knowledge, Dreamworking, Childbirth, Fertility, Past Life Recall, Imagination, the Subconcious Mind'},
    {'name': 'Mars', 'herbs': 'Aloeswood, Asafoetida, Basil, Broom Tops, Briony, Cactus, Cayenne, Cumin, Dragons Blood Resin, Galangal, Garlic, Gentian, Ginger, Hawthorn, Horseraddish, Honeysuckle, Mustard, Nettle, Peppercorn, Red Sandalwood, Rue, Safflower, Sanicle, Tobacco, Wormwood', 'energies': 'Victory, Agression, Achievement, Energy, Action, Assertiveness, Strength, Sexual Desire'},
    {'name': 'Mercurcy', 'herbs': 'Bergamot, Caraway, Cinnamon, Dill, Ephedra, Gum Arabic, Gum Mastic, Horehound, Lavender, Licorice, Marjoram, Mouse-ear, Mullein, Papyrus, Peppermint, Star Anise, Savory, Thyme, Woodruff', 'energies': 'Communication, Divination, Business Success, Intellectualization, Learning'},
    {'name': 'Jupiter', 'herbs': 'Agrimony, Borage, Carnation, Cedar, Cinquefoil, Dandelion, Figs, Fir, Hyssop, Linden, Magnolia, Maple, Meadowsweet, Oak, Oak Moss, Pine, Poplar, Saffron, Sage, Sassafras, Sumac, Rosin, Wood Betony', 'energies': 'Expansion, Career, Ambition, Luck, Material Success, Spiritual Growth, Humor'},
    {'name': 'Venus', 'herbs': 'Catnip, Cherry, Coltsfoot, Damiana, Feverfew, Lemon Verbena, Lilac, Maidenhair, Mandrake, Myrtle, Orchid, Passionflower, Peach, Periwinkle, Plumeria, Rhubarb, Raspberyy, Rose, Spikenard, Tansy, Tonka Bean, Vanilla, Vervain, Violet', 'energies': 'Love, Friendship, Artistry, Attraction, Music, Pleasure, Sensual Delights, Beauty, Balance, Compassion'},
    {'name': 'Saturn', 'herbs': 'Asafoetide, Balm of Gilead, Bistort, Boneset, Comfrey, Cypress, Dill, Fumitory, Garlic, Hawthorn, Hemlock, Hyssop, Patchouli, Petitgrain, Rosemary, Solomen''s Seal, Saint-Johns Wort, Valerian, Vetivert, Wolfsbane, Yew', 'energies': 'From, Stability, Karma, Discipline, Occult Knowledge, Protection, Patience, Endurance'},
    {'name': 'Neptune', 'herbs': 'Cannabis, Datura, Lobelia, Lotus, Orange Blossom, Peach, Poppy, Skullcap, Wild Lettuce, Willow, Wisteria', 'energies': 'Illuion, Imagination, useful in Hypnosis, Trance, Dreamwork'},
    {'name': 'Uranus', 'herbs': 'Allspice, Betel Nut, Chicory, Clove, Coffee, Elemi, Guarana, Mahuang', 'energies': 'Enlightenment, Objectivity, Technology, Genius, Eccetricity, Breaking free from old patterns'},
    {'name': 'Pluto', 'herbs': 'Barley, Black Cohosh, Corn, Damiana, Fly Agaric, Galangal Root, Muchrooms, Myrrh, Patchouli, Pomegranate, Psilocybin, Rye, Saw Palmetto, Wheat, Wormwood, Yohimbe', 'energies': 'Death, Alchemical Transformation, Regeneration, Decay, Sexual Instinct, The Deep Unconscious, Catharsis'},

]

herb= set()

for planet in planets:
    herbs = planet['herbs'].split(', ')
    herb.update(herbs)

herb_list = sorted(list(herb))

body_systems = [
    {'system': 'system name', 'plants': 'associated plants'},
    {'system': 'system name', 'plants': 'associated plants'},
    {'system': 'system name', 'plants': 'associated plants'},
    {'system': 'system name', 'plants': 'associated plants'},
    {'system': 'system name', 'plants': 'associated plants'},
    {'system': 'system name', 'plants': 'associated plants'},
    {'system': 'system name', 'plants': 'associated plants'},
    {'system': 'system name', 'plants': 'associated plants'},
    {'system': 'system name', 'plants': 'associated plants'}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')
def planets_index(request):
    return render(request, 'planets/index.html', {'planets': planets})
def herbs_index(request):
    return render(request, 'herbs/index.html', {'herbs': herb_list})
def about(request):
    return render(request, 'about.html')
def herb(request, herb):
    return render(request, 'herbs/herb', {'herb': herb})
def bodysystems_index(request):
    return render(request, 'bodysystems/index.html', {'body_systems': body_systems})