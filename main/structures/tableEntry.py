__author__ = 'shuhrat'


class TableEntry:
    def __init__(self, topic_name, question_list):
        self.topic_name = topic_name
        self.question_list = question_list
    def __unicode__(self):
        return self.topic_name, ':', self.question_list

