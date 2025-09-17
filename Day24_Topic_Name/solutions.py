# Day 24 — OOP Interview Scenarios (Python) — Solutions

"""
This file contains Python implementations for the problems defined in problem.html.
Each solution is designed with clean code and interview-ready explanations.
"""

# 1. BankAccount Design
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def transfer_to(self, other_account, amount: float):
        self.withdraw(amount)
        other_account.deposit(amount)


# 2. Singleton Class
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=SingletonMeta):
    def __init__(self, setting: str = "default"):
        self.setting = setting


# 3. Observer/Event System
class Event:
    def __init__(self):
        self._listeners = []
    def subscribe(self, fn):
        self._listeners.append(fn)
    def emit(self, *args, **kwargs):
        for fn in self._listeners:
            fn(*args, **kwargs)


# 4. Strategy Pattern
class JSONStrategy:
    def serialize(self, data):
        import json
        return json.dumps(data)

class XMLStrategy:
    def serialize(self, data):
        return "<root>" + "".join(f"<{k}>{v}</{k}>" for k,v in data.items()) + "</root>"

class Serializer:
    def __init__(self, strategy):
        self.strategy = strategy
    def run(self, data):
        return self.strategy.serialize(data)


# 5. LRU Cache
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# 6. Notification System
class NotificationChannel:
    def send(self, message: str):
        raise NotImplementedError

class EmailNotification(NotificationChannel):
    def send(self, message: str):
        print(f"Email: {message}")

class SMSNotification(NotificationChannel):
    def send(self, message: str):
        print(f"SMS: {message}")

class PushNotification(NotificationChannel):
    def send(self, message: str):
        print(f"Push: {message}")

class Notifier:
    def __init__(self):
        self.channels = []
    def add_channel(self, channel: NotificationChannel):
        self.channels.append(channel)
    def notify(self, message: str):
        for channel in self.channels:
            channel.send(message)


# 7. Plugin System
class Plugin:
    def before_test(self): pass
    def after_test(self): pass

class TestRunner:
    def __init__(self):
        self.plugins = []
    def register_plugin(self, plugin: Plugin):
        self.plugins.append(plugin)
    def run_test(self, test_fn):
        for p in self.plugins:
            p.before_test()
        test_fn()
        for p in self.plugins:
            p.after_test()


# 8. Immutable Class
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

class ImmutableUser:
    __slots__ = ("_name", "_age")
    def __init__(self, name, age):
        object.__setattr__(self, "_name", name)
        object.__setattr__(self, "_age", age)
    @property
    def name(self): return self._name
    @property
    def age(self): return self._age


# 9. Composition vs Inheritance
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        return self.engine.start() + " | Car is moving"


# 10. Refactoring Exercise (God class split)
class Database:
    def save(self, data):
        print("Saving to DB", data)

class Validator:
    def validate(self, data):
        if not data:
            raise ValueError("Invalid data")
        return True

class Reporter:
    def generate(self, data):
        print("Report:", data)

class Processor:
    def __init__(self, db: Database, validator: Validator, reporter: Reporter):
        self.db = db
        self.validator = validator
        self.reporter = reporter
    def run(self, data):
        if self.validator.validate(data):
            self.db.save(data)
            self.reporter.generate(data)


# 11. Polymorphism Example
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height


# 12. Abstract Factory Example
class Button:
    def render(self):
        raise NotImplementedError

class WindowsButton(Button):
    def render(self):
        return "Render Windows Button"

class MacButton(Button):
    def render(self):
        return "Render Mac Button"

class GUIFactory:
    def create_button(self):
        raise NotImplementedError

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()


def client_code(factory: GUIFactory):
    button = factory.create_button()
    print(button.render())


if __name__ == "__main__":
    # Small demo
    acc1, acc2 = BankAccount("Alice", 100), BankAccount("Bob", 50)
    acc1.transfer_to(acc2, 20)
    print("Balances:", acc1.balance, acc2.balance)

    cfg1, cfg2 = Config(), Config()
    print("Singleton same instance:", cfg1 is cfg2)

    event = Event()
    event.subscribe(lambda msg: print("Got:", msg))
    event.emit("Hello World")

    serializer = Serializer(JSONStrategy())
    print(serializer.run({"a":1}))

    cache = LRUCache(2)
    cache.put(1, "A"); cache.put(2, "B"); cache.get(1); cache.put(3, "C")
    print("Cache keys:", list(cache.cache.keys()))

    notifier = Notifier()
    notifier.add_channel(EmailNotification())
    notifier.add_channel(SMSNotification())
    notifier.notify("Test Passed!")

    runner = TestRunner()
    runner.register_plugin(Plugin())
    runner.run_test(lambda: print("Running test..."))

    p = Point(1,2)
    user = ImmutableUser("Alice", 30)
    print("Immutable:", p, user.name)

    car = Car()
    print(car.drive())

    processor = Processor(Database(), Validator(), Reporter())
    processor.run("sample data")

    shapes = [Circle(5), Rectangle(4, 6)]
    for shape in shapes:
        print("Area:", shape.area())

    client_code(WindowsFactory())
    client_code(MacFactory())
