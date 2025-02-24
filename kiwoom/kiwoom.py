import random

# 로또 번호 생성 함수
def generate_lotto():
    # 1부터 45까지 숫자 중 6개를 무작위로 선택
    lotto_numbers = random.sample(range(1, 46), 6)
    # 오름차순으로 정렬
    lotto_numbers.sort()
    return lotto_numbers

# 메인 실행
print("로또 번호 추첨 결과:")
numbers = generate_lotto()
print(numbers)