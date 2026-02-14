nikolay2 = {
    "id": "nikolay2",
    "title": "Расследование убийства Николая II",
    "description": "Исторический квест о последних днях семьи Романовых.",
    "questions": [
        {
            "context": "После отречения от престола Николай II и его семья были арестованы.",
            "media": None,
            "question": "Где содержалась семья Романовых перед казнью?",
            "answers": [
                {
                    "text": "В Зимнем дворце",
                    "correct": False,
                    "explanation": "Оставить семью в столице было слишком рискованно."
                },
                {
                    "text": "В Ипатьевском доме",
                    "correct": True,
                    "explanation": "Именно Ипатьевский дом стал местом заключения семьи."
                },
                {
                    "text": "В Кремле",
                    "correct": False,
                    "explanation": "Кремль был политическим центром, а не местом заключения."
                }
            ]
        }
    ],
    "result_text": "Вы проследили цепочку событий, приведших к трагической развязке."
}

ekaterina2 = {
    "id": "ekaterina2",
    "title": "Екатерина Великая",
    "description": "Узнайте великую Екатерину II поближе.",
    "questions": [
        {
            "context": "У Екатерины был муж.",
            "media": None,
            "question": "Кто был мужем Екатерины?",
            "answers": [
                {
                    "text": "Петр III",
                    "correct": True,
                    "explanation": "Он действительно был её супругом, но относились они друг к другу очень холодно и даже агрессивно"
                },
                {
                    "text": "Петр I",
                    "correct": False,
                    "explanation": "Ты додик?"
                },
                {
                    "text": "Николай",
                    "correct": False,
                    "explanation": "Ты додик?"
                },
                {
                    "text": "Иван грозный",
                    "correct": False,
                    "explanation": "Совсем олень?"
                }
            ]
        }
    ],
    "result_text": "Ну ты и додик.",
}



ALL_QUESTS = {
    nikolay2["id"]: nikolay2,
    ekaterina2["id"]: ekaterina2
}
