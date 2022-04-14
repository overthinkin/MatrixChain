
# 동적 계획 알고리즘
 - 입력 크기가 작은 부분문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분문제들을 해결하여, 최종적으로 언래 주어진 입력의 문제를 해결하는 알고리즘이다.
 - 동적 계획 알고리즘에는 부분문제들 사이에 의존적 관계가 존재한다. 이는 대부분의 경우 뚜렷이 보이지 않아 '함축적 순서'라고 한다.

------

팀: Team C

팀원: 정민성, 백도담, 장진이

------


## 연속 행렬 곱셈
- 연속된 행렬들의 곱셈에 필요한 원소 간의 최소 곱셈 횟수를 찾는 문제
- 부분문제: 주어진 행렬의 순서를 지켜 이웃하는 행렬끼리 곱하기(이웃하지 않은 행렬과는 곱할 수 없음)
- 시간 복잡도: O(n^2) * O(n) = O(n^3)

### 코드 리뷰
배열의 대각선 원소들은 0이 된다.
부분문제의 크기가 1인 경우는 아래와 같이 해준다.
~~~python
if i == 1: #차이가 1밖에 나지 않는 칸
    dp[j][j+i] = matrix[j][0] * matrix[j][1] * matrix[j+i][1]
    continue
~~~

나머지의 경우는 아래와 같이 원래 들어있던 값보다 작을 경우 값을 교체해준다.
~~~python
dp[j][j+i] = 2**32 # 최댓값을 미리 넣어줌
for k in range(j, j+i):
    temp = dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1]
    if dp[j][j+i] > temp : # 원래 들어있던 값보다 곱셈 횟수가 적으면 교체
        dp[j][j+i] = temp 
~~~

------

### 실행 결과

![](https://user-images.githubusercontent.com/80513292/163364077-d1f97e0d-c95e-47da-9617-20ea6c7ec944.png)

1행: 입력할 행렬의 수 = 4

2행~5행: 행렬 내용

6행: 연속행렬곱셈의 결과값