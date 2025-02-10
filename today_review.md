### streamlit

- 웹개발을 쉽고 빠르게하도록 도와주는 프레임워크
- python 기반, `pip install streamlit` 으로 설치 후 사용 필요
- `streamlit run main.py`

- 각 페이지들은 pages > page-1.py 등 python 파일 하나씩으로 구성 되어있다. 
- 코드 수정시 실시간 update


### LLM 이란
Large Lang. Model

### 언어 모델의 문제점

1) 데이터 한계 (모든 상세 데이터를 학습할 수는 없음)
    - 우리가 가진 우리만의 커스텀 정보를 프롬프트를 통해 넘겨준다. --> 비용이 크다.
    - rag (가지고 있는 정보를 db로 만들고, 유사한 정보를 추출해서 전달하자) --> 하려면 vector db 구성 필요(embedding model을 통해서 벡터화 됨)

2) 할루시네이션
    - 잘못된 문장 생성 (거짓을 진실처럼 )

- pdf, ppt 등 다양한 형태를 로드할 수 있지만, 결국 그 속의 텍스트만 추출하는 식이다. 언어 모델이므로 당연.

API 키는 매우 중요함 ~.~ 
비용은 사용하는 만큼 (토큰 만큼) 과금

n글자의 영어 != n개의 토큰
1개의 토큰 - 영어기준 한 개의 스펠링 ?? 

### 프롬프트 엔지니어링
1) system prompt 설정
2) output parser 설정해서 응답 형식화
3) pdf 등 정보 추출해서 넘길 수 있다. 
4) llm 모델의 구조 자체를 변경할수는 없음. 


### LLM의 일반적인 아키텍처 

- knowledge base:
- user interaction 

Data Storage / API / Legacy System --> Vector DB


### LangChain 자체 구성요소

- embedding model : 
- loader: 
- vector store : 이미 저장된 vector 정보 가져옴
- chat models : 튜닝된 버전의 lm 


### LangCahin 
- 여러가지 모델의 아웃풋을 합쳐서 더 좋은 결과를 만들어낼 수 있음
- 확률 예측 모델이기 때문에 생성형이 되는 게 가능함 -- 완벽하게 동일한 결과를 기대할 순 없다. 
