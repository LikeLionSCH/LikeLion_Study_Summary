## 1주차 - 3. CBV (1)

### CBV (Generic View)
**함수**와 **클래스** 모두 호출 가능한 객체(**Callable Object**)다.<br/>
`Django`의 `view`는 **Callable Object**로 정의한다.<br/>

#### 함수와 클래스의 차이

| 함수 (Function) | 클래스 (Class) | 
| --------------- | -------------- |
| 상속 불가능     | 상속 가능      |

**상속**을 사용하는 이유
- 중복의 제거
- 코드의 재사용

상속을 사용해 **코드가 간단**해지는 만큼 미리 **약속**된 것들이 **많다**.

#### CBV를 사용하는 이유
**상속**을 사용해 코드를 더 **간단**하게 **작성**하기 위해 사용
