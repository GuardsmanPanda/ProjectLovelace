def habitable_exoplanet(L, r):
    return 'too hot' if r < (L/1.11)**0.5 else 'too cold' if r > (L/0.54)**0.5 else 'just right'