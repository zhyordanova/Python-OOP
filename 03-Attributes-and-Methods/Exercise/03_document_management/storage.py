class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def find_category_by_id(self, id):
        return [c for c in self.categories if c.id == id][0]

    def find_topic_by_id(self, id):
        return [t for t in self.topics if t.id == id][0]

    def find_document_by_id(self, id):
        return [d for d in self.documents if d.id == id][0]

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.find_category_by_id(category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.find_topic_by_id(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self.find_document_by_id(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.find_category_by_id(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.find_topic_by_id(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.find_document_by_id(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        return self.find_document_by_id(document_id)

    def __repr__(self):
        return '\n'.join(repr(doc) for doc in self.documents)
