from rich import print
from collections import deque

users_input = {
    "user1": {"xxx@ya.ru", "foo@gmail.com", "lol@mail.ru"},
    "user2": {"foo@gmail.com", "ups@pisem.net"},
    "user3": {"xyz@pisem.net", "vasya@pupkin.com"},
    "user4": {"ups@pisem.net", "aaa@bbb.ru"},
    "user5": {"xyz@pisem.net"},
}

users_output = {
    "user1": {
        "xxx@ya.ru",
        "foo@gmail.com",
        "lol@mail.ru",
        "ups@pisem.net",
        "aaa@bbb.ru",
    },
    "user3": {"xyz@pisem.net", "vasya@pupkin.com"},
}


def merge_users(users: dict[str, set]) -> dict[str, set]:
    """
    Time:  O(n + m)
    Space: O(n + m)
    """
    # costruct graph of [emails -> users]
    graph: dict[str, set] = {}
    for user, emails in users.items():
        for email in emails:
            if email not in graph:
                graph[email] = set()
            graph[email].add(user)

    output = {}
    visited = set()
    for user in users:
        if user not in visited:
            visited.add(user)
            output[user] = set()

            # queue with emails to visit in current graph component
            queue = deque(list(users[user]))
            while queue:
                email = queue.popleft()
                output[user].add(email)  # i.e. users[user1] + {ups@}

                # extend cur emails queue to visit with connected emails through connected users
                for u in graph[email]:
                    if u not in visited:
                        visited.add(u)
                        queue.extend(users[u])  # iter through another accounts emails

    return output


print(merge_users(users_input))
print(merge_users(users_input) == users_output)
