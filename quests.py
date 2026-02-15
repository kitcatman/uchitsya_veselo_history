nikolay2 = {
    "id": "nikolay2",
    "title": "Расследование убийства Николая II",
    "description": "Исторический квест о последних днях семьи Романовых.",
    "card_image": "images/nikolay2_0.jpg",
    "questions": [
        {
            "context": "После отречения от престола Николай II и его семья были арестованы.",
            "media": {
                "type": "image",
                "file": "nikolay2_1.jpg"
            },
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



ALL_QUESTS = {
    nikolay2["id"]: nikolay2
}



# шаблон

# quest = {
#     "id": "quest",
#     "title": "quest title",
#     "description": "quest description",
#     "card_image": "images/quest.jpg",
#     "questions": [
#         {
#             "context": "context first question",
#             "media": {
#                 "type": "image / video / None",
#                 "file": "quest_question_1.jpg"
#             },
#             "question": "question",
#             "answers": [
#                 {
#                     "text": "first answer",
#                     "correct": False / True,
#                     "explanation": "answer explanation"
#                 },
#                 {
#                     "text": "second answer",
#                     "correct": False / True,
#                     "explanation": "answer explanation"
#                 },
#                 {
#                     "text": "third answer",
#                     "correct": False / True,
#                     "explanation": "answer explanation"
#                 }
#             ]
#         }
#     ],
#     "result_text": "quest result text",
# }