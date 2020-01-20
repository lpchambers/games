#!/usr/bin/python3
import asyncio

class AsyncLoopingCall:
    def __init__(self, f, *a, **kw):
        self.f = f
        self.a = a
        self.kw = kw

        self.running = False
        self.interval = None
        self._next_time = None
        self._next_call = None
        self._next_task = None


    def call(self):
        self._next_task = asyncio.create_task(self.f(*self.a, **self.kw))
        self._next_time += self.interval
        self._next_call = asyncio.get_event_loop().call_at(self._next_time, self.call)

    def start(self, interval, now=True):
        if self.running:
            return

        if interval < 0:
            raise ValueError("Interval must be > 0")

        self.running = True
        self.interval = interval
        self._next_time = asyncio.get_event_loop().time()
        if now:
            self.call()
        else:
            self._next_time += self.interval
            self._next_call = asyncio.get_event_loop().call_at(self._next_time, self.call)

    def stop(self):
        if not self.running:
            return

        self.running = False
        self.interval = None
        self._next_time = None

        self._next_call.cancel()
        self._next_call = None

        if self._next_task and not self._next_task.done():
            self._next_task.cancel()
        self._next_task = None
