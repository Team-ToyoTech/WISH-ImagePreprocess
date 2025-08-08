# WISH-ImagePreprocess

> **WI:SH Kiosk**(종이에 쓴 숫자를 스캔해 주문으로 변환하는 키오스크)의 **숫자 손글씨 데이터셋**을 학습/검증에 적합하도록 가공하는 전처리 스크립트 모음입니다.  
> handmade data(수집본) 기반 전처리를 수행하며, 사용 데이터 기록으로 **23,300 images** 링크가 포함되어 있습니다.  
> - Kiosk 본 프로젝트: https://github.com/Team-ToyoTech/WISH-Kiosk  
> - Used data: [Uploaded in Google Drive](https://drive.google.com/file/d/13Z6RSueJsrHQMfNjg8VyDbt-_C5sD_2x/view?usp=sharing)

---

## ✨ 주요 스크립트와 기능

| 파일 | 목적/기능 | 비고 |
|---|---|---|
| `handWritingPreprocess.py` | **미세 회전 증강**: 각 이미지에 대해 `±0.5°`부터 `±5.0°`까지 0.5° 간격으로 회전본 생성(총 20개 각도) | PIL 사용, `D:\Machine Learning\1-0to6-2\<digit>` → `D:\Machine Learning\tmnist_data\<digit>` 등 경로 기반 예시 포함. |
| `invert.py` | **색 반전**(RGB/RGBA 보존): 흰색 배경/검은 획으로 정규화 | RGBA 알파 보존 처리 포함. `mnist_origin` → `mnist_invert` 변환 예시. :contentReference[oaicite:2]{index=2} |
| `make.py` | **합성 데이터 생성**: 투명 처리된 숫자 이미지를 **기본 배경(NaN.png)** 위에 스케일 `[2.0, 2.5, 3.0]`로 리사이즈 후 **중앙+랜덤 위치**에 합성 | 기본 `numRandom=24`, 샘플 호출은 `8` 사용(중앙 포함 총 9 위치/스케일마다). 출력 파일명에 스케일/좌표 포함. |
| `makeNaN.py` | **NaN(배경/잡음) 합성**: 이미지 테두리에서 랜덤 짧은 선을 1~3개 그려 다양한 노이즈 샘플 생성 | `repeatCount=189000//3` 루프 × (lineCount=1,2,3) ⇒ 총 약 189k 샘플 생성. |
| `SelectImg.py` | **무작위 샘플 추출**: 폴더 내 이미지 일부(%)를 무작위 복사 | `percent=10` 예시, 확장자 필터 및 진행 로그. |
| `copyFile.py` | **단일 파일 복제**: 지정 파일을 번호 증가 형태(`{startIndex}.{ext}`)로 N개 복제 | 파일 존재/유효성 검사 포함. NaN 샘플 증대 예시. |
| `randName.py` | **무작위 파일명 부여**: 충돌 없이 6자리 랜덤 번호로 일괄 변경 | 사용된 번호 재사용 방지/중복 체크. |

> 레포에 포함된 기존 README의 개요와 used data 표기를 그대로 유지하며, 상세 사용법을 보강했습니다.

---

## 📦 실행시 권장 사항

> 스크립트에는 **Windows 절대 경로**(예: `D:\Machine Learning\...`) 예시가 포함되어 있습니다. 실행 전 **본인 환경 경로로 수정**하세요.

