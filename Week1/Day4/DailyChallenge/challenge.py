import math

class Pagination:

    def __init__(self, items=[], page_size=10):
        self.items = items
        self.page_size = page_size
        self.current_idx = 0

    def get_visible_items(self):
        return self.items[self.current_idx:self.current_idx + self.page_size]

    def get_total_pages(self):
        return math.ceil(len(self.items) / self.page_size)

    def go_to_page(self, page_num):

        if page_num < 1 or page_num > self.get_total_pages():
            raise ValueError("Invalid page number")

        self.current_idx = (page_num - 1) * self.page_size
        return self

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = (self.get_total_pages() - 1) * self.page_size
        return self

    def next_page(self):

        if self.current_idx + self.page_size < len(self.items):
            self.current_idx += self.page_size

        return self

    def previous_page(self):

        if self.current_idx - self.page_size >= 0:
            self.current_idx -= self.page_size

        return self

    def __str__(self):
        return "\n".join(self.get_visible_items())