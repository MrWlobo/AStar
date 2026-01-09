class Coordinate:
    def __init__(self, x: int, y: int, f_score: int):
        self.x = x
        self.y = y
        self.f_score = f_score

class PriorityQueue:
    def __init__(self, array: list[Coordinate], is_max_heap: bool = True):
        self.heap = array
        self.is_max_heap = is_max_heap
        self.build_heap()

    def in_order(self, parent: Coordinate, child: Coordinate) -> bool:
        if self.is_max_heap:
            return True if parent.f_score >= child.f_score else False
        else:
            return True if parent.f_score <= child.f_score else False

    def get_parent(self, index: int) -> int | None:
        if not self.heap or index <= 0:
            return None

        return (index - 1) // 2

    def get_left_child(self, index: int) -> int | None:
        left_child_index = 2 * index + 1
        if left_child_index < len(self.heap):
            return left_child_index
        else:
            return None

    def get_right_child(self, index: int) -> int | None:
        right_child_index = 2 * index + 2
        if right_child_index < len(self.heap):
            return right_child_index
        else:
            return None

    def heapify_up(self, index: int) -> None:
        current_index = index
        parent_index = self.get_parent(index)
        valid_indices = parent_index is not None and current_index is not None

        while valid_indices and not self.in_order(self.heap[parent_index], self.heap[current_index]):
            self.heap[parent_index], self.heap[current_index] = self.heap[current_index], self.heap[parent_index]

            current_index = parent_index
            parent_index = self.get_parent(current_index)
            valid_indices = parent_index is not None and current_index is not None

    def heapify_down(self, index: int) -> None:
        current_index = index
        left_child_index, right_child_index = self.get_left_child(index), self.get_right_child(index)

        if left_child_index is None:
            return
        if right_child_index is None:
            child_index = left_child_index
        else:
            if self.in_order(self.heap[left_child_index], self.heap[right_child_index]):
                child_index = left_child_index
            else:
                child_index = right_child_index

        valid_indices = current_index is not None and child_index is not None

        while valid_indices and not self.in_order(self.heap[current_index], self.heap[child_index]):
            self.heap[current_index], self.heap[child_index] = self.heap[child_index], self.heap[current_index]

            current_index = child_index
            left_child_index, right_child_index = self.get_left_child(current_index), self.get_right_child(current_index)

            if left_child_index is None:
                return
            if right_child_index is None:
                child_index = left_child_index
            else:
                if self.in_order(self.heap[left_child_index], self.heap[right_child_index]):
                    child_index = left_child_index
                else:
                    child_index = right_child_index

            valid_indices = current_index is not None and child_index is not None

    def build_heap(self):
        for index in reversed(range(len(self.heap) // 2)):
            self.heapify_down(index)

    def get_root_value(self) -> Coordinate:
        return self.heap[0]

    def insert(self, value: Coordinate) -> None:
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def remove(self):
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

    def __repr__(self):
        return str([x.f_score for x in self.heap])
