import pytest
from ..queue_with_two_stacks import Stack, Queue

# Stack == list
# Pushing to stack == list.append()
# Popping from stack == list.pop()
# Checking if stack is empty == "if list" (true if not empty, false otherwise)
# size() == len(list)
# top() == list[-1]

# ==== STACK TESTS ====
@pytest.fixture()
def setup_stack():
    stack = Stack()
    stack.push(1)
    stack.push(3)
    stack.push(5)
    return stack

def test_pushing_to_a_stack_makes_stack_grow(setup_stack):
    given = setup_stack
    given_length = given.size()
    given.push(5)
    expected_length = given_length + 1
    actual_length = given.size()
    assert expected_length == actual_length

def test_new_stack_has_size_zero():
    given = Stack()
    expected_length = 0
    actual_length = given.size()
    assert expected_length == actual_length

def test_popping_from_stack_makes_stack_shrink(setup_stack):
    given = setup_stack
    given_length = given.size()
    given.pop()
    expected_length = given_length - 1 
    actual_length = given.size()
    assert expected_length == actual_length

# === QUEUE TESTS ===

@pytest.fixture()
def setup_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue

def test_dequeue_removes_first_item(setup_queue):
    given = setup_queue
    expected = 1
    actual = given.dequeue()
    assert expected == actual

def test_enqueue_adds_item_to_end_of_queue(setup_queue):
    given = Queue()
    given.enqueue(1)
    given.enqueue(2)
    given.dequeue()
    expected = 2
    actual = given.dequeue()
    assert expected == actual

