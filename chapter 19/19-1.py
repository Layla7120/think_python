def binomial_coeff(n, k):
    '''이항 계수를 계산한다. 'n에서 k를 선택한다.'
    n: 시도횟수
    k: 성공 횟수

    반환값: int
    '''
    # if k == 0:
    #     return 1

    # if n == 0:
    #     return 0
    
    # res = binomial_coeff(n - 1, k) + binomial_coeff(n - 1, k - 1)
    # return res
    return 1 if k == 0 else  0 if n == 0 else  binomial_coeff(n - 1, k) + binomial_coeff(n - 1, k - 1)
if __name__ == "__main__":
    print(binomial_coeff(4, 8))