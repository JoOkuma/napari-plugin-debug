import napari


if __name__ == '__main__':
    viewer = napari.Viewer()
    #         id, t, z, x, y
    tracks = [[1, 0, 5, 5, 5],
              [1, 1, 10, 10, 10],
              [1, 2, 15, 15, 15]]

    viewer.add_tracks(tracks)
    napari.run()