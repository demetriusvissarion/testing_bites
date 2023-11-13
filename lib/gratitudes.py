class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted

# gratitudes = Gratitudes()
# gratitudes.add('health')
# gratitudes.add('security')
# result = gratitudes.format()
# print(result)