# 사진 특수 효과

사진에 다양한 opencv 특수 효과 함수를 적용해보는 PyQt5 기반의 GUI 애플리케이션

## 기존 기능
- **특수 효과**
  - 엠보싱
  - 카툰
  - 명암 스케치 (gray)
  - 색상 스케치 (color)
  - 유화
## 추가 기능
- **UI**
  -  현재 상태 표시 기능 추가
  -  `setGeometry`를 통해 UI를 수동으로 설정
- **편의**
  -  자동 창 종료 기능 추가
- **저장**
  - [원본사진이름]_[효과이름]을 조합하여 (.png)형식으로 자동 저장 
  - 중복 파일의 경우 저장하지 않고 중복입니다 메시지 출력

## 사용 방법
1. 프로그램 실행
2. "사진 업로드"를 통해 사진 가져오기
3. 다양한 특수 효과 적용해보기
4. 원하는 특수 효과를 선택하여 "저장하기"를 통해 저장
5. 나가기 버튼을 통해 프로그램 종료 

## 오류 수정
- 사진을 불러오지 않은 상태에서 효과 적용 버튼이나 저장하기 버튼 클릭시 프로그램이 자동으로 종료되던 오류 수정

- 저장할때 확장자를 지정해주지 않으면 생기던 오류 자동 저장 기능으로 수정


## TODO

- [ ] 동영상 특수효과 기능
- [ ] UI 개선
- [ ] 특수 효과 추가