### 정당 목록
- urls :

        /parties/
- response :

        [
            {
                "id": 1,
                "name": "새누리당"
            },
            {
                "id": 2,
                "name": "새정치민주연합"
            }
        ]

### 정당의 국회의원 목록
- urls :

        /parties/<id>/lawmakers/
- parameter :

        id: 정당의 ID
- response :

        [
            {
                "name": "강기윤",
                "generation": 19,
                "is_current": true,
                "party": 1,
                "local": "경남창원시성산구",
                "id": 1
            },
            {
                "name": "강길부",
                "generation": 19,
                "is_current": true,
                "party": 1,
                "local": "울산울주",
                "id": 3
            }
        ]