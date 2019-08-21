class FixedMultiStack(object):
    def __init__(self, capacity, num_of_stacks):
        self.capacity = capacity
        self.num_of_stacks = num_of_stacks
        self.array_list = [None] * capacity * num_of_stacks
        self.top_index = [-1] * num_of_stacks

    def get_real_top(self, stack_index):
        return stack_index * self.capacity + self.top_index[stack_index]

    def pop(self, stack_index):
        if self.top_index[stack_index] < 0:
            raise Exception("StackEmptyError")
        real_top = self.get_real_top(stack_index)
        item = self.array_list[real_top]
        self.array_list[real_top] = None
        self.top_index[stack_index] -= 1
        return item

    def push(self, item, stack_index):
        if self.top_index[stack_index] == self.capacity - 1:
            raise Exception("StackOverflow")
        real_top = self.get_real_top(stack_index) + 1
        self.array_list[real_top] = item
        self.top_index[stack_index] += 1

    def peek(self, stack_index):
        if self.top_index[stack_index] < 0:
            raise Exception("StackEmptyError")
        real_top = self.get_real_top(stack_index)
        return self.array_list[real_top]

    def is_empty(self, stack_index):
        return self.top_index[stack_index] < 0


def main():
    stack = FixedMultiStack(5, 3)
    for j in range(stack.num_of_stacks):
        for i in range(stack.capacity):
            stack.push(i, j)
        for i in range(stack.capacity):
            print(f"No {j} stack, popping {stack.pop(j)}")
        print(stack.is_empty(j))
        try:
            stack.peek(j)
        except Exception:
            print("Catch error")


if __name__ == '__main__':
    main()
