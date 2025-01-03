class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.memory_taken = 0
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def get_memory_left(self):
        return self.memory - self.memory_taken

    def install(self, app_name, app_memory):
        if self.get_memory_left() < app_memory:
            return f"Not enough memory to install {app_name}"

        if not self.is_on:
            return f"Turn on your phone to install {app_name}"

        self.apps.append(app_name)
        self.memory_taken += app_memory
        return f"Installing {app_name}"

    def status(self):
        total_apps_count = len(self.apps)
        return f"Total apps: {total_apps_count}. Memory left: {self.get_memory_left()}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
