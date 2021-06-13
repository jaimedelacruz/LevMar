# LevMar
A user-friendly Levenberg-Marquardt fitting algorithm for non-linear models.

The user only needs to provide a function that calculates the model prediction for a ser of parameters. The user can pass a container to this function with additional data that could be required by the model.

The user can easily especify parameter limits and scaling norms.

I have included a commented example (see example.py).

Coded by J. de la Cruz Rodriguez (ISP-SU 2021).
We follow the implementation described in de la Cruz Rodriguez et al. (2019),
but for the moment without regularization.

If you find this code useful for your research, I would appreciate the most a citation to [de la Cruz Rodriguez et al. (2019)](https://ui.adsabs.harvard.edu/abs/2019A%26A...623A..74D/abstract).

