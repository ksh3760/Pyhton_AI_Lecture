# 모듈 로딩 ----------------------------------------
import numpy as np
from matplotlib import pyplot as plt

# 데이터 준비 ---------------------------------------
# [거리, 시간]
data = np.array([[100, 20], [150, 24], [300, 36], [400, 47],
                 [130, 22], [240, 32], [350, 47], [200, 42],
                 [100, 21], [110, 21], [190, 30], [120, 24],
                 [130, 18], [270, 48], [255, 28]])

# 입력(Feature) x, 츨력(Target) y 데이터 추출
x = data[:, 0].reshape(-1, 1)   # 2차원 배열 변환
y = data[:, 1]

# 데이터 확인
print(data.shape)
print('입력 데이터 => 거리 data[:, 0] =>', data[:, 0])
print('출력 데이터 => 시간 data[:, 1] =>', data[:, 1])

print(f'x => {x}, {type(x)}, {x.shape}')
print(f'y => {y}, {type(y)}, {y.shape}')


# 그래프 출력 => 거리 & 시간
plt.scatter(data[:, 0], data[:, 1])
plt.title('Distance & Time')
plt.xlabel('Delivery Distance')
plt.ylabel('Time Consumed')
plt.axis([90, 420, 15, 50])
plt.show()
