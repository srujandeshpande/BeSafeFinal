def NearestNeighbours(sets):

    import sklearn
    import pandas
    from sklearn.neighbors import NearestNeighbors

    df = pandas.read_csv('KSI.csv')
    test_set = [[df.loc[i, 'LATITUDE'], df.loc[i, 'LONGITUDE']] for i in df.index]
    neigh = NearestNeighbors(radius=0.0005)
    test = sets
    neigh.fit(test_set)

    sum = 0
    for i in test:
        sum += len(neigh.radius_neighbors([i])[1][0])
    score = sum/len(test)
    return score
