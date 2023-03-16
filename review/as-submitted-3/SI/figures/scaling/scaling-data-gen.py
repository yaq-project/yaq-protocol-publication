import yaqc
import numpy as np
import time

shapes = [
    (1, 2**0),
    (1, 2**1),
    (1, 2**2),
    (1, 2**3),
    (1, 2**4),
    (1, 2**5),
    (1, 2**6),
    (1, 2**7),
    (1, 2**8),
    (1, 2**9),
    (1, 2**10),
    (1, 2**11),
    (1, 2**12),
    (1, 2**13),
    (1, 2**14),
    (1, 2**15),
    (1, 2**16),
    (1, 2**17),
    (1, 2**18),
    (1, 2**19),
    (1, 2**20),
    (1, 2**21),
    (1, 2**22),
    (1, 2**23),
    (1, 6000000),
    (512, 512),
    (1024, 1024),
    (1024, 4096),
]

c = yaqc.Client(36656)

print(f"shapex,shapey,npts,n,mean,stdev")
for shape in shapes:
    start_time = time.time()
    times = []
    for _ in range(10):
        run_time = time.time()
        a = c.rand_int32(*shape)
        end_time = time.time()
        times.append(end_time - run_time)
        if end_time - start_time > 60:
            break
    print(f"{','.join(str(i) for i in shape)}, {np.prod(shape)}, {len(times)}, {np.mean(times)}, {np.std(times)}")
