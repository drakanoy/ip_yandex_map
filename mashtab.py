def razmer(toponym):
    spn_h = str(float((toponym['boundedBy']['Envelope']['upperCorner']).split()[0]) - float(
        (toponym['boundedBy']['Envelope']['lowerCorner']).split()[0]))
    spn_d = str(float((toponym['boundedBy']['Envelope']['upperCorner']).split()[1]) - float(
        (toponym['boundedBy']['Envelope']['lowerCorner']).split()[1]))
    return spn_h, spn_d
