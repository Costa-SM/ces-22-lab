# Design pattern state
# The document has three states: draft, moderation or published.

# The document has a 40% chance of being approved for publication
# when in the moderation state.
from __future__ import annotations
import random
from abc import ABC, abstractmethod


class AbstractState(ABC):
    def document(self) -> Document:
        return self.document

    @abstractmethod
    def publish(self, publisher):
        pass

    @abstractmethod
    def review(self):
        pass

    @abstractmethod
    def expire(self):
        pass


class DraftState(AbstractState):
    def publish(self, publisher):
        if(publisher == 'user'):
            print('Document in moderation.')
            self.document.set_state(ModerationState())

        elif(publisher == 'admin'):
            print('Document published by admin.')
            self.document.set_state(PublishedState())

        return True

    def review(self):
        print('Improper state for reviewing.')
        return False

    def expire(self):
        print('Improper state for expiration.')
        return False


class ModerationState(AbstractState):
    def publish(self, publisher):
        print('Improper state for publication.')
        return False

    def review(self):
        if(random.randint(1, 10) / 10 >= 0.4):
            print('Document published.')
            self.document.set_state(PublishedState())
            return True
        else:
            print('Document review failed.')
            self.document.set_state(DraftState())
            return False

    def expire(self):
        print('Improper state for expiration.')
        return False


class PublishedState(AbstractState):
    def __init__(self):
        pass

    def publish(self, publisher):
        print('Improper state for publication.')
        return False

    def review(self):
        print('Improper state for reviewing.')
        return False

    def expire(self):
        print('Document expired.')
        self.document.set_state(DraftState())
        return True
        

class Document:
    current_state = None

    def __init__(self, state: AbstractState):
        self.set_state(state)
    
    def set_state(self, state: AbstractState):
        self.current_state = state
        self.current_state.document = self
    
    def publish(self, publisher):
        self.current_state.publish(publisher)

    def review(self):
        self.current_state.review()

    def expire(self):
        self.current_state.expire()
        

####################################################
# Simple test case

revised_document = Document(DraftState())
revised_document.publish('user')

# 40% chance of failure
revised_document.review()
revised_document.expire()

revised_document.publish('admin')
revised_document.review()
revised_document.publish('user')
revised_document.expire()