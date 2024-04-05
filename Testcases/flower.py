
# Đề bài
# https://scontent.fdad3-5.fna.fbcdn.net/v/t39.30808-6/432657759_1167388840911611_4479729588942010325_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=5f2048&_nc_ohc=hBLMa0Ya5M0Ab6Nq1tq&_nc_ht=scontent.fdad3-5.fna&oh=00_AfCGUQwtqMI_OUy5-5AOMrhdXCj3vCz0sMURZXckX8L6jQ&oe=66153657

MOD = 10**9 +7
def matmul(A,B):
  return [[sum(x*y % MOD for x,y in zip(row, col)) % MOD for col in zip(*B)] for row in A]

def matpow(A,n):
  if n==1:
    return A
  if n % 2 == 0:
    return matpow(matmul(A,A), n // 2)
  else:
    return matmul(A, matpow(matmul(A,A)), (n - 1) // 2)

transition_matrix = [
  [0,1,0,0,0],
  [1,0,1,0,0],
  [1,1,0,1,1],
  [0,0,1,0,1],
  [1,1,0,0,0],
] 

def count_Way(N):
  if N==1:
    return 5
  T = matpow(transition_matrix, N - 1)
  return sum(sum(row) for  row in T ) % MOD

N = int(input().strip())
print(count_Way(N))
