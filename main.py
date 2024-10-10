def dict_to_dict(d: dict) -> dict:
    new_d = {}
    for k, v in d.items():
        if new_d.get(v, None):
            new_d[v] = tuple({new_d[v], k})
        else:
            new_d[v] = k
    return new_d


if __name__ == "__main__":
    assert dict_to_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}) == {97832: ("Ivanov", "Kuznecov"), 55521: "Petrov"}
