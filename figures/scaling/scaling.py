import yaqd_core
import numpy as np


class NdarrayTestDaemon(yaqd_core.Base):
    _kind = "scaling"

    def rand_int32(self, dim1, dim2):
        return np.random.randint(0, 4096, dim1 * dim2).reshape(dim1, dim2).astype(np.int32)


if __name__ == "__main__":
    NdarrayTestDaemon.main()
