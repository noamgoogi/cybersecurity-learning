#dictionary = {key:values}
capitals = {"USA":"Washington D.C",
            "India": "New Delhi",
            "China":"Beijing",
            "Russia": "Moscow"}

print(dir(capitals))
help(capitals)

capitals.keys()
capitals.values()
capitals.get("USA")
capitals.update({"Germany":"Berlin"})
capitals.update({"China":"Berlin"})
capitals.pop("China")
capitals.popitem()
capitals.clear()

