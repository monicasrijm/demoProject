from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def sorted_list(self, reverse: bool = False):
        return sorted(self.to_list(), reverse=reverse)


app = FastAPI()

linked_list = LinkedList()


class SubPage(BaseModel):
    heading: Optional[str] = "subpage heading"
    description: Optional[str] = "description of subpage"
    footer: Optional[str] = "Footer of subpage"
    page_no: int = 0
    page_dim: float = 0.0


new_dict = {}


@app.get("/")
async def kalai():
    return new_dict


@app.post('/sub')
async def subPage(sub: SubPage):
    if new_dict.get(sub.page_no):
        new_dict[sub.page_no] = sub
        return "subpage updated"
    else:
        new_dict[sub.page_no] = sub
        linked_list.append(sub.page_no)  # Append page_no to the linked list
        return "subpage created"


@app.get("/sub/ascending")
async def get_ascending():
    return linked_list.sorted_list()
