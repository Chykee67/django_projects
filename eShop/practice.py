trends = {
    'maggi': 10,
    'onions': 5,
    'beans': 25,
    'garri': 27,
    'salt': 2,
    'rice': 15
}

print(sorted(trends.items(), key=lambda tre: tre[1]))