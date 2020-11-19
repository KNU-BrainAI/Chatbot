# chatbot
## 1. Kogpt2 모델 소개
![noname01](https://user-images.githubusercontent.com/57859679/99677988-acba2d00-2abd-11eb-9ef2-5be6d965d2cb.png)

이번 대회의 목적은 open-domain에서 대화할 수 있는 챗봇을 만드는 것입니다. 그러기 위해서는 제한적인 기능에 특화된 모델보다는 다양하고 많은 데이터로 학습된 범용적인 모델을 사용해야한다. 따라서 저희 팀은 대용량의 데이터로 미리 학습된 KoGPT2를 사용하였습니다.
KoGPT2를 간단하게 설명하면 GPT2는 Transformer 기반의 답변 생성 모델의 구조로 Transformer의 Decoder만을 사용하여 만든 구조입니다. 디코더에 Context와 Reply를 같이 입력하면 Decoder가 다음 단어를 예측합니다. 저희는 이 GPT2 모델을 chatbot 모델에 맞춰서 finetuning한 뒤 모두의 말뭉치 데이터를 포함한 대화데이터로 훈련시켜 사용하였습니다.

## 2. Chatbot 아키텍쳐 소개
저희는 Github에 올려져있는 Kogpt2-chatbot 모델을 사용했습니다.
(깃허브 출처: https://github.com/haven-jeon/KoGPT2-chatbot)


![noname02](https://user-images.githubusercontent.com/57859679/99680189-1fc4a300-2ac0-11eb-9f99-723a559201b0.png)

*챗봇 훈련시 KoGPT2에 3가지 데이터가 들어갑니다. 첫 번째는 사용자의 발화데이터, 두 번째는 챗봇 사용의 응답의 감정레이블(일상다반사:0, 부정:1, 긍정:2), 세 번째로는 사용자의 발화에 대한 응답 데이터를 넣습니다. 그러면 KoGPT2에 나온 응답과 본래의 응답데이터를 비교하여 나온 손실을 감소시키는 방향으로 챗봇을 학습시켰습니다.

*챗봇 대화시에는 사용자가 말을 하면 챗봇이 사용자의 발화를 미리 학습시킨 챗봇 모델에 입력하여 나온 응답으로 대답하도록 만들었습니다.

## 3. 챗봇 훈련 데이터 
1) 모두의 말뭉치 구어 데이터 중(2인 발화 데이터만 추출하여 사용하였습니다.)
2) 챗봇 트레이닝용 문답 페어 11,876개
출처: https://github.com/songys/Chatbot_data
3) AI hub에서 제공하는 한국어 감정 정보가 포함되어 있는 연속적인 대화 데이터셋
촐처: https://aihub.or.kr/keti_data_board/language_intelligence
